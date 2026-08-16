from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

import pandas as pd
import streamlit as st

from utils.auth import (
    get_current_teacher,
    require_teacher,
)

from utils.sheets_api import (
    post_to_sheets,
)

from utils.theme import (
    load_global_css,
)

from utils.navigation import (
    render_app_sidebar,
)

from utils.ui import (
    render_breadcrumb,
    render_progress_bar,
)


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="교사 대시보드 | 임베디드 구현 LAB",
    page_icon="👨‍🏫",
    layout="wide",
)

load_global_css()


# =========================================================
# 공통 사이드바
# =========================================================

render_app_sidebar(
    current_page="teacher_dashboard"
)


# =========================================================
# 교사 권한 확인
# =========================================================

require_teacher()

teacher = get_current_teacher()


# =========================================================
# 기본 설정
# =========================================================

TARGET_CLASS = "2학년 3반"

TOTAL_SECTION_COUNT = 8

SECTION_LABELS = {
    "1-1": "기술 스펙 적용 소프트웨어 검토",
    "1-2": "임베디드 시스템 평가",
    "2-1": "개발 도구 선정",
    "2-2": "개발 환경 구축",
    "3-1": "구현 및 오류 제거",
    "3-2": "디버깅 및 통합",
    "4-1": "인터페이스 구현",
    "4-2": "소스 코드 저장 및 버전 관리",
}


# =========================================================
# Helper
# =========================================================


def safe_int(
    value: Any,
    default: int = 0,
) -> int:
    """
    값을 안전하게 int로 변환합니다.
    """

    try:
        return int(
            float(value)
        )

    except (
        TypeError,
        ValueError,
    ):
        return default


def safe_float(
    value: Any,
    default: float = 0.0,
) -> float:
    """
    값을 안전하게 float로 변환합니다.
    """

    try:
        return float(value)

    except (
        TypeError,
        ValueError,
    ):
        return default


def format_score(
    value: Any,
) -> str:
    """
    점수를 보기 좋은 문자열로 반환합니다.
    """

    if value in (
        None,
        "",
    ):
        return "-"

    score = safe_float(
        value,
        0.0,
    )

    if score.is_integer():
        return f"{score:.0f}"

    return f"{score:.1f}"


def get_progress_percent(
    completed_count: int,
) -> float:
    """
    완료 소단원 개수를 진도율로 변환합니다.
    """

    if TOTAL_SECTION_COUNT <= 0:
        return 0.0

    return round(
        (
            completed_count
            / TOTAL_SECTION_COUNT
        )
        * 100,
        1,
    )


def get_student_display_name(
    student: dict[str, Any],
) -> str:
    """
    학생 선택 UI에서 사용할 표시 이름입니다.
    """

    number = safe_int(
        student.get(
            "student_number"
        )
    )

    name = str(
        student.get(
            "name",
            "",
        )
    ).strip()

    if number:
        return (
            f"{number}번 {name}"
        )

    return name or "이름 없음"


# =========================================================
# 교사용 데이터 조회
# =========================================================


@st.cache_data(
    ttl=30,
    show_spinner=False,
)
def load_teacher_dashboard_data() -> dict[str, Any]:
    """
    Apps Script에서 교사용 전체 데이터를 가져옵니다.

    예상 응답:

    {
        "success": True,
        "students": [...],
        "progress": [...],
        "formative_results": [...],
        "midterm_results": [...],
        "wrong_answers": [...]
    }
    """

    result = post_to_sheets(
        action="get_teacher_dashboard_data",
        payload={
            "class_name": TARGET_CLASS,
        },
        timeout=30,
    )

    if not isinstance(
        result,
        dict,
    ):
        return {
            "success": False,
            "error": "INVALID_RESPONSE",
        }

    return result


# =========================================================
# 데이터 불러오기
# =========================================================

with st.spinner(
    "학생 학습 데이터를 불러오고 있습니다..."
):

    dashboard_data = (
        load_teacher_dashboard_data()
    )


# =========================================================
# Header
# =========================================================

render_breadcrumb(
    "교사 대시보드"
)

st.title(
    "👨‍🏫 교사 학습 관리 대시보드"
)

