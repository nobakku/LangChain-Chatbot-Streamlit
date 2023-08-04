import streamlit as st
from streamlit_chat import message

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage
from langchain.schema import AIMessage

import os
from dotenv import load_dotenv



# 環境変数の読み込み
load_dotenv()

# ChatGPT-3.5のモデルのインスタンスの作成
chat = ChatOpenAI(model_name="gpt-3.5-turbo")


# セッション内に保存されたチャット履歴のメモリの取得
"""
このメモリは、LangChainライブラリのConversationBufferMemoryクラスを使用しており、チャットの履歴を保持するために使用
"""
try:
    memory = st.session_state["memory"]
except:
    memory = ConversationBufferMemory(return_messages=True)


# チャット用のチェーンのインスタンスの作成
"""
このチェーンは、入力されたテキストをChatGPTに送信し、ChatGPTからの応答を取得するために使用
"""
chain = ConversationChain(
    llm=chat,
    memory=memory,
)


# ================================【Streamlit UI作成】=================================================
# Streamlitによって、タイトル部分のUIをの作成
st.title("Chatbot in Streamlit")
st.caption("by Yuki Nobata")

# 入力フォームと送信ボタンのUIの作成
text_input = st.text_input("Enter your message")
send_button = st.button("Send")
# ================================【Streamlit UI作成】=================================================


# チャット履歴（HumanMessageやAIMessageなど）を格納する配列の初期化
"""
この後チャットの表示用に使用するHumanMessageやAIMessageなどが格納された配列の初期化
"""
history = []


# ================================【ボタンが押された時の処理】======================================
# ボタンが押された時、OpenAIのAPIを実行
"""
具体的には、入力されたテキストをChatGPTに送信し、ChatGPTからの応答を取得します。
そして、セッションへのチャット履歴の保存を行い、historyという配列の変数の中にチャット履歴を読み込みます。
"""
if send_button:
    send_button = False

    # ChatGPTの実行
    chain(text_input)

    # セッションへのチャット履歴の保存
    st.session_state["memory"] = memory

    # チャット履歴（HumanMessageやAIMessageなど）の読み込み
    try:
        history = memory.load_memory_variables({})["history"]
    except Exception as e:
        st.error(e)
# ================================【ボタンが押された時の処理】======================================


# チャット履歴の表示
"""
最後に、読み込んだhistoryの中に格納されているMessageのデータ型に応じて、チャット履歴を表示します。
"""
for index, chat_message in enumerate(reversed(history)):
    if type(chat_message) == HumanMessage:
        message(chat_message.content, is_user=True, key=2 * index)
    elif type(chat_message) == AIMessage:
        message(chat_message.content, is_user=False, key=2 * index + 1)

