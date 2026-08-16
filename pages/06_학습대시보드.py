from __future__ import annotations

from collections import Counter
from textwrap import dedent
from typing import Any

import pandas as pd
import streamlit as st

from utils.auth import (
    get_current_user,
    render_user_info,
    require_login,
)

from utils.progress import (
    LESSON_NAMES,
    LESSON_STRUCTURE,
    SECTION_NAMES,
    get_all_attempt_average,
    get_all_progress,
    get_best_formative_score,
    get_completed_section_count,
    get_first_formative_score,
    get_formative_average,
    get_formative_history,
    get_formative_improvement,
    get_lesson_progress,
    get_most_retried_section,
    get_overall_progress,
    get_total_attempt_count,
    get_total_section_count,
    is_section_completed,
)

from utils.sheets_api import (
    load_midterm_results,
    load_wrong_answers,
)

from utils.theme import load_global_css

from utils.ui import (
    render_breadcrumb,
    render_progress_bar,
)


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="학습 대시보드 | 임베디드 구현 LAB",
    page_icon="📊",
    layout="wide",
)

load_global_css()

require_login()


# =========================================================
# 현재 사용자
# =========================================================

current_user = get_current_user()

CURRENT_USER_ID = ""

if current_user:

    CURRENT_USER_ID = str(
        current_user.get(
            "sub",
            "",
        )
    ).strip()


# =========================================================
# Session State
# =========================================================

if "dashboard_midterm_results" not in st.session_state:
    st.session_state[
        "dashboard_midterm_results"
    ] = []

if "dashboard_wrong_answers" not in st.session_state:
    st.session_state[
        "dashboard_wrong_answers"
    ] = []


# =========================================================
# HTML Helper
# =========================================================

def render_html(
    html: str,
) -> None:

    st.html(
        dedent(
            html
        ).strip()
    )


def render_surface_header(
    title: str,
    description: str,
    label: str,
) -> None:

    render_html(
        f"""
        <div class="edu-surface-label">
            {label}
        </div>

        <div class="edu-surface-title">
            {title}
        </div>

        <div class="edu-surface-desc">
            {description}
        </div>
        """
    )


# =========================================================
# Helper
# =========================================================

def format_percent(
    value: float,
) -> str:

    if float(value).is_integer():
        return f"{value:.0f}%"

    return f"{value:.1f}%"


def format_score(
    value: int | float | None,
) -> str:

    if value is None:
        return "-"

    if float(value).is_integer():
        return f"{value:.0f}점"

    return f"{value:.1f}점"


def format_improvement(
    value: int | float | None,
) -> str:

    if value is None:
        return "-"

    if value > 0:
        return f"+{value}점"

    return f"{value}점"


def progress_status(
    progress: float,
) -> str:

    if progress >= 100:
        return "✅ 완료"

    if progress > 0:
        return "⏳ 학습 중"

    return "⬜ 시작 전"


def score_status(
    score: int | float | None,
) -> tuple[str, str]:

    if score is None:

        return (
            "⬜ 미응시",
            "형성평가를 아직 제출하지 않았습니다.",
        )

    if score >= 90:

        return (
            "🏆 강점",
            "핵심 개념을 매우 안정적으로 이해하고 있습니다.",
        )

    if score >= 80:

        return (
            "✅ 안정",
            "전반적인 핵심 개념을 잘 이해하고 있습니다.",
        )

    if score >= 70:

        return (
            "📘 보통",
            "오답을 중심으로 한 번 더 확인해보세요.",
        )

    return (
        "⚠️ 복습 권장",
        "핵심 이론과 오답을 다시 복습하는 것이 좋습니다.",
    )


