from __future__ import annotations

from typing import Any

import streamlit as st


# =========================================================
# 기본 로그인 상태
# =========================================================

def is_logged_in() -> bool:
    """
    현재 사용자가 로그인되어 있는지 확인합니다.
    """

    try:
        return bool(st.user.is_logged_in)

    except Exception:
        return False


# =========================================================
# 사용자 정보
# =========================================================

def get_current_user() -> dict[str, Any] | None:
    """
    로그인한 사용자의 기본 정보를 반환합니다.

    Returns
    -------
    dict | None
        {
            "email": "...",
            "name": "...",
            "sub": "..."
        }

        로그인하지 않은 경우 None
    """

    if not is_logged_in():
        return None

    return {
        "email": str(
            getattr(
                st.user,
                "email",
                "",
            )
            or ""
        ).strip(),

        "name": str(
            getattr(
                st.user,
                "name",
                "",
            )
            or ""
        ).strip(),

        "sub": str(
            getattr(
                st.user,
                "sub",
                "",
            )
            or ""
        ).strip(),
    }


def get_user_email() -> str:
    """
    로그인한 사용자의 이메일을 반환합니다.
    """

    user = get_current_user()

    if not user:
        return ""

    return user.get(
        "email",
        "",
    )


def get_user_name() -> str:
    """
    로그인한 사용자의 이름을 반환합니다.
    """

    user = get_current_user()

    if not user:
        return ""

    name = user.get(
        "name",
        "",
    )

    if name:
        return name

    email = user.get(
        "email",
        "",
    )

    if email:
        return email.split("@")[0]

    return "학생"


def get_user_id() -> str:
    """
    학생별 데이터를 구분하기 위한 사용자 ID를 반환합니다.

    우선순위:
    1. OIDC sub
    2. email

    Google Sheets 저장 시 학생 식별자로 사용할 수 있습니다.
    """

    user = get_current_user()

    if not user:
        return ""

    sub = user.get(
        "sub",
        "",
    )

    if sub:
        return sub

    return user.get(
        "email",
        "",
    )


# =========================================================
# 로그인 / 로그아웃
# =========================================================

def login() -> None:
    st.login()


def logout() -> None:
    """
    현재 사용자를 로그아웃합니다.
    """

    st.logout()


# =========================================================
# 로그인 필요 페이지
# =========================================================

def require_login(
    title: str = "로그인이 필요한 기능입니다",
    description: str | None = None,
) -> None:
    """
    로그인하지 않은 사용자의 페이지 접근을 차단합니다.

    로그인되어 있으면 그대로 통과하고,
    로그인되어 있지 않으면 로그인 안내 화면을 출력한 뒤
    st.stop()으로 나머지 페이지 실행을 중단합니다.
    """

    if is_logged_in():
        return

    if description is None:
        description = (
            "개인 학습 기록과 평가 결과를 저장하고 "
            "나의 학습 데이터를 확인하려면 "
            "Google 로그인이 필요합니다."
        )

    st.markdown(
        f"""
        ## 🔐 {title}

        {description}
        """
    )

    st.info(
        "📘 학습 1~4 콘텐츠는 로그인 없이 이용할 수 있습니다."
    )

    if st.button(
        "Google 계정으로 로그인",
        type="primary",
        width="stretch",
        key="auth_google_login_button",
    ):
        login()

    st.stop()


# =========================================================
# 로그인 사용자 표시
# =========================================================

def render_user_info() -> None:
    """
    로그인한 사용자의 간단한 정보를 표시합니다.

    주로 Sidebar 하단에서 사용합니다.
    """

    if not is_logged_in():
        return

    name = get_user_name()
    email = get_user_email()

    st.markdown(
        f"**👤 {name}**"
    )

    if email:
        st.caption(
            email
        )

    if st.button(
        "로그아웃",
        width="stretch",
        key="auth_logout_button",
    ):
        logout()