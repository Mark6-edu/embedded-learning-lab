from __future__ import annotations

from typing import Any

import streamlit as st

from utils.auth import (
    get_user_id,
    is_logged_in,
)

from utils.sheets_api import (
    load_formative_results as load_formative_results_from_sheets,
    load_progress as load_progress_from_sheets,
    save_formative_result as save_formative_result_to_sheets,
    save_progress as save_progress_to_sheets,
)


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
# Session State Keys
# =========================================================

PROGRESS_STATE_KEY = "learning_progress"

REMOTE_PROGRESS_USER_KEY = (
    "learning_progress_remote_user_id"
)

REMOTE_PROGRESS_SYNCED_KEY = (
    "learning_progress_remote_synced"
)

REMOTE_FORMATIVE_USER_KEY = (
    "formative_results_remote_user_id"
)

REMOTE_FORMATIVE_SYNCED_KEY = (
    "formative_results_remote_synced"
)


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
# 원격 진도 불러오기
# =========================================================

def _load_remote_progress_once() -> None:
    """
    로그인한 사용자의 Google Sheets 진도를
    Session State에 세션당 한 번 불러온다.

    API 실패 시 Session State 방식으로 계속 동작한다.
    """

    if not is_logged_in():
        return

    user_id = get_user_id()

    if not user_id:
        return


    synced_user_id = st.session_state.get(
        REMOTE_PROGRESS_USER_KEY,
        "",
    )

    is_synced = bool(
        st.session_state.get(
            REMOTE_PROGRESS_SYNCED_KEY,
            False,
        )
    )


    if (
        synced_user_id == user_id
        and is_synced
    ):
        return


    # -----------------------------------------------------
    # 중복 호출 방지
    # -----------------------------------------------------

    st.session_state[
        REMOTE_PROGRESS_USER_KEY
    ] = user_id

    st.session_state[
        REMOTE_PROGRESS_SYNCED_KEY
    ] = True


    try:

        remote_progress = (
            load_progress_from_sheets(
                user_id
            )
        )

    except Exception:

        return


    if not isinstance(
        remote_progress,
        dict,
    ):
        return


    progress = st.session_state[
        PROGRESS_STATE_KEY
    ]


    # -----------------------------------------------------
    # 원격 완료 상태 병합
    # -----------------------------------------------------

    for (
        section_id,
        remote_data,
    ) in remote_progress.items():

        if section_id not in progress:
            continue

        if not isinstance(
            remote_data,
            dict,
        ):
            continue


        progress[
            section_id
        ][
            "completed"
        ] = bool(
            remote_data.get(
                "completed",
                False,
            )
        )


# =========================================================
# 원격 형성평가 기록 불러오기
# =========================================================

