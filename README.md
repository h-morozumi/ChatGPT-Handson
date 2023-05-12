# ChatGPT-Handson

## 環境構築
Github CodeSpaces または、 Visual Studio Code のDevContainer上で作業します。

シェルの起動
```
poetry shell
```

プロジェクトの初期化（初回のみ）
```
poetry install
```

環境変数の設定
```
export OPENAI_API_KEY=
export OPENAI_API_HOST="https://<endpoint>.openai.azure.com"
export OPENAI_API_VERSION="2023-03-15-preview"
export AZURE_DEPLOYMENT_ID=
export OPENAI_DEFAULT_SYSTEM_PROMPT="あなたは親切な 親切なアシスタントです。問い合わせに対して簡潔に回答してください。"
```

アプリケーションの実行
```
python chatgpt_bot.py 
```

シェルの終了
```
exit
```


## 初期環境構築（メモ）

pythonの仮想環境を構築

```
poetry init
poetry add openai
poetry add gradio
```

