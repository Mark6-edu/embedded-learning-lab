from __future__ import annotations

import streamlit as st

from utils.auth import (
    is_logged_in,
    is_teacher,
    render_sidebar_auth,
)


# =========================================================
# 페이지 정보
# =========================================================

PAGE_INFO = {
    "home": {
        "label": "🏠 홈",
        "path": "streamlit_app.py",
    },
    "lesson_1": {
        "label": "📘 학습 1 · 기술 명세 검토",
        "path": "pages/01_학습1_기술명세.py",
    },
    "lesson_2": {
        "label": "🛠️ 학습 2 · 개발 환경 구축",
        "path": "pages/02_학습2_개발환경.py",
    },
    "lesson_3": {
        "label": "💻 학습 3 · 모듈 구현",
        "path": "pages/03_학습3_모듈구현.py",
    },
    "lesson_4": {
        "label": "🔗 학습 4 · 인터페이스 구현",
        "path": "pages/04_학습4_인터페이스.py",
    },
    "midterm": {
        "label": "🎯 중간고사 종합 대비",
        "path": "pages/05_중간고사_종합대비.py",
    },
    "dashboard": {
        "label": "📊 나의 학습 대시보드",
        "path": "pages/06_학습대시보드.py",
    },
    "teacher_dashboard": {
        "label": "👨‍🏫 교사 대시보드",
        "path": "pages/07_교사대시보드.py",
    },
}


# =========================================================
# 현재 학습 영역 표시
# =========================================================

CURRENT_AREA_LABELS = {
    "home": "📚 NCS 핵심 학습",
    "lesson_1": "📘 학습 1 · 기술 명세 검토하기",
    "lesson_2": "🛠️ 학습 2 · 개발 환경 구축하기",
    "lesson_3": "💻 학습 3 · 모듈 구현하기",
    "lesson_4": "🔗 학습 4 · 인터페이스 구현하기",
    "midterm": "🎯 중간고사 종합 대비",
    "dashboard": "📊 나의 학습 대시보드",
    "teacher_dashboard": "👨‍🏫 교사 대시보드",
}


# =========================================================
# 공통 사이드바
# =========================================================

def render_app_sidebar(
    current_page: str = "home",
) -> None:
    """
    Embedded Learning Lab 전체 페이지에서 사용하는
    공통 사이드바입니다.

    로그인 상태에 따라 메뉴를 자동으로 변경합니다.

    비로그인:
        학습 1~4 사용 가능
        중간고사 / 학습 대시보드 잠금 표시

    학생:
        학습 1~4
        중간고사
        개인 학습 대시보드

    교사:
        학습 1~4
        교사 대시보드
    """

    logged_in = is_logged_in()

    teacher = (
        is_teacher()
        if logged_in
        else False
    )

    student = (
        logged_in
        and not teacher
    )


    # =====================================================
    # 브랜드
    # =====================================================

    st.sidebar.title(
        "🔧 임베디드 구현 LAB"
    )

    st.sidebar.caption(
        "시스템 프로그래밍"
    )


    # =====================================================
    # 학습 메뉴
    # =====================================================

    st.sidebar.markdown(
        "### 학습 메뉴"
    )

    st.sidebar.page_link(
        PAGE_INFO["home"]["path"],
        label=PAGE_INFO["home"]["label"],
    )

    st.sidebar.page_link(
        PAGE_INFO["lesson_1"]["path"],
        label=PAGE_INFO["lesson_1"]["label"],
    )

    st.sidebar.page_link(
        PAGE_INFO["lesson_2"]["path"],
        label=PAGE_INFO["lesson_2"]["label"],
    )

    st.sidebar.page_link(
        PAGE_INFO["lesson_3"]["path"],
        label=PAGE_INFO["lesson_3"]["label"],
    )

    st.sidebar.page_link(
        PAGE_INFO["lesson_4"]["path"],
        label=PAGE_INFO["lesson_4"]["label"],
    )


    # =====================================================
    # 학생 로그인
    # =====================================================

    if student:

        st.sidebar.page_link(
            PAGE_INFO["midterm"]["path"],
            label=PAGE_INFO["midterm"]["label"],
        )

        st.sidebar.page_link(
            PAGE_INFO["dashboard"]["path"],
            label=PAGE_INFO["dashboard"]["label"],
        )


    # =====================================================
    # 교사 로그인
    # =====================================================

    elif teacher:

        st.sidebar.markdown(
            "### 교사 메뉴"
        )

        st.sidebar.page_link(
            PAGE_INFO[
                "teacher_dashboard"
            ]["path"],
            label=PAGE_INFO[
                "teacher_dashboard"
            ]["label"],
        )


    # =====================================================
    # 비로그인
    # =====================================================

    else:

        st.sidebar.page_link(
            PAGE_INFO["midterm"]["path"],
            label="🔒 중간고사 종합 대비",
        )

        st.sidebar.page_link(
            PAGE_INFO["dashboard"]["path"],
            label="🔒 학습 대시보드",
        )


    # =====================================================
    # 로그인 / 로그아웃
    # =====================================================

    with st.sidebar:

        render_sidebar_auth()


    # =====================================================
    # 현재 학습 영역
    # =====================================================

    st.sidebar.caption(
        "현재 학습 영역"
    )

    current_label = (
        CURRENT_AREA_LABELS.get(
            current_page,
            "📚 NCS 핵심 학습",
        )
    )

    st.sidebar.write(
        current_label
    )


    # =====================================================
    # 학습 순서
    # =====================================================

    st.sidebar.caption(
        "학습 순서"
    )

    st.sidebar.markdown(
        """
        1. 이론 학습  
        2. 개념 이해  
        3. 실습활동  
        4. 형성평가  
        5. 중간고사 대비  
        6. Arduino 프로젝트 적용
        """
    )