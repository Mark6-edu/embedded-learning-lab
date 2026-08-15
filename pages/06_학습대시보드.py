from __future__ import annotations

import pandas as pd
import streamlit as st

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


# =========================================================
# Helper Functions
# =========================================================

def progress_status(
    progress: float,
) -> str:
    """
    학습 영역의 진도 상태를 반환한다.
    """

    if progress >= 100:
        return "✅ 완료"

    if progress > 0:
        return "⏳ 학습 중"

    return "⬜ 시작 전"


def score_status(
    score: int | float | None,
) -> tuple[str, str]:
    """
    최근 형성평가 점수를 기준으로
    성취 상태와 설명을 반환한다.
    """

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


def format_percent(
    value: float,
) -> str:
    """
    백분율을 보기 좋게 변환한다.
    """

    if float(value).is_integer():
        return f"{value:.0f}%"

    return f"{value:.1f}%"


def format_improvement(
    improvement: int | float | None,
) -> str:
    """
    점수 향상도를 표시한다.
    """

    if improvement is None:
        return "-"

    if improvement > 0:
        return f"+{improvement}점"

    if improvement < 0:
        return f"{improvement}점"

    return "0점"


def get_growth_message(
    history: list[dict],
) -> tuple[str, str]:
    """
    형성평가 이력을 바탕으로 성장 상태를 해석한다.
    """

    if len(history) < 2:

        return (
            "🌱 첫 학습 기록",
            "한 번 더 도전하면 점수 변화와 성장 정도를 분석할 수 있습니다.",
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
                f"최초 점수보다 {improvement}점 향상되었습니다. "
                "복습과 재도전의 효과가 뚜렷합니다."
            ),
        )

    if improvement > 0:

        return (
            "📈 점수 상승",
            (
                f"최초 점수보다 {improvement}점 향상되었습니다. "
                "현재 학습 방법을 계속 유지해보세요."
            ),
        )

    if improvement == 0:

        return (
            "➡️ 점수 유지",
            (
                "최초 점수와 최근 점수가 같습니다. "
                "같은 문제를 반복하기보다 오답 개념을 중심으로 "
                "복습해보세요."
            ),
        )

    return (
        "📉 점수 하락",
        (
            f"최초 점수보다 {abs(improvement)}점 낮아졌습니다. "
            "최근 틀린 내용을 중심으로 다시 확인해보세요."
        ),
    )


# =========================================================
# 데이터 불러오기
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

st.sidebar.caption(
    "현재 학습 영역"
)

st.sidebar.markdown(
    "📊 **나의 학습 대시보드**"
)


# =========================================================
# 페이지 상단
# =========================================================

render_breadcrumb(
    "홈",
    "학습 대시보드",
)

st.title(
    "📊 나의 학습 대시보드"
)

st.markdown(
    """
    지금까지의 **학습 진도, 형성평가 성취도,
    재도전 기록과 점수 변화**를 한눈에 확인합니다.

    **진도율은 형성평가 제출 여부**,  
    **성취 수준은 형성평가 점수**,  
    **성장 정도는 반복 응시의 점수 변화**를 기준으로 분석합니다.
    """
)


# =========================================================
# 핵심 지표
# =========================================================

