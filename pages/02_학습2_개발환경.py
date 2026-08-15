from __future__ import annotations

from html import escape
from textwrap import dedent

import streamlit as st

from data.lessons.lesson_2_1 import LESSON_2_1
from data.lessons.lesson_2_2 import LESSON_2_2

from data.quizzes.quiz_2_1 import (
    EXAM_PRACTICE_2_1,
    FORMATIVE_QUIZ_2_1,
)

from data.quizzes.quiz_2_2 import (
    EXAM_PRACTICE_2_2,
    FORMATIVE_QUIZ_2_2,
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
    render_progress_bar,
    render_summary,
)


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="학습 2 | 개발 환경 구축",
    page_icon="🛠️",
    layout="wide",
)

load_global_css()


# =========================================================
# HTML Helper
# =========================================================

def render_html(html: str) -> None:
    """
    Markdown parser를 거치지 않고
    Custom HTML을 직접 렌더링한다.
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

    if not items:
        return

    items_html = "".join(
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
            {items_html}
        </div>
        """
    )


def render_exam_panel(
    points: list[str],
    title: str = "중간고사 핵심 포인트",
) -> None:

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

    if not steps:
        return

    parts: list[str] = []

    for index, step in enumerate(steps):

        parts.append(
            (
                '<span class="edu-process-step">'
                f"{escape(str(step))}"
                "</span>"
            )
        )

        if index < len(steps) - 1:
            parts.append(
                '<span class="edu-process-arrow">'
                "→"
                "</span>"
            )

    render_html(
        f"""
        <div class="edu-process">
            {''.join(parts)}
        </div>
        """
    )


def render_feature(
    title: str,
    description: str,
    english: str | None = None,
) -> None:

    english_html = ""

    if english:
        english_html = (
            '<div class="edu-feature-en">'
            f"{escape(str(english))}"
            "</div>"
        )

    render_html(
        f"""
        <div class="edu-feature">

            <div class="edu-feature-title">
                {escape(str(title))}
            </div>

            {english_html}

            <div class="edu-feature-desc">
                {escape(str(description))}
            </div>

        </div>
        """
    )


def render_command(
    command: str,
    caption: str | None = None,
) -> None:

    if caption:
        st.caption(caption)

    st.code(
        command,
        language="bash",
    )


# =========================================================
# 데이터
# =========================================================

metadata_2_1 = LESSON_2_1["metadata"]
cross_development = LESSON_2_1["cross_development"]
toolchain = LESSON_2_1["toolchain"]
target_board = LESSON_2_1["target_board"]
processor_architecture = LESSON_2_1["processor_architecture"]
hardware_interfaces = LESSON_2_1["hardware_interfaces"]
arduino_mapping_2_1 = LESSON_2_1["arduino_mapping"]
practice_2_1 = LESSON_2_1["practice"]


metadata_2_2 = LESSON_2_2["metadata"]
environment_overview = LESSON_2_2["environment_overview"]
virtual_machine = LESSON_2_2["virtual_machine"]
nfs = LESSON_2_2["nfs"]
linux_file_management = LESSON_2_2["linux_file_management"]
cross_compiler_installation = LESSON_2_2[
    "cross_compiler_installation"
]
cross_compilation = LESSON_2_2["cross_compilation"]
target_execution = LESSON_2_2["target_execution"]
troubleshooting = LESSON_2_2["troubleshooting"]
arduino_mapping_2_2 = LESSON_2_2["arduino_mapping"]
practice_2_2 = LESSON_2_2["practice"]


# =========================================================
# 진도
# =========================================================

lesson_2_progress = get_lesson_progress("2")


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
    "🛠️ **학습 2 · 애플리케이션 개발 환경 구축하기**"
)


# =========================================================
# Breadcrumb
# =========================================================

render_breadcrumb(
    "홈",
    "학습 2",
    "개발 환경 구축하기",
)


# =========================================================
# HERO
# =========================================================

render_html(
    """
    <div class="edu-hero">

        <div class="edu-hero-eyebrow">
            DEVELOPMENT ENVIRONMENT
        </div>

        <div class="edu-hero-title">
            학습 2. 애플리케이션 개발 환경 구축하기
        </div>

        <div class="edu-hero-desc">
            Host와 Target으로 구성되는 교차 개발 환경을 이해하고,
            Tool Chain과 Linux 기반 개발 환경을 구축하는 방법을 학습합니다.
        </div>

    </div>
    """
)


# =========================================================
# 진도율
# =========================================================

render_progress_bar(
    lesson_2_progress,
    label="학습 2 전체 진도",
)

if is_lesson_completed("2"):

    st.success(
        "🎉 학습 2의 모든 소단원을 완료했습니다!"
    )


# =========================================================
# 학습 내용 선택
# =========================================================

st.markdown(
    "## 학습 내용 선택"
)

lesson_tab_1, lesson_tab_2 = st.tabs(
    [
        "2-1. 개발 도구 선정",
        "2-2. 애플리케이션 개발 환경 구축",
    ],
    key="lesson_2_main_tabs",
    on_change="rerun",
)


# =========================================================
# 2-1
# =========================================================

