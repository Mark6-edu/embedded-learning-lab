from __future__ import annotations

import random
from collections import Counter, defaultdict
from html import escape
from textwrap import dedent
from typing import Any

import pandas as pd
import streamlit as st

from data.quizzes.quiz_1_1 import EXAM_PRACTICE_1_1
from data.quizzes.quiz_1_2 import EXAM_PRACTICE_1_2

from data.quizzes.quiz_2_1 import EXAM_PRACTICE_2_1
from data.quizzes.quiz_2_2 import EXAM_PRACTICE_2_2

from data.quizzes.quiz_3_1 import EXAM_PRACTICE_3_1
from data.quizzes.quiz_3_2 import EXAM_PRACTICE_3_2

from data.quizzes.quiz_4_1 import EXAM_PRACTICE_4_1
from data.quizzes.quiz_4_2 import EXAM_PRACTICE_4_2

from utils.theme import load_global_css

from utils.ui import (
    render_breadcrumb,
    render_progress_bar,
)

from utils.auth import (
    require_login,
    get_current_user,
    render_user_info,
)

from utils.sheets_api import register_student

# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="중간고사 종합 대비",
    page_icon="🎯",
    layout="wide",
)

load_global_css()

require_login()

user = get_current_user()

if user:
    register_result = register_student(
        user_id=user.get("sub", ""),
        email=user.get("email", ""),
        name=user.get("name", ""),
    )

    st.write("학생 등록 테스트:", register_result)

# =========================================================
# 상수
# =========================================================

QUIZ_BANK = {
    "1-1": EXAM_PRACTICE_1_1,
    "1-2": EXAM_PRACTICE_1_2,
    "2-1": EXAM_PRACTICE_2_1,
    "2-2": EXAM_PRACTICE_2_2,
    "3-1": EXAM_PRACTICE_3_1,
    "3-2": EXAM_PRACTICE_3_2,
    "4-1": EXAM_PRACTICE_4_1,
    "4-2": EXAM_PRACTICE_4_2,
}


UNIT_NAMES = {
    "1-1": "기술 스펙 적용 SW 검토",
    "1-2": "임베디드 시스템 평가",
    "2-1": "개발 도구 선정",
    "2-2": "개발 환경 구축",
    "3-1": "애플리케이션 구현 및 오류 제거",
    "3-2": "디버깅 및 프로그램 통합",
    "4-1": "인터페이스 구현",
    "4-2": "소스 코드 저장 및 버전 관리",
}


LESSON_GROUP_NAMES = {
    "1": "학습 1 · 기술 명세 검토",
    "2": "학습 2 · 개발 환경 구축",
    "3": "학습 3 · 모듈 구현",
    "4": "학습 4 · 인터페이스 구현",
}


DIFFICULTY_ORDER = [
    "쉬움",
    "보통",
    "어려움",
]


# =========================================================
# Session State
# =========================================================

DEFAULT_STATE = {
    "midterm_exam_started": False,
    "midterm_exam_finished": False,
    "midterm_exam_questions": [],
    "midterm_exam_units": [],
    "midterm_exam_answers": {},
    "midterm_exam_result": None,
    "midterm_exam_config": {},
    "midterm_exam_history": [],
}


for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        if isinstance(value, list):
            st.session_state[key] = []

        elif isinstance(value, dict):
            st.session_state[key] = {}

        else:
            st.session_state[key] = value


# =========================================================
# HTML Helper
# =========================================================

def render_html(html: str) -> None:
    """
    Markdown Parser를 거치지 않고 HTML 직접 렌더링.
    """

    st.html(
        dedent(html).strip()
    )


def render_surface_header(
    title: str,
    description: str | None = None,
    label: str | None = None,
) -> None:

    label_html = ""

    if label:
        label_html = (
            '<div class="edu-surface-label">'
            f"{escape(str(label))}"
            "</div>"
        )

    description_html = ""

    if description:
        description_html = (
            '<div class="edu-surface-desc">'
            f"{escape(str(description))}"
            "</div>"
        )

    render_html(
        f"""
        {label_html}

        <div class="edu-surface-title">
            {escape(str(title))}
        </div>

        {description_html}
        """
    )


