from __future__ import annotations

from pathlib import Path

import streamlit as st


# =========================================================
# 프로젝트 경로
# =========================================================

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

ASSETS_DIR = (
    PROJECT_ROOT
    / "assets"
)

GLOBAL_CSS_PATH = (
    ASSETS_DIR
    / "styles.css"
)


# =========================================================
# Global CSS Loader
# =========================================================

def load_global_css() -> None:
    """
    assets/styles.css 파일을 읽어
    현재 Streamlit 페이지에 공통 스타일을 적용한다.

    반드시 st.set_page_config() 이후에 호출한다.

    사용 예:
        st.set_page_config(...)
        load_global_css()
    """

    if not GLOBAL_CSS_PATH.exists():

        st.warning(
            "공통 스타일 파일을 찾을 수 없습니다.\n\n"
            f"`{GLOBAL_CSS_PATH}`"
        )

        return


    try:

        css = GLOBAL_CSS_PATH.read_text(
            encoding="utf-8"
        )

    except OSError as error:

        st.error(
            "공통 CSS 파일을 불러오는 중 "
            "오류가 발생했습니다.\n\n"
            f"`{error}`"
        )

        return


    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True,
    )