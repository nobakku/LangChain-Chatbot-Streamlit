# LangChain-Chatbot-Streamlit
LangChainを使用したStreamlit上で動くChatbot

## 環境構築
まず、ライブラリをインストールしていきます。

「streamlit、streamlit-chat、langchain、openai、python-dotenv」のライブラリをpip installしましょう。
```
pip3 install streamlit streamlit-chat langchain openai python-dotenv
```

## .envファイルから環境変数を読み込み
[OpenAI](https://platform.openai.com/)からAPIキーを取得｡

.envファイルを作成し､先ほど取得したAPIキーを記述
```
OPENAI_API_KEY="sk-..."
```

## Webアプリの実行方法
以下のコードをターミナルで実行
```
python3 -m streamlit run main.py
```