def get_growth_message(
    history: list[dict[str, Any]],
) -> tuple[str, str]:

    if len(history) < 2:

        return (
            "🌱 첫 학습 기록",
            (
                "한 번 더 도전하면 최초 점수와 최근 점수의 "
                "변화를 비교할 수 있습니다."
            ),
        )

    first_score = history[0]["score"]
    latest_score = history[-1]["score"]

    improvement = (
        latest_score
        - first_score
    )

    if improvement >= 20:

        return (
            "🚀 큰 폭으로 성장",
            (
                f"최초 응시보다 {improvement}점 향상되었습니다. "
                "복습과 재도전의 효과가 뚜렷합니다."
            ),
        )

    if improvement > 0:

        return (
            "📈 점수 상승",
            (
                f"최초 응시보다 {improvement}점 향상되었습니다. "
                "현재의 학습 흐름을 유지해보세요."
            ),
        )

    if improvement == 0:

        return (
            "➡️ 점수 유지",
            (
                "최초 점수와 최근 점수가 같습니다. "
                "오답 개념을 중심으로 복습해보세요."
            ),
        )

    return (
        "📉 점수 하락",
        (
            f"최초 응시보다 {abs(improvement)}점 낮아졌습니다. "
            "최근 오답을 다시 확인해보세요."
        ),
    )


# =========================================================
# 원격 데이터 불러오기
# =========================================================

def load_dashboard_remote_data() -> None:
    """
    Google Sheets에서 중간고사 결과와
    누적 오답을 항상 최신 상태로 불러옵니다.
    """

    if not CURRENT_USER_ID:
        return

    try:

        midterm_results = load_midterm_results(
            CURRENT_USER_ID
        )

        if isinstance(
            midterm_results,
            list,
        ):
            st.session_state[
                "dashboard_midterm_results"
            ] = midterm_results

    except Exception:
        pass


    try:

        wrong_answers = load_wrong_answers(
            CURRENT_USER_ID
        )

        if isinstance(
            wrong_answers,
            list,
        ):
            st.session_state[
                "dashboard_wrong_answers"
            ] = wrong_answers

    except Exception:
        pass

load_dashboard_remote_data()


# =========================================================
# 기본 데이터
# =========================================================

progress_data = get_all_progress()

overall_progress = get_overall_progress()

completed_sections = (
    get_completed_section_count()
)

total_sections = (
    get_total_section_count()
)

formative_average = (
    get_formative_average()
)

all_attempt_average = (
    get_all_attempt_average()
)

total_attempts = (
    get_total_attempt_count()
)

most_retried = (
    get_most_retried_section()
)

midterm_results = st.session_state[
    "dashboard_midterm_results"
]

wrong_answers = st.session_state[
    "dashboard_wrong_answers"
]


# =========================================================
# 중간고사 통계
# =========================================================

midterm_attempt_count = len(
    midterm_results
)

midterm_latest_score = None
midterm_best_score = None
midterm_average_score = None
midterm_improvement = None


if midterm_results:

    midterm_results = sorted(
        midterm_results,
        key=lambda item: int(
            item.get(
                "attempt_no",
                0,
            )
            or 0
        ),
    )

    midterm_scores = [
        float(
            item.get(
                "score",
                0,
            )
            or 0
        )
        for item in midterm_results
    ]

    midterm_latest_score = (
        midterm_scores[-1]
    )

    midterm_best_score = max(
        midterm_scores
    )

    midterm_average_score = round(
        sum(
            midterm_scores
        )
        / len(
            midterm_scores
        ),
        1,
    )

    if len(
        midterm_scores
    ) >= 2:

        midterm_improvement = (
            midterm_scores[-1]
            - midterm_scores[0]
        )


# =========================================================
# 오답 통계
# =========================================================

total_wrong_answers = len(
    wrong_answers
)


section_wrong_counter = Counter(
    str(
        item.get(
            "section_id",
            "",
        )
    ).strip()
    for item in wrong_answers
    if str(
        item.get(
            "section_id",
            "",
        )
    ).strip()
)


topic_wrong_counter = Counter(
    str(
        item.get(
            "topic",
            "",
        )
    ).strip()
    for item in wrong_answers
    if str(
        item.get(
            "topic",
            "",
        )
    ).strip()
)


difficulty_wrong_counter = Counter(
    str(
        item.get(
            "difficulty",
            "",
        )
    ).strip()
    for item in wrong_answers
    if str(
        item.get(
            "difficulty",
            "",
        )
    ).strip()
)


most_wrong_section = None

if section_wrong_counter:

    most_wrong_section = (
        section_wrong_counter.most_common(
            1
        )[0]
    )


most_wrong_topic = None

if topic_wrong_counter:

    most_wrong_topic = (
        topic_wrong_counter.most_common(
            1
        )[0]
    )


# =========================================================
# 페이지 이동
# =========================================================