st.markdown(
    f"""
    **{TARGET_CLASS} · 시스템 프로그래밍**

    학생별 학습 진도, 형성평가, 중간고사 및
    누적 오답 현황을 한 화면에서 확인합니다.
    """
)


# =========================================================
# Backend 연결 확인
# =========================================================

if not dashboard_data.get(
    "success"
):

    error_code = str(
        dashboard_data.get(
            "error",
            "UNKNOWN_ERROR",
        )
    )

    st.error(
        "교사용 학습 데이터를 불러오지 못했습니다."
    )

    if error_code == "UNKNOWN_ACTION":

        st.info(
            "현재 Apps Script에 "
            "`get_teacher_dashboard_data` API가 아직 없습니다. "
            "다음 단계에서 Code.gs에 교사용 전체 데이터 조회 기능을 "
            "추가하면 이 화면이 바로 활성화됩니다."
        )

    else:

        st.caption(
            f"오류 코드 · {error_code}"
        )

    st.stop()


# =========================================================
# 데이터 정리
# =========================================================

students = dashboard_data.get(
    "students",
    [],
)

progress_rows = dashboard_data.get(
    "progress",
    [],
)

formative_rows = dashboard_data.get(
    "formative_results",
    [],
)

midterm_rows = dashboard_data.get(
    "midterm_results",
    [],
)

wrong_rows = dashboard_data.get(
    "wrong_answers",
    [],
)


if not isinstance(
    students,
    list,
):
    students = []

if not isinstance(
    progress_rows,
    list,
):
    progress_rows = []

if not isinstance(
    formative_rows,
    list,
):
    formative_rows = []

if not isinstance(
    midterm_rows,
    list,
):
    midterm_rows = []

if not isinstance(
    wrong_rows,
    list,
):
    wrong_rows = []


# =========================================================
# 학생 정렬
# =========================================================

students = [
    student
    for student in students
    if isinstance(
        student,
        dict,
    )
]

students.sort(
    key=lambda student: (
        safe_int(
            student.get(
                "student_number"
            ),
            999,
        ),
        str(
            student.get(
                "name",
                "",
            )
        ),
    )
)


# =========================================================
# user_id 기준 그룹화
# =========================================================

progress_by_user: dict[
    str,
    list[dict[str, Any]],
] = defaultdict(list)

formative_by_user: dict[
    str,
    list[dict[str, Any]],
] = defaultdict(list)

midterm_by_user: dict[
    str,
    list[dict[str, Any]],
] = defaultdict(list)

wrong_by_user: dict[
    str,
    list[dict[str, Any]],
] = defaultdict(list)


for row in progress_rows:

    if not isinstance(
        row,
        dict,
    ):
        continue

    user_id = str(
        row.get(
            "user_id",
            "",
        )
    ).strip()

    if user_id:

        progress_by_user[
            user_id
        ].append(
            row
        )


for row in formative_rows:

    if not isinstance(
        row,
        dict,
    ):
        continue

    user_id = str(
        row.get(
            "user_id",
            "",
        )
    ).strip()

    if user_id:

        formative_by_user[
            user_id
        ].append(
            row
        )


for row in midterm_rows:

    if not isinstance(
        row,
        dict,
    ):
        continue

    user_id = str(
        row.get(
            "user_id",
            "",
        )
    ).strip()

    if user_id:

        midterm_by_user[
            user_id
        ].append(
            row
        )


for row in wrong_rows:

    if not isinstance(
        row,
        dict,
    ):
        continue

    user_id = str(
        row.get(
            "user_id",
            "",
        )
    ).strip()

    if user_id:

        wrong_by_user[
            user_id
        ].append(
            row
        )


# =========================================================
# 학생별 통계 생성
# =========================================================

student_summaries: list[
    dict[str, Any]
] = []


