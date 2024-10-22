# 使い方

# step1 (任意)
VS Codeに devcontainer をインストールしておく。

devcontainer で起動する。

# step2
```bash
cp .env.sample .env
```
.env ファイルを作成して、必要に応じて openaiとanthropicのAPI Keyを設定する。

VertexAIの設定は、下記です。
```bash
gcloud init
# 色々聞かれるのでよしなに答える
gcloud auth application-default login
# 色々聞かれるのでよしなに答える
```

# step3 (必要なら)
devcontainerを使っている場合は実行済みですが、各種ライブラリのインストール
```bash
uv sync --dev
```
