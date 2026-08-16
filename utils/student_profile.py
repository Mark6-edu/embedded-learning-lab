from __future__ import annotations

from typing import Any

import streamlit as st

from utils.auth import (
    get_current_user,
    get_user_id,
    is_logged_in,
)

from utils.sheets_api import post_to_sheets


# =========================================================
# 기본 설정
# =========================================================

CLASS_OPTIONS = [
    "2학년 1반",
    "2학년 2반",
    "2학년 3반",
    "2학년 4반",
]


# =========================================================
# 학생 프로필 조회
# =========================================================

def load_student_profile(
    user_id: str,
) -> dict[str, Any]:
    """
    Google Sheets의 students 시트에서
    현재 학생의 정보를 불러옵니다.

    반환 예시:
    {
        "user_id": "...",
        "email": "...",
        "name": "...",
        "class_name": "2학년 1반",
        "student_number": "7",
        "role": "student",
    }
    """

    user_id = str(
        user_id
    ).strip()

    if not user_id:
        return {}

    result = post_to_sheets(
        action="get_student_profile",
        payload={
            "user_id": user_id,
        },
    )

    if not result.get(
        "success"
    ):
        return {}

    profile = result.get(
        "student",
        {},
    )

    if not isinstance(
        profile,
        dict,
    ):
        return {}

    return profile


# =========================================================
# 학생 프로필 저장
# =========================================================

def save_student_profile(
    user_id: str,
    class_name: str,
    student_number: str,
) -> dict[str, Any]:
    """
    학생의 학급과 번호를 students 시트에 저장합니다.
    """

    user_id = str(
        user_id
    ).strip()

    class_name = str(
        class_name
    ).strip()

    student_number = str(
        student_number
    ).strip()

    if not user_id:

        return {
            "success": False,
            "error": "MISSING_USER_ID",
        }

    if not class_name:

        return {
            "success": False,
            "error": "MISSING_CLASS_NAME",
        }

    if not student_number:

        return {
            "success": False,
            "error": "MISSING_STUDENT_NUMBER",
        }

    return post_to_sheets(
        action="update_student_profile",
        payload={
            "user_id": user_id,
            "class_name": class_name,
            "student_number": student_number,
        },
    )


# =========================================================
# 프로필 완성 여부
# =========================================================

def is_student_profile_complete(
    profile: dict[str, Any] | None,
) -> bool:
    """
    학생 프로필에 학급과 번호가 모두 저장되어 있는지 확인합니다.
    """

    if not profile:
        return False

    class_name = str(
        profile.get(
            "class_name",
            "",
        )
    ).strip()

    student_number = str(
        profile.get(
            "student_number",
            "",
        )
    ).strip()

    return bool(
        class_name
        and student_number
    )


# =========================================================
# 현재 로그인 학생 프로필
# =========================================================

def get_current_student_profile(
    force_reload: bool = False,
) -> dict[str, Any]:
    """
    현재 로그인 학생의 프로필을 반환합니다.

    Session State에 캐시하여
    같은 화면에서 불필요한 API 호출을 줄입니다.
    """

    if not is_logged_in():
        return {}

    user_id = get_user_id()

    if not user_id:
        return {}

    cache_key = (
        f"student_profile_{user_id}"
    )

    if (
        not force_reload
        and cache_key
        in st.session_state
    ):

        cached = st.session_state[
            cache_key
        ]

        if isinstance(
            cached,
            dict,
        ):
            return cached

    profile = load_student_profile(
        user_id
    )

    st.session_state[
        cache_key
    ] = profile

    return profile


# =========================================================
# 프로필 캐시 초기화
# =========================================================

def clear_student_profile_cache() -> None:
    """
    현재 로그인 학생의 프로필 캐시를 제거합니다.
    """

    user_id = get_user_id()

    if not user_id:
        return

    cache_key = (
        f"student_profile_{user_id}"
    )

    if cache_key in st.session_state:

        del st.session_state[
            cache_key
        ]


# =========================================================
# 최초 프로필 입력 UI
# =========================================================

def render_student_profile_setup() -> bool:
    """
    학급/번호가 없는 학생에게
    최초 정보 입력 UI를 표시합니다.

    프로필이 이미 완성된 경우 True를 반환합니다.

    입력이 아직 완료되지 않은 경우 False를 반환합니다.
    """

    if not is_logged_in():
        return False

    user = get_current_user()

    if not user:
        return False

    user_id = get_user_id()

    if not user_id:
        return False

    profile = get_current_student_profile()

    if is_student_profile_complete(
        profile
    ):
        return True

    name = str(
        user.get(
            "name",
            "",
        )
    ).strip()

    email = str(
        user.get(
            "email",
            "",
        )
    ).strip()


    # =====================================================
    # 안내 화면
    # =====================================================

    st.markdown(
        "## 👋 처음 오셨군요!"
    )

    st.write(
        "개인 학습 기록을 정확하게 관리하기 위해 "
        "학급과 번호를 한 번만 입력해주세요."
    )

    st.info(
        "입력한 정보는 학습 진도와 평가 결과를 "
        "학생별로 구분하기 위해 사용됩니다."
    )


    # =====================================================
    # Google 계정 정보
    # =====================================================

    info_col1, info_col2 = st.columns(
        2
    )

    with info_col1:

        st.text_input(
            "이름",
            value=name,
            disabled=True,
            key="profile_setup_name",
        )

    with info_col2:

        st.text_input(
            "Google 계정",
            value=email,
            disabled=True,
            key="profile_setup_email",
        )


    # =====================================================
    # 학급 / 번호 입력
    # =====================================================

    with st.form(
        "student_profile_setup_form"
    ):

        class_name = st.selectbox(
            "학급",
            options=CLASS_OPTIONS,
            index=None,
            placeholder="학급을 선택하세요.",
        )

        student_number = st.number_input(
            "번호",
            min_value=1,
            max_value=40,
            value=None,
            step=1,
            placeholder="번호를 입력하세요.",
        )

        submitted = st.form_submit_button(
            "학습 시작하기",
            type="primary",
            width="stretch",
        )


    # =====================================================
    # 저장
    # =====================================================

    if not submitted:
        return False


    if not class_name:

        st.warning(
            "학급을 선택해주세요."
        )

        return False


    if student_number is None:

        st.warning(
            "번호를 입력해주세요."
        )

        return False


    result = save_student_profile(
        user_id=user_id,
        class_name=class_name,
        student_number=str(
            int(
                student_number
            )
        ),
    )


    if not result.get(
        "success"
    ):

        st.error(
            "학생 정보를 저장하지 못했습니다."
        )

        return False


    # =====================================================
    # 저장 성공
    # =====================================================

    clear_student_profile_cache()

    get_current_student_profile(
        force_reload=True
    )

    st.success(
        "✅ 학생 정보가 저장되었습니다."
    )

    st.rerun()

    return True


# =========================================================
# 프로필 필수 처리
# =========================================================

def require_student_profile() -> None:
    """
    로그인은 되어 있지만 학급/번호 정보가 없는 학생에게
    최초 정보 입력 화면을 표시합니다.

    프로필 입력이 끝날 때까지
    이후 페이지 코드는 실행하지 않습니다.
    """

    if not is_logged_in():
        return

    profile = get_current_student_profile()

    if is_student_profile_complete(
        profile
    ):
        return

    render_student_profile_setup()

    st.stop()