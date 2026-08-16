from __future__ import annotations

import streamlit as st

from utils.auth import (
    is_logged_in,
    login,
    render_sidebar_auth,
)

from utils.progress import (
    get_completed_section_count,
    get_lesson_progress,
    get_overall_progress,
    get_total_section_count,
    is_lesson_completed,
    is_section_completed,
)

from utils.student_profile import (
    require_student_profile,
)

from utils.theme import (
    load_global_css,
)

from utils.ui import (
    render_breadcrumb,
    render_progress_bar,
)


# =========================================================
# 페이지 기본 설정
# =========================================================

st.set_page_config(
    page_title="임베디드 애플리케이션 구현 LAB",
    page_icon="🔧",
    layout="wide",
)

load_global_css()


# =========================================================
# 로그인 상태
# =========================================================

LOGGED_IN = is_logged_in()


# =========================================================
# Helper Functions
# =========================================================

def get_section_icon(
    section_id: str,
) -> str:
    """
    소단원 완료 여부에 따라 아이콘을 반환합니다.

    비로그인 상태에서는 개인 진도처럼 보이지 않도록
    기본 아이콘만 표시합니다.
    """

    if not LOGGED_IN:
        return "⬜"

    return (
        "✅"
        if is_section_completed(section_id)
        else "⬜"
    )


def get_lesson_button_label(
    lesson_id: str,
    progress: float,
) -> str:
    """
    로그인 상태와 학습 진도율에 따라
    학습 이동 버튼의 문구를 결정합니다.
    """

    if not LOGGED_IN:
        return f"학습 {lesson_id} 시작하기"

    if progress >= 100:
        return f"학습 {lesson_id} 다시 보기"

    if progress > 0:
        return f"학습 {lesson_id} 계속하기"

    return f"학습 {lesson_id} 시작하기"


def format_overall_progress(
    progress: float,
) -> str:
    """
    전체 진도율을 보기 좋은 문자열로 반환합니다.

    예:
    12.5 -> 12.5%
    50.0 -> 50%
    """

    progress = float(progress)

    if progress.is_integer():
        return f"{progress:.0f}%"

    return f"{progress:.1f}%"


# =========================================================
# 사이드바
# =========================================================

st.sidebar.title(
    "🔧 임베디드 구현 LAB"
)

st.sidebar.caption(
    "시스템 프로그래밍"
)

st.sidebar.markdown(
    "### 학습 메뉴"
)

st.sidebar.page_link(
    "streamlit_app.py",
    label="🏠 홈",
)

st.sidebar.page_link(
    "pages/01_학습1_기술명세.py",
    label="📘 학습 1 · 기술 명세 검토",
)

st.sidebar.page_link(
    "pages/02_학습2_개발환경.py",
    label="🛠️ 학습 2 · 개발 환경 구축",
)

st.sidebar.page_link(
    "pages/03_학습3_모듈구현.py",
    label="💻 학습 3 · 모듈 구현",
)

st.sidebar.page_link(
    "pages/04_학습4_인터페이스.py",
    label="🔗 학습 4 · 인터페이스 구현",
)


# ---------------------------------------------------------
# 로그인 전용 메뉴
# ---------------------------------------------------------

if LOGGED_IN:

    st.sidebar.page_link(
        "pages/05_중간고사_종합대비.py",
        label="🎯 중간고사 종합 대비",
    )

    st.sidebar.page_link(
        "pages/06_학습대시보드.py",
        label="📊 학습 대시보드",
    )

else:

    st.sidebar.page_link(
        "pages/05_중간고사_종합대비.py",
        label="🔒 중간고사 종합 대비",
    )

    st.sidebar.page_link(
        "pages/06_학습대시보드.py",
        label="🔒 학습 대시보드",
    )


# =========================================================
# 사이드바 로그인 / 로그아웃 영역
# =========================================================

with st.sidebar:
    render_sidebar_auth()


# =========================================================
# 현재 학습 단계
# =========================================================

st.sidebar.caption(
    "현재 학습 단계"
)

st.sidebar.write(
    "📚 NCS 핵심 학습"
)

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


# =========================================================
# 로그인 학생 최초 정보 입력
# =========================================================
#
# Google 로그인은 되었지만 students 시트의
# class_name / student_number가 비어 있으면
# 여기에서 최초 입력 화면을 보여줍니다.
#
# 입력이 완료될 때까지 이후 홈 화면은 실행하지 않습니다.
# =========================================================

if LOGGED_IN:
    require_student_profile()