lesson_icons = {
    "1": "📘",
    "2": "🛠️",
    "3": "💻",
    "4": "🔗",
}


lesson_links = {
    "1": "pages/01_학습1_기술명세.py",
    "2": "pages/02_학습2_개발환경.py",
    "3": "pages/03_학습3_모듈구현.py",
    "4": "pages/04_학습4_인터페이스.py",
}


# =========================================================
# Sidebar
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

st.sidebar.page_link(
    "pages/05_중간고사_종합대비.py",
    label="🎯 중간고사 종합 대비",
)

st.sidebar.page_link(
    "pages/06_학습대시보드.py",
    label="📊 학습 대시보드",
)

st.sidebar.divider()

with st.sidebar:

    render_user_info()


st.sidebar.caption(
    "현재 학습 영역"
)

st.sidebar.markdown(
    "📊 **나의 학습 대시보드**"
)


# =========================================================
# Breadcrumb
# =========================================================

render_breadcrumb(
    "홈",
    "학습 대시보드",
)


# =========================================================
# HERO
# =========================================================

render_html(
    """
    <div class="edu-hero">

        <div class="edu-hero-eyebrow">
            LEARNING ANALYTICS
        </div>

        <div class="edu-hero-title">
            나의 학습 대시보드
        </div>

        <div class="edu-hero-desc">
            학습 진도, 형성평가, 중간고사 모의시험,
            누적 오답을 함께 분석하여 나의 학습 상태를
            한눈에 확인합니다.
        </div>

    </div>
    """
)


# =========================================================
# 학습 현황 요약
# =========================================================

with st.container(
    key="edu_section_dashboard_summary"
):

    render_surface_header(
        "학습 현황 요약",
        (
            "전체 학습 진도와 형성평가 성취도를 "
            "기준으로 현재 상태를 확인합니다."
        ),
        "LEARNING STATUS",
    )


    (
        metric_col1,
        metric_col2,
        metric_col3,
        metric_col4,
        metric_col5,
    ) = st.columns(
        5
    )


    with metric_col1:

        st.metric(
            "전체 진도",
            format_percent(
                overall_progress
            ),
        )


    with metric_col2:

        st.metric(
            "완료 소단원",
            (
                f"{completed_sections}"
                f" / {total_sections}"
            ),
        )


    with metric_col3:

        st.metric(
            "최근 점수 평균",
            format_score(
                formative_average
            ),
        )


    with metric_col4:

        st.metric(
            "전체 응시 평균",
            format_score(
                all_attempt_average
            ),
        )


    with metric_col5:

        st.metric(
            "형성평가 총 응시",
            f"{total_attempts}회",
        )


# =========================================================
# 전체 학습 진도
# =========================================================

with st.container(
    key="edu_section_dashboard_progress"
):

    render_surface_header(
        "전체 학습 진도",
        (
            "총 8개 소단원 중 형성평가까지 완료한 "
            "학습 영역의 비율입니다."
        ),
        "PROGRESS",
    )


    render_progress_bar(
        overall_progress,
        show_label=False,
    )


    st.caption(
        f"총 {total_sections}개 소단원 중 "
        f"{completed_sections}개를 완료했습니다."
    )


    if overall_progress >= 100:

        st.success(
            "🎉 모든 소단원을 완료했습니다!"
        )

    elif overall_progress >= 75:

        st.info(
            "🚀 거의 다 왔습니다. 남은 학습을 마무리해보세요."
        )

    elif overall_progress >= 50:

        st.info(
            "📘 시험 범위의 절반 이상을 완료했습니다."
        )

    elif overall_progress > 0:

        st.info(
            "🌱 학습이 시작되었습니다. 계속 진행해보세요."
        )

    else:

        st.info(
            "학습을 시작하면 진행 상황이 표시됩니다."
        )


# =========================================================
# 학습 영역별 진도
# =========================================================