for student in students:

    user_id = str(
        student.get(
            "user_id",
            "",
        )
    ).strip()

    number = safe_int(
        student.get(
            "student_number"
        )
    )

    name = str(
        student.get(
            "name",
            "",
        )
    ).strip()

    email = str(
        student.get(
            "email",
            "",
        )
    ).strip()


    # -----------------------------------------------------
    # 진도
    # -----------------------------------------------------

    student_progress = (
        progress_by_user.get(
            user_id,
            [],
        )
    )

    completed_sections = {
        str(
            row.get(
                "section_id",
                "",
            )
        ).strip()
        for row
        in student_progress
        if str(
            row.get(
                "completed",
                "",
            )
        ).strip().lower()
        in {
            "true",
            "1",
            "yes",
            "y",
        }
    }

    completed_count = len(
        completed_sections
    )

    progress_percent = (
        get_progress_percent(
            completed_count
        )
    )


    # -----------------------------------------------------
    # 형성평가
    # -----------------------------------------------------

    student_formative = (
        formative_by_user.get(
            user_id,
            [],
        )
    )

    formative_scores = [
        safe_float(
            row.get(
                "score"
            )
        )
        for row
        in student_formative
        if row.get(
            "score"
        )
        not in (
            None,
            "",
        )
    ]

    formative_average = (
        round(
            sum(
                formative_scores
            )
            / len(
                formative_scores
            ),
            1,
        )
        if formative_scores
        else None
    )


    # -----------------------------------------------------
    # 중간고사
    # -----------------------------------------------------

    student_midterms = (
        midterm_by_user.get(
            user_id,
            [],
        )
    )

    midterm_scores = [
        safe_float(
            row.get(
                "score"
            )
        )
        for row
        in student_midterms
        if row.get(
            "score"
        )
        not in (
            None,
            "",
        )
    ]

    latest_midterm = (
        midterm_scores[-1]
        if midterm_scores
        else None
    )

    best_midterm = (
        max(
            midterm_scores
        )
        if midterm_scores
        else None
    )


    # -----------------------------------------------------
    # 오답
    # -----------------------------------------------------

    student_wrong = (
        wrong_by_user.get(
            user_id,
            [],
        )
    )

    wrong_count = len(
        student_wrong
    )


    # -----------------------------------------------------
    # 취약 영역
    # -----------------------------------------------------

    section_counter = Counter()

    for row in student_wrong:

        section_id = str(
            row.get(
                "section_id",
                "",
            )
        ).strip()

        if section_id:

            section_counter[
                section_id
            ] += 1


    weakest_section = "-"

    if section_counter:

        section_id, count = (
            section_counter.most_common(
                1
            )[0]
        )

        weakest_section = (
            f"{section_id} "
            f"{SECTION_LABELS.get(section_id, '')}"
        ).strip()


    student_summaries.append(
        {
            "번호": number,
            "이름": name,
            "이메일": email,
            "진도율": progress_percent,
            "완료": (
                f"{completed_count}"
                f"/{TOTAL_SECTION_COUNT}"
            ),
            "형성평가 평균": (
                formative_average
            ),
            "중간고사 최근": (
                latest_midterm
            ),
            "중간고사 최고": (
                best_midterm
            ),
            "누적 오답": wrong_count,
            "취약 영역": weakest_section,
            "_user_id": user_id,
            "_completed_count": (
                completed_count
            ),
        }
    )


# =========================================================
# 등록 학생 없음
# =========================================================

if not student_summaries:

    st.info(
        f"아직 {TARGET_CLASS}에 등록된 학생이 없습니다."
    )

    st.stop()


# =========================================================
# 반 전체 요약
# =========================================================

st.markdown(
    "## 📊 학급 전체 현황"
)


registered_count = len(
    student_summaries
)

fully_completed_count = sum(
    1
    for student
    in student_summaries
    if student[
        "_completed_count"
    ]
    >= TOTAL_SECTION_COUNT
)

class_progress_average = round(
    sum(
        student[
            "진도율"
        ]
        for student
        in student_summaries
    )
    / registered_count,
    1,
)


formative_values = [
    student[
        "형성평가 평균"
    ]
    for student
    in student_summaries
    if student[
        "형성평가 평균"
    ]
    is not None
]

class_formative_average = (
    round(
        sum(
            formative_values
        )
        / len(
            formative_values
        ),
        1,
    )
    if formative_values
    else None
)


midterm_values = [
    student[
        "중간고사 최근"
    ]
    for student
    in student_summaries
    if student[
        "중간고사 최근"
    ]
    is not None
]

class_midterm_average = (
    round(
        sum(
            midterm_values
        )
        / len(
            midterm_values
        ),
        1,
    )
    if midterm_values
    else None
)