# =========================================================
# 학습 진도 데이터
# =========================================================
#
# 로그인 상태:
#   Google Sheets와 연동된 개인 진도를 사용
#
# 비로그인 상태:
#   개인 진도처럼 보이지 않도록 0으로 처리
# =========================================================

if LOGGED_IN:

    lesson_1_progress = get_lesson_progress("1")
    lesson_2_progress = get_lesson_progress("2")
    lesson_3_progress = get_lesson_progress("3")
    lesson_4_progress = get_lesson_progress("4")

    overall_progress = get_overall_progress()

    completed_sections = (
        get_completed_section_count()
    )

    total_sections = (
        get_total_section_count()
    )

else:

    lesson_1_progress = 0.0
    lesson_2_progress = 0.0
    lesson_3_progress = 0.0
    lesson_4_progress = 0.0

    overall_progress = 0.0

    completed_sections = 0

    total_sections = (
        get_total_section_count()
    )


# =========================================================
# 상단 소개
# =========================================================

render_breadcrumb(
    "홈"
)

st.title(
    "🔧 임베디드 애플리케이션 구현 LAB"
)

st.markdown(
    """
    **시스템 프로그래밍 · NCS 임베디드 애플리케이션 구현**
    """
)

st.info(
    "NCS 핵심 이론을 학습하고, 실습과 형성평가를 통해 "
    "개념을 확인한 뒤 실제 Arduino 프로젝트에 적용합니다."
)


# =========================================================
# 전체 학습 진행 상황
# =========================================================

st.markdown(
    "## 📊 나의 학습 진행 상황"
)


# ---------------------------------------------------------
# 로그인 상태
# ---------------------------------------------------------

if LOGGED_IN:

    (
        progress_col1,
        progress_col2,
        progress_col3,
    ) = st.columns(
        [
            4,
            1.3,
            1.3,
        ]
    )


    with progress_col1:

        st.caption(
            "전체 학습 진도"
        )

        render_progress_bar(
            overall_progress,
            show_label=False,
        )

        st.caption(
            f"총 {total_sections}개 소단원 중 "
            f"{completed_sections}개 완료"
        )


    with progress_col2:

        st.metric(
            "전체 진도",
            format_overall_progress(
                overall_progress
            ),
        )


    with progress_col3:

        st.metric(
            "완료 소단원",
            (
                f"{completed_sections}"
                f" / {total_sections}"
            ),
        )


    # -----------------------------------------------------
    # 진도별 안내
    # -----------------------------------------------------

    if (
        total_sections > 0
        and completed_sections == total_sections
    ):

        st.success(
            "🎉 모든 학습 영역을 완료했습니다! "
            "이제 중간고사 종합 대비와 "
            "Arduino 프로젝트에 집중해보세요."
        )

    elif completed_sections > 0:

        st.info(
            f"현재까지 {completed_sections}개의 "
            "소단원을 완료했습니다. "
            "완료하지 않은 학습을 이어서 진행해보세요."
        )

    else:

        st.info(
            "🌱 아직 완료한 소단원이 없습니다. "
            "학습 1부터 차근차근 시작해보세요."
        )


# ---------------------------------------------------------
# 비로그인 상태
# ---------------------------------------------------------

else:

    with st.container(
        border=True
    ):

        st.markdown(
            "### 🔐 Google 로그인 후 나의 학습 기록을 확인할 수 있습니다."
        )

        st.write(
            "학습 1~4의 콘텐츠는 로그인 없이 자유롭게 이용할 수 있습니다. "
            "Google 계정으로 로그인하면 개인 학습 기록을 저장하고 "
            "다른 기기에서도 이어서 학습할 수 있습니다."
        )

        st.info(
            """
            **로그인하면 다음 기능을 사용할 수 있습니다.**

            📊 학습 진도율 저장  
            📝 형성평가 결과 누적  
            🎯 중간고사 종합 대비  
            📈 개인 학습 대시보드  
            💾 다른 기기에서 학습 기록 복원
            """
        )

        if st.button(
            "Google 계정으로 로그인",
            key="home_google_login_button",
            type="primary",
            width="stretch",
        ):
            login()


# =========================================================
# 학습 안내
# =========================================================

st.divider()

st.markdown(
    "## 📚 학습 영역"
)

st.caption(
    "NCS 학습모듈의 순서에 따라 "
    "총 4개의 학습 영역을 진행합니다."
)


# =========================================================
# 학습 영역 데이터
# =========================================================

