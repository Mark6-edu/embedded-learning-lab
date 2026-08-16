from __future__ import annotations

from typing import Any

import streamlit as st

from utils.sheets_api import (
    check_teacher,
    register_student,
)


# =========================================================
# Session State Keys
# =========================================================

AUTH_REGISTERED_USER_KEY = "auth_registered_user_id"

TEACHER_CACHE_KEY_PREFIX = "teacher_status_"
TEACHER_INFO_KEY_PREFIX = "teacher_info_"


# =========================================================
# 로그인 상태
# =========================================================


def is_logged_in() -> bool:
    """
    현재 사용자가 Streamlit Google OAuth로
    로그인되어 있는지 확인합니다.
    """

    try:
        return bool(
            st.user.is_logged_in
        )

    except Exception:
        return False


# =========================================================
# 현재 사용자
# =========================================================


def get_current_user() -> dict[str, Any]:
    """
    현재 로그인한 Google 사용자의 정보를
    일반 dict 형태로 반환합니다.

    반환 예시:

    {
        "sub": "...",
        "email": "...",
        "name": "...",
        ...
    }
    """

    if not is_logged_in():
        return {}

    try:
        user_data = dict(
            st.user
        )

    except Exception:
        return {}

    return user_data


# =========================================================
# 사용자 ID
# =========================================================