def _load_remote_formative_results_once() -> None:
    """
    로그인한 사용자의 모든 형성평가 결과를
    Google Sheets에서 세션당 한 번 불러온다.

    불러온 결과를 이용하여:
    - history
    - attempt_count
    - 최근 점수
    - 최근 정답 수
    - 전체 문항 수
    - completed

    를 Session State에 복원한다.
    """

    if not is_logged_in():
        return


    user_id = get_user_id()

    if not user_id:
        return


    synced_user_id = st.session_state.get(
        REMOTE_FORMATIVE_USER_KEY,
        "",
    )

    is_synced = bool(
        st.session_state.get(
            REMOTE_FORMATIVE_SYNCED_KEY,
            False,
        )
    )


    if (
        synced_user_id == user_id
        and is_synced
    ):
        return


    # -----------------------------------------------------
    # 중복 호출 방지
    # -----------------------------------------------------

    st.session_state[
        REMOTE_FORMATIVE_USER_KEY
    ] = user_id

    st.session_state[
        REMOTE_FORMATIVE_SYNCED_KEY
    ] = True


    try:

        remote_results = (
            load_formative_results_from_sheets(
                user_id
            )
        )

    except Exception:

        return


    if not isinstance(
        remote_results,
        list,
    ):
        return


    if not remote_results:
        return


    progress = st.session_state[
        PROGRESS_STATE_KEY
    ]


    # -----------------------------------------------------
    # 소단원별 원격 기록 분류
    # -----------------------------------------------------

    grouped_results: dict[
        str,
        list[dict[str, Any]],
    ] = {}


    for item in remote_results:

        if not isinstance(
            item,
            dict,
        ):
            continue


        section_id = str(
            item.get(
                "section_id",
                "",
            )
        ).strip()


        if section_id not in progress:
            continue


        if section_id not in grouped_results:

            grouped_results[
                section_id
            ] = []


        grouped_results[
            section_id
        ].append(
            item
        )


    # -----------------------------------------------------
    # 각 소단원 형성평가 데이터 복원
    # -----------------------------------------------------

    for (
        section_id,
        results,
    ) in grouped_results.items():

        results.sort(
            key=lambda item: (
                int(
                    item.get(
                        "attempt_no",
                        0,
                    )
                    or 0
                )
            )
        )


        history = []


        for index, item in enumerate(
            results,
            start=1,
        ):

            attempt_no = int(
                item.get(
                    "attempt_no",
                    index,
                )
                or index
            )

            score = int(
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


            history.append(
                {
                    "attempt": attempt_no,
                    "score": score,
                    "correct": correct,
                    "total": total,
                }
            )


        if not history:
            continue


        latest = history[
            -1
        ]


        section = progress[
            section_id
        ]


        section[
            "history"
        ] = history


        section[
            "attempt_count"
        ] = len(
            history
        )


        section[
            "formative_score"
        ] = latest[
            "score"
        ]


        section[
            "formative_correct"
        ] = latest[
            "correct"
        ]


        section[
            "formative_total"
        ] = latest[
            "total"
        ]


        # 형성평가 기록이 존재하면
        # 해당 소단원은 완료 상태로 본다.
        section[
            "completed"
        ] = True


# =========================================================
# 원격 진도 저장
# =========================================================

def _save_remote_progress(
    section_id: str,
    completed: bool,
) -> None:
    """
    로그인한 사용자의 특정 소단원 진도를
    Google Sheets에 저장한다.

    실패해도 앱 실행은 유지한다.
    """

    if not is_logged_in():
        return


    user_id = get_user_id()

    if not user_id:
        return


    try:

        save_progress_to_sheets(
            user_id=user_id,
            section_id=section_id,
            completed=completed,
        )

    except Exception:

        pass


# =========================================================
# 원격 형성평가 저장
# =========================================================

def _save_remote_formative_result(
    section_id: str,
    score: int,
    correct_count: int,
    total_count: int,
) -> dict[str, Any] | None:
    """
    로그인한 사용자의 형성평가 결과를
    Google Sheets에 저장한다.

    성공 시 Apps Script의 결과를 반환한다.
    실패하면 None을 반환한다.
    """

    if not is_logged_in():
        return None


    user_id = get_user_id()

    if not user_id:
        return None


    try:

        result = (
            save_formative_result_to_sheets(
                user_id=user_id,
                section_id=section_id,
                score=score,
                correct=correct_count,
                total=total_count,
            )
        )

    except Exception:

        return None


    if not isinstance(
        result,
        dict,
    ):
        return None


    if not result.get(
        "success",
        False,
    ):
        return None


    return result


# =========================================================
# 초기화 및 기존 데이터 마이그레이션
# =========================================================

def initialize_progress() -> None:
    """
    학습 진도 데이터가 없다면 Session State에 생성한다.

    기존 progress 데이터에 빠진 필드가 있다면 자동 보완한다.

    로그인한 사용자의 경우:
    1. progress 시트 진도 복원
    2. formative_results 시트 응시 기록 복원

    을 수행한다.
    """

    if PROGRESS_STATE_KEY not in st.session_state:

        st.session_state[
            PROGRESS_STATE_KEY
        ] = _create_default_progress()


    progress = st.session_state[
        PROGRESS_STATE_KEY
    ]


    # -----------------------------------------------------
    # 데이터 구조 보완
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


            default_data = (
                _create_default_section_data()
            )


            for key, value in (
                default_data.items()
            ):

                if key in section:
                    continue


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


    # -----------------------------------------------------
    # Google Sheets 데이터 복원
    # -----------------------------------------------------

    _load_remote_progress_once()

    _load_remote_formative_results_once()


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


    _save_remote_progress(
        section_id=section_id,
        completed=True,
    )


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


    _save_remote_progress(
        section_id=section_id,
        completed=False,
    )


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

    저장 대상:
    1. 현재 Session State
    2. Google Sheets progress
    3. Google Sheets formative_results

    비로그인 사용자는 기존처럼
    Session State에만 저장한다.
    """

    section = get_section_progress(
        section_id
    )


    # -----------------------------------------------------
    # 점수 계산
    # -----------------------------------------------------

    if total_count <= 0:

        score = 0

    else:

        score = round(
            correct_count
            / total_count
            * 100
        )


    # -----------------------------------------------------
    # 로컬 기준 다음 회차
    # -----------------------------------------------------

    local_attempt = (
        section[
            "attempt_count"
        ]
        + 1
    )


    # -----------------------------------------------------
    # Google Sheets 형성평가 저장
    # -----------------------------------------------------

    remote_result = (
        _save_remote_formative_result(
            section_id=section_id,
            score=score,
            correct_count=correct_count,
            total_count=total_count,
        )
    )


    # -----------------------------------------------------
    # 서버의 attempt_no를 우선 사용
    # -----------------------------------------------------

    current_attempt = (
        local_attempt
    )


    if remote_result:

        remote_attempt = (
            remote_result.get(
                "attempt_no"
            )
        )


        try:

            remote_attempt = int(
                remote_attempt
            )

        except (
            TypeError,
            ValueError,
        ):

            remote_attempt = 0


        if remote_attempt > 0:

            current_attempt = (
                remote_attempt
            )


    # -----------------------------------------------------
    # 최근 결과 갱신
    # -----------------------------------------------------

    section[
        "attempt_count"
    ] = max(
        section[
            "attempt_count"
        ],
        current_attempt,
    )


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


    # 응시 회차 기준 정렬
    section[
        "history"
    ].sort(
        key=lambda item: item[
            "attempt"
        ]
    )


    # -----------------------------------------------------
    # 완료 처리
    # -----------------------------------------------------

    section[
        "completed"
    ] = True


    # -----------------------------------------------------
    # progress 시트 저장
    # -----------------------------------------------------

    _save_remote_progress(
        section_id=section_id,
        completed=True,
    )


# =========================================================
# 형성평가 이력 조회
# =========================================================

def get_formative_history(
    section_id: str,
) -> list[dict[str, Any]]:
    """
    특정 소단원의 전체 형성평가 이력을 반환한다.
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
    최초 형성평가 점수와 최근 점수의 차이를 반환한다.
    """

    history = get_formative_history(
        section_id
    )


    if len(
        history
    ) < 2:

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
    특정 소단원의 완료 여부를 반환한다.
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
    특정 학습 영역의 모든 소단원 완료 여부를 반환한다.
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
    전체 8개 소단원의 진도율을 계산한다.
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
# 완료 소단원 개수
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
    전체 소단원의 개수를 반환한다.
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
# 최근 점수 평균
# =========================================================

def get_formative_average() -> float | None:
    """
    각 소단원의 가장 최근 형성평가 점수를 기준으로
    평균을 계산한다.
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
        sum(
            scores
        )
        / len(
            scores
        ),
        1,
    )


# =========================================================
# 모든 응시 평균
# =========================================================

def get_all_attempt_average() -> float | None:
    """
    모든 형성평가 응시 기록의 평균 점수를 계산한다.
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
        sum(
            scores
        )
        / len(
            scores
        ),
        1,
    )


# =========================================================
# 전체 응시 횟수
# =========================================================

def get_total_attempt_count() -> int:
    """
    모든 형성평가 응시 횟수를 반환한다.
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
    현재 Session State의 학습 진도와
    형성평가 기록을 초기화한다.

    Google Sheets의 원격 기록은 삭제하지 않는다.
    """

    st.session_state[
        PROGRESS_STATE_KEY
    ] = _create_default_progress()