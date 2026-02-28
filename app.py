import streamlit as st

st.set_page_config(page_title="AI Quản Lý Bài Tập")

# CSS màu sắc
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: black;
    }
    .stNumberInput input {
        background-color: #ffffff;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

st.title("AI Quản Lý Bài Tập Thông Minh")

st.write("Nhập thông tin để tính mức độ ưu tiên ")

mon = st.text_input("Tên môn học")
ngay = st.number_input("Số ngày còn lại", min_value=0)
do_kho = st.slider("Độ khó", 1, 5)

if st.button("Tính ưu tiên"):
    diem = (6 - do_kho) + (10 - ngay)

    st.success(f"Điểm ưu tiên của {mon} là: {diem}")

    if diem >= 10:
        st.error("NÊN LÀM NGAY KHÉO MUỘNNN =))))!")
    else:
        st.info("Có thể làm sau")