from __future__ import annotations

from html import escape
from textwrap import dedent

import streamlit as st

from data.lessons.lesson_3_1 import LESSON_3_1
from data.lessons.lesson_3_2 import LESSON_3_2

from data.quizzes.quiz_3_1 import (
    EXAM_PRACTICE_3_1,
    FORMATIVE_QUIZ_3_1,
)

from data.quizzes.quiz_3_2 import (
    EXAM_PRACTICE_3_2,
    FORMATIVE_QUIZ_3_2,
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
from utils.navigation import render_app_sidebar

from utils.ui import (
    render_breadcrumb,
    render_progress_bar,
    render_summary,
)


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="학습 3 | 모듈 구현",
    page_icon="💻",
    layout="wide",
)

load_global_css()


# =========================================================
# HTML Helper
# =========================================================

def render_html(html: str) -> None:
    """
    Custom HTML을 Markdown parser 없이 직접 렌더링한다.
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

    html = "".join(
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
            {html}
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
    language: str = "bash",
) -> None:

    if caption:
        st.caption(caption)

    st.code(
        command,
        language=language,
    )


# =========================================================
# 데이터 - 3-1
# =========================================================

metadata_3_1 = LESSON_3_1["metadata"]

gcc_overview = LESSON_3_1["gcc_overview"]
gcc_process = LESSON_3_1["gcc_process"]
gcc_usage = LESSON_3_1["gcc_usage"]
make = LESSON_3_1["make"]
module_implementation = LESSON_3_1["module_implementation"]
compile_error = LESSON_3_1["compile_error"]
echo_server = LESSON_3_1["echo_server"]
arduino_mapping_3_1 = LESSON_3_1["arduino_mapping"]
practice_3_1 = LESSON_3_1["practice"]


# =========================================================
# 데이터 - 3-2
# =========================================================

metadata_3_2 = LESSON_3_2["metadata"]

debugging_overview = LESSON_3_2["debugging_overview"]
gdb_overview = LESSON_3_2["gdb_overview"]
gdb_modes = LESSON_3_2["gdb_modes"]
gdb_commands = LESSON_3_2["gdb_commands"]
breakpoint = LESSON_3_2["breakpoint"]
step_execution = LESSON_3_2["step_execution"]
variable_memory = LESSON_3_2["variable_memory"]
remote_debugging = LESSON_3_2["remote_debugging"]
program_integration = LESSON_3_2["program_integration"]
arduino_mapping_3_2 = LESSON_3_2["arduino_mapping"]
practice_3_2 = LESSON_3_2["practice"]


# =========================================================
# 진도
# =========================================================

lesson_3_progress = get_lesson_progress(
    "3"
)


# =========================================================
# 공통 사이드바
# =========================================================

render_app_sidebar(
    current_page="lesson_3"
)


# =========================================================
# Breadcrumb
# =========================================================

render_breadcrumb(
    "홈",
    "학습 3",
    "모듈 구현하기",
)


# =========================================================
# HERO
# =========================================================

render_html(
    """
    <div class="edu-hero">

        <div class="edu-hero-eyebrow">
            APPLICATION IMPLEMENTATION
        </div>

        <div class="edu-hero-title">
            학습 3. 애플리케이션 모듈 구현하기
        </div>

        <div class="edu-hero-desc">
            GCC와 Make를 이용해 Module을 구현하고 Error와 Warning을
            제거한 뒤 GDB를 이용한 Debugging과 Program Integration을
            학습합니다.
        </div>

    </div>
    """
)


# =========================================================
# 진도
# =========================================================

render_progress_bar(
    lesson_3_progress,
    label="학습 3 전체 진도",
)

if is_lesson_completed("3"):

    st.success(
        "🎉 학습 3의 모든 소단원을 완료했습니다!"
    )


# =========================================================
# 학습 내용 선택
# =========================================================

st.markdown(
    "## 학습 내용 선택"
)

lesson_tab_1, lesson_tab_2 = st.tabs(
    [
        "3-1. 애플리케이션 구현 및 오류 제거",
        "3-2. 디버깅 및 프로그램 통합",
    ],
    key="lesson_3_main_tabs",
    on_change="rerun",
)


# =========================================================
# 3-1
# =========================================================

if lesson_tab_1.open:

    with lesson_tab_1:

        st.markdown(
            f"## {metadata_3_1['section']}. "
            f"{metadata_3_1['title']}"
        )

        st.caption(
            "GCC와 Make를 이용하여 Module을 구현하고 "
            "Compile Error와 Warning을 제거하는 과정을 학습합니다."
        )


        # -------------------------------------------------
        # 학습 목표
        # -------------------------------------------------

        with st.container(
            key="edu_section_3_1_objectives"
        ):

            render_surface_header(
                "학습 목표",
                (
                    "GCC, Make, Module 구현과 Compile 오류 제거의 "
                    "핵심 원리를 이해합니다."
                ),
                label="LEARNING GOALS",
            )

            for objective in LESSON_3_1["objectives"]:
                st.markdown(
                    f"- {objective}"
                )


        # -------------------------------------------------
        # 내부 탭
        # -------------------------------------------------

        (
            gcc_tab,
            gcc_process_tab,
            option_tab,
            make_tab,
            module_tab,
            error_tab,
            echo_tab,
            arduino_tab_3_1,
            practice_tab_3_1,
            formative_tab_3_1,
            exam_tab_3_1,
        ) = st.tabs(
            [
                "① GCC",
                "② GCC 동작 과정",
                "③ GCC Option",
                "④ Make · Makefile",
                "⑤ Module 구현",
                "⑥ Error · Warning",
                "⑦ ECHO Server",
                "⑧ Arduino 연결",
                "⑨ 개념 체험",
                "⑩ 형성평가",
                "⑪ 중간고사 대비",
            ],
            key="lesson_3_1_inner_tabs",
            on_change="rerun",
        )


        # =================================================
        # ① GCC
        # =================================================

        if gcc_tab.open:

            with gcc_tab:

                st.markdown(
                    "## GCC"
                )

                st.caption(
                    "GNU Compiler Collection의 특징과 역할을 학습합니다."
                )


                with st.container(
                    key="edu_section_gcc_overview"
                ):

                    render_surface_header(
                        gcc_overview["title"],
                        gcc_overview["definition"],
                        label="GNU COMPILER COLLECTION",
                    )

                    render_concept(
                        "GCC의 역할",
                        gcc_overview["role"],
                    )


                with st.container(
                    key="edu_section_gcc_features"
                ):

                    render_surface_header(
                        "GCC 주요 특징",
                        (
                            "GCC가 임베디드 개발 환경에서 "
                            "활용되는 이유를 정리합니다."
                        ),
                        label="FEATURES",
                    )

                    for start in range(
                        0,
                        len(gcc_overview["features"]),
                        2,
                    ):

                        current = gcc_overview[
                            "features"
                        ][
                            start:start + 2
                        ]

                        cols = st.columns(
                            len(current)
                        )

                        for col, item in zip(
                            cols,
                            current,
                        ):

                            with col:
                                st.markdown(
                                    f"- {item}"
                                )


                with st.container(
                    key="edu_section_gcc_languages"
                ):

                    render_surface_header(
                        "지원 언어",
                        (
                            "GCC는 하나의 C Compiler가 아니라 "
                            "여러 언어를 지원하는 Compiler Collection입니다."
                        ),
                        label="LANGUAGE",
                    )

                    render_pills(
                        gcc_overview[
                            "languages"
                        ]
                    )


                render_exam_panel(
                    gcc_overview[
                        "exam_points"
                    ]
                )


        # =================================================
        # ② GCC 동작 과정
        # =================================================

        if gcc_process_tab.open:

            with gcc_process_tab:

                st.markdown(
                    "## GCC 동작 과정"
                )

                st.caption(
                    "Source Code가 Executable File이 되기까지 "
                    "GCC 내부 처리 과정을 학습합니다."
                )


                with st.container(
                    key="edu_section_gcc_process"
                ):

                    render_surface_header(
                        gcc_process["title"],
                        gcc_process["intro"],
                        label="BUILD PROCESS",
                    )

                    render_process(
                        gcc_process["flow"]
                    )

                    st.caption(
                        gcc_process[
                            "simple_flow"
                        ]
                    )


                with st.container(
                    key="edu_section_gcc_stages"
                ):

                    render_surface_header(
                        "처리 단계별 역할",
                        (
                            "Source Code가 실행 파일이 되기까지 "
                            "cpp → cc1 → as → ld가 순차적으로 처리합니다."
                        ),
                        label="PIPELINE",
                    )

                    stages = gcc_process["stages"]

                    for index, stage in enumerate(stages, start=1):

                        render_html(
                            f"""
                            <div style="
                                display: grid;
                                grid-template-columns: 76px 150px 1fr 190px;
                                gap: 1rem;
                                align-items: center;

                                margin-bottom: 0.8rem;
                                padding: 1rem 1.1rem;

                                background: #f8f9fc;
                                border: 1px solid #e7eaf1;
                                border-radius: 14px;
                            ">

                                <div style="
                                    display: flex;
                                    align-items: center;
                                    justify-content: center;

                                    width: 42px;
                                    height: 42px;

                                    color: #ffffff;
                                    background: #5b5cf0;

                                    border-radius: 12px;

                                    font-size: 0.92rem;
                                    font-weight: 800;
                                ">
                                    {index}
                                </div>

                                <div>
                                    <div style="
                                        color: #5b5cf0;
                                        font-size: 1.05rem;
                                        font-weight: 800;
                                        margin-bottom: 0.15rem;
                                    ">
                                        {escape(stage["name"])}
                                    </div>

                                    <div style="
                                        color: #98a2b3;
                                        font-size: 0.76rem;
                                        margin-bottom: 0.2rem;
                                    ">
                                        {escape(stage["english"])}
                                    </div>

                                    <div style="
                                        color: #172033;
                                        font-size: 0.9rem;
                                        font-weight: 750;
                                    ">
                                        {escape(stage["stage"])}
                                    </div>
                                </div>

                                <div style="
                                    color: #4c5a6d;
                                    font-size: 0.88rem;
                                    line-height: 1.55;
                                ">
                                    {escape(stage["description"])}
                                </div>

                                <div style="
                                    padding: 0.65rem 0.8rem;

                                    background: #ffffff;
                                    border: 1px solid #e2e7ef;
                                    border-radius: 10px;

                                    color: #4c5a6d;
                                    font-size: 0.8rem;
                                ">
                                    <div style="
                                        color: #98a2b3;
                                        font-size: 0.7rem;
                                        font-weight: 700;
                                        margin-bottom: 0.2rem;
                                    ">
                                        OUTPUT
                                    </div>

                                    {escape(stage["output"])}
                                </div>

                            </div>
                            """
                        )

                        if index < len(stages):

                            render_html(
                                """
                                <div style="
                                    text-align: center;
                                    color: #5b5cf0;
                                    font-size: 1.2rem;
                                    font-weight: 800;
                                    margin: -0.35rem 0 0.25rem;
                                ">
                                    ↓
                                </div>
                                """
                            )

                    render_surface_header(
                        "처리 단계별 역할",
                        (
                            "cpp, cc1, as, ld가 각각 어떤 역할을 "
                            "수행하는지 확인합니다."
                        ),
                        label="PIPELINE",
                    )

                    for stage in gcc_process[
                        "stages"
                    ]:

                        with st.container(
                            key=(
                                "edu_subsection_gcc_"
                                f"{stage['name']}"
                            )
                        ):

                            col1, col2 = st.columns(
                                [2, 5]
                            )

                            with col1:

                                st.markdown(
                                    f"### `{stage['name']}`"
                                )

                                st.caption(
                                    stage["english"]
                                )

                                st.markdown(
                                    f"**{stage['stage']}**"
                                )

                            with col2:

                                st.write(
                                    stage[
                                        "description"
                                    ]
                                )

                                st.caption(
                                    "출력 → "
                                    + stage[
                                        "output"
                                    ]
                                )


                with st.container(
                    key="edu_section_gcc_target_transfer"
                ):

                    render_surface_header(
                        "Target으로 실행 파일 전달",
                        gcc_process[
                            "target_transfer"
                        ],
                        label="HOST → TARGET",
                    )


                render_exam_panel(
                    gcc_process[
                        "exam_points"
                    ]
                )


        # =================================================
        # ③ GCC Option
        # =================================================

        if option_tab.open:

            with option_tab:

                st.markdown(
                    "## GCC 사용법과 주요 Option"
                )


                with st.container(
                    key="edu_section_gcc_usage"
                ):

                    render_surface_header(
                        gcc_usage["title"],
                        gcc_usage["description"],
                        label="COMMAND",
                    )

                    render_command(
                        gcc_usage[
                            "basic_syntax"
                        ],
                        "기본 문법",
                    )


                with st.container(
                    key="edu_section_gcc_options"
                ):

                    render_surface_header(
                        "GCC 주요 Option",
                        (
                            "Compile 과정과 출력 파일, 검색 경로, "
                            "Debugging 정보를 제어하는 주요 Option입니다."
                        ),
                        label="OPTION",
                    )

                    for start in range(
                        0,
                        len(gcc_usage["options"]),
                        2,
                    ):

                        current = gcc_usage[
                            "options"
                        ][
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
                                        "edu_subsection_gcc_option_"
                                        f"{start}_{index}"
                                    )
                                ):

                                    st.markdown(
                                        f"### `{item['option']}`"
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


                with st.container(
                    key="edu_section_gcc_examples"
                ):

                    render_surface_header(
                        "Compile 예제",
                        (
                            "대표적인 GCC 명령을 "
                            "빠르게 확인합니다."
                        ),
                        label="EXAMPLE",
                    )

                    for example in gcc_usage[
                        "examples"
                    ]:
                        st.code(
                            example,
                            language="bash",
                        )


                render_exam_panel(
                    gcc_usage[
                        "exam_points"
                    ]
                )


        # =================================================
        # ④ Make / Makefile
        # =================================================

        if make_tab.open:

            with make_tab:

                st.markdown(
                    "## Make와 Makefile"
                )


                with st.container(
                    key="edu_section_make_core"
                ):

                    render_surface_header(
                        make["title"],
                        make["definition"],
                        label="BUILD AUTOMATION",
                    )

                    render_concept(
                        "왜 Make를 사용하는가?",
                        make["purpose"],
                    )


                with st.container(
                    key="edu_section_make_concepts"
                ):

                    render_surface_header(
                        "Makefile 기본 구성",
                        (
                            "Target, Dependency, Command의 "
                            "관계를 이해합니다."
                        ),
                        label="STRUCTURE",
                    )

                    cols = st.columns(
                        3
                    )

                    for col, item in zip(
                        cols,
                        make["basic_concepts"],
                    ):

                        with col:

                            with st.container(
                                key=(
                                    "edu_subsection_make_"
                                    f"{item['name']}"
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


                    st.markdown(
                        "**기본 구조**"
                    )

                    st.code(
                        make["structure"],
                        language="makefile",
                    )


                with st.container(
                    key="edu_section_make_example"
                ):

                    render_surface_header(
                        "Makefile 예제",
                        (
                            "main.c와 module.c를 Build하는 "
                            "간단한 Makefile입니다."
                        ),
                        label="MAKEFILE",
                    )

                    st.code(
                        make[
                            "example_makefile"
                        ],
                        language="makefile",
                    )


                with st.container(
                    key="edu_section_make_process"
                ):

                    render_surface_header(
                        "Make 동작 과정",
                        (
                            "Makefile을 읽고 Dependency와 "
                            "수정 시간을 확인하여 Build합니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        make["process"]
                    )


                with st.container(
                    key="edu_section_make_advantages"
                ):

                    render_surface_header(
                        "Make의 장점",
                        (
                            "프로젝트가 커질수록 Build 자동화의 "
                            "효과가 커집니다."
                        ),
                        label="ADVANTAGE",
                    )

                    for item in make[
                        "advantages"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                render_exam_panel(
                    make[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑤ Module 구현
        # =================================================

        if module_tab.open:

            with module_tab:

                st.markdown(
                    "## 단위 Module과 공통 Module 구현"
                )


                with st.container(
                    key="edu_section_module_core"
                ):

                    render_surface_header(
                        module_implementation[
                            "title"
                        ],
                        module_implementation[
                            "definition"
                        ],
                        label="MODULE",
                    )


                    unit_col, common_col = st.columns(
                        2
                    )

                    unit_module = module_implementation[
                        "unit_module"
                    ]

                    common_module = module_implementation[
                        "common_module"
                    ]


                    with unit_col:

                        with st.container(
                            key="edu_subsection_unit_module"
                        ):

                            st.markdown(
                                "### 단위 Module"
                            )

                            st.write(
                                unit_module[
                                    "description"
                                ]
                            )

                            render_pills(
                                unit_module[
                                    "examples"
                                ]
                            )


                    with common_col:

                        with st.container(
                            key="edu_subsection_common_module"
                        ):

                            st.markdown(
                                "### 공통 Module"
                            )

                            st.write(
                                common_module[
                                    "description"
                                ]
                            )

                            render_pills(
                                common_module[
                                    "examples"
                                ]
                            )


                with st.container(
                    key="edu_section_module_principles"
                ):

                    render_surface_header(
                        "Module 구현 원칙",
                        (
                            "각 Module의 책임과 Interface를 "
                            "명확하게 정의해야 합니다."
                        ),
                        label="PRINCIPLE",
                    )

                    for item in module_implementation[
                        "principles"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                with st.container(
                    key="edu_section_module_flow"
                ):

                    render_surface_header(
                        "Module 구현 흐름",
                        (
                            "요구 기능 확인부터 최종 통합까지의 "
                            "전체 과정을 확인합니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        module_implementation[
                            "implementation_flow"
                        ]
                    )


                render_exam_panel(
                    module_implementation[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑥ Error / Warning
        # =================================================

        if error_tab.open:

            with error_tab:

                st.markdown(
                    "## Compile Error와 Warning 제거"
                )


                with st.container(
                    key="edu_section_compile_error_core"
                ):

                    render_surface_header(
                        compile_error["title"],
                        compile_error[
                            "important_point"
                        ],
                        label="COMPILER MESSAGE",
                    )


                    error_col, warning_col = st.columns(
                        2
                    )


                    with error_col:

                        with st.container(
                            key="edu_subsection_error"
                        ):

                            error_data = compile_error[
                                "error"
                            ]

                            st.markdown(
                                "### ❌ Error"
                            )

                            st.write(
                                error_data[
                                    "description"
                                ]
                            )

                            render_pills(
                                error_data[
                                    "examples"
                                ]
                            )


                    with warning_col:

                        with st.container(
                            key="edu_subsection_warning"
                        ):

                            warning_data = compile_error[
                                "warning"
                            ]

                            st.markdown(
                                "### ⚠️ Warning"
                            )

                            st.write(
                                warning_data[
                                    "description"
                                ]
                            )

                            render_pills(
                                warning_data[
                                    "examples"
                                ]
                            )


                with st.container(
                    key="edu_section_error_process"
                ):

                    render_surface_header(
                        "오류 제거 과정",
                        (
                            "Compiler Message를 확인하면서 "
                            "수정과 Compile을 반복합니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        compile_error[
                            "process"
                        ]
                    )


                with st.container(
                    key="edu_section_error_arduino"
                ):

                    render_surface_header(
                        "Arduino Compile Error 예제",
                        (
                            "세미콜론 누락으로 발생하는 "
                            "대표적인 Compile Error입니다."
                        ),
                        label="ARDUINO EXAMPLE",
                    )

                    arduino_example = compile_error[
                        "arduino_example"
                    ]

                    st.markdown(
                        "**오류가 있는 코드**"
                    )

                    st.code(
                        arduino_example[
                            "broken_code"
                        ],
                        language="cpp",
                    )

                    st.error(
                        arduino_example[
                            "problem"
                        ]
                    )

                    st.markdown(
                        "**수정 코드**"
                    )

                    st.code(
                        arduino_example[
                            "fixed_code"
                        ],
                        language="cpp",
                    )


                render_exam_panel(
                    compile_error[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑦ ECHO Server
        # =================================================

        if echo_tab.open:

            with echo_tab:

                st.markdown(
                    "## ECHO Server 구현 실습"
                )


                with st.container(
                    key="edu_section_echo_core"
                ):

                    render_surface_header(
                        echo_server[
                            "title"
                        ],
                        echo_server[
                            "definition"
                        ],
                        label="NETWORK PROGRAM",
                    )

                    render_concept(
                        "실습 목적",
                        echo_server[
                            "purpose"
                        ],
                    )


                with st.container(
                    key="edu_section_echo_host_target"
                ):

                    render_surface_header(
                        "Host와 Target 역할",
                        echo_server[
                            "important_note"
                        ],
                        label="HOST ↔ TARGET",
                    )

                    host_col, arrow_col, target_col = st.columns(
                        [5, 1, 5]
                    )


                    with host_col:

                        with st.container(
                            key="edu_subsection_echo_host"
                        ):

                            host = echo_server[
                                "host"
                            ]

                            st.markdown(
                                "### 💻 Host"
                            )

                            st.write(
                                host[
                                    "role"
                                ]
                            )

                            st.caption(
                                host[
                                    "environment"
                                ]
                            )

                            st.code(
                                host[
                                    "compile_command"
                                ],
                                language="bash",
                            )


                    with arrow_col:

                        st.markdown("")
                        st.markdown("")
                        st.markdown(
                            "## ↔"
                        )


                    with target_col:

                        with st.container(
                            key="edu_subsection_echo_target"
                        ):

                            target = echo_server[
                                "target"
                            ]

                            st.markdown(
                                "### 🎯 Target"
                            )

                            st.write(
                                target[
                                    "role"
                                ]
                            )

                            st.caption(
                                target[
                                    "environment"
                                ]
                            )

                            st.code(
                                target[
                                    "compile_command"
                                ],
                                language="bash",
                            )


                    st.markdown(
                        f"**Port:** `{echo_server['port']}`"
                    )

                    st.markdown(
                        f"**전송 방식:** `{echo_server['transfer_method']}`"
                    )

                    st.code(
                        echo_server[
                            "transfer_path"
                        ]
                    )


                with st.container(
                    key="edu_section_echo_communication"
                ):

                    render_surface_header(
                        "통신 흐름",
                        (
                            "Client가 전송한 데이터를 Server가 "
                            "그대로 다시 반환합니다."
                        ),
                        label="COMMUNICATION",
                    )

                    render_process(
                        echo_server[
                            "communication_flow"
                        ]
                    )


                with st.container(
                    key="edu_section_echo_development"
                ):

                    render_surface_header(
                        "개발 흐름",
                        (
                            "Source 작성부터 Target 실행과 "
                            "통신 결과 확인까지의 흐름입니다."
                        ),
                        label="DEVELOPMENT",
                    )

                    render_process(
                        echo_server[
                            "development_flow"
                        ]
                    )


                render_exam_panel(
                    echo_server[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑧ Arduino 연결
        # =================================================

        if arduino_tab_3_1.open:

            with arduino_tab_3_1:

                st.markdown(
                    "## NCS Module 구현과 Arduino 연결"
                )


                with st.container(
                    key="edu_section_arduino_mapping_3_1"
                ):

                    render_surface_header(
                        arduino_mapping_3_1[
                            "title"
                        ],
                        arduino_mapping_3_1[
                            "note"
                        ],
                        label="ARDUINO CONNECTION",
                    )

                    mapping = arduino_mapping_3_1[
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
                                        "edu_subsection_arduino31_"
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


                example = arduino_mapping_3_1[
                    "project_example"
                ]

                with st.container(
                    key="edu_section_arduino_project_3_1"
                ):

                    render_surface_header(
                        example[
                            "project"
                        ],
                        example[
                            "integration"
                        ],
                        label="PROJECT EXAMPLE",
                    )

                    render_pills(
                        example[
                            "modules"
                        ]
                    )


        # =================================================
        # ⑨ 개념 체험
        # =================================================

        if practice_tab_3_1.open:

            with practice_tab_3_1:

                st.markdown(
                    "## GCC와 Module 구현 개념 체험"
                )


                with st.container(
                    key="edu_section_practice_gcc_order"
                ):

                    render_surface_header(
                        "GCC 처리 순서",
                        practice_3_1[
                            "activities"
                        ][0]["instruction"],
                        label="ACTIVITY 01",
                    )

                    answer = st.radio(
                        "올바른 GCC 내부 처리 순서는?",
                        [
                            "cpp → cc1 → as → ld",
                            "cc1 → cpp → ld → as",
                            "as → cpp → cc1 → ld",
                        ],
                        index=None,
                        key="3_1_gcc_order",
                    )

                    if answer == "cpp → cc1 → as → ld":
                        st.success(
                            "정답입니다! ✅"
                        )

                    elif answer:
                        st.error(
                            "GCC 처리 순서를 다시 확인해보세요."
                        )


                with st.container(
                    key="edu_section_practice_gcc_option"
                ):

                    render_surface_header(
                        "GCC Option 선택",
                        practice_3_1[
                            "activities"
                        ][1]["instruction"],
                        label="ACTIVITY 02",
                    )

                    option_case = st.selectbox(
                        "상황을 선택하세요.",
                        [
                            "선택하세요",
                            "출력 파일 이름 지정",
                            "Object File까지만 생성",
                            "Debug 정보 포함",
                            "Warning 활성화",
                        ],
                        key="3_1_option_case",
                    )

                    option_answers = {
                        "출력 파일 이름 지정": "-o",
                        "Object File까지만 생성": "-c",
                        "Debug 정보 포함": "-g",
                        "Warning 활성화": "-Wall",
                    }

                    if option_case != "선택하세요":

                        option_answer = st.selectbox(
                            "적절한 Option은?",
                            [
                                "선택하세요",
                                "-o",
                                "-c",
                                "-g",
                                "-Wall",
                                "-L",
                            ],
                            key="3_1_option_answer",
                        )

                        if option_answer != "선택하세요":

                            if (
                                option_answer
                                == option_answers[
                                    option_case
                                ]
                            ):
                                st.success(
                                    "정답입니다! ✅"
                                )

                            else:
                                st.error(
                                    "다시 확인해보세요."
                                )


                with st.container(
                    key="edu_section_practice_error"
                ):

                    render_surface_header(
                        "Compile Error 찾기",
                        practice_3_1[
                            "activities"
                        ][3]["instruction"],
                        label="ACTIVITY 03",
                    )

                    st.code(
                        """