def render_pills(
    items: list[str],
) -> None:

    if not items:
        return

    pills_html = "".join(
        (
            '<span class="edu-pill">'
            f"{escape(str(item))}"
            "</span>"
        )
        for item in items
    )

    render_html(
        f"""
        <div class="edu-pills">
            {pills_html}
        </div>
        """
    )


def render_exam_notice(
    title: str,
    content: str,
) -> None:

    render_html(
        f"""
        <div class="edu-concept">

            <div class="edu-concept-title">
                {escape(title)}
            </div>

            <div class="edu-concept-body">
                {escape(content)}
            </div>

        </div>
        """
    )


# =========================================================
# Question Helper
# =========================================================

def question_id(question: Any) -> str:

    return str(
        getattr(
            question,
            "id",
            id(question),
        )
    )


def question_type(question: Any) -> str:

    value = str(
        getattr(
            question,
            "type",
            "",
        )
    ).strip().lower()

    aliases = {
        "multiple_choice": "multiple_choice",
        "multiple-choice": "multiple_choice",
        "mcq": "multiple_choice",
        "객관식": "multiple_choice",

        "true_false": "true_false",
        "true-false": "true_false",
        "ox": "true_false",
        "o/x": "true_false",
        "참거짓": "true_false",

        "short_answer": "short_answer",
        "short-answer": "short_answer",
        "단답형": "short_answer",
        "주관식": "short_answer",
    }

    return aliases.get(
        value,
        value,
    )


def normalize_text(value: Any) -> str:

    if value is None:
        return ""

    return (
        str(value)
        .strip()
        .lower()
        .replace(" ", "")
        .replace("\n", "")
    )


def answer_candidates(answer: Any) -> list[Any]:

    if isinstance(
        answer,
        (
            list,
            tuple,
            set,
        ),
    ):
        return list(answer)

    return [answer]


def is_correct(
    question: Any,
    user_answer: Any,
) -> bool:

    if user_answer is None:
        return False

    correct_answers = answer_candidates(
        getattr(
            question,
            "answer",
            "",
        )
    )

    normalized_user = normalize_text(
        user_answer
    )

    return any(
        normalized_user
        == normalize_text(correct)
        for correct in correct_answers
    )


def correct_answer_text(
    question: Any,
) -> str:

    answers = answer_candidates(
        getattr(
            question,
            "answer",
            "",
        )
    )

    return " / ".join(
        str(answer)
        for answer in answers
    )


def question_unit(
    question: Any,
) -> str:

    qid = question_id(
        question
    )

    parts = qid.split("_")

    if len(parts) >= 2:

        candidate = (
            f"{parts[0]}-{parts[1]}"
        )

        if candidate in QUIZ_BANK:
            return candidate

    return "기타"


def question_difficulty(
    question: Any,
) -> str:

    value = str(
        getattr(
            question,
            "difficulty",
            "보통",
        )
    ).strip()

    return value or "보통"


def question_topic(
    question: Any,
) -> str:

    value = str(
        getattr(
            question,
            "topic",
            "",
        )
    ).strip()

    return value or "기타"


# =========================================================
# 문제 Widget
# =========================================================

