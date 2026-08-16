import streamlit as st

from utils.auth import (
    get_current_user,
    is_logged_in,
    login,
    logout,
)


st.set_page_config(
    page_title="로그인 테스트",
    page_icon="🔐",
    layout="centered",
)


st.title("🔐 Google 로그인 테스트")


if not is_logged_in():

    st.info(
        "현재 로그인되어 있지 않습니다."
    )

    if st.button(
        "Google 계정으로 로그인",
        type="primary",
        width="stretch",
    ):
        login()

    st.stop()


user = get_current_user()


st.success(
    "Google 로그인이 정상적으로 완료되었습니다."
)

st.write("### 로그인 사용자 정보")

st.write(
    "이름:",
    user.get("name", "")
)

st.write(
    "이메일:",
    user.get("email", "")
)

st.write(
    "사용자 ID(sub):",
    user.get("sub", "")
)


if st.button(
    "로그아웃",
    width="stretch",
):
    logout()