void setup() {
    pinMode(13, OUTPUT)
}
                        """.strip(),
                        language="cpp",
                    )

                    error_answer = st.radio(
                        "오류의 원인은?",
                        [
                            "세미콜론 누락",
                            "변수 자료형 오류",
                            "함수 이름 오류",
                            "Header File 누락",
                        ],
                        index=None,
                        key="3_1_error_answer",
                    )

                    if error_answer == "세미콜론 누락":
                        st.success(
                            "정답입니다! ✅"
                        )

                    elif error_answer:
                        st.error(
                            "문장 끝을 다시 확인해보세요."
                        )


        # =================================================
        # ⑩ 형성평가
        # =================================================

        if formative_tab_3_1.open:

            with formative_tab_3_1:

                render_quiz(
                    FORMATIVE_QUIZ_3_1,
                    title="✅ 3-1 형성평가",
                    description=(
                        "GCC, Make, Module 구현, Compile Error와 "
                        "ECHO Server 내용을 확인합니다."
                    ),
                )


        # =================================================
        # ⑪ 중간고사
        # =================================================

        if exam_tab_3_1.open:

            with exam_tab_3_1:

                render_exam_practice(
                    EXAM_PRACTICE_3_1
                )


        if is_section_completed("3-1"):

            st.success(
                "✅ 3-1 학습 완료"
            )


# =========================================================
# 3-2
# =========================================================

if lesson_tab_2.open:

    with lesson_tab_2:

        st.markdown(
            f"## {metadata_3_2['section']}. "
            f"{metadata_3_2['title']}"
        )

        st.caption(
            "GDB를 이용한 Debugging과 Remote Debugging, "
            "Module Integration 과정을 학습합니다."
        )


        # -------------------------------------------------
        # 학습 목표
        # -------------------------------------------------

        with st.container(
            key="edu_section_3_2_objectives"
        ):

            render_surface_header(
                "학습 목표",
                (
                    "GDB 명령과 Debugging 절차를 이해하고 "
                    "검증된 Module을 하나의 프로그램으로 통합합니다."
                ),
                label="LEARNING GOALS",
            )

            for objective in LESSON_3_2[
                "objectives"
            ]:
                st.markdown(
                    f"- {objective}"
                )


        # -------------------------------------------------
        # 내부 탭
        # -------------------------------------------------

        (
            debugging_tab,
            gdb_tab,
            command_tab,
            breakpoint_tab,
            variable_tab,
            remote_tab,
            integration_tab,
            arduino_tab_3_2,
            practice_tab_3_2,
            formative_tab_3_2,
            exam_tab_3_2,
        ) = st.tabs(
            [
                "① Debugging",
                "② GDB",
                "③ GDB Command",
                "④ Breakpoint · Step",
                "⑤ 변수 상태 확인",
                "⑥ Remote Debugging",
                "⑦ Program Integration",
                "⑧ Arduino 연결",
                "⑨ 개념 체험",
                "⑩ 형성평가",
                "⑪ 중간고사 대비",
            ],
            key="lesson_3_2_inner_tabs",
            on_change="rerun",
        )


        # =================================================
        # ① Debugging
        # =================================================

        if debugging_tab.open:

            with debugging_tab:

                st.markdown(
                    "## Debugging"
                )


                with st.container(
                    key="edu_section_debugging_core"
                ):

                    render_surface_header(
                        debugging_overview[
                            "title"
                        ],
                        debugging_overview[
                            "definition"
                        ],
                        label="DEBUGGING",
                    )

                    render_concept(
                        "왜 Debugging이 필요한가?",
                        debugging_overview[
                            "purpose"
                        ],
                    )


                with st.container(
                    key="edu_section_debugging_types"
                ):

                    render_surface_header(
                        "오류의 유형",
                        (
                            "Syntax, Runtime, Logical Error의 "
                            "차이를 구분합니다."
                        ),
                        label="ERROR TYPE",
                    )

                    cols = st.columns(
                        3
                    )

                    for col, item in zip(
                        cols,
                        debugging_overview[
                            "types_of_problem"
                        ],
                    ):

                        with col:

                            with st.container(
                                key=(
                                    "edu_subsection_debug_type_"
                                    f"{item['name']}"
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


                with st.container(
                    key="edu_section_debugging_process"
                ):

                    render_surface_header(
                        "Debugging 과정",
                        debugging_overview[
                            "important_point"
                        ],
                        label="PROCESS",
                    )

                    render_process(
                        debugging_overview[
                            "process"
                        ]
                    )


                render_exam_panel(
                    debugging_overview[
                        "exam_points"
                    ]
                )


        # =================================================
        # ② GDB
        # =================================================

        if gdb_tab.open:

            with gdb_tab:

                st.markdown(
                    "## GDB"
                )


                with st.container(
                    key="edu_section_gdb_overview"
                ):

                    render_surface_header(
                        gdb_overview[
                            "title"
                        ],
                        gdb_overview[
                            "definition"
                        ],
                        label="GNU DEBUGGER",
                    )

                    render_pills(
                        gdb_overview[
                            "features"
                        ]
                    )


                with st.container(
                    key="edu_section_gdb_debug_option"
                ):

                    debug_option = gdb_overview[
                        "debug_option"
                    ]

                    render_surface_header(
                        "Debug 정보 포함",
                        debug_option[
                            "description"
                        ],
                        label="GCC -g",
                    )

                    st.code(
                        debug_option[
                            "example"
                        ],
                        language="bash",
                    )


                with st.container(
                    key="edu_section_gdb_procedure"
                ):

                    render_surface_header(
                        "GDB 기본 사용 절차",
                        (
                            "Compile부터 Breakpoint와 변수 확인까지의 "
                            "전체 흐름입니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        gdb_overview[
                            "basic_procedure"
                        ]
                    )


                with st.container(
                    key="edu_section_gdb_modes"
                ):

                    render_surface_header(
                        gdb_modes[
                            "title"
                        ],
                        (
                            "Local Debugging과 Remote Debugging의 "
                            "실행 위치를 비교합니다."
                        ),
                        label="MODE",
                    )

                    cols = st.columns(
                        2
                    )

                    for col, mode in zip(
                        cols,
                        gdb_modes[
                            "modes"
                        ],
                    ):

                        with col:

                            with st.container(
                                key=(
                                    "edu_subsection_gdb_mode_"
                                    f"{mode['name']}"
                                )
                            ):

                                st.markdown(
                                    f"### {mode['name']}"
                                )

                                st.write(
                                    mode[
                                        "description"
                                    ]
                                )

                                st.caption(
                                    mode[
                                        "example"
                                    ]
                                )


                render_exam_panel(
                    [
                        *gdb_overview[
                            "exam_points"
                        ],
                        *gdb_modes[
                            "exam_points"
                        ],
                    ]
                )


        # =================================================
        # ③ GDB Command
        # =================================================

        if command_tab.open:

            with command_tab:

                st.markdown(
                    "## GDB 주요 명령어"
                )


                with st.container(
                    key="edu_section_gdb_commands"
                ):

                    render_surface_header(
                        gdb_commands[
                            "title"
                        ],
                        (
                            "Source 확인, 실행 제어, 변수 확인, "
                            "Stack 이동 명령을 학습합니다."
                        ),
                        label="COMMAND REFERENCE",
                    )


                    for command in gdb_commands[
                        "commands"
                    ]:

                        col1, col2 = st.columns(
                            [2, 5]
                        )

                        with col1:

                            st.markdown(
                                f"### `{command['command']}`"
                            )

                            if command.get(
                                "short"
                            ):
                                st.caption(
                                    "단축형: "
                                    + command[
                                        "short"
                                    ]
                                )

                        with col2:

                            st.write(
                                command[
                                    "description"
                                ]
                            )

                            if command.get(
                                "example"
                            ):
                                st.code(
                                    command[
                                        "example"
                                    ],
                                    language="text",
                                )

                        st.divider()


                render_exam_panel(
                    gdb_commands[
                        "exam_points"
                    ]
                )


        # =================================================
        # ④ Breakpoint · Step
        # =================================================

        if breakpoint_tab.open:

            with breakpoint_tab:

                st.markdown(
                    "## Breakpoint와 Step Execution"
                )


                with st.container(
                    key="edu_section_breakpoint"
                ):

                    render_surface_header(
                        breakpoint[
                            "title"
                        ],
                        breakpoint[
                            "definition"
                        ],
                        label="BREAKPOINT",
                    )

                    render_concept(
                        "Breakpoint를 사용하는 이유",
                        breakpoint[
                            "purpose"
                        ],
                    )

                    for item in breakpoint[
                        "commands"
                    ]:

                        st.code(
                            item[
                                "command"
                            ],
                            language="text",
                        )

                        st.caption(
                            item[
                                "description"
                            ]
                        )

                    render_process(
                        breakpoint[
                            "flow"
                        ]
                    )


                with st.container(
                    key="edu_section_step_execution"
                ):

                    render_surface_header(
                        step_execution[
                            "title"
                        ],
                        step_execution[
                            "definition"
                        ],
                        label="STEP EXECUTION",
                    )

                    step_col, next_col = st.columns(
                        2
                    )

                    comparison = step_execution[
                        "comparison"
                    ]

                    with step_col:

                        with st.container(
                            key="edu_subsection_step"
                        ):

                            item = comparison[0]

                            st.markdown(
                                "### `step`"
                            )

                            st.write(
                                item[
                                    "description"
                                ]
                            )

                            st.caption(
                                item[
                                    "use_case"
                                ]
                            )


                    with next_col:

                        with st.container(
                            key="edu_subsection_next"
                        ):

                            item = comparison[1]

                            st.markdown(
                                "### `next`"
                            )

                            st.write(
                                item[
                                    "description"
                                ]
                            )

                            st.caption(
                                item[
                                    "use_case"
                                ]
                            )


                    st.markdown(
                        "### 관련 명령어"
                    )

                    for item in step_execution[
                        "related_commands"
                    ]:

                        st.markdown(
                            f"**`{item['command']}`** — "
                            f"{item['description']}"
                        )


                render_exam_panel(
                    [
                        *breakpoint[
                            "exam_points"
                        ],
                        *step_execution[
                            "exam_points"
                        ],
                    ]
                )


        # =================================================
        # ⑤ 변수 상태 확인
        # =================================================

        if variable_tab.open:

            with variable_tab:

                st.markdown(
                    "## 변수와 프로그램 상태 확인"
                )


                with st.container(
                    key="edu_section_variable_memory"
                ):

                    render_surface_header(
                        variable_memory[
                            "title"
                        ],
                        variable_memory[
                            "description"
                        ],
                        label="VARIABLE",
                    )

                    for item in variable_memory[
                        "commands"
                    ]:

                        with st.container(
                            key=(
                                "edu_subsection_variable_"
                                f"{item['command']}"
                            )
                        ):

                            st.markdown(
                                f"**`{item['command']}`**"
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
                                language="text",
                            )


                with st.container(
                    key="edu_section_variable_example"
                ):

                    example = variable_memory[
                        "example"
                    ]

                    render_surface_header(
                        "변수 분석 예제",
                        (
                            "count 변수의 값을 GDB 명령으로 "
                            "확인하는 예입니다."
                        ),
                        label="EXAMPLE",
                    )

                    st.code(
                        example[
                            "code"
                        ],
                        language="c",
                    )

                    for item in example[
                        "analysis"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                render_exam_panel(
                    variable_memory[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑥ Remote Debugging
        # =================================================

        if remote_tab.open:

            with remote_tab:

                st.markdown(
                    "## Remote Debugging"
                )


                with st.container(
                    key="edu_section_remote_core"
                ):

                    render_surface_header(
                        remote_debugging[
                            "title"
                        ],
                        remote_debugging[
                            "definition"
                        ],
                        label="REMOTE DEBUGGING",
                    )

                    render_concept(
                        "왜 Remote Debugging이 필요한가?",
                        remote_debugging[
                            "why_needed"
                        ],
                    )


                    host_col, arrow_col, target_col = st.columns(
                        [5, 1, 5]
                    )

                    with host_col:

                        with st.container(
                            key="edu_subsection_remote_host"
                        ):

                            st.markdown(
                                "### 💻 Host"
                            )

                            st.write(
                                remote_debugging[
                                    "host"
                                ]
                            )


                    with arrow_col:

                        st.markdown("")
                        st.markdown("")
                        st.markdown(
                            "## ↔"
                        )


                    with target_col:

                        with st.container(
                            key="edu_subsection_remote_target"
                        ):

                            st.markdown(
                                "### 🎯 Target"
                            )

                            st.write(
                                remote_debugging[
                                    "target"
                                ]
                            )


                with st.container(
                    key="edu_section_remote_components"
                ):

                    render_surface_header(
                        "구성 도구",
                        (
                            "Host GDB, DDD, gdbserver의 "
                            "역할을 구분합니다."
                        ),
                        label="COMPONENT",
                    )

                    cols = st.columns(
                        3
                    )

                    for col, item in zip(
                        cols,
                        remote_debugging[
                            "components"
                        ],
                    ):

                        with col:

                            with st.container(
                                key=(
                                    "edu_subsection_remote_component_"
                                    f"{item['name']}"
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


                with st.container(
                    key="edu_section_remote_process"
                ):

                    render_surface_header(
                        "Remote Debugging 과정",
                        (
                            "Target용 실행 파일 생성부터 "
                            "Host GDB 연결까지의 흐름입니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        remote_debugging[
                            "process"
                        ]
                    )


                with st.container(
                    key="edu_section_remote_commands"
                ):

                    render_surface_header(
                        "명령어 예제",
                        (
                            "Compile → Target gdbserver → "
                            "Host GDB 연결의 예입니다."
                        ),
                        label="COMMAND",
                    )

                    commands = remote_debugging[
                        "example_commands"
                    ]

                    st.markdown(
                        "**Compile**"
                    )

                    st.code(
                        commands[
                            "compile"
                        ],
                        language="bash",
                    )

                    st.markdown(
                        "**Target**"
                    )

                    st.code(
                        commands[
                            "target"
                        ],
                        language="bash",
                    )

                    st.markdown(
                        "**Host GDB**"
                    )

                    st.code(
                        commands[
                            "host"
                        ],
                        language="text",
                    )


                render_exam_panel(
                    remote_debugging[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑦ Program Integration
        # =================================================

        if integration_tab.open:

            with integration_tab:

                st.markdown(
                    "## Program Integration"
                )


                with st.container(
                    key="edu_section_integration_core"
                ):

                    render_surface_header(
                        program_integration[
                            "title"
                        ],
                        program_integration[
                            "definition"
                        ],
                        label="INTEGRATION",
                    )

                    render_concept(
                        "왜 통합 후 다시 검증해야 하는가?",
                        program_integration[
                            "why_needed"
                        ],
                    )


                with st.container(
                    key="edu_section_integration_process"
                ):

                    render_surface_header(
                        "Program Integration 과정",
                        (
                            "개별 Module 검증부터 전체 기능 확인까지의 "
                            "통합 흐름입니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        program_integration[
                            "process"
                        ]
                    )


                with st.container(
                    key="edu_section_integration_points"
                ):

                    render_surface_header(
                        "통합 시 확인 사항",
                        (
                            "Interface, Data 전달, 공유 Resource와 "
                            "실행 순서를 확인합니다."
                        ),
                        label="CHECK POINT",
                    )

                    for item in program_integration[
                        "important_points"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                with st.container(
                    key="edu_section_integration_problems"
                ):

                    render_surface_header(
                        "통합 과정에서 발생할 수 있는 문제",
                        (
                            "각 Module은 정상이어도 통합 시 "
                            "새로운 문제가 발생할 수 있습니다."
                        ),
                        label="TROUBLESHOOTING",
                    )

                    for item in program_integration[
                        "integration_problem_examples"
                    ]:

                        with st.expander(
                            f"⚠️ {item['problem']}"
                        ):

                            st.write(
                                item[
                                    "possible_cause"
                                ]
                            )


                render_exam_panel(
                    program_integration[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑧ Arduino 연결
        # =================================================

        if arduino_tab_3_2.open:

            with arduino_tab_3_2:

                st.markdown(
                    "## NCS Debugging과 Arduino 연결"
                )


                with st.container(
                    key="edu_section_arduino_mapping_3_2"
                ):

                    render_surface_header(
                        arduino_mapping_3_2[
                            "title"
                        ],
                        arduino_mapping_3_2[
                            "note"
                        ],
                        label="ARDUINO CONNECTION",
                    )

                    mapping = arduino_mapping_3_2[
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
                                        "edu_subsection_arduino32_"
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


                example = arduino_mapping_3_2[
                    "project_example"
                ]

                with st.container(
                    key="edu_section_arduino_debug_project"
                ):

                    render_surface_header(
                        example[
                            "project"
                        ],
                        (
                            "기능별 Test → 통합 → Debugging의 "
                            "흐름을 Arduino 프로젝트에 적용합니다."
                        ),
                        label="PROJECT EXAMPLE",
                    )

                    render_pills(
                        example[
                            "modules"
                        ]
                    )

                    render_process(
                        example[
                            "debugging_flow"
                        ]
                    )


                st.warning(
                    arduino_mapping_3_2[
                        "important_distinction"
                    ]
                )


        # =================================================
        # ⑨ 개념 체험
        # =================================================

        if practice_tab_3_2.open:

            with practice_tab_3_2:

                st.markdown(
                    "## GDB와 Debugging 개념 체험"
                )


                with st.container(
                    key="edu_section_practice_gdb_command"
                ):

                    render_surface_header(
                        "GDB 명령어 맞추기",
                        practice_3_2[
                            "activities"
                        ][0]["instruction"],
                        label="ACTIVITY 01",
                    )

                    command_case = st.selectbox(
                        "상황을 선택하세요.",
                        [
                            "선택하세요",
                            "Breakpoint 설정",
                            "변수 값 확인",
                            "실행 계속",
                            "함수 내부로 진입",
                            "함수 내부로 들어가지 않고 다음 줄",
                        ],
                        key="3_2_command_case",
                    )

                    answers = {
                        "Breakpoint 설정": "break",
                        "변수 값 확인": "print",
                        "실행 계속": "continue",
                        "함수 내부로 진입": "step",
                        (
                            "함수 내부로 들어가지 않고 다음 줄"
                        ): "next",
                    }

                    if command_case != "선택하세요":

                        command_answer = st.selectbox(
                            "적절한 명령어는?",
                            [
                                "선택하세요",
                                "break",
                                "print",
                                "continue",
                                "step",
                                "next",
                                "run",
                            ],
                            key="3_2_command_answer",
                        )

                        if command_answer != "선택하세요":

                            if (
                                command_answer
                                == answers[
                                    command_case
                                ]
                            ):
                                st.success(
                                    "정답입니다! ✅"
                                )

                            else:
                                st.error(
                                    "다시 확인해보세요."
                                )


                with st.container(
                    key="edu_section_practice_step_next"
                ):

                    render_surface_header(
                        "step과 next 구분",
                        practice_3_2[
                            "activities"
                        ][1]["instruction"],
                        label="ACTIVITY 02",
                    )

                    step_question = st.radio(
                        (
                            "호출되는 함수 내부의 동작까지 "
                            "한 줄씩 확인하고 싶습니다. "
                            "어떤 명령을 사용해야 할까요?"
                        ),
                        [
                            "step",
                            "next",
                            "continue",
                        ],
                        index=None,
                        key="3_2_step_question",
                    )

                    if step_question == "step":
                        st.success(
                            "정답입니다! ✅"
                        )

                    elif step_question:
                        st.error(
                            "`step`은 함수 내부로 진입합니다."
                        )


                with st.container(
                    key="edu_section_practice_remote"
                ):

                    render_surface_header(
                        "Remote Debugging 역할 구분",
                        practice_3_2[
                            "activities"
                        ][3]["instruction"],
                        label="ACTIVITY 03",
                    )

                    remote_question = st.radio(
                        (
                            "Target에서 Host GDB와 연결하기 위해 "
                            "사용할 수 있는 프로그램은?"
                        ),
                        [
                            "gdbserver",
                            "gcc",
                            "make",
                            "cpp",
                        ],
                        index=None,
                        key="3_2_remote_question",
                    )

                    if remote_question == "gdbserver":
                        st.success(
                            "정답입니다! ✅"
                        )

                    elif remote_question:
                        st.error(
                            "Target에서 사용하는 Remote Debugging "
                            "도구를 다시 확인해보세요."
                        )


        # =================================================
        # ⑩ 형성평가
        # =================================================

        if formative_tab_3_2.open:

            with formative_tab_3_2:

                render_quiz(
                    FORMATIVE_QUIZ_3_2,
                    title="✅ 3-2 형성평가",
                    description=(
                        "Debugging, GDB 명령어, Breakpoint, "
                        "Remote Debugging과 Program Integration을 확인합니다."
                    ),
                )


        # =================================================
        # ⑪ 중간고사
        # =================================================

        if exam_tab_3_2.open:

            with exam_tab_3_2:

                render_exam_practice(
                    EXAM_PRACTICE_3_2
                )


        if is_section_completed("3-2"):

            st.success(
                "✅ 3-2 학습 완료"
            )


# =========================================================
# 학습 3 전체 완료
# =========================================================

if is_lesson_completed("3"):

    st.divider()

    st.success(
        "🎉 학습 3 · 애플리케이션 모듈 구현하기를 "
        "모두 완료했습니다!"
    )

    with st.expander(
        "📚 학습 3 핵심 내용 다시 보기"
    ):

        st.markdown(
            "### 3-1 핵심 정리"
        )

        render_summary(
            LESSON_3_1[
                "summary"
            ]
        )

        st.divider()

        st.markdown(
            "### 3-2 핵심 정리"
        )

        render_summary(
            LESSON_3_2[
                "summary"
            ]
        )