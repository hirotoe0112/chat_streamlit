import streamlit as st
import pandas

st.title("Lorem Ipsum")
st.header("Chapter 1", divider="grey")
st.subheader("1")

st.write(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Nunc convallis orci odio, sed porttitor diam tempor blandit.
    Donec fringilla, metus at tincidunt egestas, odio felis iaculis ligula,
    id tristique eros leo ac lectus.
    """
)

st.divider()

st.caption("This is a caption")

st.divider()

st.code(
    """
def add(*args):
    return sum(args)

print(add(123, 456, 789))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))
""",
    line_numbers=True,
)

st.divider()


with st.echo():

    def add(*args):
        return sum(args)

    st.write(add(123, 456, 789))
    st.write(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


st.divider()

st.button("This is a button")
st.checkbox("This is a checkbox")
st.toggle("False")
st.page_link("https://www.google.com", label="Google検索")
st.radio("一つ選択してください", ["Apple", "Orange", "Banana"])
st.text_input("何か入力してください", placeholder="sample text")
st.slider("スライダー", value=30)
st.file_uploader("ファイルをアップロードしてください")

st.divider()

st.camera_input("カメラを起動してください")

st.divider()

csv = pandas.read_csv("c01.csv")
df = pandas.DataFrame(csv, columns=["都道府県名", "人口（男）", "人口（女）"])
edit = st.data_editor(df)

st.divider()

st.bar_chart(df, x="都道府県名")

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.write("This is column 1")
    st.button("Button 1")
with col2:
    st.write("This is column 2")
    st.button("Button 2")
with col3:
    st.write("This is column 3")
    st.button("Button 3")

st.sidebar.header("Menu")
st.sidebar.selectbox("種類を選択してください", ["朝食", "昼食", "夕食"])
st.sidebar.number_input("数量を入力してください", value=1)


# if st.button("続きを読む"):
#    st.write("Button clicked")
# else:
#    st.write("Click the button")

# st.write("Hello, *World!* :sunglasses:")

# with open("post.md", "r", encoding="utf-8") as md:
#    st.markdown(md.read())

# if "messages" not in st.session_state:
#    st.session_state.messages = []

# prompt = st.chat_input("Say something")
# if prompt:
#    with st.chat_message("user"):
#        st.write(f"{prompt}")
#        st.session_state.messages.append({"role": "user", "content": prompt})
