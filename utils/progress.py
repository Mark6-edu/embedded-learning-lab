from __future__ import annotations

from typing import Any

import streamlit as st


# =========================================================
# 학습 구조
# =========================================================

LESSON_STRUCTURE = {
    "1": [
        "1-1",
        "1-2",
    ],
    "2": [
        "2-1",
        "2-2",
    ],
    "3": [
        "3-1",
        "3-2",
    ],
    "4": [
        "4-1",
        "4-2",
    ],
}


LESSON_NAMES = {
    "1": "기술 명세 검토하기",
    "2": "애플리케이션 개발 환경 구축하기",
    "3": "애플리케이션 모듈 구현하기",
    "4": "애플리케이션 인터페이스 구현하기",
}


SECTION_NAMES = {
    "1-1": "검토한 기술 스펙이 적용된 소프트웨어 검토",
    "1-2": "임베디드 시스템의 평가",
    "2-1": "개발 도구 선정",
    "2-2": "애플리케이션 개발 환경 구축",
    "3-1": "애플리케이션 구현 및 오류 제거",
    "3-2": "디버깅 및 프로그램 통합",
    "4-1": "환경 준비 후 인터페이스 구현",
    "4-2": "소스 코드 저장 및 버전 관리",
}


# =========================================================
# Session State Key
# =========================================================

PROGRESS_STATE_KEY = "learning_progress"


# =========================================================
# 기본 데이터 생성
# =========================================================

def _create_default_section_data() -> dict[str, Any]:
    """
    하나의 소단원에 대한 기본 진도 데이터를 생성한다.
    """

    return {
        "completed": False,

        # 가장 최근 형성평가 결과
        "formative_score": None,
        "formative_correct": None,
        "formative_total": None,

        # 총 응시 횟수
        "attempt_count": 0,

        # 형성평가 전체 응시 이력
        "history": [],
    }


def _create_default_progress() -> dict[str, dict[str, Any]]:
    """
    전체 학습 진도의 기본 데이터를 생성한다.
    """

    progress = {}

    for sections in LESSON_STRUCTURE.values():

        for section_id in sections:

            progress[
                section_id
            ] = _create_default_section_data()

    return progress


# =========================================================
# 초기화 및 기존 데이터 마이그레이션
# =========================================================

def initialize_progress() -> None:
    """
    학습 진도 데이터가 없다면 Session State에 생성한다.

    기존 버전의 progress 데이터가 이미 존재하는 경우에도
    새롭게 추가된 history 필드 등을 자동으로 보완한다.
    """

    if PROGRESS_STATE_KEY not in st.session_state:

        st.session_state[
            PROGRESS_STATE_KEY
        ] = _create_default_progress()

        return

    progress = st.session_state[
        PROGRESS_STATE_KEY
    ]

    # -----------------------------------------------------
    # 소단원이 새로 추가된 경우 자동 생성
    # -----------------------------------------------------

    for sections in LESSON_STRUCTURE.values():

        for section_id in sections:

            if section_id not in progress:

                progress[
                    section_id
                ] = _create_default_section_data()

                continue

            section = progress[
                section_id
            ]

            # -------------------------------------------------
            # 기존 데이터 구조 자동 보완
            # -------------------------------------------------

            default_data = (
                _create_default_section_data()
            )

            for key, value in (
                default_data.items()
            ):

                if key not in section:

                    # 리스트는 새로운 객체로 생성
                    if isinstance(
                        value,
                        list,
                    ):

                        section[
                            key
                        ] = []

                    else:

                        section[
                            key
                        ] = value


# =========================================================
# 전체 데이터 조회
# =========================================================

def get_all_progress() -> dict[str, dict[str, Any]]:
    """
    전체 학습 진도 데이터를 반환한다.
    """

    initialize_progress()

    return st.session_state[
        PROGRESS_STATE_KEY
    ]


# =========================================================
# 소단원 데이터 조회
# =========================================================

def get_section_progress(
    section_id: str,
) -> dict[str, Any]:
    """
    특정 소단원의 학습 정보를 반환한다.

    예:
        get_section_progress("3-1")
    """

    initialize_progress()

    progress = st.session_state[
        PROGRESS_STATE_KEY
    ]

    if section_id not in progress:

        raise ValueError(
            f"존재하지 않는 소단원입니다: {section_id}"
        )

    return progress[
        section_id
    ]


# =========================================================
# 소단원 완료 처리
# =========================================================

def complete_section(
    section_id: str,
) -> None:
    """
    특정 소단원을 완료 상태로 변경한다.
    """

    section = get_section_progress(
        section_id
    )

    section[
        "completed"
    ] = True


# =========================================================
# 완료 상태 해제
# =========================================================

