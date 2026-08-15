from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

import streamlit as st

from utils.progress import (
    get_section_progress,
    save_formative_result,
)


# =========================================================
# 문제 데이터 구조
# =========================================================

@dataclass
class QuizQuestion:
    id: str
    type: str
    question: str
    answer: Any
    options: Sequence[str] | None = None
    explanation: str = ""
    topic: str = ""
    difficulty: str = "보통"
    passage: str = ""


# =========================================================
# 문자열 처리
# =========================================================

def _normalize_text(
    value: Any,
) -> str:
    """
    단답형 비교를 위한 문자열 정규화.

    - 앞뒤 공백 제거
    - 소문자 변환
    - 내부 공백 제거
    """

    return (
        str(value)
        .strip()
        .lower()
        .replace(" ", "")
    )


# =========================================================
# Widget Key
# =========================================================

def _question_key(
    question: QuizQuestion,
    prefix: str = "quiz",
) -> str:
    """
    Streamlit Widget Key를 생성한다.
    """

    return (
        f"{prefix}_"
        f"{question.id}"
    )


# =========================================================
# 형성평가 소단원 자동 판별
# =========================================================

def _get_section_id_from_questions(
    questions: Sequence[QuizQuestion],
) -> str | None:
    """
    문제 ID를 이용하여 소단원 ID를 자동으로 찾는다.

    예:
        1_1_f01 → 1-1
        3_2_f15 → 3-2
        4_2_e01 → 4-2

    문제 목록의 모든 문항이 같은 소단원일 때만 반환한다.
    """

    section_ids = set()

    for question in questions:

        parts = question.id.split(
            "_"
        )

        if len(parts) < 3:
            continue

        lesson_number = parts[0]
        section_number = parts[1]

        if (
            lesson_number.isdigit()
            and section_number.isdigit()
        ):

            section_ids.add(
                f"{lesson_number}-"
                f"{section_number}"
            )

    if len(section_ids) == 1:

        return next(
            iter(section_ids)
        )

    return None


# =========================================================
# 문제 텍스트
# =========================================================

def _render_question_text(
    question: QuizQuestion,
    number: int | None = None,
) -> None:
    """
    문제 본문과 제시문을 출력한다.
    """

    if number is None:

        st.markdown(
            f"### {question.question}"
        )

    else:

        st.markdown(
            f"### {number}. "
            f"{question.question}"
        )

    if question.passage:

        st.info(
            question.passage
        )

    meta = []

    if question.topic:

        meta.append(
            f"주제 · {question.topic}"
        )

    if question.difficulty:

        meta.append(
            f"난이도 · {question.difficulty}"
        )

    if meta:

        st.caption(
            " | ".join(
                meta
            )
        )


# =========================================================
# 정답 처리
# =========================================================

def _get_answer_list(
    answer: Any,
) -> list[Any]:
    """
    하나의 정답 또는 여러 허용 정답을
    리스트 형태로 반환한다.
    """

    if isinstance(
        answer,
        (list, tuple, set),
    ):

        return list(
            answer
        )

    return [
        answer
    ]


def _is_correct(
    question: QuizQuestion,
    user_answer: Any,
) -> bool:
    """
    문제 유형별 정답 여부를 판단한다.
    """

    # -----------------------------------------------------
    # 객관식
    # -----------------------------------------------------

    if (
        question.type
        == "multiple_choice"
    ):

        return (
            user_answer
            == question.answer
        )

    # -----------------------------------------------------
    # OX
    # -----------------------------------------------------

    if (
        question.type
        == "true_false"
    ):

        if user_answer is None:

            return False

        if isinstance(
            user_answer,
            bool,
        ):

            return (
                user_answer
                == question.answer
            )

        answer_map = {
            "O": True,
            "X": False,
            "True": True,
            "False": False,
            "참": True,
            "거짓": False,
        }

        converted = answer_map.get(
            str(user_answer)
        )

        return (
            converted
            == question.answer
        )

    # -----------------------------------------------------
    # 단답형
    # -----------------------------------------------------

    if (
        question.type
        == "short_answer"
    ):

        if user_answer is None:

            return False

        normalized_user = (
            _normalize_text(
                user_answer
            )
        )

        if not normalized_user:

            return False

        normalized_answers = [
            _normalize_text(
                answer
            )
            for answer
            in _get_answer_list(
                question.answer
            )
        ]

        return (
            normalized_user
            in normalized_answers
        )

    return False


def _correct_answer_text(
    question: QuizQuestion,
) -> str:
    """
    화면에 표시할 정답 문자열을 생성한다.
    """

    if (
        question.type
        == "true_false"
    ):

        return (
            "O"
            if question.answer
            else "X"
        )

    if isinstance(
        question.answer,
        (list, tuple, set),
    ):

        return " / ".join(
            str(answer)
            for answer
            in question.answer
        )

    return str(
        question.answer
    )


