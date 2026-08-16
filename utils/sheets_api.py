from __future__ import annotations

from typing import Any

import requests
import streamlit as st


# =========================================================
# 기본 설정
# =========================================================

def get_api_url() -> str:
    """
    Google Apps Script Web App URL을 반환합니다.
    """

    try:
        return str(
            st.secrets["sheets_api"]["url"]
        ).strip()

    except Exception:
        return ""


def get_api_secret() -> str:
    """
    Google Apps Script 요청 인증용 Secret을 반환합니다.
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
    Apps Script Web App에 POST 요청을 보냅니다.

    모든 Google Sheets 관련 요청은
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

    body: dict[str, Any] = {
        "action": action,
        "api_secret": api_secret,
    }

    if payload:
        body.update(
            payload
        )

    try:
        response = requests.post(
            api_url,
            json=body,
            timeout=timeout,
        )

        response.raise_for_status()

        data = response.json()

        if not isinstance(
            data,
            dict,
        ):
            return {
                "success": False,
                "error": "INVALID_RESPONSE",
            }

        return data

    except requests.Timeout as exc:
        return {
            "success": False,
            "error": "REQUEST_TIMEOUT",
            "message": str(exc),
        }

    except requests.RequestException as exc:
        return {
            "success": False,
            "error": "REQUEST_FAILED",
            "message": str(exc),
        }

    except ValueError as exc:
        return {
            "success": False,
            "error": "INVALID_JSON",
            "message": str(exc),
        }


# =========================================================
# 학생 등록 / 로그인 기록
# =========================================================

def register_student(
    user_id: str,
    email: str,
    name: str,
) -> dict[str, Any]:
    """
    학생이 처음 로그인하면 students 시트에 등록하고,
    기존 학생이면 last_login_at을 갱신합니다.
    """

    return post_to_sheets(
        action="register_student",
        payload={
            "user_id": user_id,
            "email": email,
            "name": name,
        },
    )


# =========================================================
# 진도 저장
# =========================================================

def save_progress(
    user_id: str,
    section_id: str,
    completed: bool = True,
) -> dict[str, Any]:
    """
    학생의 소단원 완료 상태를
    progress 시트에 저장합니다.
    """

    return post_to_sheets(
        action="save_progress",
        payload={
            "user_id": user_id,
            "section_id": section_id,
            "completed": completed,
        },
    )


# =========================================================
# 진도 불러오기
# =========================================================

def load_progress(
    user_id: str,
) -> dict[str, Any]:
    """
    학생의 전체 소단원 진도를
    progress 시트에서 불러옵니다.
    """

    result = post_to_sheets(
        action="get_progress",
        payload={
            "user_id": user_id,
        },
    )

    if not result.get(
        "success"
    ):
        return {}

    progress = result.get(
        "progress",
        {},
    )

    if not isinstance(
        progress,
        dict,
    ):
        return {}

    return progress


# =========================================================
# 형성평가 결과 저장
# =========================================================

def save_formative_result(
    user_id: str,
    section_id: str,
    score: int,
    correct: int,
    total: int,
) -> dict[str, Any]:
    """
    학생의 형성평가 결과를
    formative_results 시트에 저장합니다.

    attempt_no는 Apps Script에서
    기존 기록을 기준으로 자동 계산합니다.
    """

    return post_to_sheets(
        action="save_formative_result",
        payload={
            "user_id": user_id,
            "section_id": section_id,
            "score": score,
            "correct": correct,
            "total": total,
        },
    )


# =========================================================
# 형성평가 결과 불러오기
# =========================================================

def load_formative_results(
    user_id: str,
) -> list[dict[str, Any]]:
    """
    학생의 전체 형성평가 응시 이력을
    formative_results 시트에서 불러옵니다.
    """

    result = post_to_sheets(
        action="get_formative_results",
        payload={
            "user_id": user_id,
        },
    )

    if not result.get(
        "success"
    ):
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
        if isinstance(
            item,
            dict,
        )
    ]


# =========================================================
# 중간고사 모의고사 결과 저장
# =========================================================

def save_midterm_result(
    user_id: str,
    selected_units: list[str] | str,
    difficulties: list[str] | str,
    question_count: int,
    score: int | float,
    correct: int,
    total: int,
    wrong_count: int,
) -> dict[str, Any]:
    """
    중간고사 종합 대비 모의고사 결과를
    midterm_results 시트에 저장합니다.

    반환 결과에 exam_id와 attempt_no가 포함됩니다.
    """

    if isinstance(
        selected_units,
        list,
    ):
        selected_units_value = "|".join(
            str(item)
            for item in selected_units
        )

    else:
        selected_units_value = str(
            selected_units
        )

    if isinstance(
        difficulties,
        list,
    ):
        difficulties_value = "|".join(
            str(item)
            for item in difficulties
        )

    else:
        difficulties_value = str(
            difficulties
        )

    return post_to_sheets(
        action="save_midterm_result",
        payload={
            "user_id": user_id,
            "selected_units": selected_units_value,
            "difficulties": difficulties_value,
            "question_count": question_count,
            "score": score,
            "correct": correct,
            "total": total,
            "wrong_count": wrong_count,
        },
    )


# =========================================================
# 중간고사 모의고사 결과 불러오기
# =========================================================

def load_midterm_results(
    user_id: str,
) -> list[dict[str, Any]]:
    """
    학생의 전체 중간고사 모의고사 응시 기록을
    midterm_results 시트에서 불러옵니다.
    """

    result = post_to_sheets(
        action="get_midterm_results",
        payload={
            "user_id": user_id,
        },
    )

    if not result.get(
        "success"
    ):
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
        if isinstance(
            item,
            dict,
        )
    ]


# =========================================================
# 오답 일괄 저장
# =========================================================

def save_wrong_answers(
    user_id: str,
    source_id: str,
    answers: list[dict[str, Any]],
    source_type: str = "midterm",
) -> dict[str, Any]:
    """
    한 번의 시험에서 발생한 오답을
    wrong_answers 시트에 일괄 저장합니다.

    answers 예:
    [
        {
            "question_id": "3_2_e09",
            "section_id": "3-2",
            "topic": "GDB 실습",
            "difficulty": "보통",
            "user_answer": "...",
            "correct_answer": "...",
        }
    ]
    """

    clean_answers: list[
        dict[str, Any]
    ] = []

    for item in answers:

        if not isinstance(
            item,
            dict,
        ):
            continue

        clean_answers.append(
            {
                "question_id": str(
                    item.get(
                        "question_id",
                        "",
                    )
                ),

                "section_id": str(
                    item.get(
                        "section_id",
                        "",
                    )
                ),

                "topic": str(
                    item.get(
                        "topic",
                        "",
                    )
                ),

                "difficulty": str(
                    item.get(
                        "difficulty",
                        "",
                    )
                ),

                "user_answer": str(
                    item.get(
                        "user_answer",
                        "",
                    )
                ),

                "correct_answer": str(
                    item.get(
                        "correct_answer",
                        "",
                    )
                ),
            }
        )

    return post_to_sheets(
        action="save_wrong_answers",
        payload={
            "user_id": user_id,
            "source_type": source_type,
            "source_id": source_id,
            "answers": clean_answers,
        },
        timeout=20,
    )