def render_exam_question(
    question: Any,
    number: int,
) -> Any:

    qid = question_id(
        question
    )

    qtype = question_type(
        question
    )

    question_text = str(
        getattr(
            question,
            "question",
            "",
        )
    )

    passage = str(
        getattr(
            question,
            "passage",
            "",
        )
    ).strip()

    unit = question_unit(
        question
    )

    difficulty = question_difficulty(
        question
    )

    topic = question_topic(
        question
    )


    with st.container(
        key=f"midterm_question_{qid}"
    ):

        header_col, difficulty_col = st.columns(
            [7, 2]
        )

        with header_col:

            st.markdown(
                f"### {number}. {question_text}"
            )

        with difficulty_col:

            st.caption(
                f"{unit} · {difficulty}"
            )


        if topic != "기타":

            st.caption(
                f"주제: {topic}"
            )


        if passage:

            code_keywords = [
                "(gdb)",
                "gcc ",
                "make ",
                "git ",
                "svn ",
            ]

            is_code_passage = any(
                keyword in passage
                for keyword in code_keywords
            )

            if is_code_passage:

                st.code(
                    passage,
                    language="text",
                )

            else:

                st.info(
                    passage
                )


        widget_key = (
            f"midterm_answer_{qid}"
        )


        if qtype == "multiple_choice":

            options = list(
                getattr(
                    question,
                    "options",
                    [],
                )
                or []
            )

            value = st.radio(
                "답을 선택하세요.",
                options,
                index=None,
                key=widget_key,
                label_visibility="collapsed",
            )


        elif qtype == "true_false":

            options = list(
                getattr(
                    question,
                    "options",
                    [],
                )
                or []
            )

            if not options:
                options = [
                    "O",
                    "X",
                ]

            value = st.radio(
                "O / X",
                options,
                index=None,
                horizontal=True,
                key=widget_key,
                label_visibility="collapsed",
            )


        elif qtype == "short_answer":

            value = st.text_input(
                "답을 입력하세요.",
                key=widget_key,
                placeholder="정답 입력",
                label_visibility="collapsed",
            )


        else:

            options = list(
                getattr(
                    question,
                    "options",
                    [],
                )
                or []
            )

            if options:

                value = st.radio(
                    "답을 선택하세요.",
                    options,
                    index=None,
                    key=widget_key,
                    label_visibility="collapsed",
                )

            else:

                value = st.text_input(
                    "답을 입력하세요.",
                    key=widget_key,
                    label_visibility="collapsed",
                )


        st.session_state[
            "midterm_exam_answers"
        ][qid] = value

        return value


# =========================================================
# 문제 Bank
# =========================================================

def filtered_question_pool(
    selected_units: list[str],
    selected_difficulties: list[str],
) -> list[Any]:

    questions: list[Any] = []

    for unit in selected_units:

        for question in QUIZ_BANK[
            unit
        ]:

            difficulty = (
                question_difficulty(
                    question
                )
            )

            if (
                not selected_difficulties
                or difficulty
                in selected_difficulties
            ):

                questions.append(
                    question
                )

    return questions


# =========================================================
# Exam Start / Reset
# =========================================================

def start_exam(
    selected_units: list[str],
    selected_difficulties: list[str],
    question_count: int,
) -> None:

    pool = filtered_question_pool(
        selected_units,
        selected_difficulties,
    )

    actual_count = min(
        question_count,
        len(pool),
    )

    selected_questions = random.sample(
        pool,
        actual_count,
    )

    st.session_state[
        "midterm_exam_questions"
    ] = selected_questions

    st.session_state[
        "midterm_exam_units"
    ] = selected_units.copy()

    st.session_state[
        "midterm_exam_answers"
    ] = {}

    st.session_state[
        "midterm_exam_result"
    ] = None

    st.session_state[
        "midterm_exam_config"
    ] = {
        "units": selected_units.copy(),
        "difficulties": selected_difficulties.copy(),
        "question_count": actual_count,
    }

    st.session_state[
        "midterm_exam_started"
    ] = True

    st.session_state[
        "midterm_exam_finished"
    ] = False


def clear_active_exam() -> None:

    st.session_state[
        "midterm_exam_started"
    ] = False

    st.session_state[
        "midterm_exam_finished"
    ] = False

    st.session_state[
        "midterm_exam_questions"
    ] = []

    st.session_state[
        "midterm_exam_units"
    ] = []

    st.session_state[
        "midterm_exam_answers"
    ] = {}

    st.session_state[
        "midterm_exam_result"
    ] = None

    st.session_state[
        "midterm_exam_config"
    ] = {}


# =========================================================
# Grading
# =========================================================