st.markdown(
    "## 🎯 학습 현황 요약"
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

    if formative_average is None:

        average_text = "-"

    else:

        average_text = (
            f"{formative_average:.1f}점"
        )

    st.metric(
        "최근 점수 평균",
        average_text,
    )

with metric_col4:

    if all_attempt_average is None:

        all_average_text = "-"

    else:

        all_average_text = (
            f"{all_attempt_average:.1f}점"
        )

    st.metric(
        "전체 응시 평균",
        all_average_text,
    )

with metric_col5:

    st.metric(
        "총 응시 횟수",
        f"{total_attempts}회",
    )


# =========================================================
# 전체 진도
# =========================================================

st.markdown(
    "### 📚 전체 학습 진도"
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
        "🎉 학습 1~4의 모든 소단원을 완료했습니다!"
    )

elif overall_progress >= 75:

    st.info(
        "🚀 거의 다 왔습니다. "
        "남은 소단원을 마무리해보세요."
    )

elif overall_progress >= 50:

    st.info(
        "📘 전체 범위의 절반 이상을 완료했습니다."
    )

elif overall_progress > 0:

    st.info(
        "🌱 학습이 시작되었습니다. "
        "완료하지 않은 소단원을 이어서 진행해보세요."
    )

else:

    st.info(
        "학습을 시작하면 이곳에 진행 상황이 표시됩니다."
    )


# =========================================================
# 학습 영역별 진도
# =========================================================

st.divider()

st.markdown(
    "## 📚 학습 영역별 진도"
)

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
                use_container_width=True,
            )


# =========================================================
# 소단원별 상세 현황
# =========================================================

st.divider()

st.markdown(
    "## 🧩 소단원별 학습 현황"
)

