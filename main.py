import streamlit as st
from openai import OpenAI

client = OpenAI()

# 初期化
messages = [
    {
        "role": "system",
        "content": "You are an assistant. Please answer the user's questions.",
    }
]


def chat():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    answer = completion.choices[0].message
    print(f"AI: {answer.content}")
    messages.append({"role": "assistant", "content": answer.content})


while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})
    chat()
