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