import streamlit as st

if st.button("Click me"):
    st.write("Button clicked")
else:
    st.write("Click the button")

st.write("Hello, *World!* :sunglasses:")

with open("post.md", "r", encoding="utf-8") as md:
    st.markdown(md.read())

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message("user"):
        st.write(f"{prompt}")
        st.session_state.messages.append({"role": "user", "content": prompt})