with st.container(
    key="edu_section_dashboard_lessons"
):

    render_surface_header(
        "학습 영역별 진도",
        "NCS 학습 1~4의 완료 상태를 영역별로 확인합니다.",
        "LESSON PROGRESS",
    )


    lesson_cols = st.columns(
        4
    )


    for col, lesson_id in zip(
        lesson_cols,
        LESSON_STRUCTURE.keys(),
    ):

        lesson_progress = (
            get_lesson_progress(
                lesson_id
            )
        )


        with col:

            with st.container(
                border=True
            ):

                st.markdown(
                    f"### "
                    f"{lesson_icons[lesson_id]} "
                    f"학습 {lesson_id}"
                )

                st.caption(
                    LESSON_NAMES[
                        lesson_id
                    ]
                )

                st.metric(
                    "진도율",
                    format_percent(
                        lesson_progress
                    ),
                )

                render_progress_bar(
                    lesson_progress,
                    show_label=False,
                )

                st.markdown(
                    progress_status(
                        lesson_progress
                    )
                )

                st.page_link(
                    lesson_links[
                        lesson_id
                    ],
                    label=(
                        f"학습 {lesson_id} 보기"
                    ),
                    width="stretch",
                )


# =========================================================
# 소단원별 현황
# =========================================================

with st.container(
    key="edu_section_dashboard_sections"
):

    render_surface_header(
        "소단원별 학습 현황",
        (
            "완료 여부와 최근 점수, 최고 점수, "
            "최근 정답 및 응시 횟수를 확인합니다."
        ),
        "SECTION STATUS",
    )


    for lesson_id, section_ids in (
        LESSON_STRUCTURE.items()
    ):

        st.markdown(
            f"### "
            f"{lesson_icons[lesson_id]} "
            f"학습 {lesson_id} · "
            f"{LESSON_NAMES[lesson_id]}"
        )


        for section_id in section_ids:

            data = progress_data[
                section_id
            ]

            completed = (
                is_section_completed(
                    section_id
                )
            )

            status, message = (
                score_status(
                    data[
                        "formative_score"
                    ]
                )
            )

            best_score = (
                get_best_formative_score(
                    section_id
                )
            )


            with st.container(
                border=True
            ):

                (
                    col1,
                    col2,
                    col3,
                    col4,
                    col5,
                ) = st.columns(
                    [
                        5,
                        1.4,
                        1.4,
                        1.4,
                        1.4,
                    ]
                )


                with col1:

                    icon = (
                        "✅"
                        if completed
                        else "⬜"
                    )

                    st.markdown(
                        f"### {icon} "
                        f"{section_id}. "
                        f"{SECTION_NAMES[section_id]}"
                    )

                    st.caption(
                        message
                    )


                with col2:

                    st.metric(
                        "최근 점수",
                        format_score(
                            data[
                                "formative_score"
                            ]
                        ),
                    )


                with col3:

                    st.metric(
                        "최고 점수",
                        format_score(
                            best_score
                        ),
                    )


                with col4:

                    correct = data[
                        "formative_correct"
                    ]

                    total = data[
                        "formative_total"
                    ]


                    st.metric(
                        "최근 정답",
                        (
                            f"{correct}/{total}"
                            if (
                                correct is not None
                                and total is not None
                            )
                            else "-"
                        ),
                    )


                with col5:

                    st.metric(
                        "응시 횟수",
                        (
                            f"{data['attempt_count']}회"
                        ),
                    )

                    st.caption(
                        status
                    )


# =========================================================
# 형성평가 성장 분석
# =========================================================