def grade_exam() -> dict[str, Any]:

    questions = st.session_state[
        "midterm_exam_questions"
    ]

    answers = st.session_state[
        "midterm_exam_answers"
    ]


    correct_count = 0

    unit_stats: dict[str, dict[str, int]] = (
        defaultdict(
            lambda: {
                "correct": 0,
                "total": 0,
            }
        )
    )

    difficulty_stats: dict[
        str,
        dict[str, int],
    ] = defaultdict(
        lambda: {
            "correct": 0,
            "total": 0,
        }
    )

    topic_stats: dict[
        str,
        dict[str, int],
    ] = defaultdict(
        lambda: {
            "correct": 0,
            "total": 0,
        }
    )

    question_results = []

    wrong_questions = []


    for question in questions:

        qid = question_id(
            question
        )

        user_answer = answers.get(
            qid
        )

        correct = is_correct(
            question,
            user_answer,
        )

        unit = question_unit(
            question
        )

        difficulty = question_difficulty(
            question
        )

        topic = question_topic(
            question
        )


        unit_stats[
            unit
        ]["total"] += 1

        difficulty_stats[
            difficulty
        ]["total"] += 1

        topic_stats[
            topic
        ]["total"] += 1


        if correct:

            correct_count += 1

            unit_stats[
                unit
            ]["correct"] += 1

            difficulty_stats[
                difficulty
            ]["correct"] += 1

            topic_stats[
                topic
            ]["correct"] += 1


        result_item = {
            "question_id": qid,
            "unit": unit,
            "topic": topic,
            "difficulty": difficulty,
            "question": str(
                getattr(
                    question,
                    "question",
                    "",
                )
            ),
            "user_answer": (
                ""
                if user_answer is None
                else str(user_answer)
            ),
            "correct_answer": (
                correct_answer_text(
                    question
                )
            ),
            "correct": correct,
            "explanation": str(
                getattr(
                    question,
                    "explanation",
                    "",
                )
            ),
        }

        question_results.append(
            result_item
        )

        if not correct:

            wrong_questions.append(
                result_item.copy()
            )


    total_count = len(
        questions
    )

    score = (
        round(
            correct_count
            / total_count
            * 100
        )
        if total_count
        else 0
    )


    def serialize_stats(
        stats: dict,
    ) -> dict:

        serialized = {}

        for name, values in stats.items():

            total = values[
                "total"
            ]

            correct = values[
                "correct"
            ]

            serialized[
                name
            ] = {
                "correct": correct,
                "total": total,
                "score": (
                    round(
                        correct
                        / total
                        * 100
                    )
                    if total
                    else 0
                ),
            }

        return serialized


    result = {
        "score": score,
        "correct_count": correct_count,
        "total_count": total_count,
        "wrong_count": (
            total_count
            - correct_count
        ),
        "unit_stats": serialize_stats(
            unit_stats
        ),
        "difficulty_stats": serialize_stats(
            difficulty_stats
        ),
        "topic_stats": serialize_stats(
            topic_stats
        ),
        "question_results": question_results,
        "wrong_questions": wrong_questions,
    }


    st.session_state[
        "midterm_exam_result"
    ] = result

    st.session_state[
        "midterm_exam_finished"
    ] = True


    save_exam_history(
        result
    )

    return result


# =========================================================
# Exam History
# =========================================================

def save_exam_history(
    result: dict[str, Any],
) -> None:

    history = st.session_state[
        "midterm_exam_history"
    ]

    attempt = (
        len(history) + 1
    )

    config = st.session_state[
        "midterm_exam_config"
    ]


    history_item = {
        "attempt": attempt,
        "score": result[
            "score"
        ],
        "correct_count": result[
            "correct_count"
        ],
        "total_count": result[
            "total_count"
        ],
        "wrong_count": result[
            "wrong_count"
        ],
        "units": config.get(
            "units",
            [],
        ).copy(),
        "difficulties": config.get(
            "difficulties",
            [],
        ).copy(),
        "unit_stats": result[
            "unit_stats"
        ],
        "difficulty_stats": result[
            "difficulty_stats"
        ],
        "topic_stats": result[
            "topic_stats"
        ],
        "wrong_questions": result[
            "wrong_questions"
        ],
    }

    history.append(
        history_item
    )


def latest_exam_score() -> int | None:

    history = st.session_state[
        "midterm_exam_history"
    ]

    if not history:
        return None

    return history[-1][
        "score"
    ]


def best_exam_score() -> int | None:

    history = st.session_state[
        "midterm_exam_history"
    ]

    if not history:
        return None

    return max(
        item["score"]
        for item in history
    )


def average_exam_score() -> float | None:

    history = st.session_state[
        "midterm_exam_history"
    ]

    if not history:
        return None

    return round(
        sum(
            item["score"]
            for item in history
        )
        / len(history),
        1,
    )


def exam_improvement() -> int | None:

    history = st.session_state[
        "midterm_exam_history"
    ]

    if len(history) < 2:
        return None

    return (
        history[-1]["score"]
        - history[0]["score"]
    )


# =========================================================
# 분석 Helper
# =========================================================