metric_cols = st.columns(
    5
)


with metric_cols[0]:

    st.metric(
        "등록 학생",
        f"{registered_count}명",
    )


with metric_cols[1]:

    st.metric(
        "평균 진도율",
        f"{class_progress_average:.1f}%",
    )


with metric_cols[2]:

    st.metric(
        "전체 학습 완료",
        f"{fully_completed_count}명",
    )


with metric_cols[3]:

    st.metric(
        "형성평가 평균",
        (
            format_score(
                class_formative_average
            )
            if class_formative_average
            is not None
            else "-"
        ),
    )


with metric_cols[4]:

    st.metric(
        "중간고사 평균",
        (
            format_score(
                class_midterm_average
            )
            if class_midterm_average
            is not None
            else "-"
        ),
    )


# =========================================================
# 학급 전체 진도
# =========================================================

st.caption(
    "전체 학생의 소단원 완료 상태를 기준으로 계산한 평균 진도입니다."
)

render_progress_bar(
    class_progress_average,
    show_label=False,
)


# =========================================================
# 학생별 요약
# =========================================================

st.divider()

st.markdown(
    "## 👥 학생별 학습 현황"
)

st.caption(
    "학생 번호 순으로 정렬됩니다."
)


summary_df = pd.DataFrame(
    [
        {
            "번호": (
                f"{student['번호']}번"
                if student[
                    "번호"
                ]
                else "-"
            ),
            "이름": student[
                "이름"
            ],
            "진도율": (
                f"{student['진도율']:.1f}%"
            ),
            "완료": student[
                "완료"
            ],
            "형성평가 평균": (
                format_score(
                    student[
                        "형성평가 평균"
                    ]
                )
            ),
            "중간고사 최근": (
                format_score(
                    student[
                        "중간고사 최근"
                    ]
                )
            ),
            "중간고사 최고": (
                format_score(
                    student[
                        "중간고사 최고"
                    ]
                )
            ),
            "누적 오답": student[
                "누적 오답"
            ],
            "취약 영역": student[
                "취약 영역"
            ],
        }
        for student
        in student_summaries
    ]
)


st.dataframe(
    summary_df,
    hide_index=True,
    width="stretch",
)


# =========================================================
# 진도율 시각화
# =========================================================

st.markdown(
    "### 📈 학생별 진도율"
)


progress_chart_df = pd.DataFrame(
    {
        "학생": [
            (
                f"{student['번호']}번 "
                f"{student['이름']}"
            )
            for student
            in student_summaries
        ],
        "진도율": [
            student[
                "진도율"
            ]
            for student
            in student_summaries
        ],
    }
)


st.bar_chart(
    progress_chart_df,
    x="학생",
    y="진도율",
    y_label="진도율 (%)",
)


# =========================================================
# 학생 상세 분석
# =========================================================

st.divider()

st.markdown(
    "## 🔎 학생 상세 분석"
)


student_options = {
    get_student_display_name(
        student
    ): student
    for student
    in students
}


selected_student_label = (
    st.selectbox(
        "분석할 학생",
        options=list(
            student_options.keys()
        ),
        key=(
            "teacher_dashboard_"
            "student_select"
        ),
    )
)


selected_student = (
    student_options[
        selected_student_label
    ]
)

selected_user_id = str(
    selected_student.get(
        "user_id",
        "",
    )
).strip()


selected_progress = (
    progress_by_user.get(
        selected_user_id,
        [],
    )
)

selected_formative = (
    formative_by_user.get(
        selected_user_id,
        [],
    )
)

selected_midterm = (
    midterm_by_user.get(
        selected_user_id,
        [],
    )
)

selected_wrong = (
    wrong_by_user.get(
        selected_user_id,
        [],
    )
)


# =========================================================
# 선택 학생 기본 정보
# =========================================================

student_number = safe_int(
    selected_student.get(
        "student_number"
    )
)

student_name = str(
    selected_student.get(
        "name",
        "",
    )
).strip()

student_email = str(
    selected_student.get(
        "email",
        "",
    )
).strip()


with st.container(
    border=True
):

    st.markdown(
        f"### 👤 {student_number}번 {student_name}"
    )

    st.caption(
        student_email
    )