def uncomplete_section(
    section_id: str,
) -> None:
    """
    특정 소단원의 완료 상태를 해제한다.
    """

    section = get_section_progress(
        section_id
    )

    section[
        "completed"
    ] = False


# =========================================================
# 형성평가 결과 저장
# =========================================================

def save_formative_result(
    section_id: str,
    correct_count: int,
    total_count: int,
) -> None:
    """
    특정 소단원의 형성평가 결과를 저장한다.

    저장 내용:
    - 최근 점수
    - 최근 정답 수
    - 전체 문항 수
    - 응시 횟수
    - 전체 점수 이력
    - 소단원 완료 상태
    """

    section = get_section_progress(
        section_id
    )

    if total_count <= 0:

        score = 0

    else:

        score = round(
            correct_count
            / total_count
            * 100
        )


    # -----------------------------------------------------
    # 응시 횟수 증가
    # -----------------------------------------------------

    section[
        "attempt_count"
    ] += 1

    current_attempt = section[
        "attempt_count"
    ]


    # -----------------------------------------------------
    # 최근 결과 갱신
    # -----------------------------------------------------

    section[
        "formative_score"
    ] = score

    section[
        "formative_correct"
    ] = correct_count

    section[
        "formative_total"
    ] = total_count


    # -----------------------------------------------------
    # 전체 이력 추가
    # -----------------------------------------------------

    section[
        "history"
    ].append(
        {
            "attempt": current_attempt,
            "score": score,
            "correct": correct_count,
            "total": total_count,
        }
    )


    # -----------------------------------------------------
    # 학습 완료 처리
    # -----------------------------------------------------

    section[
        "completed"
    ] = True


# =========================================================
# 형성평가 이력 조회
# =========================================================

def get_formative_history(
    section_id: str,
) -> list[dict[str, Any]]:
    """
    특정 소단원의 형성평가 전체 이력을 반환한다.

    예:
        [
            {
                "attempt": 1,
                "score": 67,
                "correct": 8,
                "total": 12,
            },
            {
                "attempt": 2,
                "score": 83,
                "correct": 10,
                "total": 12,
            },
        ]
    """

    section = get_section_progress(
        section_id
    )

    return list(
        section[
            "history"
        ]
    )


# =========================================================
# 최고 형성평가 점수
# =========================================================

def get_best_formative_score(
    section_id: str,
) -> int | None:
    """
    특정 소단원의 최고 형성평가 점수를 반환한다.
    """

    history = get_formative_history(
        section_id
    )

    if not history:

        return None

    return max(
        item[
            "score"
        ]
        for item
        in history
    )


# =========================================================
# 최초 형성평가 점수
# =========================================================

def get_first_formative_score(
    section_id: str,
) -> int | None:
    """
    특정 소단원의 최초 형성평가 점수를 반환한다.
    """

    history = get_formative_history(
        section_id
    )

    if not history:

        return None

    return history[
        0
    ][
        "score"
    ]


# =========================================================
# 점수 향상도
# =========================================================

def get_formative_improvement(
    section_id: str,
) -> int | None:
    """
    최초 점수와 최근 점수의 차이를 반환한다.

    예:
        최초 65점
        최근 90점

        → +25
    """

    history = get_formative_history(
        section_id
    )

    if len(history) < 2:

        return None

    first_score = history[
        0
    ][
        "score"
    ]

    latest_score = history[
        -1
    ][
        "score"
    ]

    return (
        latest_score
        - first_score
    )


# =========================================================
# 소단원 완료 여부
# =========================================================

def is_section_completed(
    section_id: str,
) -> bool:
    """
    특정 소단원이 완료되었는지 반환한다.
    """

    section = get_section_progress(
        section_id
    )

    return bool(
        section[
            "completed"
        ]
    )


# =========================================================
# 학습 영역 진도율
# =========================================================

def get_lesson_progress(
    lesson_id: str,
) -> float:
    """
    학습 1~4의 진도율을 계산한다.
    """

    initialize_progress()

    if lesson_id not in LESSON_STRUCTURE:

        raise ValueError(
            f"존재하지 않는 학습 영역입니다: {lesson_id}"
        )

    section_ids = LESSON_STRUCTURE[
        lesson_id
    ]

    completed_count = sum(
        1
        for section_id in section_ids
        if is_section_completed(
            section_id
        )
    )

    total_count = len(
        section_ids
    )

    if total_count == 0:

        return 0.0

    return (
        completed_count
        / total_count
        * 100
    )


# =========================================================
# 학습 영역 완료 여부
# =========================================================

def is_lesson_completed(
    lesson_id: str,
) -> bool:
    """
    특정 학습 영역의 모든 소단원이 완료되었는지 반환한다.
    """

    return (
        get_lesson_progress(
            lesson_id
        )
        >= 100
    )


# =========================================================
# 전체 진도율
# =========================================================