with st.container(
    key="edu_section_dashboard_growth"
):

    render_surface_header(
        "형성평가 성장 분석",
        (
            "반복 응시한 형성평가의 점수 변화를 통해 "
            "학습 성장 정도를 확인합니다."
        ),
        "FORMATIVE GROWTH",
    )


    history_sections = []


    for section_id in SECTION_NAMES:

        history = get_formative_history(
            section_id
        )

        if history:

            history_sections.append(
                section_id
            )


    if not history_sections:

        st.info(
            "아직 누적된 형성평가 이력이 없습니다."
        )


    else:

        selected_section = (
            st.selectbox(
                "성장 추이를 확인할 소단원을 선택하세요.",
                options=history_sections,
                format_func=lambda section_id: (
                    f"{section_id}. "
                    f"{SECTION_NAMES[section_id]}"
                ),
                key="dashboard_growth_section",
            )
        )


        history = get_formative_history(
            selected_section
        )

        first_score = (
            get_first_formative_score(
                selected_section
            )
        )

        latest_score = (
            history[-1]["score"]
        )

        best_score = (
            get_best_formative_score(
                selected_section
            )
        )

        improvement = (
            get_formative_improvement(
                selected_section
            )
        )


        (
            col1,
            col2,
            col3,
            col4,
        ) = st.columns(
            4
        )


        with col1:

            st.metric(
                "최초 점수",
                format_score(
                    first_score
                ),
            )


        with col2:

            st.metric(
                "최근 점수",
                format_score(
                    latest_score
                ),
            )


        with col3:

            st.metric(
                "최고 점수",
                format_score(
                    best_score
                ),
            )


        with col4:

            st.metric(
                "최초 대비",
                format_improvement(
                    improvement
                ),
            )


        growth_title, growth_message = (
            get_growth_message(
                history
            )
        )


        st.info(
            f"**{growth_title}**  \n"
            f"{growth_message}"
        )


        st.markdown(
            "### 📊 점수 변화"
        )


        chart_data = pd.DataFrame(
            {
                "응시 회차": [
                    item[
                        "attempt"
                    ]
                    for item
                    in history
                ],

                "점수": [
                    item[
                        "score"
                    ]
                    for item
                    in history
                ],
            }
        ).set_index(
            "응시 회차"
        )


        st.line_chart(
            chart_data,
            height=300,
        )


        st.markdown(
            "### 🗂️ 응시 이력"
        )


        for item in history:

            with st.container(
                border=True
            ):

                col1, col2, col3 = (
                    st.columns(
                        [
                            1,
                            2,
                            2,
                        ]
                    )
                )


                with col1:

                    st.markdown(
                        f"### {item['attempt']}회차"
                    )


                with col2:

                    st.metric(
                        "점수",
                        f"{item['score']}점",
                    )


                with col3:

                    st.metric(
                        "정답",
                        (
                            f"{item['correct']}"
                            f"/{item['total']}"
                        ),
                    )


# =========================================================
# 중간고사 분석
# =========================================================

with st.container(
    key="edu_section_dashboard_midterm"
):

    render_surface_header(
        "중간고사 모의고사 분석",
        (
            "중간고사 종합 대비의 누적 응시 결과와 "
            "점수 변화를 확인합니다."
        ),
        "MIDTERM ANALYTICS",
    )


    if not midterm_results:

        st.info(
            "아직 중간고사 모의고사 응시 기록이 없습니다."
        )


    else:

        (
            col1,
            col2,
            col3,
            col4,
            col5,
        ) = st.columns(
            5
        )


        with col1:

            st.metric(
                "총 응시",
                f"{midterm_attempt_count}회",
            )


        with col2:

            st.metric(
                "최근 점수",
                format_score(
                    midterm_latest_score
                ),
            )


        with col3:

            st.metric(
                "최고 점수",
                format_score(
                    midterm_best_score
                ),
            )


        with col4:

            st.metric(
                "평균 점수",
                format_score(
                    midterm_average_score
                ),
            )


        with col5:

            st.metric(
                "첫 시험 대비",
                format_improvement(
                    midterm_improvement
                ),
            )


        if len(
            midterm_results
        ) >= 2:

            st.markdown(
                "### 📈 모의고사 점수 변화"
            )


            midterm_chart = (
                pd.DataFrame(
                    {
                        "응시 회차": [
                            int(
                                item.get(
                                    "attempt_no",
                                    0,
                                )
                                or 0
                            )
                            for item
                            in midterm_results
                        ],

                        "점수": [
                            float(
                                item.get(
                                    "score",
                                    0,
                                )
                                or 0
                            )
                            for item
                            in midterm_results
                        ],
                    }
                )
                .set_index(
                    "응시 회차"
                )
            )


            st.line_chart(
                midterm_chart,
                height=300,
            )


        st.markdown(
            "### 🗂️ 모의고사 응시 기록"
        )


        for item in reversed(
            midterm_results
        ):

            attempt_no = int(
                item.get(
                    "attempt_no",
                    0,
                )
                or 0
            )

            score = float(
                item.get(
                    "score",
                    0,
                )
                or 0
            )

            correct = int(
                item.get(
                    "correct",
                    0,
                )
                or 0
            )

            total = int(
                item.get(
                    "total",
                    0,
                )
                or 0
            )

            wrong_count = int(
                item.get(
                    "wrong_count",
                    0,
                )
                or 0
            )


            with st.container(
                border=True
            ):

                (
                    record_col1,
                    record_col2,
                    record_col3,
                    record_col4,
                ) = st.columns(
                    [
                        1.2,
                        2,
                        2,
                        2,
                    ]
                )


                with record_col1:

                    st.markdown(
                        f"### {attempt_no}회차"
                    )


                with record_col2:

                    st.metric(
                        "점수",
                        format_score(
                            score
                        ),
                    )


                with record_col3:

                    st.metric(
                        "정답",
                        f"{correct}/{total}",
                    )


                with record_col4:

                    st.metric(
                        "오답",
                        f"{wrong_count}문제",
                    )