# =========================================================
# 객관식
# =========================================================

def render_multiple_choice(
    question: QuizQuestion,
    key_prefix: str = "quiz",
    disabled: bool = False,
):
    """
    객관식 문제를 출력하고
    학생의 답을 반환한다.
    """

    if not question.options:

        st.error(
            "객관식 문제의 보기가 없습니다."
        )

        return None

    return st.radio(
        "정답을 선택하세요.",
        options=list(
            question.options
        ),
        index=None,
        key=_question_key(
            question,
            key_prefix,
        ),
        disabled=disabled,
    )


# =========================================================
# OX
# =========================================================

def render_true_false(
    question: QuizQuestion,
    key_prefix: str = "quiz",
    disabled: bool = False,
):
    """
    OX 문제를 출력한다.
    """

    return st.radio(
        "O 또는 X를 선택하세요.",
        options=[
            "O",
            "X",
        ],
        index=None,
        horizontal=True,
        key=_question_key(
            question,
            key_prefix,
        ),
        disabled=disabled,
    )


# =========================================================
# 단답형
# =========================================================

def render_short_answer(
    question: QuizQuestion,
    key_prefix: str = "quiz",
    disabled: bool = False,
):
    """
    단답형 문제를 출력한다.
    """

    return st.text_input(
        "정답을 입력하세요.",
        key=_question_key(
            question,
            key_prefix,
        ),
        disabled=disabled,
    )


# =========================================================
# 문제 하나 출력
# =========================================================

def render_question(
    question: QuizQuestion,
    number: int | None = None,
    key_prefix: str = "quiz",
    disabled: bool = False,
):
    """
    문제 유형을 확인한 뒤
    적절한 입력 Widget을 출력한다.
    """

    _render_question_text(
        question,
        number,
    )

    if (
        question.type
        == "multiple_choice"
    ):

        return render_multiple_choice(
            question,
            key_prefix=key_prefix,
            disabled=disabled,
        )

    if (
        question.type
        == "true_false"
    ):

        return render_true_false(
            question,
            key_prefix=key_prefix,
            disabled=disabled,
        )

    if (
        question.type
        == "short_answer"
    ):

        return render_short_answer(
            question,
            key_prefix=key_prefix,
            disabled=disabled,
        )

    st.error(
        f"지원하지 않는 문제 유형입니다: "
        f"{question.type}"
    )

    return None


# =========================================================
# 일반 형성평가
# =========================================================

