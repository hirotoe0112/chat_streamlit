import streamlit as st
from openai import OpenAI

client = OpenAI()

# 初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": "You are an assistant. Please answer the user's questions.",
        }
    ]


def chat():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state["messages"],
    )

    answer = completion.choices[0].message
    print(f"AI: {answer.content}")
    st.session_state.messages.append({"role": "assistant", "content": answer.content})


if user_input := st.chat_input("What is up?"):
    # ユーザの入力をメッセージに追加
    st.session_state.messages.append({"role": "user", "content": user_input})
    chat()

# Streamlitではユーザのアクションのたびに画面が再描画されるので、都度すべてのメッセージを描画
for message in st.session_state.messages:
    if not message["role"] == "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