# =========================================================
# 누적 오답 분석
# =========================================================

with st.container(
    key="edu_section_dashboard_wrong"
):

    render_surface_header(
        "누적 오답 분석",
        (
            "중간고사 모의시험에서 반복적으로 틀린 "
            "소단원, 주제, 난이도를 분석합니다."
        ),
        "WRONG ANSWER ANALYTICS",
    )


    if not wrong_answers:

        st.info(
            "저장된 오답 기록이 없습니다."
        )


    else:

        (
            wrong_col1,
            wrong_col2,
            wrong_col3,
        ) = st.columns(
            3
        )


        with wrong_col1:

            st.metric(
                "누적 오답",
                f"{total_wrong_answers}문제",
            )


        with wrong_col2:

            if most_wrong_section:

                section_id = (
                    most_wrong_section[
                        0
                    ]
                )

                section_count = (
                    most_wrong_section[
                        1
                    ]
                )


                st.metric(
                    "가장 많이 틀린 소단원",
                    section_id,
                )

                st.caption(
                    (
                        f"{SECTION_NAMES.get(section_id, '')} · "
                        f"{section_count}회"
                    )
                )

            else:

                st.metric(
                    "가장 많이 틀린 소단원",
                    "-",
                )


        with wrong_col3:

            if most_wrong_topic:

                st.metric(
                    "가장 많이 틀린 주제",
                    most_wrong_topic[
                        0
                    ],
                )

                st.caption(
                    f"{most_wrong_topic[1]}회"
                )

            else:

                st.metric(
                    "가장 많이 틀린 주제",
                    "-",
                )


        # -------------------------------------------------
        # 소단원별 오답
        # -------------------------------------------------

        st.markdown(
            "### 📚 소단원별 오답"
        )


        section_wrong_rows = []


        for (
            section_id,
            count,
        ) in section_wrong_counter.most_common():

            section_wrong_rows.append(
                {
                    "소단원": section_id,

                    "학습 내용": SECTION_NAMES.get(
                        section_id,
                        section_id,
                    ),

                    "오답 수": count,
                }
            )


        if section_wrong_rows:

            st.dataframe(
                pd.DataFrame(
                    section_wrong_rows
                ),
                hide_index=True,
                width="stretch",
            )


        # -------------------------------------------------
        # 난이도별 오답
        # -------------------------------------------------

        st.markdown(
            "### 🎚️ 난이도별 오답"
        )


        difficulty_order = [
            "쉬움",
            "보통",
            "어려움",
        ]


        difficulty_cols = st.columns(
            3
        )


        for col, difficulty in zip(
            difficulty_cols,
            difficulty_order,
        ):

            with col:

                st.metric(
                    difficulty,
                    (
                        f"{difficulty_wrong_counter.get(
                            difficulty,
                            0,
                        )}문제"
                    ),
                )


        # -------------------------------------------------
        # 많이 틀린 주제
        # -------------------------------------------------

        st.markdown(
            "### 🧠 자주 틀린 주제"
        )


        top_topics = (
            topic_wrong_counter.most_common(
                5
            )
        )


        if top_topics:

            for index, (
                topic,
                count,
            ) in enumerate(
                top_topics,
                start=1,
            ):

                with st.container(
                    border=True
                ):

                    col1, col2 = st.columns(
                        [
                            5,
                            1,
                        ]
                    )

                    with col1:

                        st.markdown(
                            f"**{index}. {topic}**"
                        )

                    with col2:

                        st.metric(
                            "오답",
                            f"{count}회",
                        )


        # -------------------------------------------------
        # 최근 오답
        # -------------------------------------------------

        st.markdown(
            "### 📝 최근 오답"
        )


        recent_wrong_answers = list(
            reversed(
                wrong_answers[
                    -5:
                ]
            )
        )


        for item in (
            recent_wrong_answers
        ):

            section_id = str(
                item.get(
                    "section_id",
                    "",
                )
            )

            topic = str(
                item.get(
                    "topic",
                    "",
                )
            )

            difficulty = str(
                item.get(
                    "difficulty",
                    "",
                )
            )

            user_answer = str(
                item.get(
                    "user_answer",
                    "",
                )
            )

            correct_answer = str(
                item.get(
                    "correct_answer",
                    "",
                )
            )


            with st.expander(
                (
                    f"❌ {section_id} · "
                    f"{topic} · "
                    f"{difficulty}"
                )
            ):

                st.markdown(
                    f"**내 답**  \n"
                    f"{user_answer or '-'}"
                )

                st.markdown(
                    f"**정답**  \n"
                    f"{correct_answer or '-'}"
                )