def score_message(
    score: int,
) -> tuple[str, str]:

    if score >= 90:

        return (
            "🏆 매우 안정적입니다.",
            (
                "핵심 개념을 잘 이해하고 있습니다. "
                "이제 오답과 세부 용어를 중심으로 마무리하세요."
            ),
        )

    if score >= 80:

        return (
            "✅ 좋은 수준입니다.",
            (
                "기본 개념은 안정적입니다. "
                "틀린 문제의 개념을 한 번 더 확인하세요."
            ),
        )

    if score >= 70:

        return (
            "📘 기본 개념은 이해하고 있습니다.",
            (
                "취약 단원을 중심으로 복습하면 "
                "점수를 빠르게 올릴 수 있습니다."
            ),
        )

    return (
        "⚠️ 추가 복습이 필요합니다.",
        (
            "단원별 분석에서 70점 미만 영역을 먼저 복습하고 "
            "다시 모의고사에 도전해보세요."
        ),
    )


def weak_units(
    unit_stats: dict[str, dict[str, int]],
) -> list[str]:

    result = []

    for unit, stats in unit_stats.items():

        if (
            stats[
                "score"
            ]
            < 70
        ):

            result.append(
                unit
            )

    return result


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
    "🎯 **중간고사 종합 대비**"
)


# =========================================================
# Breadcrumb
# =========================================================

render_breadcrumb(
    "홈",
    "중간고사",
    "종합 대비",
)


# =========================================================
# HERO
# =========================================================

render_html(
    """
    <div class="edu-hero">

        <div class="edu-hero-eyebrow">
            MIDTERM EXAM PREPARATION
        </div>

        <div class="edu-hero-title">
            중간고사 종합 대비
        </div>

        <div class="edu-hero-desc">
            학습 1부터 학습 4까지의 핵심 개념을 무작위 문제로
            점검하고 단원별 성취도와 오답을 분석합니다.
        </div>

    </div>
    """
)


# =========================================================
# 현재 활성 시험이 없는 경우
# =========================================================

