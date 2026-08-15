from __future__ import annotations

from html import escape
from textwrap import dedent

import streamlit as st

from data.lessons.lesson_1_1 import LESSON_1_1
from data.lessons.lesson_1_2 import LESSON_1_2

from data.quizzes.quiz_1_1 import (
    EXAM_PRACTICE_1_1,
    FORMATIVE_QUIZ_1_1,
)

from data.quizzes.quiz_1_2 import (
    EXAM_PRACTICE_1_2,
    FORMATIVE_QUIZ_1_2,
)

from utils.progress import (
    get_lesson_progress,
    is_lesson_completed,
    is_section_completed,
)

from utils.quiz import (
    render_exam_practice,
    render_quiz,
)

from utils.theme import load_global_css

from utils.ui import (
    render_breadcrumb,
    render_learning_objectives,
    render_progress_bar,
    render_summary,
)


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="학습 1 | 기술 명세 검토",
    page_icon="📘",
    layout="wide",
)

load_global_css()


# =========================================================
# 페이지 전용 HTML Helper
# =========================================================

def render_html(html: str) -> None:
    """
    Custom HTML을 Markdown 파서 없이 직접 렌더링한다.
    """

    st.html(
        dedent(html).strip()
    )


def render_surface_header(
    title: str,
    description: str | None = None,
    label: str | None = None,
) -> None:
    """
    큰 학습 Surface 내부의 제목 영역.
    """

    label_html = ""

    if label:
        label_html = (
            '<div class="edu-surface-label">'
            f"{escape(label)}"
            "</div>"
        )

    description_html = ""

    if description:
        description_html = (
            '<div class="edu-surface-desc">'
            f"{escape(description)}"
            "</div>"
        )

    render_html(
        f"""
        {label_html}

        <div class="edu-surface-title">
            {escape(title)}
        </div>

        {description_html}
        """
    )


def render_concept(
    title: str,
    content: str,
) -> None:
    """
    핵심 개념 강조 영역.
    """

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


def render_pills(
    items: list[str],
) -> None:
    """
    짧은 개념을 Pill 형태로 표시한다.
    """

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


def render_exam_panel(
    points: list[str],
    title: str = "중간고사 핵심 포인트",
) -> None:
    """
    시험 핵심 내용 강조 영역.
    """

    if not points:
        return

    items_html = "".join(
        f"<li>{escape(str(point))}</li>"
        for point in points
    )

    render_html(
        f"""
        <div class="edu-exam">
            <div class="edu-exam-title">
                🎯 {escape(title)}
            </div>

            <ul>
                {items_html}
            </ul>
        </div>
        """
    )


def render_process(
    steps: list[str],
) -> None:
    """
    순서가 중요한 내용을
    Compact Process 형태로 표시한다.
    """

    if not steps:
        return

    html_parts: list[str] = []

    for index, step in enumerate(steps):

        html_parts.append(
            (
                '<span class="edu-process-step">'
                f"{escape(str(step))}"
                "</span>"
            )
        )

        if index < len(steps) - 1:
            html_parts.append(
                '<span class="edu-process-arrow">'
                "→"
                "</span>"
            )

    render_html(
        f"""
        <div class="edu-process">
            {''.join(html_parts)}
        </div>
        """
    )


def render_feature(
    title: str,
    description: str,
    english: str | None = None,
) -> None:
    """
    특성/용어 + 설명을 표시한다.
    """

    english_html = ""

    if english:
        english_html = (
            '<div class="edu-feature-en">'
            f"{escape(english)}"
            "</div>"
        )

    render_html(
        f"""
        <div class="edu-feature">
            <div class="edu-feature-title">
                {escape(title)}
            </div>

            {english_html}

            <div class="edu-feature-desc">
                {escape(description)}
            </div>
        </div>
        """
    )


# =========================================================
# 학습 1-1 데이터
# =========================================================

metadata_1_1 = LESSON_1_1["metadata"]

embedded_system = LESSON_1_1[
    "embedded_system"
]

software_fields = LESSON_1_1[
    "software_fields"
]

specification_documents = LESSON_1_1[
    "specification_documents"
]

embedded_os = LESSON_1_1[
    "embedded_os"
]

hardware_review = LESSON_1_1[
    "hardware_review"
]

os_selection = LESSON_1_1[
    "os_selection"
]


# =========================================================
# 학습 1-2 데이터
# =========================================================

metadata_1_2 = LESSON_1_2[
    "metadata"
]

models_and_standards = LESSON_1_2[
    "models_and_standards"
]

open_source_license = LESSON_1_2[
    "open_source_license"
]

reliability_prediction = LESSON_1_2[
    "reliability_prediction"
]

control_system_reliability = LESSON_1_2[
    "control_system_reliability"
]

skill_set = LESSON_1_2[
    "skill_set"
]

software_testing_certification = LESSON_1_2[
    "software_testing_certification"
]

functionality_evaluation = LESSON_1_2[
    "functionality_evaluation"
]

quality_evaluation = LESSON_1_2[
    "quality_evaluation"
]


# =========================================================
# 진도
# =========================================================

lesson_1_progress = get_lesson_progress(
    "1"
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
    "📘 **학습 1 · 기술 명세 검토하기**"
)


# =========================================================
# Breadcrumb
# =========================================================

render_breadcrumb(
    "홈",
    "학습 1",
    "기술 명세 검토하기",
)


