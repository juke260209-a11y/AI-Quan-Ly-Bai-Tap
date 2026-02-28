import streamlit as st

st.set_page_config(page_title="AI Quản Lý Bài Tập")

st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}

.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background-color: #1e222a;
    color: white;
}

.stButton > button {
    background-color: #00c8ff;
    color: black;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("AI Quản Lý Bài Tập Thông Minh")

st.write("Nhập thông tin để tính mức độ ưu tiên ")

mon = st.text_input("Tên môn học")
ngay = st.number_input("Số ngày còn lại", min_value=1, step=1)
do_kho = st.slider("Độ khó", 1, 5)

if st.button("Tính ưu tiên"):
    diem = (do_kho * 2) + (10 / ngay)
    st.success(f"Điểm ưu tiên: {diem:.2f}")

    st.success(f"Điểm ưu tiên của {mon} là: {diem}")

    if diem >= 10:
        st.error("NÊN LÀM NGAY KHÉO MUỘNNN =))))!")
    else:

        st.info("Có thể làm sau")

