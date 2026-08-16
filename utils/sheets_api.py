from __future__ import annotations

from typing import Any

import requests
import streamlit as st


# =========================================================
# Google Apps Script API 기본 설정
# =========================================================


def get_api_url() -> str:
    """
    Streamlit secrets에서
    Google Apps Script Web App URL을 가져옵니다.
    """

    try:
        return str(
            st.secrets["sheets_api"]["url"]
        ).strip()

    except Exception:
        return ""


def get_api_secret() -> str:
    """
    Streamlit secrets에서
    Google Apps Script API Secret을 가져옵니다.
    """

    try:
        return str(
            st.secrets["sheets_api"]["secret"]
        ).strip()

    except Exception:
        return ""


# =========================================================
# 공통 POST 요청
# =========================================================


def post_to_sheets(
    action: str,
    payload: dict[str, Any] | None = None,
    timeout: int = 15,
) -> dict[str, Any]:
    """
    Google Apps Script Web App으로
    POST 요청을 전송합니다.

    모든 Google Sheets API 요청은
    이 함수를 통해 처리합니다.
    """

    api_url = get_api_url()
    api_secret = get_api_secret()

    if not api_url:
        return {
            "success": False,
            "error": "MISSING_API_URL",
        }

    if not api_secret:
        return {
            "success": False,
            "error": "MISSING_API_SECRET",
        }

    request_body: dict[str, Any] = {
        "action": str(action).strip(),
        "api_secret": api_secret,
    }

    if payload:
        request_body.update(payload)

    try:
        response = requests.post(
            api_url,
            json=request_body,
            timeout=timeout,
        )

        response.raise_for_status()

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "REQUEST_TIMEOUT",
        }

    except requests.exceptions.RequestException as exc:
        return {
            "success": False,
            "error": "REQUEST_FAILED",
            "message": str(exc),
        }

    try:
        result = response.json()

    except ValueError:
        return {
            "success": False,
            "error": "INVALID_JSON_RESPONSE",
        }

    if not isinstance(result, dict):
        return {
            "success": False,
            "error": "INVALID_RESPONSE",
        }

    return result


# =========================================================
# 학생 등록
# =========================================================


def register_student(
    user_id: str,
    email: str,
    name: str,
) -> dict[str, Any]:
    """
    Google 로그인 사용자를 students 시트에 등록합니다.

    이미 등록된 학생이라면
    Apps Script에서 기존 정보를 유지하면서
    마지막 로그인 시각을 갱신합니다.
    """

    user_id = str(user_id).strip()
    email = str(email).strip()
    name = str(name).strip()

    if not user_id:
        return {
            "success": False,
            "error": "MISSING_USER_ID",
        }

    return post_to_sheets(
        action="register_student",
        payload={
            "user_id": user_id,
            "email": email,
            "name": name,
        },
    )


# =========================================================
# 학생 프로필
# =========================================================


def load_student_profile(
    user_id: str,
) -> dict[str, Any]:
    """
    students 시트에서 학생 프로필을 불러옵니다.
    """

    user_id = str(user_id).strip()

    if not user_id:
        return {}

    result = post_to_sheets(
        action="get_student_profile",
        payload={
            "user_id": user_id,
        },
    )

    if not result.get("success"):
        return {}

    student = result.get(
        "student",
        {},
    )

    if not isinstance(
        student,
        dict,
    ):
        return {}

    return student


