import litellm
from dotenv import load_dotenv
from litellm import completion
from litellm.types.utils import Message, ModelResponse

load_dotenv()


def openai() -> None:
    # model は https://platform.openai.com/docs/models 参照
    response: ModelResponse = completion(
        model="gpt-4o-mini", messages=[{"content": "こんちは", "role": "user"}]
    )
    msg: Message = response.choices[0].message
    print(msg.role)
    print(msg.content)


def anthropic() -> None:
    # model は https://docs.anthropic.com/en/docs/about-claude/models#model-names 参照
    response: ModelResponse = completion(
        model="claude-3-haiku-20240307",
        messages=[{"content": "こんちは", "role": "user"}],
    )
    msg: Message = response.choices[0].message
    print(msg.role)
    print(msg.content)


def gemini() -> None:
    # ちなみにVertexAI想定 glcoud でログイン情報をお忘れなく
    # model は https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference 参照。
    # 公式サンプルで指定している　text-bison はもう死んでるっぽい
    response = completion(
        model="gemini-1.5-flash-002",
        messages=[{"content": "こんちは", "role": "user"}],
    )

    msg: Message = response.choices[0].message
    print(msg.role)
    print(msg.content)


def compare() -> None:
    messages = [
        {"content": "あなたはツンデレなAIチャットボットです", "role": "system"},
        {"content": "2+4はいくつ?", "role": "user"},
        {"content": "どうしても言うなら教えてあげてもいいけど", "role": "assistant"},
        {"content": "お願いします", "role": "user"},
    ]

    models = ["gpt-4o-mini", "claude-3-haiku-20240307", "gemini-1.5-flash-001"]
    for model_name in models:
        result: ModelResponse = litellm.completion(
            model=model_name,
            messages=messages,
            temperature=0.0,
            max_tokens=1000,
        )
        print(model_name)
        print()
        print(result.choices[0].message.content)
        print("----")


if __name__ == "__main__":
    compare()
