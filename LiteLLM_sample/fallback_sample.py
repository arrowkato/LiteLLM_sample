import litellm
from dotenv import load_dotenv
from litellm.types.utils import ModelResponse

load_dotenv()


def fallback() -> None:
    model_list = [
        # ここでモデル名とモデルのパラメーターを定義する
        {
            "model_name": "palm",
            "litellm_params": {
                "model": "text-bison",  # もう使えないモデル
            },
        },
        {
            "model_name": "chatgpt",
            "litellm_params": {
                "model": "gpt-4o-mini",
            },
        },
        {
            "model_name": "cluade",
            "litellm_params": {
                "model": "claude-3-haiku-20240307",
            },
        },
        {
            "model_name": "gemini",
            "litellm_params": {
                "model": "gemini-1.5-flash-002",
            },
        },
    ]
    fallbacks = [
        {"palm": ["chatgpt", "claude", "gemini"]}
    ]  # palm -> chatgpt -> claude ->  gemini
    messages = [
        {"content": "あなたはツンデレなAIチャットボットです", "role": "system"},
        {"content": "2+4はいくつ?", "role": "user"},
        {"content": "どうしても言うなら教えてあげてもいいけど", "role": "assistant"},
        {"content": "お願いします", "role": "user"},
    ]
    router = litellm.router.Router(
        model_list=model_list,
        fallbacks=fallbacks,
        num_retries=0,  # タイムアウト以外は即フォールバックする
        retry_policy=litellm.router.RetryPolicy(TimeoutErrorRetries=1),
    )
    result: ModelResponse = router.completion(model="palm", messages=messages)

    # palm の実体の text-bison は使えないので、chatgpt の実態のgpt-4o-mini-2024-07-18 にフォールバックする
    print(result.model)
    print(result.choices[0].message.content)


if __name__ == "__main__":
    fallback()