if not st.session_state[
    "midterm_exam_started"
]:

    # =====================================================
    # 시험 설정
    # =====================================================

    with st.container(
        key="edu_section_midterm_setup"
    ):

        render_surface_header(
            "모의고사 설정",
            (
                "출제 범위와 난이도, 문제 수를 선택한 뒤 "
                "나만의 중간고사 모의시험을 시작합니다."
            ),
            label="EXAM SETUP",
        )


        # -------------------------------------------------
        # 범위
        # -------------------------------------------------

        st.markdown(
            "### 1. 시험 범위"
        )

        selected_units = st.multiselect(
            "출제할 소단원을 선택하세요.",
            options=list(
                QUIZ_BANK.keys()
            ),
            default=list(
                QUIZ_BANK.keys()
            ),
            format_func=lambda unit: (
                f"{unit} · "
                f"{UNIT_NAMES[unit]}"
            ),
            key="midterm_setup_units",
        )


        # -------------------------------------------------
        # 선택 범위 시각화
        # -------------------------------------------------

        if selected_units:

            render_pills(
                [
                    f"{unit} {UNIT_NAMES[unit]}"
                    for unit
                    in selected_units
                ]
            )


        st.markdown(
            "### 2. 난이도"
        )

        selected_difficulties = (
            st.multiselect(
                "출제 난이도를 선택하세요.",
                options=DIFFICULTY_ORDER,
                default=DIFFICULTY_ORDER,
                key="midterm_setup_difficulty",
            )
        )


        st.markdown(
            "### 3. 문제 수"
        )

        question_count = st.radio(
            "응시할 문제 수",
            [
                10,
                20,
                30,
            ],
            horizontal=True,
            key="midterm_setup_count",
        )


        # -------------------------------------------------
        # 출제 가능 문제
        # -------------------------------------------------

        available_pool = (
            filtered_question_pool(
                selected_units,
                selected_difficulties,
            )
        )

        col1, col2, col3 = st.columns(
            3
        )

        with col1:

            st.metric(
                "선택 소단원",
                f"{len(selected_units)}개",
            )

        with col2:

            st.metric(
                "출제 가능 문제",
                f"{len(available_pool)}문제",
            )

        with col3:

            st.metric(
                "응시 예정",
                (
                    f"{min(question_count, len(available_pool))}"
                    "문제"
                ),
            )


        if (
            selected_units
            and selected_difficulties
            and available_pool
        ):

            if len(
                available_pool
            ) < question_count:

                st.warning(
                    (
                        f"현재 조건에서는 "
                        f"{len(available_pool)}문제만 출제할 수 있습니다. "
                        "가능한 문제 전체가 출제됩니다."
                    )
                )


            if st.button(
                "🎯 모의고사 시작",
                type="primary",
                width="stretch",
            ):

                start_exam(
                    selected_units,
                    selected_difficulties,
                    question_count,
                )

                st.rerun()


        else:

            st.warning(
                "시험 범위와 난이도를 하나 이상 선택하세요."
            )


    # =====================================================
    # 시험 기록
    # =====================================================

    history = st.session_state[
        "midterm_exam_history"
    ]

    if history:

        with st.container(
            key="edu_section_midterm_history"
        ):

            render_surface_header(
                "나의 모의고사 기록",
                (
                    "지금까지 응시한 모의고사의 점수 변화와 "
                    "학습 성장을 확인합니다."
                ),
                label="EXAM HISTORY",
            )


            latest = latest_exam_score()
            best = best_exam_score()
            average = average_exam_score()
            improvement = exam_improvement()


            metric1, metric2, metric3, metric4 = (
                st.columns(
                    4
                )
            )

            with metric1:

                st.metric(
                    "응시 횟수",
                    f"{len(history)}회",
                )

            with metric2:

                st.metric(
                    "최근 점수",
                    f"{latest}점",
                )

            with metric3:

                st.metric(
                    "최고 점수",
                    f"{best}점",
                )

            with metric4:

                if improvement is None:

                    st.metric(
                        "첫 시험 대비",
                        "-",
                    )

                else:

                    st.metric(
                        "첫 시험 대비",
                        f"{improvement:+d}점",
                    )


            st.markdown(
                "### 📈 점수 변화"
            )

            history_df = pd.DataFrame(
                {
                    "응시 회차": [
                        item["attempt"]
                        for item in history
                    ],
                    "점수": [
                        item["score"]
                        for item in history
                    ],
                }
            ).set_index(
                "응시 회차"
            )

            st.line_chart(
                history_df,
                height=290,
            )


            # ---------------------------------------------
            # 기록 목록
            # ---------------------------------------------

            with st.expander(
                "📋 전체 응시 기록 보기"
            ):

                for item in reversed(
                    history
                ):

                    st.markdown(
                        (
                            f"**{item['attempt']}회차 · "
                            f"{item['score']}점** "
                            f"({item['correct_count']}/"
                            f"{item['total_count']})"
                        )
                    )

                    st.caption(
                        "범위: "
                        + ", ".join(
                            item[
                                "units"
                            ]
                        )
                    )

                    st.divider()


# =========================================================
# 시험 진행
# =========================================================

elif (
    st.session_state[
        "midterm_exam_started"
    ]
    and not st.session_state[
        "midterm_exam_finished"
    ]
):

    questions = st.session_state[
        "midterm_exam_questions"
    ]

    answers = st.session_state[
        "midterm_exam_answers"
    ]

    config = st.session_state[
        "midterm_exam_config"
    ]


    # =====================================================
    # Exam Header
    # =====================================================

    with st.container(
        key="edu_section_midterm_exam_header"
    ):

        render_surface_header(
            "중간고사 실전 모의고사",
            (
                "모든 문제에 답한 뒤 시험을 제출하세요. "
                "제출 즉시 자동 채점됩니다."
            ),
            label="EXAM IN PROGRESS",
        )

        render_pills(
            [
                f"{unit} {UNIT_NAMES[unit]}"
                for unit
                in config.get(
                    "units",
                    []
                )
            ]
        )


    # =====================================================
    # 답변 진행률
    # =====================================================

    answered_count = 0

    for question in questions:

        qid = question_id(
            question
        )

        value = answers.get(
            qid
        )

        if (
            value is not None
            and normalize_text(
                value
            )
        ):

            answered_count += 1


    progress = (
        answered_count
        / len(questions)
        * 100
        if questions
        else 0
    )


    render_progress_bar(
        progress,
        label=(
            f"답변 진행률 · "
            f"{answered_count}/{len(questions)}"
        ),
    )


    st.divider()


    # =====================================================
    # 문제
    # =====================================================

    for index, question in enumerate(
        questions,
        start=1,
    ):

        render_exam_question(
            question,
            index,
        )


    # 문제 렌더링 후 다시 계산
    answered_count = sum(
        1
        for question in questions
        if (
            st.session_state[
                "midterm_exam_answers"
            ].get(
                question_id(
                    question
                )
            )
            is not None
            and normalize_text(
                st.session_state[
                    "midterm_exam_answers"
                ].get(
                    question_id(
                        question
                    )
                )
            )
        )
    )


    st.divider()


    # =====================================================
    # 제출
    # =====================================================

    submit_col, cancel_col = st.columns(
        [4, 1]
    )


    with submit_col:

        if answered_count < len(
            questions
        ):

            st.warning(
                (
                    f"아직 {len(questions) - answered_count}문제에 "
                    "답하지 않았습니다."
                )
            )


        if st.button(
            "✅ 시험 제출 및 채점",
            type="primary",
            width="stretch",
            disabled=(
                answered_count
                < len(questions)
            ),
        ):

            grade_exam()

            st.rerun()


    with cancel_col:

        if st.button(
            "시험 취소",
            width="stretch",
        ):

            clear_active_exam()

            st.rerun()