# =========================================================
# 선택 학생 요약
# =========================================================

selected_summary = next(
    (
        student
        for student
        in student_summaries
        if student[
            "_user_id"
        ]
        == selected_user_id
    ),
    None,
)


if selected_summary:

    detail_metrics = st.columns(
        5
    )


    with detail_metrics[0]:

        st.metric(
            "진도율",
            (
                f"{selected_summary['진도율']:.1f}%"
            ),
        )


    with detail_metrics[1]:

        st.metric(
            "완료 소단원",
            selected_summary[
                "완료"
            ],
        )


    with detail_metrics[2]:

        st.metric(
            "형성평가 평균",
            format_score(
                selected_summary[
                    "형성평가 평균"
                ]
            ),
        )


    with detail_metrics[3]:

        st.metric(
            "중간고사 최고",
            format_score(
                selected_summary[
                    "중간고사 최고"
                ]
            ),
        )


    with detail_metrics[4]:

        st.metric(
            "누적 오답",
            selected_summary[
                "누적 오답"
            ],
        )


# =========================================================
# 학습 진행 상세
# =========================================================

st.markdown(
    "### 📚 소단원 학습 진행"
)


completed_section_ids = {
    str(
        row.get(
            "section_id",
            "",
        )
    ).strip()
    for row
    in selected_progress
    if str(
        row.get(
            "completed",
            "",
        )
    ).strip().lower()
    in {
        "true",
        "1",
        "yes",
        "y",
    }
}


section_rows = []


for section_id, label in (
    SECTION_LABELS.items()
):

    completed = (
        section_id
        in completed_section_ids
    )

    section_rows.append(
        {
            "소단원": section_id,
            "학습 내용": label,
            "상태": (
                "✅ 완료"
                if completed
                else "⬜ 미완료"
            ),
        }
    )


st.dataframe(
    pd.DataFrame(
        section_rows
    ),
    hide_index=True,
    width="stretch",
)


# =========================================================
# 형성평가 분석
# =========================================================

st.markdown(
    "### 📝 형성평가 이력"
)


if selected_formative:

    formative_df = pd.DataFrame(
        [
            {
                "소단원": row.get(
                    "section_id",
                    "",
                ),
                "응시": (
                    f"{row.get('attempt_no', '')}회"
                ),
                "점수": row.get(
                    "score",
                    "",
                ),
                "정답": (
                    f"{row.get('correct', '')}"
                    f"/{row.get('total', '')}"
                ),
                "응시일": row.get(
                    "submitted_at",
                    "",
                ),
            }
            for row
            in selected_formative
        ]
    )

    st.dataframe(
        formative_df,
        hide_index=True,
        width="stretch",
    )

else:

    st.info(
        "아직 형성평가 응시 기록이 없습니다."
    )


# =========================================================
# 중간고사 분석
# =========================================================

st.markdown(
    "### 🎯 중간고사 종합 대비 이력"
)


if selected_midterm:

    midterm_df = pd.DataFrame(
        [
            {
                "응시": (
                    f"{row.get('attempt_no', '')}회"
                ),
                "점수": row.get(
                    "score",
                    "",
                ),
                "정답": (
                    f"{row.get('correct', '')}"
                    f"/{row.get('total', '')}"
                ),
                "오답": row.get(
                    "wrong_count",
                    "",
                ),
                "응시일": row.get(
                    "submitted_at",
                    "",
                ),
            }
            for row
            in selected_midterm
        ]
    )

    st.dataframe(
        midterm_df,
        hide_index=True,
        width="stretch",
    )


    chart_df = pd.DataFrame(
        {
            "응시": [
                f"{index + 1}회"
                for index
                in range(
                    len(
                        selected_midterm
                    )
                )
            ],
            "점수": [
                safe_float(
                    row.get(
                        "score"
                    )
                )
                for row
                in selected_midterm
            ],
        }
    )

    st.line_chart(
        chart_df,
        x="응시",
        y="점수",
        y_label="점수",
    )


else:

    st.info(
        "아직 중간고사 종합 대비 응시 기록이 없습니다."
    )


# =========================================================
# 오답 분석
# =========================================================

st.markdown(
    "### ❌ 누적 오답 분석"
)


