"""Claude API 단일 호출 예제.

한 번의 요청을 보내고 한 번의 응답을 받는다.
요약, 분류, 추출, 질의응답처럼 대화가 필요 없는 작업에 쓴다.

실행:
    python claude_single_call.py "한국의 수도는 어디인가"
    cat 문서.txt | python claude_single_call.py
"""

import sys

import anthropic

MODEL = "claude-opus-5"
SYSTEM = "너는 정확하고 간결하게 답하는 조수다. 확실하지 않으면 모른다고 말한다."


def ask(client: anthropic.Anthropic, question: str) -> anthropic.types.Message:
    """질문 하나를 보내고 응답 객체를 돌려준다."""
    return client.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=SYSTEM,
        # 적응형 사고. 모델이 언제 얼마나 생각할지 스스로 정한다.
        # display 를 지정하지 않으면 사고 요약이 빈 문자열로 온다.
        thinking={"type": "adaptive", "display": "summarized"},
        # low / medium / high / xhigh / max. 생략하면 high 다.
        output_config={"effort": "high"},
        messages=[{"role": "user", "content": question}],
    )


def main() -> int:
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        question = sys.stdin.read().strip()
    else:
        print("질문을 인자나 표준입력으로 넘겨라.", file=sys.stderr)
        return 2

    if not question:
        print("질문이 비어 있다.", file=sys.stderr)
        return 2

    # 자격 증명은 환경에서 읽는다. ANTHROPIC_API_KEY 또는 `ant auth login` 프로필.
    client = anthropic.Anthropic()

    try:
        response = ask(client, question)
    except anthropic.AuthenticationError:
        print("API 키가 잘못되었다. ANTHROPIC_API_KEY 를 확인해라.", file=sys.stderr)
        return 1
    except anthropic.BadRequestError as e:
        print(f"요청이 잘못되었다: {e.message}", file=sys.stderr)
        return 1
    except anthropic.RateLimitError as e:
        retry_after = e.response.headers.get("retry-after", "60")
        print(f"요청 한도를 넘었다. {retry_after}초 뒤에 다시 시도해라.", file=sys.stderr)
        return 1
    except anthropic.APIStatusError as e:
        print(f"API 오류 {e.status_code}: {e.message}", file=sys.stderr)
        return 1
    except anthropic.APIConnectionError:
        print("네트워크 연결에 실패했다.", file=sys.stderr)
        return 1

    # 안전 정책으로 거절된 경우. content 를 읽기 전에 먼저 확인한다.
    if response.stop_reason == "refusal":
        detail = response.stop_details
        print(f"모델이 응답을 거절했다: {detail.category if detail else '사유 없음'}", file=sys.stderr)
        return 1

    # content 는 블록 목록이다. type 을 보고 꺼낸다.
    for block in response.content:
        if block.type == "thinking" and block.thinking:
            print(f"[사고 요약] {block.thinking}\n", file=sys.stderr)
        elif block.type == "text":
            print(block.text)

    if response.stop_reason == "max_tokens":
        print("\n[경고] max_tokens 에서 잘렸다. 값을 늘려라.", file=sys.stderr)

    usage = response.usage
    print(
        f"\n[토큰] 입력 {usage.input_tokens} / 출력 {usage.output_tokens}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