st.caption(
    "형성평가 제출 여부와 최근 점수, 최고 점수, 응시 횟수를 확인합니다."
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
                [5, 1.4, 1.4, 1.4, 1.5]
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

                score = data[
                    "formative_score"
                ]

                st.metric(
                    "최근 점수",
                    (
                        f"{score}점"
                        if score is not None
                        else "-"
                    ),
                )

            with col3:

                st.metric(
                    "최고 점수",
                    (
                        f"{best_score}점"
                        if best_score is not None
                        else "-"
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
# 학습 성장 분석
# =========================================================

st.divider()

st.markdown(
    "## 📈 형성평가 성장 분석"
)

st.caption(
    "형성평가를 다시 풀었을 때 점수가 어떻게 변화했는지 확인합니다."
)


# ---------------------------------------------------------
# history가 존재하는 소단원
# ---------------------------------------------------------

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
        "아직 누적된 형성평가 이력이 없습니다. "
        "형성평가를 다시 제출하면 이곳에 성장 그래프가 나타납니다."
    )

else:

    # -----------------------------------------------------
    # 분석할 소단원 선택
    # -----------------------------------------------------

    selected_section = st.selectbox(
        "성장 추이를 확인할 소단원을 선택하세요.",
        options=history_sections,
        format_func=lambda section_id: (
            f"{section_id}. "
            f"{SECTION_NAMES[section_id]}"
        ),
        key="dashboard_growth_section",
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
        history[-1][
            "score"
        ]
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


    # -----------------------------------------------------
    # 성장 요약
    # -----------------------------------------------------

    (
        growth_col1,
        growth_col2,
        growth_col3,
        growth_col4,
    ) = st.columns(
        4
    )

    with growth_col1:

        st.metric(
            "최초 점수",
            f"{first_score}점",
        )

    with growth_col2:

        st.metric(
            "최근 점수",
            f"{latest_score}점",
        )

    with growth_col3:

        st.metric(
            "최고 점수",
            f"{best_score}점",
        )

    with growth_col4:

        st.metric(
            "최초 대비",
            format_improvement(
                improvement
            ),
        )


    # -----------------------------------------------------
    # 성장 상태 해석
    # -----------------------------------------------------

    growth_title, growth_message = (
        get_growth_message(
            history
        )
    )

    with st.container(
        border=True
    ):

        st.markdown(
            f"### {growth_title}"
        )

        st.write(
            growth_message
        )


    # -----------------------------------------------------
    # 성장 그래프
    # -----------------------------------------------------

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
    )

    chart_data = chart_data.set_index(
        "응시 회차"
    )

    st.line_chart(
        chart_data,
        height=320,
    )


    # -----------------------------------------------------
    # 점수 변화 문자열
    # -----------------------------------------------------

    score_flow = " → ".join(
        (
            f"{item['score']}점"
        )
        for item
        in history
    )

    st.info(
        f"📈 점수 흐름 · {score_flow}"
    )


    # -----------------------------------------------------
    # 응시 이력
    # -----------------------------------------------------

    st.markdown(
        "### 🗂️ 응시 이력"
    )

    for item in history:

        with st.container(
            border=True
        ):

            col1, col2, col3 = st.columns(
                [1, 2, 2]
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
# 재도전 분석
# =========================================================

st.divider()

st.markdown(
    "## 🔄 재도전 분석"
)


if total_attempts == 0:

    st.info(
        "형성평가 응시 기록이 아직 없습니다."
    )

else:

    retry_col1, retry_col2 = st.columns(
        2
    )

    with retry_col1:

        with st.container(
            border=True
        ):

            st.markdown(
                "### 🔢 전체 형성평가 응시"
            )

            st.metric(
                "총 응시",
                f"{total_attempts}회",
            )

            if all_attempt_average is not None:

                st.metric(
                    "전체 응시 평균",
                    f"{all_attempt_average:.1f}점",
                )


    with retry_col2:

        with st.container(
            border=True
        ):

            st.markdown(
                "### 🔁 가장 많이 도전한 영역"
            )

            if most_retried:

                retried_id = (
                    most_retried[
                        "section_id"
                    ]
                )

                st.markdown(
                    f"**{retried_id}. "
                    f"{SECTION_NAMES[retried_id]}**"
                )

                st.metric(
                    "응시 횟수",
                    (
                        f"{most_retried['attempt_count']}회"
                    ),
                )

            else:

                st.write(
                    "응시 기록이 없습니다."
                )


# =========================================================
# 성취도 분석
# =========================================================

st.divider()

st.markdown(
    "## 🧠 나의 성취도 분석"
)


scored_sections = []

for section_id, data in (
    progress_data.items()
):

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

    sorted_by_score = sorted(
        scored_sections,
        key=lambda item: item[
            "score"
        ],
        reverse=True,
    )

    strong_sections = [
        item
        for item
        in sorted_by_score
        if item[
            "score"
        ] >= 90
    ]

    review_sections = [
        item
        for item
        in sorted_by_score
        if item[
            "score"
        ] < 70
    ]


    strong_col, review_col = st.columns(
        2
    )

    with strong_col:

        with st.container(
            border=True
        ):

            st.markdown(
                "### 💪 강점 영역"
            )

            if strong_sections:

                for item in strong_sections:

                    st.markdown(
                        f"🏆 **{item['section_id']} "
                        f"{item['name']}**"
                    )

                    st.caption(
                        f"최근 형성평가 "
                        f"{item['score']}점"
                    )

            else:

                best = sorted_by_score[
                    0
                ]

                st.markdown(
                    f"현재 최고 성취 영역은 "
                    f"**{best['section_id']} "
                    f"{best['name']}**입니다."
                )

                st.caption(
                    f"최근 형성평가 "
                    f"{best['score']}점"
                )


    with review_col:

        with st.container(
            border=True
        ):

            st.markdown(
                "### 🔥 우선 복습 영역"
            )

            if review_sections:

                for item in sorted(
                    review_sections,
                    key=lambda value: value[
                        "score"
                    ],
                ):

                    st.markdown(
                        f"⚠️ **{item['section_id']} "
                        f"{item['name']}**"
                    )

                    st.caption(
                        f"최근 형성평가 "
                        f"{item['score']}점 · "
                        f"응시 {item['attempt_count']}회"
                    )

            else:

                st.success(
                    "현재 형성평가 70점 미만인 "
                    "소단원이 없습니다."
                )


# =========================================================
# 최근 점수 현황
# =========================================================

if scored_sections:

    st.markdown(
        "### 📊 소단원별 최근 점수"
    )

    for item in sorted(
        scored_sections,
        key=lambda value: value[
            "section_id"
        ],
    ):

        score = item[
            "score"
        ]

        with st.container(
            border=True
        ):

            label_col, score_col = (
                st.columns(
                    [5, 1]
                )
            )

            with label_col:

                st.markdown(
                    f"**{item['section_id']} · "
                    f"{item['name']}**"
                )

                st.progress(
                    score / 100
                )

            with score_col:

                st.metric(
                    "최근 점수",
                    f"{score}점",
                )


# =========================================================
# 다음 학습 추천
# =========================================================

st.divider()

st.markdown(
    "## 🧭 다음 학습 추천"
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
            "### ▶️ 아직 완료하지 않은 다음 학습"
        )

        st.markdown(
            f"**{next_section_id}. "
            f"{SECTION_NAMES[next_section_id]}**"
        )

        st.caption(
            "형성평가까지 완료하면 "
            "학습 진도에 반영됩니다."
        )

        st.page_link(
            lesson_links[
                lesson_id
            ],
            label=(
                f"학습 {lesson_id}으로 이동"
            ),
            use_container_width=True,
        )

else:

    st.success(
        "🎉 모든 소단원을 완료했습니다!"
    )


# ---------------------------------------------------------
# 낮은 점수 복습 추천
# ---------------------------------------------------------

if scored_sections:

    lowest_section = min(
        scored_sections,
        key=lambda item: item[
            "score"
        ],
    )

    if lowest_section[
        "score"
    ] < 80:

        lesson_id = (
            lowest_section[
                "section_id"
            ].split(
                "-"
            )[0]
        )

        with st.container(
            border=True
        ):

            st.markdown(
                "### 🔄 복습하면 좋은 영역"
            )

            st.markdown(
                f"**{lowest_section['section_id']} · "
                f"{lowest_section['name']}**"
            )

            st.caption(
                f"최근 형성평가 "
                f"{lowest_section['score']}점입니다. "
                f"핵심 개념과 오답을 다시 확인해보세요."
            )

            st.page_link(
                lesson_links[
                    lesson_id
                ],
                label="📘 해당 학습 복습하기",
                use_container_width=True,
            )


# =========================================================
# 중간고사 종합 대비
# =========================================================

st.divider()

st.markdown(
    "## 🎯 중간고사 준비"
)

exam_col1, exam_col2 = st.columns(
    [3, 1]
)

with exam_col1:

    if completed_sections >= 6:

        st.success(
            "시험 범위 학습이 상당 부분 완료되었습니다. "
            "종합 모의고사로 실전 점검을 해보세요."
        )

    elif completed_sections >= 4:

        st.info(
            "절반 이상의 소단원을 완료했습니다. "
            "학습과 모의고사를 병행해도 좋습니다."
        )

    else:

        st.info(
            "이론 학습을 진행하면서 중간고사 종합 대비 문제도 "
            "함께 활용할 수 있습니다."
        )

with exam_col2:

    st.page_link(
        "pages/05_중간고사_종합대비.py",
        label="🎯 종합 모의고사",
        use_container_width=True,
    )


# =========================================================
# 저장 방식 안내
# =========================================================

st.divider()

with st.expander(
    "ℹ️ 학습 기록 안내"
):

    st.markdown(
        """
        현재 학습 기록은 **Streamlit Session State**를 이용합니다.

        - 페이지를 이동해도 기록은 유지됩니다.
        - 형성평가를 다시 제출하면 최근 점수가 갱신됩니다.
        - 각 응시 결과는 `history`에 누적됩니다.
        - 최초 점수, 최근 점수, 최고 점수, 향상도를 분석합니다.
        - 현재 버전에서는 브라우저 세션이나 서버가 초기화되면
          기록이 사라질 수 있습니다.

        이후 필요하면 Firebase나 별도의 데이터베이스를 이용해
        학생별 기록을 영구 저장할 수 있습니다.
        """
    )


# =========================================================
# 하단
# =========================================================

st.divider()

st.caption(
    "📊 학습 대시보드 · "
    "형성평가 진도 · 성취도 · 성장 데이터 기반"
)