def get_user_id() -> str:
    """
    Google OAuth의 sub 값을
    사용자 고유 ID로 사용합니다.
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
# 사용자 이메일
# =========================================================


def get_user_email() -> str:
    """
    현재 로그인 사용자의 이메일을 반환합니다.
    """

    user = get_current_user()

    if not user:
        return ""

    return str(
        user.get(
            "email",
            "",
        )
    ).strip().lower()


# =========================================================
# 사용자 이름
# =========================================================


def get_user_name() -> str:
    """
    현재 로그인 사용자의 이름을 반환합니다.
    """

    user = get_current_user()

    if not user:
        return ""

    return str(
        user.get(
            "name",
            "",
        )
    ).strip()


# =========================================================
# 로그인
# =========================================================


def login() -> None:
    """
    Google 로그인을 시작합니다.

    현재 프로젝트는 단일 Google OIDC Provider 구조이므로
    provider 이름을 전달하지 않습니다.
    """

    st.login()


# =========================================================
# 로그아웃
# =========================================================


def logout() -> None:
    """
    현재 사용자를 로그아웃합니다.
    """

    clear_auth_cache()

    st.logout()


# =========================================================
# 교사 캐시 Key
# =========================================================


def _get_teacher_cache_key(
    user_id: str,
) -> str:

    return (
        f"{TEACHER_CACHE_KEY_PREFIX}"
        f"{user_id}"
    )


def _get_teacher_info_key(
    user_id: str,
) -> str:

    return (
        f"{TEACHER_INFO_KEY_PREFIX}"
        f"{user_id}"
    )


# =========================================================
# 교사 권한 조회
# =========================================================


def _load_teacher_status(
    force_reload: bool = False,
) -> dict[str, Any]:
    """
    Google Sheets의 teachers 시트를 통해
    현재 사용자의 교사 권한을 확인합니다.

    같은 Streamlit 세션에서는 결과를 캐시하여
    API 호출을 줄입니다.
    """

    if not is_logged_in():

        return {
            "success": True,
            "is_teacher": False,
        }

    user_id = get_user_id()
    email = get_user_email()

    if not user_id:

        return {
            "success": False,
            "is_teacher": False,
            "error": "MISSING_USER_ID",
        }

    cache_key = (
        _get_teacher_cache_key(
            user_id
        )
    )

    info_key = (
        _get_teacher_info_key(
            user_id
        )
    )


    # -----------------------------------------------------
    # 기존 캐시 사용
    # -----------------------------------------------------

    if (
        not force_reload
        and cache_key
        in st.session_state
    ):

        is_teacher_cached = bool(
            st.session_state[
                cache_key
            ]
        )

        teacher_cached = (
            st.session_state.get(
                info_key,
                {},
            )
        )

        return {
            "success": True,
            "is_teacher": (
                is_teacher_cached
            ),
            "teacher": (
                teacher_cached
                if isinstance(
                    teacher_cached,
                    dict,
                )
                else {}
            ),
        }


    # -----------------------------------------------------
    # Google Sheets API 확인
    # -----------------------------------------------------

    result = check_teacher(
        user_id=user_id,
        email=email,
    )


    if not result.get(
        "success"
    ):

        # API 오류를 교사 권한으로 잘못 인정하면 안 되므로
        # 항상 False 처리
        return {
            "success": False,
            "is_teacher": False,
            "error": result.get(
                "error",
                "TEACHER_CHECK_FAILED",
            ),
        }


    teacher_status = bool(
        result.get(
            "is_teacher",
            False,
        )
    )

    teacher_info = result.get(
        "teacher",
        {},
    )

    if not isinstance(
        teacher_info,
        dict,
    ):
        teacher_info = {}


    # -----------------------------------------------------
    # Session State 저장
    # -----------------------------------------------------

    st.session_state[
        cache_key
    ] = teacher_status

    st.session_state[
        info_key
    ] = teacher_info


    return {
        "success": True,
        "is_teacher": teacher_status,
        "teacher": teacher_info,
    }


# =========================================================
# 교사 여부
# =========================================================


def is_teacher(
    force_reload: bool = False,
) -> bool:
    """
    현재 로그인한 사용자가
    활성화된 교사 계정이면 True를 반환합니다.
    """

    if not is_logged_in():
        return False

    result = _load_teacher_status(
        force_reload=force_reload
    )

    return (
        bool(
            result.get(
                "success"
            )
        )
        and bool(
            result.get(
                "is_teacher"
            )
        )
    )


# =========================================================
# 현재 교사 정보
# =========================================================


def get_current_teacher(
    force_reload: bool = False,
) -> dict[str, Any]:
    """
    현재 사용자가 교사이면
    teachers 시트의 교사 정보를 반환합니다.
    """

    if not is_logged_in():
        return {}

    result = _load_teacher_status(
        force_reload=force_reload
    )

    if not result.get(
        "success"
    ):
        return {}

    if not result.get(
        "is_teacher"
    ):
        return {}

    teacher = result.get(
        "teacher",
        {},
    )

    if not isinstance(
        teacher,
        dict,
    ):
        return {}

    return teacher


# =========================================================
# 학생 사용자 등록
# =========================================================


def ensure_student_registered() -> bool:
    """
    로그인 사용자를 students 시트에 등록합니다.

    단, 교사 계정은 students 시트에
    새 학생으로 등록하지 않습니다.

    같은 세션에서는 한 번만 등록합니다.
    """

    if not is_logged_in():
        return False


    # -----------------------------------------------------
    # 교사는 학생 등록 제외
    # -----------------------------------------------------

    if is_teacher():
        return True


    user_id = get_user_id()

    if not user_id:
        return False


    # -----------------------------------------------------
    # 같은 세션에서 이미 등록됨
    # -----------------------------------------------------

    registered_user_id = str(
        st.session_state.get(
            AUTH_REGISTERED_USER_KEY,
            "",
        )
    ).strip()

    if registered_user_id == user_id:
        return True


    # -----------------------------------------------------
    # Google 사용자 정보
    # -----------------------------------------------------

    email = get_user_email()
    name = get_user_name()


    # -----------------------------------------------------
    # students 시트 등록
    # -----------------------------------------------------

    result = register_student(
        user_id=user_id,
        email=email,
        name=name,
    )

    if not result.get(
        "success"
    ):
        return False


    st.session_state[
        AUTH_REGISTERED_USER_KEY
    ] = user_id

    return True


# =========================================================
# 인증 관련 캐시 초기화
# =========================================================


def clear_auth_cache() -> None:
    """
    로그아웃하거나 권한 정보를 새로 불러와야 할 때
    인증 관련 Session State를 제거합니다.
    """

    keys_to_delete: list[str] = []

    for key in st.session_state.keys():

        key_string = str(
            key
        )

        if (
            key_string
            == AUTH_REGISTERED_USER_KEY
        ):

            keys_to_delete.append(
                key
            )

        elif key_string.startswith(
            TEACHER_CACHE_KEY_PREFIX
        ):

            keys_to_delete.append(
                key
            )

        elif key_string.startswith(
            TEACHER_INFO_KEY_PREFIX
        ):

            keys_to_delete.append(
                key
            )


    for key in keys_to_delete:

        del st.session_state[
            key
        ]


# =========================================================
# 로그인 필수 안내
# =========================================================


def render_login_required() -> None:
    """
    로그인 전용 페이지에서
    로그인 안내 UI를 표시합니다.
    """

    st.warning(
        "🔐 Google 로그인이 필요한 기능입니다."
    )

    st.write(
        "학습 기록을 불러오거나 저장하려면 "
        "Google 계정으로 로그인해주세요."
    )

    if st.button(
        "Google 계정으로 로그인",
        key="auth_login_required_button",
        type="primary",
        width="stretch",
    ):

        login()


# =========================================================
# 로그인 필수
# =========================================================


def require_login() -> None:
    """
    현재 페이지가 로그인 전용인 경우 사용합니다.

    로그인하지 않은 사용자는
    안내 화면을 보여주고 이후 실행을 중단합니다.
    """

    if is_logged_in():

        ensure_student_registered()

        return


    render_login_required()

    st.stop()


# =========================================================
# 교사 권한 필수
# =========================================================


def require_teacher() -> None:
    """
    교사 전용 페이지에서 사용합니다.

    조건:
    1. Google 로그인
    2. teachers 시트에 등록
    3. role == teacher
    4. active == TRUE
    """

    # -----------------------------------------------------
    # 먼저 로그인 확인
    # -----------------------------------------------------

    if not is_logged_in():

        st.warning(
            "🔐 교사 로그인이 필요한 페이지입니다."
        )

        st.write(
            "교사용 대시보드는 등록된 교사 계정으로만 "
            "접근할 수 있습니다."
        )

        if st.button(
            "Google 계정으로 로그인",
            key="teacher_login_button",
            type="primary",
            width="stretch",
        ):

            login()

        st.stop()


    # -----------------------------------------------------
    # 교사 권한 확인
    # -----------------------------------------------------

    if is_teacher():
        return


    # -----------------------------------------------------
    # 학생 또는 미등록 사용자
    # -----------------------------------------------------

    st.error(
        "⛔ 교사만 접근할 수 있는 페이지입니다."
    )

    st.write(
        "현재 Google 계정에는 "
        "교사 권한이 등록되어 있지 않습니다."
    )

    st.caption(
        "교사 권한은 Google Sheets의 "
        "teachers 시트에서 관리됩니다."
    )

    st.stop()


# =========================================================
# 사이드바 로그인 UI
# =========================================================


def render_sidebar_auth() -> None:
    """
    사이드바에서 로그인 상태와
    사용자 정보를 표시합니다.

    학생과 교사를 구분하여 표시합니다.
    """

    st.divider()

    st.markdown(
        "### 🔐 학습 계정"
    )


    # =====================================================
    # 비로그인
    # =====================================================

    if not is_logged_in():

        st.caption(
            "Google 로그인 후 개인 학습 기록을 "
            "저장할 수 있습니다."
        )

        if st.button(
            "Google 계정으로 로그인",
            key="sidebar_google_login_button",
            type="primary",
            width="stretch",
        ):

            login()

        return


    # =====================================================
    # 로그인 사용자
    # =====================================================

    user = get_current_user()

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


    # -----------------------------------------------------
    # 교사 여부 확인
    # -----------------------------------------------------

    teacher = is_teacher()


    # -----------------------------------------------------
    # 학생이면 students 등록
    # -----------------------------------------------------

    if not teacher:

        ensure_student_registered()


    # -----------------------------------------------------
    # 사용자 정보
    # -----------------------------------------------------

    if name:

        if teacher:

            st.markdown(
                f"**👨‍🏫 {name} 선생님**"
            )

        else:

            st.markdown(
                f"**👤 {name}**"
            )


    if email:

        st.caption(
            email
        )


    # =====================================================
    # 교사
    # =====================================================

    if teacher:

        st.success(
            "✅ 교사 계정"
        )

        st.caption(
            "학생 학습 현황과 평가 결과를 "
            "확인할 수 있습니다."
        )


    # =====================================================
    # 학생
    # =====================================================

    else:

        st.success(
            "✅ 학습 기록 저장 중"
        )

        st.caption(
            "학습 진도와 평가 결과가 "
            "Google 계정에 저장됩니다."
        )


    # -----------------------------------------------------
    # 로그아웃
    # -----------------------------------------------------

    if st.button(
        "로그아웃",
        key="sidebar_logout_button",
        width="stretch",
    ):

        logout()


# =========================================================
# 기존 코드 호환용 사용자 정보 UI
# =========================================================


def render_user_info() -> None:
    """
    기존 페이지에서 render_user_info()를
    사용하고 있을 경우를 위한 호환 함수입니다.
    """

    if not is_logged_in():

        st.info(
            "Google 로그인 후 "
            "학습 기록을 저장할 수 있습니다."
        )

        return


    name = get_user_name()
    email = get_user_email()


    if is_teacher():

        st.markdown(
            f"**👨‍🏫 {name} 선생님**"
        )

        if email:
            st.caption(
                email
            )

        st.success(
            "교사 계정"
        )

        return


    st.markdown(
        f"**👤 {name}**"
    )

    if email:

        st.caption(
            email
        )

    st.success(
        "학습 기록 저장 중"
    )