if lesson_tab_1.open:

    with lesson_tab_1:

        st.markdown(
            f"## {metadata_2_1['section']}. "
            f"{metadata_2_1['title']}"
        )

        st.caption(
            "교차 개발 환경, Tool Chain, Target Board, "
            "Processor Architecture와 주요 Hardware Interface를 "
            "학습합니다."
        )


        # -------------------------------------------------
        # 학습 목표
        # -------------------------------------------------

        with st.container(
            key="edu_section_2_1_objectives"
        ):

            render_surface_header(
                "학습 목표",
                (
                    "개발 도구와 교차 개발 환경을 구성하는 "
                    "핵심 개념을 이해합니다."
                ),
                label="LEARNING GOALS",
            )

            for objective in LESSON_2_1["objectives"]:
                st.markdown(
                    f"- {objective}"
                )


        # -------------------------------------------------
        # 내부 탭
        # -------------------------------------------------

        (
            cross_tab,
            toolchain_tab,
            target_tab,
            processor_tab,
            interface_tab,
            arduino_tab_2_1,
            practice_tab_2_1,
            formative_tab_2_1,
            exam_tab_2_1,
        ) = st.tabs(
            [
                "① 교차 개발 환경",
                "② Tool Chain",
                "③ Target Board",
                "④ RISC · CISC",
                "⑤ Hardware Interface",
                "⑥ Arduino 연결",
                "⑦ 개념 체험",
                "⑧ 형성평가",
                "⑨ 중간고사 대비",
            ],
            key="lesson_2_1_inner_tabs",
            on_change="rerun",
        )


        # =================================================
        # ① 교차 개발 환경
        # =================================================

        if cross_tab.open:

            with cross_tab:

                st.markdown(
                    "## 교차 개발 환경"
                )

                st.caption(
                    "Host System에서 개발하고 Target System에서 "
                    "실행하는 임베디드 개발 구조를 이해합니다."
                )


                # -----------------------------------------
                # 핵심 개념
                # -----------------------------------------

                with st.container(
                    key="edu_section_cross_core"
                ):

                    render_surface_header(
                        "교차 개발 환경이란?",
                        cross_development[
                            "definition"
                        ],
                        label="CROSS DEVELOPMENT",
                    )

                    render_concept(
                        "왜 교차 개발 환경이 필요한가?",
                        cross_development[
                            "why_needed"
                        ],
                    )


                    # Host / Target
                    host_col, arrow_col, target_col = st.columns(
                        [5, 1, 5]
                    )

                    host = cross_development["host"]
                    target = cross_development["target"]

                    with host_col:

                        with st.container(
                            key="edu_subsection_cross_host"
                        ):

                            st.markdown(
                                "### 💻 Host System"
                            )

                            st.write(
                                host["description"]
                            )

                            st.markdown(
                                "**주요 역할**"
                            )

                            for role in host["roles"]:
                                st.markdown(
                                    f"- {role}"
                                )

                            st.caption(
                                "예: "
                                + " · ".join(
                                    host["examples"]
                                )
                            )


                    with arrow_col:

                        st.markdown("")
                        st.markdown("")
                        st.markdown("")
                        st.markdown(
                            "## →"
                        )


                    with target_col:

                        with st.container(
                            key="edu_subsection_cross_target"
                        ):

                            st.markdown(
                                "### 🎯 Target System"
                            )

                            st.write(
                                target["description"]
                            )

                            st.markdown(
                                "**주요 역할**"
                            )

                            for role in target["roles"]:
                                st.markdown(
                                    f"- {role}"
                                )

                            st.caption(
                                "예: "
                                + " · ".join(
                                    target["examples"]
                                )
                            )


                # -----------------------------------------
                # 연결 Interface
                # -----------------------------------------

                with st.container(
                    key="edu_section_cross_interfaces"
                ):

                    render_surface_header(
                        "Host ↔ Target 연결",
                        (
                            "Host와 Target 사이에서 프로그램 전송과 "
                            "디버깅 등에 사용할 수 있는 연결 방식입니다."
                        ),
                        label="CONNECTION",
                    )

                    render_pills(
                        cross_development[
                            "interfaces"
                        ]
                    )


                # -----------------------------------------
                # 개발 흐름
                # -----------------------------------------

                with st.container(
                    key="edu_section_cross_flow"
                ):

                    render_surface_header(
                        "교차 개발 흐름",
                        (
                            "Source 작성부터 Target 실행까지의 "
                            "기본 순서입니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        cross_development[
                            "development_flow"
                        ]
                    )


                render_exam_panel(
                    cross_development[
                        "exam_points"
                    ]
                )


        # =================================================
        # ② Tool Chain
        # =================================================

        if toolchain_tab.open:

            with toolchain_tab:

                st.markdown(
                    "## 개발 Tool Chain"
                )

                st.caption(
                    "Source Code를 Target이 실행할 수 있는 "
                    "프로그램으로 만드는 개발 도구의 역할을 구분합니다."
                )


                with st.container(
                    key="edu_section_toolchain_intro"
                ):

                    render_surface_header(
                        "Tool Chain이란?",
                        toolchain[
                            "intro"
                        ],
                        label="TOOL CHAIN",
                    )


                    # -------------------------------------
                    # Tool 종류
                    # -------------------------------------

                    tools = toolchain[
                        "tools"
                    ]

                    for start in range(
                        0,
                        len(tools),
                        2,
                    ):

                        current = tools[
                            start:start + 2
                        ]

                        cols = st.columns(
                            len(current)
                        )

                        for index, (col, item) in enumerate(
                            zip(cols, current)
                        ):

                            with col:

                                with st.container(
                                    key=(
                                        "edu_subsection_tool_"
                                        f"{start}_{index}"
                                    )
                                ):

                                    render_feature(
                                        item["name"],
                                        item["description"],
                                    )


                # -----------------------------------------
                # Flow
                # -----------------------------------------

                with st.container(
                    key="edu_section_toolchain_flow"
                ):

                    render_surface_header(
                        "Build Flow",
                        (
                            "Source Code가 실행 파일로 변환되는 "
                            "과정을 순서대로 확인합니다."
                        ),
                        label="BUILD PROCESS",
                    )

                    render_process(
                        toolchain[
                            "flow"
                        ]
                    )

                    st.caption(
                        toolchain[
                            "simple_flow"
                        ]
                    )


                render_exam_panel(
                    toolchain[
                        "exam_points"
                    ]
                )


        # =================================================
        # ③ Target Board
        # =================================================

        if target_tab.open:

            with target_tab:

                st.markdown(
                    "## Target Board와 Reference Board"
                )

                st.caption(
                    "프로그램이 실제로 실행되는 Target Hardware와 "
                    "제품 설계의 기준이 되는 Reference Board를 구분합니다."
                )


                # -----------------------------------------
                # 비교
                # -----------------------------------------

                with st.container(
                    key="edu_section_target_compare"
                ):

                    render_surface_header(
                        "Target Board vs Reference Board",
                        (
                            "두 Board는 비슷해 보이지만 "
                            "개발 과정에서 사용하는 목적이 다릅니다."
                        ),
                        label="BOARD",
                    )

                    target_col, reference_col = st.columns(
                        2
                    )

                    with target_col:

                        with st.container(
                            key="edu_subsection_target_board"
                        ):

                            target_data = target_board[
                                "target_board"
                            ]

                            st.markdown(
                                "### 🎯 Target Board"
                            )

                            st.write(
                                target_data[
                                    "description"
                                ]
                            )


                    with reference_col:

                        with st.container(
                            key="edu_subsection_reference_board"
                        ):

                            reference_data = target_board[
                                "reference_board"
                            ]

                            st.markdown(
                                "### 📐 Reference Board"
                            )

                            st.write(
                                reference_data[
                                    "description"
                                ]
                            )


                # -----------------------------------------
                # 구성
                # -----------------------------------------

                with st.container(
                    key="edu_section_target_components"
                ):

                    render_surface_header(
                        "주요 구성 요소",
                        (
                            "Target Board를 구성하는 대표적인 "
                            "Hardware 요소입니다."
                        ),
                        label="COMPONENT",
                    )

                    render_pills(
                        target_board[
                            "components"
                        ]
                    )


                # -----------------------------------------
                # 선정 요소
                # -----------------------------------------

                with st.container(
                    key="edu_section_target_selection"
                ):

                    render_surface_header(
                        "Board 선정 시 확인할 사항",
                        (
                            "목표 시스템에 적합한 Board를 "
                            "선정하기 위한 주요 기준입니다."
                        ),
                        label="SELECTION",
                    )

                    render_pills(
                        target_board[
                            "selection_points"
                        ]
                    )


                render_exam_panel(
                    target_board[
                        "exam_points"
                    ]
                )


        # =================================================
        # ④ RISC · CISC
        # =================================================

        if processor_tab.open:

            with processor_tab:

                st.markdown(
                    "## Processor Architecture"
                )

                st.caption(
                    "RISC와 CISC의 명령어 구조와 특징을 비교합니다."
                )


                risc = processor_architecture[
                    "risc"
                ]

                cisc = processor_architecture[
                    "cisc"
                ]


                # -----------------------------------------
                # 두 Architecture 비교
                # -----------------------------------------

                with st.container(
                    key="edu_section_processor_compare"
                ):

                    render_surface_header(
                        "RISC vs CISC",
                        (
                            "Processor를 설계하는 대표적인 "
                            "두 Architecture를 비교합니다."
                        ),
                        label="PROCESSOR",
                    )

                    risc_col, cisc_col = st.columns(
                        2
                    )

                    with risc_col:

                        with st.container(
                            key="edu_subsection_risc"
                        ):

                            st.markdown(
                                "### RISC"
                            )

                            st.caption(
                                risc[
                                    "full_name"
                                ]
                            )

                            st.write(
                                risc[
                                    "description"
                                ]
                            )

                            for feature in risc[
                                "features"
                            ]:
                                st.markdown(
                                    f"- {feature}"
                                )

                            st.caption(
                                "대표 예: "
                                + ", ".join(
                                    risc["examples"]
                                )
                            )


                    with cisc_col:

                        with st.container(
                            key="edu_subsection_cisc"
                        ):

                            st.markdown(
                                "### CISC"
                            )

                            st.caption(
                                cisc[
                                    "full_name"
                                ]
                            )

                            st.write(
                                cisc[
                                    "description"
                                ]
                            )

                            for feature in cisc[
                                "features"
                            ]:
                                st.markdown(
                                    f"- {feature}"
                                )

                            st.caption(
                                "대표 예: "
                                + ", ".join(
                                    cisc["examples"]
                                )
                            )


                # -----------------------------------------
                # 항목별 비교
                # -----------------------------------------

                with st.container(
                    key="edu_section_processor_table"
                ):

                    render_surface_header(
                        "항목별 비교",
                        (
                            "명령어, 실행 방식, 구조와 대표 예를 "
                            "한눈에 비교합니다."
                        ),
                        label="COMPARISON",
                    )

                    for item in processor_architecture[
                        "comparison"
                    ]:

                        category_col, risc_col, cisc_col = (
                            st.columns(
                                [1.5, 3, 3]
                            )
                        )

                        with category_col:
                            st.markdown(
                                f"**{item['category']}**"
                            )

                        with risc_col:
                            st.write(
                                item[
                                    "risc"
                                ]
                            )

                        with cisc_col:
                            st.write(
                                item[
                                    "cisc"
                                ]
                            )


                render_exam_panel(
                    processor_architecture[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑤ Hardware Interface
        # =================================================

        if interface_tab.open:

            with interface_tab:

                st.markdown(
                    "## 주요 Hardware Interface"
                )

                st.caption(
                    "Processor와 Sensor, Module, 외부 장치가 "
                    "데이터를 주고받는 방법을 학습합니다."
                )


                with st.container(
                    key="edu_section_interfaces_intro"
                ):

                    render_surface_header(
                        "Hardware Interface",
                        hardware_interfaces[
                            "intro"
                        ],
                        label="INTERFACE",
                    )


                # -----------------------------------------
                # 각각의 Interface
                # -----------------------------------------

                for index, interface in enumerate(
                    hardware_interfaces[
                        "interfaces"
                    ]
                ):

                    with st.container(
                        key=(
                            "edu_section_interface_"
                            f"{index}"
                        )
                    ):

                        render_surface_header(
                            interface[
                                "name"
                            ],
                            interface[
                                "description"
                            ],
                            label=(
                                interface[
                                    "full_name"
                                ]
                            ),
                        )

                        render_pills(
                            interface[
                                "features"
                            ]
                        )

                        st.info(
                            "Arduino 연결: "
                            + interface[
                                "arduino_example"
                            ]
                        )


                # -----------------------------------------
                # 비교
                # -----------------------------------------

                with st.container(
                    key="edu_section_interface_compare"
                ):

                    render_surface_header(
                        "Interface 빠른 비교",
                        (
                            "주요 용도와 Arduino에서의 연결 방법을 "
                            "함께 확인합니다."
                        ),
                        label="QUICK VIEW",
                    )

                    for item in hardware_interfaces[
                        "comparison"
                    ]:

                        name_col, use_col, arduino_col = (
                            st.columns(
                                [1.5, 3, 3]
                            )
                        )

                        with name_col:
                            st.markdown(
                                f"**{item['interface']}**"
                            )

                        with use_col:
                            st.write(
                                item[
                                    "main_use"
                                ]
                            )

                        with arduino_col:
                            st.code(
                                item[
                                    "arduino"
                                ]
                            )


                render_exam_panel(
                    hardware_interfaces[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑥ Arduino 연결
        # =================================================

        if arduino_tab_2_1.open:

            with arduino_tab_2_1:

                st.markdown(
                    "## NCS 개념과 Arduino 연결"
                )

                st.caption(
                    "NCS의 Host · Target · Tool Chain 개념을 "
                    "Arduino 프로젝트와 연결하여 이해합니다."
                )


                with st.container(
                    key="edu_section_arduino_map_2_1"
                ):

                    render_surface_header(
                        arduino_mapping_2_1[
                            "title"
                        ],
                        arduino_mapping_2_1[
                            "note"
                        ],
                        label="ARDUINO CONNECTION",
                    )


                    mapping = arduino_mapping_2_1[
                        "mapping"
                    ]

                    for start in range(
                        0,
                        len(mapping),
                        2,
                    ):

                        current = mapping[
                            start:start + 2
                        ]

                        cols = st.columns(
                            len(current)
                        )

                        for index, (col, item) in enumerate(
                            zip(cols, current)
                        ):

                            with col:

                                with st.container(
                                    key=(
                                        "edu_subsection_map_2_1_"
                                        f"{start}_{index}"
                                    )
                                ):

                                    st.markdown(
                                        f"**{item['ncs']}**"
                                    )

                                    st.write(
                                        item[
                                            "arduino"
                                        ]
                                    )


                # -----------------------------------------
                # 프로젝트 예시
                # -----------------------------------------

                example = arduino_mapping_2_1[
                    "example"
                ]

                with st.container(
                    key="edu_section_arduino_example_2_1"
                ):

                    render_surface_header(
                        example[
                            "project"
                        ],
                        (
                            "교차 개발 환경을 실제 Arduino 프로젝트 "
                            "상황으로 연결한 예입니다."
                        ),
                        label="PROJECT EXAMPLE",
                    )

                    host_col, target_col = st.columns(
                        2
                    )

                    with host_col:
                        st.markdown(
                            "**Host**"
                        )
                        st.write(
                            example[
                                "host"
                            ]
                        )

                    with target_col:
                        st.markdown(
                            "**Target**"
                        )
                        st.write(
                            example[
                                "target"
                            ]
                        )

                    st.markdown(
                        "**사용 Interface**"
                    )

                    render_pills(
                        example[
                            "interfaces"
                        ]
                    )


        # =================================================
        # ⑦ 개념 체험
        # =================================================

        if practice_tab_2_1.open:

            with practice_tab_2_1:

                st.markdown(
                    "## 개발 도구 선정 개념 체험"
                )

                st.caption(
                    "Host / Target, Tool Chain, Interface를 "
                    "짧은 문제로 확인합니다."
                )


                # -----------------------------------------
                # Host / Target
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_2_1_host"
                ):

                    render_surface_header(
                        "Host와 Target 구분",
                        practice_2_1[
                            "activities"
                        ][0]["instruction"],
                        label="ACTIVITY 01",
                    )

                    host_target_question = st.radio(
                        (
                            "Cross Compile은 일반적으로 "
                            "어느 시스템에서 수행할까요?"
                        ),
                        [
                            "Host System",
                            "Target System",
                        ],
                        index=None,
                        key="2_1_host_target_question",
                    )

                    if host_target_question == "Host System":

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif host_target_question:

                        st.error(
                            "Cross Compile은 Host에서 수행합니다."
                        )


                # -----------------------------------------
                # Linker
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_2_1_linker"
                ):

                    render_surface_header(
                        "Tool Chain 연결하기",
                        practice_2_1[
                            "activities"
                        ][1]["instruction"],
                        label="ACTIVITY 02",
                    )

                    linker_question = st.radio(
                        (
                            "여러 Object File과 Library를 결합하여 "
                            "실행 파일을 만드는 도구는?"
                        ),
                        [
                            "Assembler",
                            "Debugger",
                            "Linker",
                            "Editor",
                        ],
                        index=None,
                        key="2_1_linker_question",
                    )

                    if linker_question == "Linker":

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif linker_question:

                        st.error(
                            "다시 확인해보세요."
                        )


                # -----------------------------------------
                # Interface
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_2_1_interface"
                ):

                    render_surface_header(
                        "Hardware Interface 선택",
                        practice_2_1[
                            "activities"
                        ][2]["instruction"],
                        label="ACTIVITY 03",
                    )

                    interface_case = st.selectbox(
                        "상황을 선택하세요.",
                        [
                            "선택하세요",
                            "LED를 ON/OFF 한다.",
                            "SDA와 SCL로 센서를 연결한다.",
                            "Serial Monitor와 데이터를 주고받는다.",
                            "SCK, MOSI, MISO, CS를 사용한다.",
                            "버튼 이벤트에 즉시 반응한다.",
                        ],
                        key="2_1_interface_case",
                    )

                    interface_answers = {
                        "LED를 ON/OFF 한다.": "GPIO",
                        "SDA와 SCL로 센서를 연결한다.": "I2C",
                        (
                            "Serial Monitor와 데이터를 주고받는다."
                        ): "UART",
                        (
                            "SCK, MOSI, MISO, CS를 사용한다."
                        ): "SPI",
                        (
                            "버튼 이벤트에 즉시 반응한다."
                        ): "Interrupt",
                    }

                    if interface_case != "선택하세요":

                        interface_answer = st.selectbox(
                            "적절한 Interface는?",
                            [
                                "선택하세요",
                                "GPIO",
                                "I2C",
                                "SPI",
                                "UART",
                                "Interrupt",
                            ],
                            key="2_1_interface_answer",
                        )

                        if interface_answer != "선택하세요":

                            if (
                                interface_answer
                                == interface_answers[
                                    interface_case
                                ]
                            ):
                                st.success(
                                    "정답입니다! ✅"
                                )

                            else:
                                st.error(
                                    "다시 확인해보세요."
                                )


        # =================================================
        # ⑧ 형성평가
        # =================================================

        if formative_tab_2_1.open:

            with formative_tab_2_1:

                render_quiz(
                    FORMATIVE_QUIZ_2_1,
                    title="✅ 2-1 형성평가",
                    description=(
                        "교차 개발 환경, Tool Chain, Target Board, "
                        "RISC/CISC와 Hardware Interface를 확인합니다."
                    ),
                )


        # =================================================
        # ⑨ 중간고사
        # =================================================

        if exam_tab_2_1.open:

            with exam_tab_2_1:

                render_exam_practice(
                    EXAM_PRACTICE_2_1
                )


        if is_section_completed("2-1"):

            st.success(
                "✅ 2-1 학습 완료"
            )


# =========================================================
# 2-2
# =========================================================

if lesson_tab_2.open:

    with lesson_tab_2:

        st.markdown(
            f"## {metadata_2_2['section']}. "
            f"{metadata_2_2['title']}"
        )

        st.caption(
            "Linux 기반 Host 환경을 구성하고 NFS와 "
            "ARM Cross Compiler를 이용하여 Target용 프로그램을 "
            "생성하고 실행하는 과정을 학습합니다."
        )


        # -------------------------------------------------
        # 학습 목표
        # -------------------------------------------------

        with st.container(
            key="edu_section_2_2_objectives"
        ):

            render_surface_header(
                "학습 목표",
                (
                    "Host와 Target 개발 환경을 실제로 구성하는 "
                    "절차와 명령을 이해합니다."
                ),
                label="LEARNING GOALS",
            )

            for objective in LESSON_2_2["objectives"]:
                st.markdown(
                    f"- {objective}"
                )


        # -------------------------------------------------
        # 내부 탭
        # -------------------------------------------------

        (
            environment_tab,
            vm_tab,
            nfs_tab,
            linux_tab,
            compiler_tab,
            target_execution_tab,
            arduino_tab_2_2,
            practice_tab_2_2,
            formative_tab_2_2,
            exam_tab_2_2,
        ) = st.tabs(
            [
                "① 개발 환경",
                "② 가상 머신",
                "③ NFS",
                "④ Linux 명령어",
                "⑤ Cross Compiler",
                "⑥ Target 실행",
                "⑦ Arduino 연결",
                "⑧ 개념 체험",
                "⑨ 형성평가",
                "⑩ 중간고사 대비",
            ],
            key="lesson_2_2_inner_tabs",
            on_change="rerun",
        )


        # =================================================
        # ① 개발 환경
        # =================================================

        if environment_tab.open:

            with environment_tab:

                st.markdown(
                    "## 애플리케이션 개발 환경"
                )

                st.caption(
                    "NCS 학습모듈에서 제시하는 Host와 Target의 "
                    "개발 환경 구성을 확인합니다."
                )


                # -----------------------------------------
                # 핵심 구조
                # -----------------------------------------

                with st.container(
                    key="edu_section_environment_overview"
                ):

                    render_surface_header(
                        environment_overview[
                            "title"
                        ],
                        environment_overview[
                            "definition"
                        ],
                        label="ENVIRONMENT",
                    )

                    host_col, arrow_col, target_col = st.columns(
                        [5, 1, 5]
                    )

                    with host_col:

                        with st.container(
                            key="edu_subsection_environment_host"
                        ):

                            st.markdown(
                                "### 💻 Host"
                            )

                            st.write(
                                environment_overview[
                                    "host_description"
                                ]
                            )

                            render_pills(
                                environment_overview[
                                    "host"
                                ]
                            )


                    with arrow_col:

                        st.markdown("")
                        st.markdown("")
                        st.markdown(
                            "## →"
                        )


                    with target_col:

                        with st.container(
                            key="edu_subsection_environment_target"
                        ):

                            st.markdown(
                                "### 🎯 Target"
                            )

                            st.write(
                                environment_overview[
                                    "target_description"
                                ]
                            )

                            render_pills(
                                environment_overview[
                                    "target"
                                ]
                            )


                # -----------------------------------------
                # 네트워크
                # -----------------------------------------

                with st.container(
                    key="edu_section_environment_network"
                ):

                    render_surface_header(
                        "Host ↔ Target Network",
                        (
                            "Host와 Target 사이에서 사용하는 "
                            "대표적인 연결과 공유 방식입니다."
                        ),
                        label="NETWORK",
                    )

                    for item in environment_overview[
                        "network"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                # -----------------------------------------
                # 개발 흐름
                # -----------------------------------------

                with st.container(
                    key="edu_section_environment_flow"
                ):

                    render_surface_header(
                        "전체 개발 흐름",
                        (
                            "환경 구성부터 Target 실행까지의 "
                            "전체 과정을 확인합니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        environment_overview[
                            "development_flow"
                        ]
                    )


                st.warning(
                    environment_overview[
                        "important_note"
                    ]
                )

                render_exam_panel(
                    environment_overview[
                        "exam_points"
                    ]
                )


        # =================================================
        # ② 가상 머신
        # =================================================

        if vm_tab.open:

            with vm_tab:

                st.markdown(
                    "## 가상 머신을 이용한 개발 환경 구성"
                )


                with st.container(
                    key="edu_section_virtual_machine"
                ):

                    render_surface_header(
                        virtual_machine[
                            "title"
                        ],
                        virtual_machine[
                            "definition"
                        ],
                        label="VIRTUAL MACHINE",
                    )

                    render_concept(
                        "왜 가상 머신을 사용하는가?",
                        virtual_machine[
                            "description"
                        ],
                    )


                # -----------------------------------------
                # 장점
                # -----------------------------------------

                with st.container(
                    key="edu_section_vm_advantages"
                ):

                    render_surface_header(
                        "가상 머신의 장점",
                        (
                            "개발 환경을 독립적으로 구성할 때 얻을 수 "
                            "있는 장점입니다."
                        ),
                        label="ADVANTAGE",
                    )

                    render_pills(
                        virtual_machine[
                            "advantages"
                        ]
                    )


                # -----------------------------------------
                # 설치 과정
                # -----------------------------------------

                with st.container(
                    key="edu_section_vm_steps"
                ):

                    render_surface_header(
                        "구축 과정",
                        (
                            "VirtualBox와 Ubuntu 기반 환경을 "
                            "구성하는 기본 순서입니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        [
                            item["title"]
                            for item in virtual_machine[
                                "steps"
                            ]
                        ]
                    )

                    with st.expander(
                        "단계별 설명 보기"
                    ):

                        for item in virtual_machine[
                            "steps"
                        ]:

                            st.markdown(
                                f"**{item['step']}. "
                                f"{item['title']}**"
                            )

                            st.write(
                                item[
                                    "description"
                                ]
                            )


                render_exam_panel(
                    virtual_machine[
                        "exam_points"
                    ]
                )


        # =================================================
        # ③ NFS
        # =================================================

        if nfs_tab.open:

            with nfs_tab:

                st.markdown(
                    "## NFS를 이용한 파일 공유"
                )


                # -----------------------------------------
                # 정의
                # -----------------------------------------

                with st.container(
                    key="edu_section_nfs_core"
                ):

                    render_surface_header(
                        nfs[
                            "title"
                        ],
                        nfs[
                            "definition"
                        ],
                        label="NETWORK FILE SYSTEM",
                    )

                    render_concept(
                        "NFS를 사용하는 목적",
                        nfs[
                            "purpose"
                        ],
                    )


                # -----------------------------------------
                # exports
                # -----------------------------------------

                with st.container(
                    key="edu_section_nfs_exports"
                ):

                    render_surface_header(
                        "/etc/exports",
                        nfs[
                            "exports_description"
                        ],
                        label="CONFIGURATION",
                    )

                    render_command(
                        nfs[
                            "exports_example"
                        ],
                        "공유 설정 예시",
                    )

                    render_command(
                        nfs[
                            "restart_command"
                        ],
                        "NFS Server 재시작",
                    )


                # -----------------------------------------
                # 절차
                # -----------------------------------------

                with st.container(
                    key="edu_section_nfs_process"
                ):

                    render_surface_header(
                        "NFS 설정 절차",
                        (
                            "Host 공유 Directory를 Target에서 "
                            "사용하기까지의 과정입니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        [
                            item["title"]
                            for item in nfs[
                                "procedure"
                            ]
                        ]
                    )

                    with st.expander(
                        "NFS 설정 단계 자세히 보기"
                    ):

                        for item in nfs[
                            "procedure"
                        ]:

                            st.markdown(
                                f"**{item['step']}. "
                                f"{item['title']}**"
                            )

                            st.write(
                                item[
                                    "description"
                                ]
                            )

                            if item.get(
                                "command"
                            ):
                                st.code(
                                    item[
                                        "command"
                                    ],
                                    language="bash",
                                )


                render_exam_panel(
                    nfs[
                        "exam_points"
                    ]
                )


        # =================================================
        # ④ Linux 명령어
        # =================================================

        if linux_tab.open:

            with linux_tab:

                st.markdown(
                    "## Linux 파일 관리와 환경 설정"
                )

                st.caption(
                    "개발 환경 구축에 필요한 핵심 Linux 명령어를 "
                    "실제 사용 예와 함께 확인합니다."
                )


                with st.container(
                    key="edu_section_linux_commands"
                ):

                    render_surface_header(
                        linux_file_management[
                            "title"
                        ],
                        linux_file_management[
                            "intro"
                        ],
                        label="LINUX COMMAND",
                    )


                    commands = linux_file_management[
                        "commands"
                    ]

                    for start in range(
                        0,
                        len(commands),
                        2,
                    ):

                        current = commands[
                            start:start + 2
                        ]

                        cols = st.columns(
                            len(current)
                        )

                        for index, (col, item) in enumerate(
                            zip(cols, current)
                        ):

                            with col:

                                with st.container(
                                    key=(
                                        "edu_subsection_linux_"
                                        f"{start}_{index}"
                                    )
                                ):

                                    st.markdown(
                                        f"### `{item['command']}`"
                                    )

                                    st.write(
                                        item[
                                            "description"
                                        ]
                                    )

                                    st.code(
                                        item[
                                            "example"
                                        ],
                                        language="bash",
                                    )


                render_exam_panel(
                    linux_file_management[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑤ Cross Compiler
        # =================================================

        if compiler_tab.open:

            with compiler_tab:

                st.markdown(
                    "## ARM Cross Compiler"
                )

                st.caption(
                    "Cross Compiler 설치부터 Target용 실행 파일 "
                    "생성 및 Architecture 확인까지 학습합니다."
                )


                # -----------------------------------------
                # 설치
                # -----------------------------------------

                with st.container(
                    key="edu_section_cross_compiler_install"
                ):

                    render_surface_header(
                        cross_compiler_installation[
                            "title"
                        ],
                        cross_compiler_installation[
                            "definition"
                        ],
                        label="INSTALLATION",
                    )

                    st.markdown(
                        "**설치 Directory**"
                    )

                    st.code(
                        cross_compiler_installation[
                            "install_directory"
                        ]
                    )

                    render_process(
                        [
                            item[
                                "title"
                            ]
                            for item in cross_compiler_installation[
                                "procedure"
                            ]
                        ]
                    )

                    with st.expander(
                        "설치 명령어 자세히 보기"
                    ):

                        for item in cross_compiler_installation[
                            "procedure"
                        ]:

                            st.markdown(
                                f"**{item['step']}. "
                                f"{item['title']}**"
                            )

                            st.write(
                                item[
                                    "description"
                                ]
                            )

                            st.code(
                                item[
                                    "command"
                                ],
                                language="bash",
                            )


                # -----------------------------------------
                # Cross Compilation
                # -----------------------------------------

                with st.container(
                    key="edu_section_cross_compilation"
                ):

                    render_surface_header(
                        cross_compilation[
                            "title"
                        ],
                        cross_compilation[
                            "definition"
                        ],
                        label="COMPILATION",
                    )

                    st.markdown(
                        "**Source File**"
                    )

                    st.code(
                        cross_compilation[
                            "source_file"
                        ]
                    )

                    st.markdown(
                        "**Cross Compile Command**"
                    )

                    render_command(
                        cross_compilation[
                            "command"
                        ]
                    )

                    st.write(
                        cross_compilation[
                            "description"
                        ]
                    )


                    st.markdown(
                        "**Architecture 확인**"
                    )

                    render_command(
                        cross_compilation[
                            "file_command"
                        ]
                    )

                    st.code(
                        cross_compilation[
                            "file_result"
                        ]
                    )

                    st.info(
                        cross_compilation[
                            "architecture_note"
                        ]
                    )


                render_exam_panel(
                    [
                        *cross_compiler_installation[
                            "exam_points"
                        ],
                        *cross_compilation[
                            "exam_points"
                        ],
                    ]
                )


        # =================================================
        # ⑥ Target 실행
        # =================================================

        if target_execution_tab.open:

            with target_execution_tab:

                st.markdown(
                    "## Target System에서 실행"
                )

                st.caption(
                    "Host에서 생성한 ARM용 실행 파일을 Target에서 "
                    "실행하고 문제가 발생했을 때 해결 방법을 확인합니다."
                )


                # -----------------------------------------
                # 실행
                # -----------------------------------------

                with st.container(
                    key="edu_section_target_execution"
                ):

                    render_surface_header(
                        target_execution[
                            "title"
                        ],
                        target_execution[
                            "intro"
                        ],
                        label="TARGET EXECUTION",
                    )

                    render_process(
                        [
                            item[
                                "title"
                            ]
                            for item in target_execution[
                                "procedure"
                            ]
                        ]
                    )

                    with st.expander(
                        "실행 과정 자세히 보기"
                    ):

                        for item in target_execution[
                            "procedure"
                        ]:

                            st.markdown(
                                f"**{item['step']}. "
                                f"{item['title']}**"
                            )

                            st.write(
                                item[
                                    "description"
                                ]
                            )

                            if item.get(
                                "command"
                            ):

                                st.code(
                                    item[
                                        "command"
                                    ],
                                    language="bash",
                                )


                # -----------------------------------------
                # Troubleshooting
                # -----------------------------------------

                with st.container(
                    key="edu_section_troubleshooting"
                ):

                    render_surface_header(
                        troubleshooting[
                            "title"
                        ],
                        (
                            "개발 환경에서 자주 발생할 수 있는 "
                            "문제와 원인, 해결 방법입니다."
                        ),
                        label="TROUBLESHOOTING",
                    )

                    for index, item in enumerate(
                        troubleshooting[
                            "items"
                        ]
                    ):

                        with st.expander(
                            f"⚠️ {item['problem']}"
                        ):

                            st.markdown(
                                "**원인**"
                            )

                            st.write(
                                item[
                                    "cause"
                                ]
                            )

                            st.markdown(
                                "**해결 방법**"
                            )

                            st.write(
                                item[
                                    "solution"
                                ]
                            )


                render_exam_panel(
                    [
                        *target_execution[
                            "exam_points"
                        ],
                        *troubleshooting[
                            "exam_points"
                        ],
                    ]
                )


        # =================================================
        # ⑦ Arduino 연결
        # =================================================

        if arduino_tab_2_2.open:

            with arduino_tab_2_2:

                st.markdown(
                    "## NCS 개발 환경과 Arduino 연결"
                )


                with st.container(
                    key="edu_section_arduino_2_2"
                ):

                    render_surface_header(
                        arduino_mapping_2_2[
                            "title"
                        ],
                        arduino_mapping_2_2[
                            "note"
                        ],
                        label="ARDUINO CONNECTION",
                    )


                    mapping = arduino_mapping_2_2[
                        "mapping"
                    ]

                    for start in range(
                        0,
                        len(mapping),
                        2,
                    ):

                        current = mapping[
                            start:start + 2
                        ]

                        cols = st.columns(
                            len(current)
                        )

                        for index, (col, item) in enumerate(
                            zip(cols, current)
                        ):

                            with col:

                                with st.container(
                                    key=(
                                        "edu_subsection_arduino_2_2_"
                                        f"{start}_{index}"
                                    )
                                ):

                                    st.markdown(
                                        f"**{item['ncs']}**"
                                    )

                                    st.write(
                                        item[
                                            "arduino"
                                        ]
                                    )


                # -----------------------------------------
                # Arduino Flow
                # -----------------------------------------

                with st.container(
                    key="edu_section_arduino_flow_2_2"
                ):

                    render_surface_header(
                        "Arduino 개발 흐름",
                        (
                            "Host → Compile → Program Transfer → "
                            "Target 실행의 구조를 Arduino에 연결합니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        arduino_mapping_2_2[
                            "development_flow"
                        ]
                    )


                st.warning(
                    arduino_mapping_2_2[
                        "important_distinction"
                    ]
                )


        # =================================================
        # ⑧ 개념 체험
        # =================================================

        if practice_tab_2_2.open:

            with practice_tab_2_2:

                st.markdown(
                    "## 개발 환경 구축 개념 체험"
                )


                # -----------------------------------------
                # Linux command
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_linux"
                ):

                    render_surface_header(
                        "Linux 명령어 맞추기",
                        practice_2_2[
                            "activities"
                        ][0]["instruction"],
                        label="ACTIVITY 01",
                    )

                    linux_case = st.selectbox(
                        "작업을 선택하세요.",
                        [
                            "선택하세요",
                            "새 Directory 생성",
                            "File 복사",
                            "환경변수 확인",
                            "실행 파일 Architecture 확인",
                        ],
                        key="2_2_linux_case",
                    )

                    linux_answers = {
                        "새 Directory 생성": "mkdir",
                        "File 복사": "cp",
                        "환경변수 확인": "env",
                        (
                            "실행 파일 Architecture 확인"
                        ): "file",
                    }

                    if linux_case != "선택하세요":

                        linux_answer = st.selectbox(
                            "적절한 명령어는?",
                            [
                                "선택하세요",
                                "mkdir",
                                "cp",
                                "env",
                                "file",
                                "tar",
                            ],
                            key="2_2_linux_answer",
                        )

                        if linux_answer != "선택하세요":

                            if (
                                linux_answer
                                == linux_answers[
                                    linux_case
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
                # Architecture
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_architecture"
                ):

                    render_surface_header(
                        "Architecture 확인",
                        practice_2_2[
                            "activities"
                        ][2]["instruction"],
                        label="ACTIVITY 02",
                    )

                    st.code(
                        "ELF 32-bit LSB executable, ARM"
                    )

                    architecture_answer = st.radio(
                        "위 실행 파일은 어떤 Architecture용일까요?",
                        [
                            "ARM",
                            "x86",
                            "JVM",
                        ],
                        index=None,
                        key="2_2_architecture_answer",
                    )

                    if architecture_answer == "ARM":

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif architecture_answer:

                        st.error(
                            "`ARM`이라는 표시를 확인해보세요."
                        )


                # -----------------------------------------
                # NFS
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_nfs"
                ):

                    render_surface_header(
                        "NFS 문제 해결",
                        practice_2_2[
                            "activities"
                        ][3]["instruction"],
                        label="ACTIVITY 03",
                    )

                    nfs_question = st.radio(
                        (
                            "NFS 공유 Directory를 설정하는 "
                            "대표 파일은?"
                        ),
                        [
                            "/etc/exports",
                            "/etc/passwd",
                            "/etc/hosts",
                            "/etc/profile",
                        ],
                        index=None,
                        key="2_2_nfs_question",
                    )

                    if nfs_question == "/etc/exports":

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif nfs_question:

                        st.error(
                            "NFS 공유 설정 파일을 다시 확인해보세요."
                        )


        # =================================================
        # ⑨ 형성평가
        # =================================================

        if formative_tab_2_2.open:

            with formative_tab_2_2:

                render_quiz(
                    FORMATIVE_QUIZ_2_2,
                    title="✅ 2-2 형성평가",
                    description=(
                        "가상 머신, NFS, Linux 명령어, "
                        "Cross Compiler와 Target 실행을 확인합니다."
                    ),
                )


        # =================================================
        # ⑩ 중간고사
        # =================================================

        if exam_tab_2_2.open:

            with exam_tab_2_2:

                render_exam_practice(
                    EXAM_PRACTICE_2_2
                )


        if is_section_completed("2-2"):

            st.success(
                "✅ 2-2 학습 완료"
            )


# =========================================================
# 학습 2 전체 완료
# =========================================================

if is_lesson_completed("2"):

    st.divider()

    st.success(
        "🎉 학습 2 · 애플리케이션 개발 환경 구축하기를 "
        "모두 완료했습니다!"
    )

    with st.expander(
        "📚 학습 2 핵심 내용 다시 보기"
    ):

        st.markdown(
            "### 2-1 핵심 정리"
        )

        render_summary(
            LESSON_2_1[
                "summary"
            ]
        )

        st.divider()

        st.markdown(
            "### 2-2 핵심 정리"
        )

        render_summary(
            LESSON_2_2[
                "summary"
            ]
        )