def render_quiz(
    questions: Sequence[QuizQuestion],
    title: str = "✅ 형성평가",
    description: str | None = None,
    section_id: str | None = None,
) -> None:
    """
    형성평가 전체를 출력한다.

    제출하면:
    1. 자동 채점
    2. 점수 표시
    3. 문제별 정답과 해설 표시
    4. utils.progress에 형성평가 결과 저장
    5. 해당 소단원 완료 처리

    section_id를 전달하지 않은 경우
    문제 ID에서 자동 판별한다.
    """

    questions = list(
        questions
    )

    if not questions:

        st.info(
            "등록된 형성평가 문제가 없습니다."
        )

        return


    # -----------------------------------------------------
    # 소단원 자동 판별
    # -----------------------------------------------------

    resolved_section_id = (
        section_id
        or _get_section_id_from_questions(
            questions
        )
    )


    # -----------------------------------------------------
    # Quiz 고유 Prefix
    # -----------------------------------------------------

    first_question_id = (
        questions[0].id
    )

    quiz_prefix = (
        f"formative_"
        f"{first_question_id}"
    )

    submitted_key = (
        f"{quiz_prefix}_submitted"
    )

    result_key = (
        f"{quiz_prefix}_result"
    )


    if submitted_key not in st.session_state:

        st.session_state[
            submitted_key
        ] = False

    if result_key not in st.session_state:

        st.session_state[
            result_key
        ] = {}


    # -----------------------------------------------------
    # 제목
    # -----------------------------------------------------

    st.markdown(
        f"## {title}"
    )

    if description:

        st.caption(
            description
        )


    # -----------------------------------------------------
    # 기존 학습 기록 안내
    # -----------------------------------------------------

    if resolved_section_id:

        try:

            section_progress = (
                get_section_progress(
                    resolved_section_id
                )
            )

            if (
                section_progress[
                    "completed"
                ]
                and section_progress[
                    "formative_score"
                ] is not None
            ):

                st.success(
                    f"✅ 이미 완료한 학습입니다. "
                    f"최근 형성평가 점수 "
                    f"**{section_progress['formative_score']}점** · "
                    f"응시 "
                    f"**{section_progress['attempt_count']}회**"
                )

        except ValueError:

            # progress.py에 등록되지 않은
            # 단원이라면 진도 저장 없이
            # 퀴즈만 정상 진행한다.
            resolved_section_id = None


    # -----------------------------------------------------
    # 제출 전
    # -----------------------------------------------------

    if not st.session_state[
        submitted_key
    ]:

        user_answers = {}

        for number, question in enumerate(
            questions,
            start=1,
        ):

            st.divider()

            answer = render_question(
                question,
                number=number,
                key_prefix=quiz_prefix,
            )

            user_answers[
                question.id
            ] = answer


        # -------------------------------------------------
        # 답변 현황
        # -------------------------------------------------

        answered_count = 0

        for question in questions:

            answer = user_answers.get(
                question.id
            )

            if answer not in [
                None,
                "",
            ]:

                answered_count += 1


        st.divider()

        st.markdown(
            "### 📊 응답 현황"
        )

        progress = (
            answered_count
            / len(questions)
        )

        st.progress(
            progress
        )

        st.caption(
            f"{answered_count} / "
            f"{len(questions)}문제 응답"
        )


        # -------------------------------------------------
        # 제출
        # -------------------------------------------------

        if st.button(
            "✅ 형성평가 제출",
            type="primary",
            use_container_width=True,
            key=(
                f"{quiz_prefix}_submit"
            ),
        ):

            if (
                answered_count
                < len(questions)
            ):

                st.warning(
                    "아직 답하지 않은 문제가 있습니다. "
                    "모든 문제에 답한 뒤 제출해주세요."
                )

                return


            # ---------------------------------------------
            # 채점
            # ---------------------------------------------

            correct_count = 0

            graded_questions = []

            for question in questions:

                user_answer = (
                    user_answers[
                        question.id
                    ]
                )

                correct = _is_correct(
                    question,
                    user_answer,
                )

                if correct:

                    correct_count += 1

                graded_questions.append(
                    {
                        "question": question,
                        "user_answer": (
                            user_answer
                        ),
                        "correct": (
                            correct
                        ),
                    }
                )


            total_count = len(
                questions
            )

            score = round(
                correct_count
                / total_count
                * 100
            )


            # ---------------------------------------------
            # 결과 저장
            # ---------------------------------------------

            st.session_state[
                result_key
            ] = {
                "correct_count": (
                    correct_count
                ),
                "total_count": (
                    total_count
                ),
                "score": score,
                "questions": (
                    graded_questions
                ),
            }


            # ---------------------------------------------
            # 학습 진도 저장
            # ---------------------------------------------

            if resolved_section_id:

                save_formative_result(
                    resolved_section_id,
                    correct_count,
                    total_count,
                )


            st.session_state[
                submitted_key
            ] = True

            st.rerun()


    # -----------------------------------------------------
    # 제출 후
    # -----------------------------------------------------

    else:

        result = st.session_state[
            result_key
        ]

        correct_count = result[
            "correct_count"
        ]

        total_count = result[
            "total_count"
        ]

        score = result[
            "score"
        ]


        # -------------------------------------------------
        # 결과 요약
        # -------------------------------------------------

        st.markdown(
            "### 🏁 형성평가 결과"
        )

        score_col, correct_col, wrong_col = (
            st.columns(
                3
            )
        )

        with score_col:

            st.metric(
                "점수",
                f"{score}점",
            )

        with correct_col:

            st.metric(
                "정답",
                (
                    f"{correct_count}"
                    f"/{total_count}"
                ),
            )

        with wrong_col:

            st.metric(
                "오답",
                (
                    f"{total_count - correct_count}"
                    f"문제"
                ),
            )


        # -------------------------------------------------
        # 완료 안내
        # -------------------------------------------------

        if resolved_section_id:

            st.success(
                f"🎉 {resolved_section_id} "
                f"학습이 완료되었습니다!"
            )


        # -------------------------------------------------
        # 결과 메시지
        # -------------------------------------------------

        if score >= 90:

            st.success(
                "🏆 핵심 개념을 매우 잘 이해하고 있습니다!"
            )

        elif score >= 80:

            st.success(
                "👏 잘했습니다. "
                "틀린 문제만 한 번 더 확인해보세요."
            )

        elif score >= 70:

            st.info(
                "📘 기본 개념은 이해하고 있습니다. "
                "오답을 중심으로 복습해보세요."
            )

        else:

            st.warning(
                "📚 해설을 확인한 뒤 "
                "핵심 이론을 다시 복습해보세요."
            )


        # -------------------------------------------------
        # 문제별 결과
        # -------------------------------------------------

        st.markdown(
            "### 🔍 문제별 확인"
        )

        for number, item in enumerate(
            result[
                "questions"
            ],
            start=1,
        ):

            question = item[
                "question"
            ]

            user_answer = item[
                "user_answer"
            ]

            correct = item[
                "correct"
            ]

            icon = (
                "✅"
                if correct
                else "❌"
            )

            with st.expander(
                (
                    f"{icon} {number}. "
                    f"{question.question}"
                ),
                expanded=not correct,
            ):

                if question.passage:

                    st.info(
                        question.passage
                    )

                st.markdown(
                    "**내 답**"
                )

                if correct:

                    st.success(
                        str(
                            user_answer
                        )
                    )

                else:

                    st.error(
                        str(
                            user_answer
                        )
                    )

                st.markdown(
                    "**정답**"
                )

                st.success(
                    _correct_answer_text(
                        question
                    )
                )

                if question.explanation:

                    st.markdown(
                        "**해설**"
                    )

                    st.write(
                        question.explanation
                    )

                if question.topic:

                    st.caption(
                        f"주제 · {question.topic} "
                        f"| 난이도 · "
                        f"{question.difficulty}"
                    )


        # -------------------------------------------------
        # 다시 풀기
        # -------------------------------------------------

        st.divider()

        if st.button(
            "🔄 형성평가 다시 풀기",
            use_container_width=True,
            key=(
                f"{quiz_prefix}_retry"
            ),
        ):

            st.session_state[
                submitted_key
            ] = False

            st.session_state[
                result_key
            ] = {}

            # 기존 Widget 답 제거
            for question in questions:

                widget_key = (
                    _question_key(
                        question,
                        quiz_prefix,
                    )
                )

                if (
                    widget_key
                    in st.session_state
                ):

                    del st.session_state[
                        widget_key
                    ]

            st.rerun()