# =========================================================
# 종합 성취도 분석
# =========================================================

with st.container(
    key="edu_section_dashboard_achievement"
):

    render_surface_header(
        "나의 성취도 분석",
        (
            "형성평가와 누적 오답을 함께 참고하여 "
            "강점 영역과 복습 우선 영역을 확인합니다."
        ),
        "ACHIEVEMENT",
    )


    scored_sections = []


    for (
        section_id,
        data,
    ) in progress_data.items():

        score = data[
            "formative_score"
        ]

        if score is None:
            continue


        scored_sections.append(
            {
                "section_id": section_id,

                "name": SECTION_NAMES[
                    section_id
                ],

                "score": score,

                "attempt_count": data[
                    "attempt_count"
                ],
            }
        )


    if not scored_sections:

        st.info(
            "아직 분석할 형성평가 결과가 없습니다."
        )


    else:

        strong_sections = [
            item
            for item
            in scored_sections
            if item[
                "score"
            ] >= 90
        ]


        review_sections = [
            item
            for item
            in scored_sections
            if item[
                "score"
            ] < 70
        ]


        strong_col, review_col = (
            st.columns(
                2
            )
        )


        with strong_col:

            with st.container(
                border=True
            ):

                st.markdown(
                    "### 💪 강점 영역"
                )


                if strong_sections:

                    for item in sorted(
                        strong_sections,
                        key=lambda value: (
                            value[
                                "score"
                            ]
                        ),
                        reverse=True,
                    ):

                        st.markdown(
                            f"🏆 **"
                            f"{item['section_id']} "
                            f"{item['name']}**"
                        )

                        st.caption(
                            (
                                f"최근 형성평가 "
                                f"{item['score']}점"
                            )
                        )


                else:

                    st.caption(
                        "아직 90점 이상인 형성평가 영역이 없습니다."
                    )


        with review_col:

            with st.container(
                border=True
            ):

                st.markdown(
                    "### 🔥 우선 복습 영역"
                )


                combined_review_ids = set(
                    item[
                        "section_id"
                    ]
                    for item
                    in review_sections
                )


                if most_wrong_section:

                    combined_review_ids.add(
                        most_wrong_section[
                            0
                        ]
                    )


                if combined_review_ids:

                    for section_id in sorted(
                        combined_review_ids
                    ):

                        formative_data = (
                            progress_data.get(
                                section_id,
                                {},
                            )
                        )

                        score = (
                            formative_data.get(
                                "formative_score"
                            )
                        )

                        wrong_count = (
                            section_wrong_counter.get(
                                section_id,
                                0,
                            )
                        )


                        st.markdown(
                            f"⚠️ **"
                            f"{section_id} · "
                            f"{SECTION_NAMES.get(
                                section_id,
                                section_id,
                            )}**"
                        )


                        details = []


                        if score is not None:

                            details.append(
                                f"형성평가 {score}점"
                            )


                        if wrong_count:

                            details.append(
                                f"누적 오답 {wrong_count}회"
                            )


                        st.caption(
                            " · ".join(
                                details
                            )
                        )


                else:

                    st.success(
                        "현재 특별히 우선 복습이 필요한 영역이 없습니다."
                    )


# =========================================================
# 다음 학습 추천
# =========================================================