def update_student_profile(
    user_id: str,
    class_name: str,
    student_number: int | str,
) -> dict[str, Any]:
    """
    학생의 학급 및 번호를 저장합니다.
    """

    user_id = str(user_id).strip()
    class_name = str(class_name).strip()
    student_number = str(
        student_number
    ).strip()

    if not user_id:
        return {
            "success": False,
            "error": "MISSING_USER_ID",
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
# 학습 진행도
# =========================================================


def save_progress(
    user_id: str,
    section_id: str,
    completed: bool = True,
) -> dict[str, Any]:
    """
    학생의 소단원 완료 상태를 저장합니다.
    """

    user_id = str(user_id).strip()
    section_id = str(section_id).strip()

    if not user_id:
        return {
            "success": False,
            "error": "MISSING_USER_ID",
        }

    if not section_id:
        return {
            "success": False,
            "error": "MISSING_SECTION_ID",
        }

    return post_to_sheets(
        action="save_progress",
        payload={
            "user_id": user_id,
            "section_id": section_id,
            "completed": bool(completed),
        },
    )


def load_progress(
    user_id: str,
) -> list[dict[str, Any]]:
    """
    학생의 전체 학습 진행 상태를 불러옵니다.
    """

    user_id = str(user_id).strip()

    if not user_id:
        return []

    result = post_to_sheets(
        action="get_progress",
        payload={
            "user_id": user_id,
        },
    )

    if not result.get("success"):
        return []

    progress = result.get(
        "progress",
        [],
    )

    if not isinstance(
        progress,
        list,
    ):
        return []

    return [
        item
        for item in progress
        if isinstance(item, dict)
    ]


# =========================================================
# 형성평가 저장
# =========================================================


def save_formative_result(
    user_id: str,
    section_id: str,
    score: int | float,
    correct: int,
    total: int,
) -> dict[str, Any]:
    """
    형성평가 결과를 저장합니다.
    """

    user_id = str(user_id).strip()
    section_id = str(
        section_id
    ).strip()

    if not user_id:
        return {
            "success": False,
            "error": "MISSING_USER_ID",
        }

    if not section_id:
        return {
            "success": False,
            "error": "MISSING_SECTION_ID",
        }

    return post_to_sheets(
        action="save_formative_result",
        payload={
            "user_id": user_id,
            "section_id": section_id,
            "score": score,
            "correct": int(correct),
            "total": int(total),
        },
    )


# =========================================================
# 형성평가 조회
# =========================================================


def load_formative_results(
    user_id: str,
) -> list[dict[str, Any]]:
    """
    학생의 전체 형성평가 응시 이력을 불러옵니다.
    """

    user_id = str(user_id).strip()

    if not user_id:
        return []

    result = post_to_sheets(
        action="get_formative_results",
        payload={
            "user_id": user_id,
        },
    )

    if not result.get("success"):
        return []

    results = result.get(
        "results",
        [],
    )

    if not isinstance(
        results,
        list,
    ):
        return []

    return [
        item
        for item in results
        if isinstance(item, dict)
    ]


# =========================================================
# 중간고사 결과 저장
# =========================================================


def save_midterm_result(
    user_id: str,
    exam_id: str,
    selected_units: list[str],
    difficulties: list[str],
    question_count: int,
    score: int | float,
    correct: int,
    total: int,
    wrong_answers: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """
    중간고사 종합 대비 결과를 저장합니다.

    오답이 존재하면 wrong_answers 데이터도
    함께 Apps Script로 전달합니다.
    """

    user_id = str(user_id).strip()
    exam_id = str(exam_id).strip()

    if not user_id:
        return {
            "success": False,
            "error": "MISSING_USER_ID",
        }

    if wrong_answers is None:
        wrong_answers = []

    return post_to_sheets(
        action="save_midterm_result",
        payload={
            "user_id": user_id,
            "exam_id": exam_id,
            "selected_units": selected_units,
            "difficulties": difficulties,
            "question_count": int(
                question_count
            ),
            "score": score,
            "correct": int(correct),
            "total": int(total),
            "wrong_count": len(
                wrong_answers
            ),
            "wrong_answers": wrong_answers,
        },
    )


# =========================================================
# 중간고사 결과 조회
# =========================================================


def load_midterm_results(
    user_id: str,
) -> list[dict[str, Any]]:
    """
    학생의 중간고사 종합 대비 응시 이력을 불러옵니다.
    """

    user_id = str(user_id).strip()

    if not user_id:
        return []

    result = post_to_sheets(
        action="get_midterm_results",
        payload={
            "user_id": user_id,
        },
    )

    if not result.get("success"):
        return []

    results = result.get(
        "results",
        [],
    )

    if not isinstance(
        results,
        list,
    ):
        return []

    return [
        item
        for item in results
        if isinstance(item, dict)
    ]


# =========================================================
# 누적 오답 조회
# =========================================================


def load_wrong_answers(
    user_id: str,
) -> list[dict[str, Any]]:
    """
    학생의 누적 오답 기록을 불러옵니다.
    """

    user_id = str(user_id).strip()

    if not user_id:
        return []

    result = post_to_sheets(
        action="get_wrong_answers",
        payload={
            "user_id": user_id,
        },
    )

    if not result.get("success"):
        return []

    results = result.get(
        "results",
        [],
    )

    if not isinstance(
        results,
        list,
    ):
        return []

    return [
        item
        for item in results
        if isinstance(item, dict)
    ]


# =========================================================
# 교사 권한 확인
# =========================================================


def check_teacher(
    user_id: str,
    email: str = "",
) -> dict[str, Any]:
    """
    현재 Google 로그인 사용자가
    teachers 시트에 등록된 활성 교사인지 확인합니다.

    Apps Script 응답 예시:

    {
        "success": True,
        "is_teacher": True,
        "teacher": {
            "user_id": "...",
            "email": "...",
            "name": "...",
            "role": "teacher",
            "active": True
        }
    }
    """

    user_id = str(
        user_id
    ).strip()

    email = str(
        email
    ).strip().lower()

    if not user_id and not email:
        return {
            "success": False,
            "is_teacher": False,
            "error": "MISSING_USER_ID_AND_EMAIL",
        }

    result = post_to_sheets(
        action="check_teacher",
        payload={
            "user_id": user_id,
            "email": email,
        },
    )

    if not isinstance(
        result,
        dict,
    ):
        return {
            "success": False,
            "is_teacher": False,
            "error": "INVALID_RESPONSE",
        }

    return result


def is_teacher_account(
    user_id: str,
    email: str = "",
) -> bool:
    """
    check_teacher() 결과를 단순 True / False로 반환하는
    편의 함수입니다.

    실제 화면에서는 utils.auth.is_teacher()를
    사용하는 것을 권장합니다.
    """

    result = check_teacher(
        user_id=user_id,
        email=email,
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
# 교사 정보 조회
# =========================================================


def get_teacher_info(
    user_id: str,
    email: str = "",
) -> dict[str, Any]:
    """
    교사 권한이 확인되면
    teachers 시트의 교사 정보를 반환합니다.
    """

    result = check_teacher(
        user_id=user_id,
        email=email,
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