# =========================================================
# HERO
# =========================================================

render_html(
    """
    <div class="edu-hero">

        <div class="edu-hero-eyebrow">
            EMBEDDED APPLICATION
        </div>

        <div class="edu-hero-title">
            학습 1. 기술 명세 검토하기
        </div>

        <div class="edu-hero-desc">
            임베디드 애플리케이션 구현 전 기술 스펙과 요구사항을
            검토하고 시스템의 적용 수준을 평가합니다.
        </div>

    </div>
    """
)


# =========================================================
# 진도율
# =========================================================

render_progress_bar(
    lesson_1_progress,
    label="학습 1 전체 진도",
)

if is_lesson_completed("1"):

    st.success(
        "🎉 학습 1의 모든 소단원을 완료했습니다!"
    )


# =========================================================
# 학습 내용 선택
# =========================================================

st.markdown(
    "## 학습 내용 선택"
)


lesson_tab_1, lesson_tab_2 = st.tabs(
    [
        "1-1. 기술 스펙이 적용된 소프트웨어 검토",
        "1-2. 임베디드 시스템의 평가",
    ],
    key="lesson_1_main_tabs",
    on_change="rerun",
)


# =========================================================
# 1-1
# =========================================================

if lesson_tab_1.open:

    with lesson_tab_1:

        st.markdown(
            f"## {metadata_1_1['section']}. "
            f"{metadata_1_1['title']}"
        )

        st.caption(
            "임베디드 시스템의 기본 개념부터 제품 사양서, "
            "SRS, 하드웨어 검토와 운영체제 선정까지 학습합니다."
        )


        # -------------------------------------------------
        # 학습 목표
        # -------------------------------------------------

        with st.container(
            key="edu_section_1_1_objectives"
        ):

            render_surface_header(
                "학습 목표",
                "이 소단원에서 도달해야 하는 핵심 학습 목표입니다.",
                label="LEARNING GOALS",
            )

            for objective in LESSON_1_1["objectives"]:
                st.markdown(f"- {objective}")


        # -------------------------------------------------
        # 내부 탭
        # -------------------------------------------------

        (
            embedded_tab,
            software_tab,
            document_tab,
            os_tab,
            hardware_tab,
            os_selection_tab,
            experience_1_1_tab,
            formative_1_1_tab,
            exam_1_1_tab,
        ) = st.tabs(
            [
                "① 임베디드 시스템",
                "② SW 기술 분야",
                "③ 제품 사양서 · SRS",
                "④ 임베디드 OS",
                "⑤ 하드웨어 검토",
                "⑥ 운영체제 선정",
                "⑦ 개념 체험",
                "⑧ 형성평가",
                "⑨ 중간고사 대비",
            ],
            key="lesson_1_1_inner_tabs",
            on_change="rerun",
        )


        # =================================================
        # ① 임베디드 시스템
        # =================================================

        if embedded_tab.open:

            with embedded_tab:

                st.markdown(
                    "## 임베디드 시스템"
                )

                st.caption(
                    "특정 목적을 수행하는 Hardware와 "
                    "Software의 결합 구조를 이해합니다."
                )


                # -----------------------------------------
                # 핵심 개념
                # -----------------------------------------

                with st.container(
                    key="edu_section_embedded_core"
                ):

                    render_surface_header(
                        "임베디드 시스템이란?",
                        (
                            "일반 컴퓨터와 구분되는 "
                            "임베디드 시스템의 기본 개념입니다."
                        ),
                        label="CORE CONCEPT",
                    )

                    definition = embedded_system[
                        "definition"
                    ]

                    render_concept(
                        definition[
                            "title"
                        ],
                        definition[
                            "content"
                        ],
                    )


                    st.markdown(
                        "### Hardware + Software"
                    )

                    hw_col, plus_col, sw_col = (
                        st.columns(
                            [5, 1, 5]
                        )
                    )


                    with hw_col:

                        with st.container(
                            key="edu_subsection_hw"
                        ):

                            st.markdown(
                                "**Hardware**"
                            )

                            st.caption(
                                "시스템의 물리적 구성"
                            )

                            st.markdown(
                                "- 프로세서\n"
                                "- 메모리\n"
                                "- 입출력 장치"
                            )


                    with plus_col:

                        st.markdown("")
                        st.markdown("")
                        st.markdown(
                            "### +"
                        )


                    with sw_col:

                        with st.container(
                            key="edu_subsection_sw"
                        ):

                            st.markdown(
                                "**Software**"
                            )

                            st.caption(
                                "하드웨어를 제어하는 프로그램"
                            )

                            st.markdown(
                                "- HW 제어\n"
                                "- 기능 수행\n"
                                "- 시스템 동작 관리"
                            )


                # -----------------------------------------
                # 적용 분야
                # -----------------------------------------

                with st.container(
                    key="edu_section_embedded_application"
                ):

                    render_surface_header(
                        "주요 적용 분야",
                        (
                            "임베디드 시스템은 일상 기기부터 "
                            "산업 장비까지 다양한 영역에 적용됩니다."
                        ),
                        label="APPLICATION",
                    )

                    render_pills(
                        embedded_system[
                            "application_fields"
                        ]
                    )


                # -----------------------------------------
                # 특성
                # -----------------------------------------

                with st.container(
                    key="edu_section_embedded_features"
                ):

                    render_surface_header(
                        "주요 특성",
                        (
                            "일반 컴퓨터 시스템과 구분되는 "
                            "임베디드 시스템의 핵심 특성입니다."
                        ),
                        label="KEY FEATURES",
                    )

                    characteristics = embedded_system[
                        "characteristics"
                    ]

                    for start in range(
                        0,
                        len(characteristics),
                        2,
                    ):

                        current_items = (
                            characteristics[
                                start:start + 2
                            ]
                        )

                        cols = st.columns(
                            len(
                                current_items
                            )
                        )

                        for col, item in zip(
                            cols,
                            current_items,
                        ):

                            with col:

                                render_feature(
                                    item[
                                        "name"
                                    ],
                                    item[
                                        "description"
                                    ],
                                    item.get(
                                        "english"
                                    ),
                                )


                render_exam_panel(
                    embedded_system[
                        "exam_points"
                    ]
                )


        # =================================================
        # ② SW 기술 분야
        # =================================================

        if software_tab.open:

            with software_tab:

                st.markdown(
                    "## 임베디드 SW의 주요 기술 분야"
                )

                st.caption(
                    "임베디드 Software가 어떤 영역으로 "
                    "구성되는지 살펴봅니다."
                )


                with st.container(
                    key="edu_section_software_intro"
                ):

                    render_surface_header(
                        "임베디드 Software 기술 구조",
                        software_fields[
                            "intro"
                        ],
                        label="SOFTWARE FIELD",
                    )


                    items = software_fields[
                        "items"
                    ]

                    for start in range(
                        0,
                        len(items),
                        2,
                    ):

                        current_items = items[
                            start:start + 2
                        ]

                        cols = st.columns(
                            len(
                                current_items
                            )
                        )

                        for index, (col, item) in enumerate(
                            zip(
                                cols,
                                current_items,
                            )
                        ):

                            with col:

                                with st.container(
                                    key=(
                                        "edu_subsection_"
                                        f"software_{start}_{index}"
                                    )
                                ):

                                    st.markdown(
                                        f"**{item['name']}**"
                                    )

                                    st.write(
                                        item[
                                            "description"
                                        ]
                                    )


                st.info(
                    "임베디드 애플리케이션은 일반 응용 프로그램과 달리 "
                    "**Hardware Specification의 영향을 크게 받습니다.**"
                )


        # =================================================
        # ③ 제품 사양서 · SRS
        # =================================================

        if document_tab.open:

            with document_tab:

                st.markdown(
                    "## 제품 사양서와 SRS"
                )

                st.caption(
                    "구현 전에 반드시 확인해야 하는 "
                    "대표 요구사항 문서입니다."
                )


                product_specification = (
                    specification_documents[
                        "product_specification"
                    ]
                )

                srs = specification_documents[
                    "srs"
                ]


                # -----------------------------------------
                # 제품 사양서
                # -----------------------------------------

                with st.container(
                    key="edu_section_product_spec"
                ):

                    render_surface_header(
                        "제품 기획서(제품 사양서)",
                        product_specification[
                            "description"
                        ],
                        label="PRODUCT SPEC",
                    )

                    st.markdown(
                        "**주요 항목**"
                    )

                    render_pills(
                        product_specification[
                            "items"
                        ]
                    )


                    with st.expander(
                        "🚗 차량용 블랙박스 제품 사양서 예시"
                    ):

                        for item in product_specification[
                            "example"
                        ]:

                            col1, col2 = st.columns(
                                [2, 5]
                            )

                            with col1:

                                st.markdown(
                                    f"**{item['category']}**"
                                )

                            with col2:

                                st.write(
                                    item[
                                        "value"
                                    ]
                                )


                # -----------------------------------------
                # SRS
                # -----------------------------------------

                with st.container(
                    key="edu_section_srs"
                ):

                    render_surface_header(
                        "소프트웨어 요구사항 명세서(SRS)",
                        srs[
                            "description"
                        ],
                        label="SOFTWARE REQUIREMENTS",
                    )

                    st.markdown(
                        "**SRS 주요 구성 항목**"
                    )

                    for index, item in enumerate(
                        srs[
                            "sections"
                        ],
                        start=1,
                    ):

                        st.markdown(
                            f"{index}. {item}"
                        )


                render_exam_panel(
                    specification_documents[
                        "exam_points"
                    ]
                )


        # =================================================
        # ④ 임베디드 OS
        # =================================================

        if os_tab.open:

            with os_tab:

                st.markdown(
                    "## 임베디드 운영체제"
                )

                st.caption(
                    "대표적인 Embedded OS의 특징을 비교합니다."
                )


                with st.container(
                    key="edu_section_embedded_os"
                ):

                    render_surface_header(
                        "대표 임베디드 운영체제",
                        (
                            "Target 환경과 요구사항에 따라 "
                            "적합한 운영체제를 선택해야 합니다."
                        ),
                        label="EMBEDDED OS",
                    )

                    systems = embedded_os[
                        "systems"
                    ]

                    cols = st.columns(
                        len(
                            systems
                        )
                    )

                    for index, (col, system) in enumerate(
                        zip(
                            cols,
                            systems,
                        )
                    ):

                        with col:

                            with st.container(
                                key=(
                                    "edu_subsection_os_"
                                    f"{index}"
                                )
                            ):

                                st.markdown(
                                    f"**{system['name']}**"
                                )

                                st.write(
                                    system[
                                        "description"
                                    ]
                                )


                st.info(
                    "운영체제는 익숙한 제품을 선택하는 것이 아니라 "
                    "**Target Hardware · 개발 환경 · Memory · "
                    "Driver · License** 등을 함께 고려해야 합니다."
                )


        # =================================================
        # ⑤ 하드웨어 검토
        # =================================================

        if hardware_tab.open:

            with hardware_tab:

                st.markdown(
                    "## 하드웨어 구성요소 검토"
                )

                st.caption(
                    "요구사항에 맞는 Hardware를 선정하고 "
                    "자원 활용도를 검토합니다."
                )


                process = hardware_review[
                    "process"
                ]


                # -----------------------------------------
                # 검토 흐름
                # -----------------------------------------

                with st.container(
                    key="edu_section_hardware_process"
                ):

                    render_surface_header(
                        "하드웨어 검토 과정",
                        (
                            "요구사항 검토부터 자원 활용도 확인, "
                            "필요 시 재선정까지의 흐름입니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        [
                            item[
                                "name"
                            ]
                            for item in process
                        ]
                    )


                    with st.expander(
                        "검토 단계 자세히 보기"
                    ):

                        for item in process:

                            st.markdown(
                                f"**{item['step']}. "
                                f"{item['name']}**"
                            )

                            st.write(
                                item[
                                    "description"
                                ]
                            )


                # -----------------------------------------
                # 검토 항목
                # -----------------------------------------

                with st.container(
                    key="edu_section_hardware_requirements"
                ):

                    render_surface_header(
                        "주요 하드웨어 검토 항목",
                        (
                            "Target Hardware를 선정할 때 "
                            "확인해야 하는 주요 조건입니다."
                        ),
                        label="CHECK POINT",
                    )

                    render_pills(
                        hardware_review[
                            "requirements"
                        ]
                    )


                # -----------------------------------------
                # 선정 결과
                # -----------------------------------------

                with st.container(
                    key="edu_section_hardware_example"
                ):

                    render_surface_header(
                        "하드웨어 선정 결과 예시",
                        (
                            "요구사항을 기준으로 선정된 "
                            "Hardware 예시입니다."
                        ),
                        label="EXAMPLE",
                    )

                    st.dataframe(
                        hardware_review[
                            "selection_example"
                        ],
                        width="stretch",
                        hide_index=True,
                    )


                # -----------------------------------------
                # 자원 활용도
                # -----------------------------------------

                resource = hardware_review[
                    "resource_utilization"
                ]

                with st.container(
                    key="edu_section_resource_review"
                ):

                    render_surface_header(
                        "자원 활용도 검토",
                        resource[
                            "description"
                        ],
                        label="RESOURCE",
                    )

                    render_pills(
                        resource[
                            "targets"
                        ]
                    )

                    st.dataframe(
                        resource[
                            "example"
                        ],
                        width="stretch",
                        hide_index=True,
                    )

                    st.warning(
                        resource[
                            "example_result"
                        ]
                    )


                render_exam_panel(
                    hardware_review[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑥ 운영체제 선정
        # =================================================

        if os_selection_tab.open:

            with os_selection_tab:

                st.markdown(
                    "## 최적의 임베디드 운영체제 선정"
                )

                st.caption(
                    "Target 환경에 적합한 Embedded OS를 "
                    "선택하기 위한 기준을 살펴봅니다."
                )


                with st.container(
                    key="edu_section_os_selection"
                ):

                    render_surface_header(
                        "운영체제 선정 시 확인할 14가지 요소",
                        os_selection[
                            "intro"
                        ],
                        label="SELECTION GUIDE",
                    )

                    factors = os_selection[
                        "factors"
                    ]

                    for start in range(
                        0,
                        len(factors),
                        2,
                    ):

                        current_items = factors[
                            start:start + 2
                        ]

                        cols = st.columns(
                            len(
                                current_items
                            )
                        )

                        for col, item in zip(
                            cols,
                            current_items,
                        ):

                            with col:

                                render_feature(
                                    (
                                        f"{item['number']}. "
                                        f"{item['title']}"
                                    ),
                                    item[
                                        "description"
                                    ],
                                )


                render_exam_panel(
                    os_selection[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑦ 개념 체험
        # =================================================

        if experience_1_1_tab.open:

            with experience_1_1_tab:

                st.markdown(
                    "## 개념 체험"
                )

                st.caption(
                    "학습한 개념을 짧은 판단 활동으로 확인합니다."
                )


                # -----------------------------------------
                # 특성
                # -----------------------------------------

                with st.container(
                    key="edu_section_experience_characteristic"
                ):

                    render_surface_header(
                        "임베디드 시스템 특성 구분",
                        (
                            "상황에 가장 적합한 "
                            "임베디드 시스템 특성을 찾아보세요."
                        ),
                        label="ACTIVITY 01",
                    )

                    characteristic_question = st.selectbox(
                        "상황을 선택하세요.",
                        [
                            "선택하세요",
                            "정해진 시간 안에 반드시 동작해야 한다.",
                            "배터리 사용 시간을 늘려야 한다.",
                            "제한된 메모리를 효율적으로 사용해야 한다.",
                            "사용자가 요구하는 서비스 수준을 제공해야 한다.",
                        ],
                        key="1_1_characteristic_question",
                    )

                    characteristic_answers = {
                        (
                            "정해진 시간 안에 반드시 동작해야 한다."
                        ): "실시간성",

                        (
                            "배터리 사용 시간을 늘려야 한다."
                        ): "저전력",

                        (
                            "제한된 메모리를 효율적으로 사용해야 한다."
                        ): "경량성",

                        (
                            "사용자가 요구하는 서비스 수준을 제공해야 한다."
                        ): "QoS",
                    }


                    if characteristic_question != "선택하세요":

                        answer = st.selectbox(
                            "가장 적절한 특성은?",
                            [
                                "선택하세요",
                                "실시간성",
                                "경량성",
                                "저전력",
                                "보안성",
                                "QoS",
                            ],
                            key="1_1_characteristic_answer",
                        )

                        if answer != "선택하세요":

                            if (
                                answer
                                == characteristic_answers[
                                    characteristic_question
                                ]
                            ):

                                st.success(
                                    "정답입니다! ✅"
                                )

                            else:

                                st.error(
                                    "다시 생각해보세요."
                                )


                # -----------------------------------------
                # 문서
                # -----------------------------------------

                with st.container(
                    key="edu_section_experience_document"
                ):

                    render_surface_header(
                        "기술 명세 문서 구분",
                        (
                            "제품 사양서와 SRS의 역할을 "
                            "구분해봅니다."
                        ),
                        label="ACTIVITY 02",
                    )

                    document_question = st.radio(
                        (
                            "사용자와 개발자 사이의 요구사항을 "
                            "명세하여 Software 개발 기준이 되는 문서는?"
                        ),
                        [
                            "제품 사양서",
                            "SRS",
                            "회로도",
                        ],
                        index=None,
                        key="1_1_document_question",
                    )

                    if document_question == "SRS":

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif document_question:

                        st.error(
                            "다시 확인해보세요."
                        )


                # -----------------------------------------
                # HW 검토 순서
                # -----------------------------------------

                with st.container(
                    key="edu_section_experience_hardware"
                ):

                    render_surface_header(
                        "하드웨어 검토 순서",
                        (
                            "Hardware 검토 과정의 "
                            "올바른 순서를 확인합니다."
                        ),
                        label="ACTIVITY 03",
                    )

                    flow_question = st.radio(
                        "올바른 검토 흐름은?",
                        [
                            (
                                "요구사항 검토 → "
                                "자원 활용도 검토 → "
                                "필요 시 재선정"
                            ),
                            (
                                "재선정 → "
                                "요구사항 검토 → "
                                "자원 활용도 검토"
                            ),
                        ],
                        index=None,
                        key="1_1_hardware_flow",
                    )

                    if flow_question == (
                        "요구사항 검토 → "
                        "자원 활용도 검토 → "
                        "필요 시 재선정"
                    ):

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif flow_question:

                        st.error(
                            "순서를 다시 확인해보세요."
                        )


        # =================================================
        # ⑧ 형성평가
        # =================================================

        if formative_1_1_tab.open:

            with formative_1_1_tab:

                render_quiz(
                    FORMATIVE_QUIZ_1_1,
                    title="✅ 1-1 형성평가",
                    description=(
                        "임베디드 시스템, 기술 스펙 문서, "
                        "하드웨어 검토와 운영체제 선정 내용을 확인합니다."
                    ),
                )


        # =================================================
        # ⑨ 중간고사
        # =================================================

        if exam_1_1_tab.open:

            with exam_1_1_tab:

                render_exam_practice(
                    EXAM_PRACTICE_1_1
                )


        if is_section_completed(
            "1-1"
        ):

            st.success(
                "✅ 1-1 학습 완료"
            )


# =========================================================
# 1-2
# =========================================================

if lesson_tab_2.open:

    with lesson_tab_2:

        st.markdown(
            f"## {metadata_1_2['section']}. "
            f"{metadata_1_2['title']}"
        )

        st.caption(
            "관련 모델과 표준을 검토하고 신뢰성, Skill-Set, "
            "시험 인증, 기능성과 품질 평가 방법을 학습합니다."
        )


        # -------------------------------------------------
        # 학습 목표
        # -------------------------------------------------

        with st.container(
            key="edu_section_1_2_objectives"
        ):

            render_surface_header(
                "학습 목표",
                "임베디드 시스템 평가와 관련된 핵심 개념을 학습합니다.",
                label="LEARNING GOALS",
            )

            for objective in LESSON_1_2["objectives"]:
                st.markdown(f"- {objective}")


        (
            license_tab,
            reliability_tab,
            skill_tab,
            certification_tab,
            functionality_tab,
            quality_tab,
            experience_1_2_tab,
            formative_1_2_tab,
            exam_1_2_tab,
        ) = st.tabs(
            [
                "① 라이선스",
                "② 신뢰성 평가",
                "③ Skill-Set",
                "④ 시험 인증",
                "⑤ 기능성 평가",
                "⑥ 품질 평가",
                "⑦ 개념 체험",
                "⑧ 형성평가",
                "⑨ 중간고사 대비",
            ],
            key="lesson_1_2_inner_tabs",
            on_change="rerun",
        )


        # =================================================
        # ① 라이선스
        # =================================================

        if license_tab.open:

            with license_tab:

                st.markdown(
                    "## 관련 모델 및 표준과 라이선스"
                )


                with st.container(
                    key="edu_section_models_standards"
                ):

                    render_surface_header(
                        "관련 모델 및 표준",
                        models_and_standards[
                            "intro"
                        ],
                        label="MODEL & STANDARD",
                    )

                    render_pills(
                        models_and_standards[
                            "review_targets"
                        ]
                    )


                with st.container(
                    key="edu_section_open_source"
                ):

                    render_surface_header(
                        open_source_license[
                            "title"
                        ],
                        open_source_license[
                            "intro"
                        ],
                        label="OPEN SOURCE",
                    )

                    for item in open_source_license[
                        "review_points"
                    ]:

                        st.markdown(
                            f"- {item}"
                        )

                    st.warning(
                        open_source_license[
                            "caution"
                        ]
                    )


                render_exam_panel(
                    [
                        *models_and_standards[
                            "exam_points"
                        ],
                        *open_source_license[
                            "exam_points"
                        ],
                    ]
                )


        # =================================================
        # ② 신뢰성 평가
        # =================================================

        if reliability_tab.open:

            with reliability_tab:

                st.markdown(
                    "## 임베디드 시스템 신뢰성 평가"
                )


                # -----------------------------------------
                # 모델
                # -----------------------------------------

                with st.container(
                    key="edu_section_reliability_models"
                ):

                    render_surface_header(
                        reliability_prediction[
                            "title"
                        ],
                        reliability_prediction[
                            "intro"
                        ],
                        label="RELIABILITY",
                    )

                    models = reliability_prediction[
                        "models"
                    ]

                    for start in range(
                        0,
                        len(models),
                        2,
                    ):

                        current_items = models[
                            start:start + 2
                        ]

                        cols = st.columns(
                            len(
                                current_items
                            )
                        )

                        for index, (col, model) in enumerate(
                            zip(
                                cols,
                                current_items,
                            )
                        ):

                            with col:

                                with st.container(
                                    key=(
                                        "edu_subsection_model_"
                                        f"{start}_{index}"
                                    )
                                ):

                                    st.markdown(
                                        f"**{model['name']}**"
                                    )

                                    st.caption(
                                        model[
                                            "category"
                                        ]
                                    )


                # -----------------------------------------
                # 관점
                # -----------------------------------------

                with st.container(
                    key="edu_section_reliability_aspects"
                ):

                    render_surface_header(
                        "평가 관점",
                        (
                            "신뢰성을 평가할 때 확인하는 "
                            "주요 관점입니다."
                        ),
                        label="ASPECT",
                    )

                    render_pills(
                        reliability_prediction[
                            "evaluation_aspects"
                        ]
                    )


                # -----------------------------------------
                # 절차
                # -----------------------------------------

                procedure = reliability_prediction[
                    "procedure"
                ]

                with st.container(
                    key="edu_section_reliability_process"
                ):

                    render_surface_header(
                        "신뢰성 평가 절차",
                        (
                            "신뢰성 평가가 진행되는 "
                            "순서를 살펴봅니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        [
                            item[
                                "title"
                            ]
                            for item in procedure
                        ]
                    )


                    with st.expander(
                        "평가 절차 자세히 보기"
                    ):

                        for item in procedure:

                            st.markdown(
                                f"**{item['step']}. "
                                f"{item['title']}**"
                            )

                            st.write(
                                item[
                                    "description"
                                ]
                            )


                # -----------------------------------------
                # 평가 방법
                # -----------------------------------------

                with st.container(
                    key="edu_section_reliability_methods"
                ):

                    render_surface_header(
                        "평가 방법",
                        (
                            "전문가의 판단과 의견을 "
                            "수집하기 위한 평가 방법입니다."
                        ),
                        label="METHOD",
                    )

                    render_pills(
                        reliability_prediction[
                            "evaluation_methods"
                        ]
                    )

                    st.info(
                        "전문가 평가에는 **리커트 척도**를 활용할 수 있으며, "
                        "**델파이 방법과 브레인스토밍법**을 통해 "
                        "전문가 집단의 의견과 판단을 수집할 수 있습니다."
                    )


                # -----------------------------------------
                # 제어 시스템
                # -----------------------------------------

                with st.container(
                    key="edu_section_control_reliability"
                ):

                    render_surface_header(
                        "임베디드 제어 시스템의 신뢰성 평가",
                        control_system_reliability[
                            "intro"
                        ],
                        label="CONTROL SYSTEM",
                    )

                    for item in control_system_reliability[
                        "review_points"
                    ]:

                        st.markdown(
                            f"- {item}"
                        )


                render_exam_panel(
                    [
                        *reliability_prediction[
                            "exam_points"
                        ],
                        *control_system_reliability[
                            "exam_points"
                        ],
                    ]
                )


        # =================================================
        # ③ Skill-Set
        # =================================================

        if skill_tab.open:

            with skill_tab:

                st.markdown(
                    "## 임베디드 SW 적용 인력 Skill-Set"
                )


                with st.container(
                    key="edu_section_skill_set"
                ):

                    render_surface_header(
                        "Skill-Set 7개 영역",
                        skill_set[
                            "intro"
                        ],
                        label="SKILL SET",
                    )

                    items = skill_set[
                        "items"
                    ]

                    for start in range(
                        0,
                        len(items),
                        2,
                    ):

                        current_items = items[
                            start:start + 2
                        ]

                        cols = st.columns(
                            len(
                                current_items
                            )
                        )

                        for col, item in zip(
                            cols,
                            current_items,
                        ):

                            with col:

                                render_feature(
                                    (
                                        f"{item['number']}. "
                                        f"{item['name']}"
                                    ),
                                    item[
                                        "description"
                                    ],
                                    item[
                                        "english"
                                    ],
                                )


                render_exam_panel(
                    skill_set[
                        "exam_points"
                    ]
                )


        # =================================================
        # ④ 시험 인증
        # =================================================

        if certification_tab.open:

            with certification_tab:

                st.markdown(
                    "## 임베디드 소프트웨어 시험 인증"
                )


                with st.container(
                    key="edu_section_certification"
                ):

                    render_surface_header(
                        "시험 인증 적용 분야",
                        software_testing_certification[
                            "intro"
                        ],
                        label="CERTIFICATION",
                    )

                    fields = software_testing_certification[
                        "application_fields"
                    ]

                    cols = st.columns(
                        len(
                            fields
                        )
                    )

                    for index, (col, item) in enumerate(
                        zip(
                            cols,
                            fields,
                        )
                    ):

                        with col:

                            with st.container(
                                key=(
                                    "edu_subsection_cert_"
                                    f"{index}"
                                )
                            ):

                                st.markdown(
                                    f"**{item['field']}**"
                                )

                                st.write(
                                    item[
                                        "description"
                                    ]
                                )


                render_exam_panel(
                    software_testing_certification[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑤ 기능성 평가
        # =================================================

        if functionality_tab.open:

            with functionality_tab:

                st.markdown(
                    "## 임베디드 SW 기능성 평가"
                )


                # -----------------------------------------
                # 품질 특성
                # -----------------------------------------

                with st.container(
                    key="edu_section_iso_quality"
                ):

                    render_surface_header(
                        "ISO/IEC 9126 품질 특성",
                        functionality_evaluation[
                            "intro"
                        ],
                        label="ISO / IEC 9126",
                    )

                    render_pills(
                        functionality_evaluation[
                            "quality_characteristics"
                        ]
                    )


                # -----------------------------------------
                # AP OP HP
                # -----------------------------------------

                with st.container(
                    key="edu_section_ap_op_hp"
                ):

                    render_surface_header(
                        "임베디드 SW 구성",
                        (
                            "임베디드 Software를 "
                            "AP · OP · HP 관점에서 구분합니다."
                        ),
                        label="SOFTWARE COMPONENT",
                    )

                    components = functionality_evaluation[
                        "components"
                    ]

                    cols = st.columns(
                        3
                    )

                    for col, item in zip(
                        cols,
                        components,
                    ):

                        with col:

                            with st.container(
                                key=(
                                    "edu_subsection_component_"
                                    f"{item['code']}"
                                )
                            ):

                                st.markdown(
                                    f"### {item['code']}"
                                )

                                st.markdown(
                                    f"**{item['name']}**"
                                )

                                st.caption(
                                    item[
                                        "korean"
                                    ]
                                )

                                st.write(
                                    item[
                                        "description"
                                    ]
                                )


                # -----------------------------------------
                # 절차
                # -----------------------------------------

                with st.container(
                    key="edu_section_function_process"
                ):

                    render_surface_header(
                        "기능성 평가 절차",
                        (
                            "기능성 평가의 전체 흐름을 "
                            "확인합니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        functionality_evaluation[
                            "procedure"
                        ]
                    )


                render_exam_panel(
                    functionality_evaluation[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑥ 품질 평가
        # =================================================

        if quality_tab.open:

            with quality_tab:

                st.markdown(
                    "## 임베디드 소프트웨어 품질 평가"
                )


                with st.container(
                    key="edu_section_quality"
                ):

                    render_surface_header(
                        "소프트웨어 품질 특성 6가지",
                        quality_evaluation[
                            "intro"
                        ],
                        label="QUALITY",
                    )

                    characteristics = quality_evaluation[
                        "quality_characteristics"
                    ]

                    render_pills(
                        characteristics
                    )

                    st.info(
                        "Software 품질은 하나의 요소만으로 판단하지 않고 "
                        "**기능성 · 신뢰성 · 이식성 · 사용성 · "
                        "유지보수성 · 효율성**을 함께 고려합니다."
                    )


                render_exam_panel(
                    quality_evaluation[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑦ 개념 체험
        # =================================================

        if experience_1_2_tab.open:

            with experience_1_2_tab:

                st.markdown(
                    "## 평가 개념 체험"
                )


                # -----------------------------------------
                # 신뢰성 모델
                # -----------------------------------------

                with st.container(
                    key="edu_section_experience_model"
                ):

                    render_surface_header(
                        "신뢰성 예측 모델",
                        (
                            "신뢰성 예측 모델을 "
                            "구분해봅니다."
                        ),
                        label="ACTIVITY 01",
                    )

                    model_question = st.radio(
                        (
                            "다음 중 Embedded SW "
                            "신뢰성 예측 모델이 아닌 것은?"
                        ),
                        [
                            "MUSA Model",
                            "Putnam Model",
                            "SoftRel Prediction Model",
                            "OSI Model",
                        ],
                        index=None,
                        key="1_2_model_question",
                    )

                    if model_question == "OSI Model":

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif model_question:

                        st.error(
                            "다시 확인해보세요."
                        )


                # -----------------------------------------
                # 전문가 의견
                # -----------------------------------------

                with st.container(
                    key="edu_section_experience_method"
                ):

                    render_surface_header(
                        "전문가 의견 수렴 방법",
                        (
                            "전문가 집단을 활용하는 "
                            "평가 방법을 구분합니다."
                        ),
                        label="ACTIVITY 02",
                    )

                    method_question = st.radio(
                        (
                            "전문가 집단의 의견과 판단을 "
                            "수집하는 데 활용되는 방법은?"
                        ),
                        [
                            "델파이 방법",
                            "FIFO",
                            "DMA",
                            "Polling",
                        ],
                        index=None,
                        key="1_2_method_question",
                    )

                    if method_question == "델파이 방법":

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif method_question:

                        st.error(
                            "다시 확인해보세요."
                        )


                # -----------------------------------------
                # AP OP HP
                # -----------------------------------------

                with st.container(
                    key="edu_section_experience_component"
                ):

                    render_surface_header(
                        "AP · OP · HP 구분",
                        (
                            "Software 구성 요소의 역할을 "
                            "구분합니다."
                        ),
                        label="ACTIVITY 03",
                    )

                    component_case = st.selectbox(
                        "설명을 선택하세요.",
                        [
                            "선택하세요",
                            "애플리케이션 자체의 기능과 로직에 의존",
                            "운영체제 기능을 사용하기 위해 구현",
                            "하드웨어 접근과 제어를 위해 구현",
                        ],
                        key="1_2_component_case",
                    )

                    component_answers = {
                        (
                            "애플리케이션 자체의 기능과 로직에 의존"
                        ): "AP",

                        (
                            "운영체제 기능을 사용하기 위해 구현"
                        ): "OP",

                        (
                            "하드웨어 접근과 제어를 위해 구현"
                        ): "HP",
                    }


                    if component_case != "선택하세요":

                        component_answer = st.selectbox(
                            "어떤 부분인가요?",
                            [
                                "선택하세요",
                                "AP",
                                "OP",
                                "HP",
                            ],
                            key="1_2_component_answer",
                        )

                        if component_answer != "선택하세요":

                            if (
                                component_answer
                                == component_answers[
                                    component_case
                                ]
                            ):

                                st.success(
                                    "정답입니다! ✅"
                                )

                            else:

                                st.error(
                                    "다시 확인해보세요."
                                )


                # -----------------------------------------
                # 품질 특성
                # -----------------------------------------

                with st.container(
                    key="edu_section_experience_quality"
                ):

                    render_surface_header(
                        "품질 특성 확인",
                        (
                            "ISO/IEC 9126의 품질 특성을 "
                            "구분합니다."
                        ),
                        label="ACTIVITY 04",
                    )

                    quality_question = st.multiselect(
                        (
                            "다음 중 ISO/IEC 9126 품질 평가 기준에 "
                            "포함되는 항목을 선택하세요."
                        ),
                        [
                            "기능성",
                            "신뢰성",
                            "이식성",
                            "사용성",
                            "유지보수성",
                            "효율성",
                            "케이블 길이",
                        ],
                        key="1_2_quality_question",
                    )

                    expected_quality = {
                        "기능성",
                        "신뢰성",
                        "이식성",
                        "사용성",
                        "유지보수성",
                        "효율성",
                    }


                    if quality_question:

                        if (
                            set(
                                quality_question
                            )
                            == expected_quality
                        ):

                            st.success(
                                "6가지 품질 특성을 "
                                "정확하게 선택했습니다! ✅"
                            )

                        elif (
                            "케이블 길이"
                            in quality_question
                        ):

                            st.error(
                                "케이블 길이는 품질 특성 "
                                "6가지에 포함되지 않습니다."
                            )

                        else:

                            st.info(
                                "아직 선택하지 않은 "
                                "품질 특성이 있습니다."
                            )


        # =================================================
        # ⑧ 형성평가
        # =================================================

        if formative_1_2_tab.open:

            with formative_1_2_tab:

                render_quiz(
                    FORMATIVE_QUIZ_1_2,
                    title="✅ 1-2 형성평가",
                    description=(
                        "라이선스, 신뢰성 평가, Skill-Set, "
                        "시험 인증, 기능성 및 품질 평가 내용을 확인합니다."
                    ),
                )


        # =================================================
        # ⑨ 중간고사
        # =================================================

        if exam_1_2_tab.open:

            with exam_1_2_tab:

                render_exam_practice(
                    EXAM_PRACTICE_1_2
                )


        if is_section_completed(
            "1-2"
        ):

            st.success(
                "✅ 1-2 학습 완료"
            )


# =========================================================
# 전체 완료
# =========================================================

if is_lesson_completed(
    "1"
):

    st.divider()

    st.success(
        "🎉 학습 1 · 기술 명세 검토하기를 "
        "모두 완료했습니다!"
    )

    with st.expander(
        "📚 학습 1 핵심 내용 다시 보기"
    ):

        st.markdown(
            "### 1-1 핵심 정리"
        )

        render_summary(
            LESSON_1_1[
                "summary"
            ]
        )

        st.divider()

        st.markdown(
            "### 1-2 핵심 정리"
        )

        render_summary(
            LESSON_1_2[
                "summary"
            ]
        )