with st.container(
    key="edu_section_dashboard_next"
):

    render_surface_header(
        "다음 학습 추천",
        (
            "현재 학습 진도와 평가 결과를 기준으로 "
            "다음 학습 방향을 안내합니다."
        ),
        "NEXT STEP",
    )


    next_section_id = None


    for lesson_id in LESSON_STRUCTURE:

        for section_id in (
            LESSON_STRUCTURE[
                lesson_id
            ]
        ):

            if not is_section_completed(
                section_id
            ):

                next_section_id = (
                    section_id
                )

                break


        if next_section_id:
            break


    if next_section_id:

        lesson_id = (
            next_section_id.split(
                "-"
            )[0]
        )


        with st.container(
            border=True
        ):

            st.markdown(
                "### ▶️ 다음 학습"
            )

            st.markdown(
                f"**{next_section_id}. "
                f"{SECTION_NAMES[next_section_id]}**"
            )

            st.caption(
                "형성평가까지 완료하면 진도에 반영됩니다."
            )

            st.page_link(
                lesson_links[
                    lesson_id
                ],
                label=(
                    f"학습 {lesson_id}으로 이동"
                ),
                width="stretch",
            )


    else:

        st.success(
            "🎉 모든 소단원을 완료했습니다!"
        )


    if most_wrong_section:

        review_section_id = (
            most_wrong_section[
                0
            ]
        )

        wrong_count = (
            most_wrong_section[
                1
            ]
        )


        if review_section_id in SECTION_NAMES:

            lesson_id = (
                review_section_id.split(
                    "-"
                )[0]
            )


            with st.container(
                border=True
            ):

                st.markdown(
                    "### 🔄 오답 기반 복습 추천"
                )

                st.markdown(
                    f"**{review_section_id}. "
                    f"{SECTION_NAMES[review_section_id]}**"
                )

                st.caption(
                    (
                        f"중간고사 모의시험에서 "
                        f"{wrong_count}회 오답이 기록된 영역입니다."
                    )
                )

                st.page_link(
                    lesson_links[
                        lesson_id
                    ],
                    label="📘 해당 학습 복습하기",
                    width="stretch",
                )


# =========================================================
# 중간고사 바로가기
# =========================================================

with st.container(
    key="edu_section_dashboard_exam"
):

    render_surface_header(
        "중간고사 준비",
        (
            "학습 진도와 오답을 확인한 뒤 "
            "다시 종합 모의고사에 도전해보세요."
        ),
        "MIDTERM",
    )


    exam_col1, exam_col2 = (
        st.columns(
            [
                3,
                1,
            ]
        )
    )


    with exam_col1:

        if midterm_attempt_count == 0:

            st.info(
                "아직 모의고사를 응시하지 않았습니다."
            )

        elif (
            midterm_latest_score
            is not None
            and midterm_latest_score
            >= 90
        ):

            st.success(
                "🏆 최근 모의고사 성취도가 매우 안정적입니다."
            )

        elif (
            midterm_latest_score
            is not None
            and midterm_latest_score
            >= 80
        ):

            st.info(
                "✅ 좋은 수준입니다. 누적 오답을 복습한 뒤 다시 도전해보세요."
            )

        else:

            st.warning(
                "📘 취약 영역을 복습한 뒤 모의고사에 다시 도전하는 것을 권장합니다."
            )


    with exam_col2:

        st.page_link(
            "pages/05_중간고사_종합대비.py",
            label="🎯 종합 모의고사",
            width="stretch",
        )


# =========================================================
# 기록 안내
# =========================================================

with st.expander(
    "ℹ️ 학습 기록 안내"
):

    st.markdown(
        """
        로그인한 Google 계정을 기준으로 학습 기록을 관리합니다.

        - `progress` : 소단원 완료 상태
        - `formative_results` : 형성평가 응시 이력
        - `midterm_results` : 중간고사 모의고사 응시 이력
        - `wrong_answers` : 중간고사 누적 오답
        - 다른 기기에서 다시 로그인해도 Google Sheets에 저장된
          기록을 다시 불러옵니다.
        """
    )


# =========================================================
# 하단
# =========================================================

st.caption(
    "📊 Learning Analytics Dashboard · "
    "진도 · 형성평가 · 중간고사 · 누적 오답"
)