learning_steps = [
    {
        "lesson_id": "1",
        "icon": "📘",
        "title": "학습 1",
        "description": "기술 명세 검토하기",
        "topics": [
            {
                "section_id": "1-1",
                "title": (
                    "1-1. 검토한 기술 스펙이 적용된 "
                    "소프트웨어 검토"
                ),
            },
            {
                "section_id": "1-2",
                "title": (
                    "1-2. 임베디드 시스템의 평가"
                ),
            },
        ],
        "link": "pages/01_학습1_기술명세.py",
        "progress": lesson_1_progress,
    },
    {
        "lesson_id": "2",
        "icon": "🛠️",
        "title": "학습 2",
        "description": "애플리케이션 개발 환경 구축하기",
        "topics": [
            {
                "section_id": "2-1",
                "title": (
                    "2-1. 개발 도구 선정"
                ),
            },
            {
                "section_id": "2-2",
                "title": (
                    "2-2. 애플리케이션 개발 환경 구축"
                ),
            },
        ],
        "link": "pages/02_학습2_개발환경.py",
        "progress": lesson_2_progress,
    },
    {
        "lesson_id": "3",
        "icon": "💻",
        "title": "학습 3",
        "description": "애플리케이션 모듈 구현하기",
        "topics": [
            {
                "section_id": "3-1",
                "title": (
                    "3-1. 애플리케이션 구현 및 오류 제거"
                ),
            },
            {
                "section_id": "3-2",
                "title": (
                    "3-2. 디버깅 및 프로그램 통합"
                ),
            },
        ],
        "link": "pages/03_학습3_모듈구현.py",
        "progress": lesson_3_progress,
    },
    {
        "lesson_id": "4",
        "icon": "🔗",
        "title": "학습 4",
        "description": "애플리케이션 인터페이스 구현하기",
        "topics": [
            {
                "section_id": "4-1",
                "title": (
                    "4-1. 환경 준비 후 인터페이스 구현"
                ),
            },
            {
                "section_id": "4-2",
                "title": (
                    "4-2. 소스 코드 저장 및 버전 관리"
                ),
            },
        ],
        "link": "pages/04_학습4_인터페이스.py",
        "progress": lesson_4_progress,
    },
]


# =========================================================
# 학습 카드 출력
# =========================================================

left_col, right_col = st.columns(
    2,
    gap="large",
)


for index, item in enumerate(
    learning_steps
):

    target_col = (
        left_col
        if index % 2 == 0
        else right_col
    )


    with target_col:

        with st.container(
            border=True
        ):

            # -------------------------------------------------
            # 카드 제목
            # -------------------------------------------------

            title_col, status_col = st.columns(
                [
                    4,
                    1,
                ]
            )


            with title_col:

                st.markdown(
                    f"### {item['icon']} "
                    f"{item['title']}"
                )


            with status_col:

                if (
                    LOGGED_IN
                    and is_lesson_completed(
                        item[
                            "lesson_id"
                        ]
                    )
                ):

                    st.success(
                        "완료"
                    )


            st.markdown(
                f"**{item['description']}**"
            )

            st.write("")


            # -------------------------------------------------
            # 소단원 상태
            # -------------------------------------------------

            for topic in item[
                "topics"
            ]:

                icon = get_section_icon(
                    topic[
                        "section_id"
                    ]
                )

                st.markdown(
                    f"{icon} "
                    f"{topic['title']}"
                )


            st.write("")


            # -------------------------------------------------
            # 로그인 상태
            # -------------------------------------------------

            if LOGGED_IN:

                st.caption(
                    f"현재 진도율 · "
                    f"{item['progress']:.0f}%"
                )

                render_progress_bar(
                    item[
                        "progress"
                    ],
                    show_label=False,
                )


                if item[
                    "progress"
                ] >= 100:

                    st.success(
                        f"🎉 {item['title']}의 "
                        "모든 소단원을 완료했습니다."
                    )


                elif item[
                    "progress"
                ] > 0:

                    remaining_count = sum(
                        1
                        for topic
                        in item[
                            "topics"
                        ]
                        if not is_section_completed(
                            topic[
                                "section_id"
                            ]
                        )
                    )

                    st.caption(
                        f"⏳ 남은 소단원 · "
                        f"{remaining_count}개"
                    )


            # -------------------------------------------------
            # 비로그인 상태
            # -------------------------------------------------

            else:

                st.caption(
                    "💡 Google 로그인 후 학습하면 "
                    "소단원별 학습 진도가 저장됩니다."
                )


            # -------------------------------------------------
            # 이동 버튼
            # -------------------------------------------------

            st.page_link(
                item[
                    "link"
                ],
                label=get_lesson_button_label(
                    item[
                        "lesson_id"
                    ],
                    item[
                        "progress"
                    ],
                ),
                width="stretch",
            )