if selected_wrong:

    wrong_section_counter = Counter()

    wrong_topic_counter = Counter()


    for row in selected_wrong:

        section_id = str(
            row.get(
                "section_id",
                "",
            )
        ).strip()

        topic = str(
            row.get(
                "topic",
                "",
            )
        ).strip()


        if section_id:

            wrong_section_counter[
                section_id
            ] += 1


        if topic:

            wrong_topic_counter[
                topic
            ] += 1


    if wrong_section_counter:

        st.markdown(
            "**오답이 많은 소단원**"
        )

        weak_rows = []

        for (
            section_id,
            count,
        ) in wrong_section_counter.most_common():

            weak_rows.append(
                {
                    "소단원": section_id,
                    "학습 내용": (
                        SECTION_LABELS.get(
                            section_id,
                            ""
                        )
                    ),
                    "오답 수": count,
                }
            )


        st.dataframe(
            pd.DataFrame(
                weak_rows
            ),
            hide_index=True,
            width="stretch",
        )


    with st.expander(
        "누적 오답 상세 보기"
    ):

        wrong_detail_df = (
            pd.DataFrame(
                [
                    {
                        "소단원": row.get(
                            "section_id",
                            "",
                        ),
                        "주제": row.get(
                            "topic",
                            "",
                        ),
                        "난이도": row.get(
                            "difficulty",
                            "",
                        ),
                        "학생 답": row.get(
                            "user_answer",
                            "",
                        ),
                        "정답": row.get(
                            "correct_answer",
                            "",
                        ),
                        "기록일": row.get(
                            "created_at",
                            "",
                        ),
                    }
                    for row
                    in selected_wrong
                ]
            )
        )

        st.dataframe(
            wrong_detail_df,
            hide_index=True,
            width="stretch",
        )


else:

    st.success(
        "현재 저장된 누적 오답이 없습니다."
    )


# =========================================================
# 보충 지도 대상
# =========================================================

st.divider()

st.markdown(
    "## 🧭 보충 지도 참고"
)

st.caption(
    "학습 진도와 평가 기록을 기준으로 "
    "추가 확인이 필요한 학생을 빠르게 확인합니다."
)


support_students = []


for student in student_summaries:

    reasons = []

    if student[
        "진도율"
    ] < 50:

        reasons.append(
            "진도 50% 미만"
        )


    formative_average = student[
        "형성평가 평균"
    ]

    if (
        formative_average
        is not None
        and formative_average < 60
    ):

        reasons.append(
            "형성평가 평균 60점 미만"
        )


    latest_midterm = student[
        "중간고사 최근"
    ]

    if (
        latest_midterm
        is not None
        and latest_midterm < 60
    ):

        reasons.append(
            "중간고사 최근 점수 60점 미만"
        )


    if student[
        "누적 오답"
    ] >= 5:

        reasons.append(
            "누적 오답 5개 이상"
        )


    if reasons:

        support_students.append(
            {
                "번호": (
                    f"{student['번호']}번"
                ),
                "이름": student[
                    "이름"
                ],
                "확인 필요": (
                    ", ".join(
                        reasons
                    )
                ),
                "취약 영역": student[
                    "취약 영역"
                ],
            }
        )


if support_students:

    st.warning(
        f"현재 추가 확인이 필요한 학생이 "
        f"{len(support_students)}명 있습니다."
    )

    st.dataframe(
        pd.DataFrame(
            support_students
        ),
        hide_index=True,
        width="stretch",
    )

else:

    st.success(
        "현재 설정된 기준에서 추가 확인이 필요한 학생이 없습니다."
    )


# =========================================================
# 새로고침
# =========================================================

st.divider()


refresh_col1, refresh_col2 = (
    st.columns(
        [
            1,
            4,
        ]
    )
)


with refresh_col1:

    if st.button(
        "🔄 데이터 새로고침",
        key=(
            "teacher_dashboard_"
            "refresh"
        ),
        width="stretch",
    ):

        load_teacher_dashboard_data.clear()

        st.rerun()


with refresh_col2:

    st.caption(
        "교사 대시보드는 최대 30초 동안 데이터를 캐시합니다. "
        "학생이 방금 평가를 제출했다면 새로고침 버튼을 눌러주세요."
    )