# =========================================================
# 시험 결과
# =========================================================

else:

    result = st.session_state[
        "midterm_exam_result"
    ]


    # =====================================================
    # 결과 상단
    # =====================================================

    with st.container(
        key="edu_section_midterm_result"
    ):

        render_surface_header(
            "모의고사 결과",
            (
                "전체 점수와 단원별 성취도를 분석하고 "
                "틀린 문제를 중심으로 복습하세요."
            ),
            label="EXAM RESULT",
        )


        metric1, metric2, metric3 = st.columns(
            3
        )

        with metric1:

            st.metric(
                "점수",
                f"{result['score']}점",
            )

        with metric2:

            st.metric(
                "정답",
                (
                    f"{result['correct_count']}"
                    f"/{result['total_count']}"
                ),
            )

        with metric3:

            st.metric(
                "오답",
                f"{result['wrong_count']}문제",
            )


        title, message = score_message(
            result[
                "score"
            ]
        )

        st.info(
            f"**{title}**  \n{message}"
        )


    # =====================================================
    # 단원별 분석
    # =====================================================

    with st.container(
        key="edu_section_midterm_unit_analysis"
    ):

        render_surface_header(
            "단원별 성취도",
            (
                "어느 소단원에서 강점과 약점이 나타났는지 "
                "확인합니다."
            ),
            label="UNIT ANALYSIS",
        )


        unit_stats = result[
            "unit_stats"
        ]

        for unit in sorted(
            unit_stats.keys()
        ):

            stats = unit_stats[
                unit
            ]

            unit_name = UNIT_NAMES.get(
                unit,
                unit,
            )

            col1, col2, col3 = st.columns(
                [5, 1.5, 1.5]
            )

            with col1:

                st.markdown(
                    f"**{unit} · {unit_name}**"
                )

                st.progress(
                    stats[
                        "score"
                    ]
                    / 100
                )

            with col2:

                st.metric(
                    "정답",
                    (
                        f"{stats['correct']}"
                        f"/{stats['total']}"
                    ),
                )

            with col3:

                st.metric(
                    "성취도",
                    f"{stats['score']}%",
                )


    # =====================================================
    # 취약 영역
    # =====================================================

    weak = weak_units(
        result[
            "unit_stats"
        ]
    )

    with st.container(
        key="edu_section_midterm_weakness"
    ):

        render_surface_header(
            "복습이 필요한 영역",
            (
                "70% 미만의 소단원을 우선적으로 복습하는 것을 "
                "권장합니다."
            ),
            label="REVIEW PRIORITY",
        )


        if weak:

            for unit in weak:

                score = result[
                    "unit_stats"
                ][unit]["score"]

                st.warning(
                    (
                        f"📘 **{unit} · "
                        f"{UNIT_NAMES.get(unit, unit)}** "
                        f"— {score}%"
                    )
                )

        else:

            st.success(
                "🎉 모든 출제 단원에서 70% 이상을 달성했습니다."
            )


    # =====================================================
    # 난이도 분석
    # =====================================================

    with st.container(
        key="edu_section_midterm_difficulty"
    ):

        render_surface_header(
            "난이도별 분석",
            (
                "쉬움 · 보통 · 어려움 문제의 정답률을 "
                "비교합니다."
            ),
            label="DIFFICULTY ANALYSIS",
        )


        difficulty_stats = result[
            "difficulty_stats"
        ]


        columns = st.columns(
            max(
                1,
                len(
                    difficulty_stats
                ),
            )
        )


        for col, difficulty in zip(
            columns,
            difficulty_stats,
        ):

            stats = difficulty_stats[
                difficulty
            ]

            with col:

                st.metric(
                    difficulty,
                    f"{stats['score']}%",
                )

                st.caption(
                    (
                        f"{stats['correct']}/"
                        f"{stats['total']} 정답"
                    )
                )


    # =====================================================
    # 오답
    # =====================================================

    with st.container(
        key="edu_section_midterm_wrong"
    ):

        render_surface_header(
            "오답 다시 보기",
            (
                "틀린 문제의 정답과 해설을 확인하고 "
                "관련 개념을 복습하세요."
            ),
            label="WRONG ANSWERS",
        )


        wrong_questions = result[
            "wrong_questions"
        ]


        if not wrong_questions:

            st.success(
                "🏆 모든 문제를 맞혔습니다!"
            )

        else:

            for index, item in enumerate(
                wrong_questions,
                start=1,
            ):

                with st.expander(
                    (
                        f"❌ 오답 {index} · "
                        f"{item['unit']} · "
                        f"{item['topic']}"
                    )
                ):

                    st.markdown(
                        f"**문제**  \n"
                        f"{item['question']}"
                    )

                    st.markdown(
                        f"**내 답**  \n"
                        f"{item['user_answer'] or '미입력'}"
                    )

                    st.markdown(
                        f"**정답**  \n"
                        f"{item['correct_answer']}"
                    )

                    if item[
                        "explanation"
                    ]:

                        st.info(
                            item[
                                "explanation"
                            ]
                        )


    # =====================================================
    # 누적 기록
    # =====================================================

    history = st.session_state[
        "midterm_exam_history"
    ]

    if history:

        with st.container(
            key="edu_section_midterm_growth"
        ):

            render_surface_header(
                "모의고사 성장 기록",
                (
                    "이번 응시 결과가 누적 기록에 저장되었습니다."
                ),
                label="GROWTH",
            )

            metric1, metric2, metric3, metric4 = (
                st.columns(
                    4
                )
            )

            with metric1:

                st.metric(
                    "총 응시",
                    f"{len(history)}회",
                )

            with metric2:

                st.metric(
                    "최근 점수",
                    f"{latest_exam_score()}점",
                )

            with metric3:

                st.metric(
                    "최고 점수",
                    f"{best_exam_score()}점",
                )

            with metric4:

                improvement = exam_improvement()

                if improvement is None:

                    st.metric(
                        "첫 시험 대비",
                        "-",
                    )

                else:

                    st.metric(
                        "첫 시험 대비",
                        f"{improvement:+d}점",
                    )


            if len(history) >= 2:

                history_df = pd.DataFrame(
                    {
                        "응시 회차": [
                            item["attempt"]
                            for item in history
                        ],
                        "점수": [
                            item["score"]
                            for item in history
                        ],
                    }
                ).set_index(
                    "응시 회차"
                )

                st.line_chart(
                    history_df,
                    height=280,
                )


    # =====================================================
    # 다시 응시
    # =====================================================

    st.divider()

    col1, col2, col3 = st.columns(
        [2, 2, 1]
    )


    with col1:

        if st.button(
            "🔄 같은 조건으로 다시 풀기",
            type="primary",
            width="stretch",
        ):

            config = st.session_state[
                "midterm_exam_config"
            ]

            start_exam(
                config.get(
                    "units",
                    list(
                        QUIZ_BANK.keys()
                    ),
                ),
                config.get(
                    "difficulties",
                    DIFFICULTY_ORDER,
                ),
                config.get(
                    "question_count",
                    20,
                ),
            )

            st.rerun()


    with col2:

        if st.button(
            "⚙️ 새로운 시험 설정",
            width="stretch",
        ):

            clear_active_exam()

            st.rerun()


    with col3:

        st.page_link(
            "pages/06_학습대시보드.py",
            label="📊 대시보드",
            width="stretch",
        )