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

    body = {
        "action": action,
        "api_secret": api_secret,
    }

    if payload:
        body.update(payload)

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
    이미 존재하면 last_login_at을 갱신합니다.
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
    학생의 소단원 진도를 Google Sheets에 저장합니다.
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
    학생의 전체 소단원 진도를 Google Sheets에서 불러옵니다.
    """

    result = post_to_sheets(
        action="get_progress",
        payload={
            "user_id": user_id,
        },
    )

    if not result.get("success"):
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
    학생의 형성평가 결과를 Google Sheets에 저장합니다.

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
    Google Sheets에서 불러옵니다.

    반환 예:
    [
        {
            "result_id": "...",
            "section_id": "1-1",
            "attempt_no": 1,
            "score": 80,
            "correct": 4,
            "total": 5,
            "submitted_at": "2026-08-16 23:10:00",
        }
    ]
    """

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
        if isinstance(
            item,
            dict,
        )
    ]