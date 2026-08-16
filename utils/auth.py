from __future__ import annotations

from typing import Any

import streamlit as st


# =========================================================
# 기본 로그인 상태
# =========================================================

def is_logged_in() -> bool:
    """
    현재 사용자가 Google 로그인 상태인지 확인합니다.
    """

    try:
        return bool(
            st.user.is_logged_in
        )

    except Exception:
        return False


# =========================================================
# 현재 사용자 정보
# =========================================================

def get_current_user() -> dict[str, Any] | None:
    """
    현재 로그인한 사용자의 정보를 dict 형태로 반환합니다.

    로그인하지 않은 경우 None을 반환합니다.
    """

    if not is_logged_in():
        return None

    try:

        user_data = dict(
            st.user
        )

        return {
            "sub": str(
                user_data.get(
                    "sub",
                    "",
                )
            ).strip(),

            "email": str(
                user_data.get(
                    "email",
                    "",
                )
            ).strip(),

            "name": str(
                user_data.get(
                    "name",
                    "",
                )
            ).strip(),

            "picture": str(
                user_data.get(
                    "picture",
                    "",
                )
            ).strip(),
        }

    except Exception:
        return None

# =========================================================
# 현재 사용자 ID
# =========================================================

def get_user_id() -> str:
    """
    현재 로그인한 사용자의 고유 Google 사용자 ID(sub)를 반환합니다.

    로그인하지 않았거나 사용자 정보를 가져올 수 없는 경우
    빈 문자열을 반환합니다.
    """

    user = get_current_user()

    if not user:
        return ""

    return str(
        user.get(
            "sub",
            "",
        )
    ).strip()

# =========================================================
# 로그인
# =========================================================

def login() -> None:
    """
    Google 로그인 절차를 시작합니다.
    """

    st.login(
        "google"
    )


# =========================================================
# 로그아웃
# =========================================================

def logout() -> None:
    """
    현재 사용자를 로그아웃합니다.
    """

    st.logout()


# =========================================================
# Sidebar 인증 UI
# =========================================================

def render_sidebar_auth() -> None:
    """
    사이드바에 로그인 / 로그아웃 영역을 표시합니다.

    비로그인 상태:
        - Google 로그인 안내
        - 로그인하면 사용할 수 있는 기능 안내
        - Google 로그인 버튼

    로그인 상태:
        - 사용자 이름
        - 이메일
        - 학습 기록 저장 상태
        - 로그아웃 버튼
    """

    st.divider()

    # -----------------------------------------------------
    # 로그인 상태
    # -----------------------------------------------------

    if is_logged_in():

        user = get_current_user()

        if not user:
            return

        name = (
            user.get(
                "name"
            )
            or "사용자"
        )

        email = (
            user.get(
                "email"
            )
            or ""
        )

        st.markdown(
            f"### 👤 {name}"
        )

        if email:

            st.caption(
                email
            )

        st.success(
            "✅ 학습 기록 저장 중"
        )

        st.caption(
            (
                "학습 진도, 형성평가, "
                "중간고사 기록이 "
                "내 계정에 저장됩니다."
            )
        )

        if st.button(
            "로그아웃",
            key="sidebar_logout_button",
            width="stretch",
        ):

            logout()

        return


    # -----------------------------------------------------
    # 비로그인 상태
    # -----------------------------------------------------

    st.markdown(
        "### 🔐 학습 계정"
    )

    st.caption(
        (
            "Google 로그인 후 개인 학습 기록을 "
            "저장할 수 있습니다."
        )
    )

    st.markdown(
        """
        **로그인하면 사용할 수 있어요.**

        - 📊 학습 진도율 저장
        - 📝 형성평가 기록 저장
        - 🎯 중간고사 종합 대비
        - 📈 개인 학습 대시보드
        """
    )

    if st.button(
        "Google 계정으로 로그인",
        key="sidebar_google_login_button",
        type="primary",
        width="stretch",
    ):

        login()


# =========================================================
# 간단한 사용자 정보 UI
# =========================================================

def render_user_info() -> None:
    """
    로그인 사용자 정보를 간단히 표시합니다.

    기존 05, 06 등에서 사용하던 함수와
    호환성을 유지하기 위한 함수입니다.
    """

    if not is_logged_in():
        return

    user = get_current_user()

    if not user:
        return

    name = (
        user.get(
            "name"
        )
        or "사용자"
    )

    email = (
        user.get(
            "email"
        )
        or ""
    )

    st.markdown(
        f"### 👤 {name}"
    )

    if email:

        st.caption(
            email
        )

    if st.button(
        "로그아웃",
        key="user_info_logout_button",
        width="stretch",
    ):

        logout()


# =========================================================
# 로그인 필수 안내 화면
# =========================================================

def render_login_required(
    title: str = "로그인이 필요한 기능입니다",
) -> None:
    """
    로그인하지 않은 사용자가
    로그인 필수 페이지에 접근했을 때 표시합니다.
    """

    st.markdown(
        f"## 🔐 {title}"
    )

    st.write(
        (
            "개인 학습 기록과 평가 결과를 저장하고 "
            "나의 학습 데이터를 확인하려면 "
            "Google 로그인이 필요합니다."
        )
    )

    st.info(
        (
            "📘 학습 1~4 콘텐츠는 "
            "로그인 없이 이용할 수 있습니다."
        )
    )

    st.markdown(
        """
        로그인하면 다음 기능을 사용할 수 있습니다.

        - 학습 진도율 저장
        - 형성평가 결과 누적
        - 중간고사 종합 대비
        - 모의고사 응시 기록 저장
        - 누적 오답 관리
        - 개인 학습 대시보드
        """
    )

    if st.button(
        "Google 계정으로 로그인",
        key="required_google_login_button",
        type="primary",
        width="stretch",
    ):

        login()


# =========================================================
# 로그인 필수 처리
# =========================================================

def require_login() -> None:
    """
    현재 페이지를 로그인 전용으로 제한합니다.

    로그인하지 않았다면 로그인 안내 화면을 표시하고
    이후 페이지 코드를 실행하지 않습니다.
    """

    if is_logged_in():
        return

    render_login_required()

    st.stop()