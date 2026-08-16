from __future__ import annotations

from typing import Any

import streamlit as st

from utils.auth import (
    get_current_user,
    get_user_id,
    is_logged_in,
)

from utils.sheets_api import (
    post_to_sheets,
)


# =========================================================
# 학생 기본 설정
# =========================================================

# 현재 시스템 프로그래밍 수업 학급은 고정
FIXED_CLASS_NAME = "2학년 3반"

# 학생 번호는 1번 ~ 10번
STUDENT_NUMBER_OPTIONS = list(
    range(1, 11)
)


# =========================================================
# 학생 프로필 조회
# =========================================================

def load_student_profile(
    user_id: str,
) -> dict[str, Any]:
    """
    Google Sheets의 students 시트에서
    현재 학생의 프로필 정보를 불러옵니다.

    반환 예시:

    {
        "user_id": "...",
        "email": "...",
        "name": "...",
        "class_name": "2학년 3반",
        "student_number": "7",
        "role": "student",
        "created_at": "...",
        "last_login_at": "...",
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
    student_number: int | str,
) -> dict[str, Any]:
    """
    학생의 학급과 번호를 Google Sheets에 저장합니다.

    학급은 항상 '2학년 3반'으로 저장합니다.
    학생 번호는 1~10만 허용합니다.
    """

    user_id = str(
        user_id
    ).strip()

    if not user_id:

        return {
            "success": False,
            "error": "MISSING_USER_ID",
        }

    # -----------------------------------------------------
    # 학생 번호 검증
    # -----------------------------------------------------

    try:
        parsed_student_number = int(
            student_number
        )

    except (
        TypeError,
        ValueError,
    ):

        return {
            "success": False,
            "error": "INVALID_STUDENT_NUMBER",
        }

    if (
        parsed_student_number
        not in STUDENT_NUMBER_OPTIONS
    ):

        return {
            "success": False,
            "error": "INVALID_STUDENT_NUMBER",
        }

    # -----------------------------------------------------
    # Google Sheets 저장
    # -----------------------------------------------------

    return post_to_sheets(
        action="update_student_profile",
        payload={
            "user_id": user_id,
            "class_name": FIXED_CLASS_NAME,
            "student_number": str(
                parsed_student_number
            ),
        },
    )


# =========================================================
# 프로필 완성 여부
# =========================================================

def is_student_profile_complete(
    profile: dict[str, Any] | None,
) -> bool:
    """
    학생 프로필의 필수 정보가
    모두 저장되어 있는지 확인합니다.

    현재 필수 정보:
    - class_name
    - student_number
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

    if not class_name:
        return False

    if not student_number:
        return False

    # -----------------------------------------------------
    # 현재 학급이 맞는지도 확인
    # -----------------------------------------------------

    if class_name != FIXED_CLASS_NAME:
        return False

    # -----------------------------------------------------
    # 번호 범위 확인
    # -----------------------------------------------------

    try:
        parsed_student_number = int(
            student_number
        )

    except ValueError:
        return False

    return (
        parsed_student_number
        in STUDENT_NUMBER_OPTIONS
    )


# =========================================================
# 현재 로그인 학생 프로필
# =========================================================

def get_current_student_profile(
    force_reload: bool = False,
) -> dict[str, Any]:
    """
    현재 로그인한 학생의 프로필을 반환합니다.

    같은 세션 안에서 Google Sheets API를
    불필요하게 반복 호출하지 않도록
    Session State에 캐시합니다.

    force_reload=True를 사용하면
    Google Sheets에서 다시 불러옵니다.
    """

    if not is_logged_in():
        return {}

    user_id = get_user_id()

    if not user_id:
        return {}

    cache_key = (
        f"student_profile_{user_id}"
    )

    # -----------------------------------------------------
    # 캐시 사용
    # -----------------------------------------------------

    if (
        not force_reload
        and cache_key
        in st.session_state
    ):

        cached_profile = (
            st.session_state[
                cache_key
            ]
        )

        if isinstance(
            cached_profile,
            dict,
        ):
            return cached_profile

    # -----------------------------------------------------
    # Google Sheets에서 조회
    # -----------------------------------------------------

    profile = load_student_profile(
        user_id
    )

    st.session_state[
        cache_key
    ] = profile

    return profile


# =========================================================
# 프로필 캐시 삭제
# =========================================================

def clear_student_profile_cache() -> None:
    """
    현재 로그인한 학생의 프로필 캐시를 삭제합니다.
    """

    user_id = get_user_id()

    if not user_id:
        return

    cache_key = (
        f"student_profile_{user_id}"
    )

    if (
        cache_key
        in st.session_state
    ):

        del st.session_state[
            cache_key
        ]


# =========================================================
# 학생 번호 표시용 함수
# =========================================================