# =========================================================
# 중간고사 대비 문제
# =========================================================

def render_exam_practice(
    questions: Sequence[QuizQuestion],
    title: str = "🎯 중간고사 대비",
    description: str | None = None,
) -> None:
    """
    단원별 중간고사 대비 문제를 출력한다.

    중요:
    이 함수는 형성평가 완료 진도에 영향을 주지 않는다.

    즉:
        render_quiz()
            → 형성평가
            → 진도 저장 O

        render_exam_practice()
            → 시험 대비
            → 진도 저장 X
    """

    questions = list(
        questions
    )

    if not questions:

        st.info(
            "등록된 중간고사 대비 문제가 없습니다."
        )

        return


    st.markdown(
        f"## {title}"
    )

    if description:

        st.caption(
            description
        )

    st.info(
        "문제를 풀고 바로 정답과 해설을 "
        "확인하며 시험 내용을 복습해보세요."
    )


    for number, question in enumerate(
        questions,
        start=1,
    ):

        st.divider()

        _render_question_text(
            question,
            number,
        )

        key_prefix = (
            f"exam_{question.id}"
        )


        # -------------------------------------------------
        # 객관식
        # -------------------------------------------------

        if (
            question.type
            == "multiple_choice"
        ):

            user_answer = st.radio(
                "정답을 선택하세요.",
                options=list(
                    question.options
                    or []
                ),
                index=None,
                key=(
                    f"{key_prefix}_answer"
                ),
            )


        # -------------------------------------------------
        # OX
        # -------------------------------------------------

        elif (
            question.type
            == "true_false"
        ):

            user_answer = st.radio(
                "O 또는 X를 선택하세요.",
                options=[
                    "O",
                    "X",
                ],
                index=None,
                horizontal=True,
                key=(
                    f"{key_prefix}_answer"
                ),
            )


        # -------------------------------------------------
        # 단답형
        # -------------------------------------------------

        elif (
            question.type
            == "short_answer"
        ):

            user_answer = st.text_input(
                "정답을 입력하세요.",
                key=(
                    f"{key_prefix}_answer"
                ),
            )

        else:

            st.error(
                f"지원하지 않는 문제 유형입니다: "
                f"{question.type}"
            )

            continue


        # -------------------------------------------------
        # 개별 정답 확인
        # -------------------------------------------------

        if st.button(
            f"{number}번 정답 확인",
            key=(
                f"{key_prefix}_check"
            ),
        ):

            if user_answer in [
                None,
                "",
            ]:

                st.warning(
                    "먼저 답을 입력하거나 선택해주세요."
                )

                continue

            correct = _is_correct(
                question,
                user_answer,
            )

            if correct:

                st.success(
                    "정답입니다! ✅"
                )

            else:

                st.error(
                    "정답이 아닙니다."
                )

                st.markdown(
                    f"**정답:** "
                    f"{_correct_answer_text(question)}"
                )

            if question.explanation:

                st.info(
                    question.explanation
                )