def get_overall_progress() -> float:
    """
    1-1 ~ 4-2 전체 진도율을 계산한다.
    """

    initialize_progress()

    all_sections = [
        section_id
        for sections
        in LESSON_STRUCTURE.values()
        for section_id
        in sections
    ]

    completed_count = sum(
        1
        for section_id in all_sections
        if is_section_completed(
            section_id
        )
    )

    total_count = len(
        all_sections
    )

    if total_count == 0:

        return 0.0

    return (
        completed_count
        / total_count
        * 100
    )


# =========================================================
# 완료한 소단원 개수
# =========================================================

def get_completed_section_count() -> int:
    """
    완료한 소단원의 개수를 반환한다.
    """

    initialize_progress()

    return sum(
        1
        for section_id
        in SECTION_NAMES
        if is_section_completed(
            section_id
        )
    )


# =========================================================
# 전체 소단원 개수
# =========================================================

def get_total_section_count() -> int:
    """
    전체 소단원 개수를 반환한다.
    """

    return len(
        SECTION_NAMES
    )


# =========================================================
# 학습 영역 요약
# =========================================================

def get_lesson_summary(
    lesson_id: str,
) -> dict[str, Any]:
    """
    특정 학습 영역의 요약 정보를 반환한다.
    """

    if lesson_id not in LESSON_STRUCTURE:

        raise ValueError(
            f"존재하지 않는 학습 영역입니다: {lesson_id}"
        )

    sections = LESSON_STRUCTURE[
        lesson_id
    ]

    completed_count = sum(
        1
        for section_id in sections
        if is_section_completed(
            section_id
        )
    )

    return {
        "lesson_id": lesson_id,

        "name": LESSON_NAMES[
            lesson_id
        ],

        "progress": get_lesson_progress(
            lesson_id
        ),

        "completed": is_lesson_completed(
            lesson_id
        ),

        "completed_sections": (
            completed_count
        ),

        "total_sections": len(
            sections
        ),
    }


# =========================================================
# 전체 학습 요약
# =========================================================

def get_overall_summary() -> dict[str, Any]:
    """
    전체 학습 진행 상황을 요약하여 반환한다.
    """

    return {
        "progress": (
            get_overall_progress()
        ),

        "completed_sections": (
            get_completed_section_count()
        ),

        "total_sections": (
            get_total_section_count()
        ),

        "lessons": {
            lesson_id: (
                get_lesson_summary(
                    lesson_id
                )
            )
            for lesson_id
            in LESSON_STRUCTURE
        },
    }


# =========================================================
# 최근 점수 기준 형성평가 평균
# =========================================================

def get_formative_average() -> float | None:
    """
    각 소단원의 가장 최근 형성평가 점수를 기준으로
    전체 평균을 계산한다.
    """

    progress = get_all_progress()

    scores = [
        section[
            "formative_score"
        ]
        for section
        in progress.values()
        if section[
            "formative_score"
        ] is not None
    ]

    if not scores:

        return None

    return round(
        sum(scores)
        / len(scores),
        1,
    )


# =========================================================
# 모든 응시 결과 평균
# =========================================================

def get_all_attempt_average() -> float | None:
    """
    모든 형성평가 응시 이력을 기준으로
    전체 평균 점수를 계산한다.

    예:
        1-1: 60, 80
        1-2: 90

        전체 응시 평균 = 76.7
    """

    progress = get_all_progress()

    scores = []

    for section in progress.values():

        for item in section[
            "history"
        ]:

            scores.append(
                item[
                    "score"
                ]
            )

    if not scores:

        return None

    return round(
        sum(scores)
        / len(scores),
        1,
    )


# =========================================================
# 전체 형성평가 응시 횟수
# =========================================================

def get_total_attempt_count() -> int:
    """
    모든 소단원의 형성평가 응시 횟수를 합산한다.
    """

    progress = get_all_progress()

    return sum(
        section[
            "attempt_count"
        ]
        for section
        in progress.values()
    )


# =========================================================
# 가장 많이 재응시한 소단원
# =========================================================

def get_most_retried_section() -> dict[str, Any] | None:
    """
    가장 많이 응시한 소단원을 반환한다.
    """

    progress = get_all_progress()

    attempted_sections = [
        {
            "section_id": section_id,
            "attempt_count": data[
                "attempt_count"
            ],
        }
        for section_id, data
        in progress.items()
        if data[
            "attempt_count"
        ] > 0
    ]

    if not attempted_sections:

        return None

    return max(
        attempted_sections,
        key=lambda item: item[
            "attempt_count"
        ],
    )


# =========================================================
# 학습 진도 초기화
# =========================================================

def reset_progress() -> None:
    """
    모든 학습 진도와 형성평가 기록을 초기화한다.
    """

    st.session_state[
        PROGRESS_STATE_KEY
    ] = _create_default_progress()