def format_student_number(
    number: int,
) -> str:
    """
    번호 선택 UI에서
    '1번', '2번' 형태로 표시합니다.
    """

    return f"{number}번"


# =========================================================
# 최초 프로필 입력 UI
# =========================================================

def render_student_profile_setup() -> bool:
    """
    최초 로그인 학생에게
    학급 및 번호 확인 화면을 표시합니다.

    학급:
        2학년 3반으로 고정

    번호:
        1~10번 중 선택

    프로필이 이미 완성되어 있으면 True,
    아직 입력 중이면 False를 반환합니다.
    """

    # -----------------------------------------------------
    # 로그인 확인
    # -----------------------------------------------------

    if not is_logged_in():
        return False

    user = get_current_user()

    if not user:
        return False

    user_id = get_user_id()

    if not user_id:
        return False

    # -----------------------------------------------------
    # 기존 프로필 확인
    # -----------------------------------------------------

    profile = get_current_student_profile()

    if is_student_profile_complete(
        profile
    ):
        return True

    # -----------------------------------------------------
    # Google 사용자 정보
    # -----------------------------------------------------

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
    # 상단 안내
    # =====================================================

    st.markdown(
        "## 👋 처음 오셨군요!"
    )

    st.write(
        "개인 학습 기록을 정확하게 관리하기 위해 "
        "학생 번호를 한 번만 선택해주세요."
    )

    st.info(
        "📘 학급은 **2학년 3반**으로 자동 지정됩니다. "
        "입력한 정보는 학습 진도와 평가 결과를 "
        "학생별로 구분하기 위해 사용됩니다."
    )


    # =====================================================
    # Google 계정 정보
    # =====================================================

    account_col1, account_col2 = st.columns(
        2
    )


    with account_col1:

        st.text_input(
            "이름",
            value=name,
            disabled=True,
            key="student_profile_name",
        )


    with account_col2:

        st.text_input(
            "Google 계정",
            value=email,
            disabled=True,
            key="student_profile_email",
        )


    # =====================================================
    # 학생 정보 입력
    # =====================================================

    with st.form(
        "student_profile_setup_form"
    ):

        # -------------------------------------------------
        # 학급
        # -------------------------------------------------

        st.text_input(
            "학급",
            value=FIXED_CLASS_NAME,
            disabled=True,
        )


        # -------------------------------------------------
        # 번호
        # -------------------------------------------------

        student_number = st.selectbox(
            "번호",
            options=STUDENT_NUMBER_OPTIONS,
            index=None,
            placeholder="번호를 선택하세요.",
            format_func=format_student_number,
        )


        st.caption(
            "본인의 번호를 정확하게 선택해주세요. "
            "최초 등록 후 개인 학습 기록과 연결됩니다."
        )


        submitted = (
            st.form_submit_button(
                "학습 시작하기",
                type="primary",
                width="stretch",
            )
        )


    # =====================================================
    # 아직 제출하지 않음
    # =====================================================

    if not submitted:
        return False


    # =====================================================
    # 번호 확인
    # =====================================================

    if student_number is None:

        st.warning(
            "학생 번호를 선택해주세요."
        )

        return False


    # =====================================================
    # 저장
    # =====================================================

    with st.spinner(
        "학생 정보를 저장하고 있습니다..."
    ):

        result = save_student_profile(
            user_id=user_id,
            student_number=student_number,
        )


    # =====================================================
    # 저장 실패
    # =====================================================

    if not result.get(
        "success"
    ):

        error_code = result.get(
            "error",
            "UNKNOWN_ERROR",
        )

        if (
            error_code
            == "INVALID_STUDENT_NUMBER"
        ):

            st.error(
                "학생 번호가 올바르지 않습니다."
            )

        elif (
            error_code
            == "STUDENT_NOT_FOUND"
        ):

            st.error(
                "Google Sheets에서 학생 정보를 "
                "찾을 수 없습니다."
            )

        else:

            st.error(
                "학생 정보를 저장하지 못했습니다. "
                "잠시 후 다시 시도해주세요."
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
        f"✅ {FIXED_CLASS_NAME} "
        f"{student_number}번으로 등록되었습니다."
    )

    st.rerun()

    return True


# =========================================================
# 학생 프로필 필수 처리
# =========================================================

def require_student_profile() -> None:
    """
    Google 로그인은 완료했지만
    학생 프로필이 아직 완성되지 않은 경우
    최초 프로필 입력 화면을 표시합니다.

    입력이 완료될 때까지
    현재 페이지의 이후 코드는 실행하지 않습니다.
    """

    if not is_logged_in():
        return

    profile = (
        get_current_student_profile()
    )

    if is_student_profile_complete(
        profile
    ):
        return

    render_student_profile_setup()

    st.stop()