# =========================================================
# 중간고사 종합 대비 안내
# =========================================================

st.divider()

st.markdown(
    "## 🎯 중간고사 종합 대비"
)

exam_col1, exam_col2 = st.columns(
    [
        3,
        1,
    ]
)


with exam_col1:

    st.write(
        "학습 1부터 학습 4까지의 중간고사 대비 문제를 "
        "무작위로 출제하여 실제 시험처럼 연습할 수 있습니다."
    )

    st.caption(
        "시험 범위 · 난이도 · 문제 수 선택 → "
        "자동 채점 → 단원별 분석 → 오답 확인"
    )


    if not LOGGED_IN:

        st.info(
            "🔐 중간고사 종합 대비와 개인 학습 대시보드는 "
            "Google 로그인 후 사용할 수 있습니다."
        )


with exam_col2:

    if LOGGED_IN:

        st.page_link(
            "pages/05_중간고사_종합대비.py",
            label="🎯 종합 모의고사 시작",
            width="stretch",
        )

        st.page_link(
            "pages/06_학습대시보드.py",
            label="📊 나의 학습 현황 보기",
            width="stretch",
        )

    else:

        st.page_link(
            "pages/05_중간고사_종합대비.py",
            label="🔒 종합 모의고사",
            width="stretch",
        )

        st.page_link(
            "pages/06_학습대시보드.py",
            label="🔒 학습 대시보드",
            width="stretch",
        )


# =========================================================
# 학습 흐름
# =========================================================

st.divider()

st.markdown(
    "## 🧭 학습 흐름"
)

st.caption(
    "모든 학습 영역은 가능한 한 "
    "동일한 학습 흐름으로 구성합니다."
)


flow_cols = st.columns(
    4
)

flow_items = [
    (
        "📖",
        "핵심 이론",
        "NCS 원문과 핵심 개념 학습",
    ),
    (
        "💡",
        "쉽게 이해하기",
        "학생 눈높이의 설명과 예시",
    ),
    (
        "🎮",
        "개념 체험",
        "선택·예측·조작 활동",
    ),
    (
        "🔧",
        "미니 실습",
        "배운 개념을 직접 적용",
    ),
]


for col, (
    icon,
    title,
    description,
) in zip(
    flow_cols,
    flow_items,
):

    with col:

        with st.container(
            border=True
        ):

            st.markdown(
                f"### {icon}"
            )

            st.markdown(
                f"**{title}**"
            )

            st.caption(
                description
            )


flow_cols_2 = st.columns(
    4
)

flow_items_2 = [
    (
        "🤖",
        "Arduino 연결",
        "실제 프로젝트와 연결",
    ),
    (
        "📝",
        "핵심 정리",
        "시험에 필요한 내용 정리",
    ),
    (
        "✅",
        "형성평가",
        "학습 내용 즉시 확인",
    ),
    (
        "🎯",
        "중간고사 대비",
        "객관식·단답형 문제 연습",
    ),
]


for col, (
    icon,
    title,
    description,
) in zip(
    flow_cols_2,
    flow_items_2,
):

    with col:

        with st.container(
            border=True
        ):

            st.markdown(
                f"### {icon}"
            )

            st.markdown(
                f"**{title}**"
            )

            st.caption(
                description
            )


# =========================================================
# 수업 활용 안내
# =========================================================

st.divider()

st.markdown(
    "## 🧩 이 웹앱은 이렇게 활용합니다"
)

guide_col1, guide_col2, guide_col3 = st.columns(
    3
)


with guide_col1:

    with st.container(
        border=True
    ):

        st.markdown(
            "### ① 배우기"
        )

        st.write(
            "NCS 학습모듈의 핵심 이론을 읽고 "
            "중요 개념을 이해합니다."
        )


with guide_col2:

    with st.container(
        border=True
    ):

        st.markdown(
            "### ② 확인하기"
        )

        st.write(
            "실습 활동과 형성평가를 통해 "
            "이해한 내용을 바로 확인합니다."
        )


with guide_col3:

    with st.container(
        border=True
    ):

        st.markdown(
            "### ③ 적용하기"
        )

        st.write(
            "학습한 내용을 Arduino 기반 "
            "임베디드 프로젝트에 적용합니다."
        )


# =========================================================
# 하단 안내
# =========================================================

st.divider()

st.caption(
    "📌 학습 콘텐츠는 NCS 「임베디드 애플리케이션 구현」 "
    "학습모듈의 구조를 기준으로 구성합니다."
)