from __future__ import annotations

from html import escape
from textwrap import dedent

import streamlit as st

from data.lessons.lesson_4_1 import LESSON_4_1
from data.lessons.lesson_4_2 import LESSON_4_2

from data.quizzes.quiz_4_1 import (
    EXAM_PRACTICE_4_1,
    FORMATIVE_QUIZ_4_1,
)

from data.quizzes.quiz_4_2 import (
    EXAM_PRACTICE_4_2,
    FORMATIVE_QUIZ_4_2,
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
    page_title="학습 4 | 인터페이스 구현",
    page_icon="🔗",
    layout="wide",
)

load_global_css()


# =========================================================
# HTML Helper
# =========================================================

def render_html(html: str) -> None:
    """
    Custom HTML을 Markdown Parser 없이 직접 렌더링한다.
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


def render_concept(
    title: str,
    content: str,
) -> None:

    render_html(
        f"""
        <div class="edu-concept">

            <div class="edu-concept-title">
                {escape(str(title))}
            </div>

            <div class="edu-concept-body">
                {escape(str(content))}
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


def render_framework_license(
    framework: str,
    license_name: str,
) -> None:

    render_html(
        f"""
        <div style="
            display:flex;
            align-items:center;
            justify-content:space-between;
            gap:1rem;

            padding:0.72rem 0.85rem;
            margin-bottom:0.55rem;

            background:#f8f9fc;
            border:1px solid #e7eaf1;
            border-radius:11px;
        ">

            <div style="
                color:#172033;
                font-weight:750;
                font-size:0.9rem;
            ">
                {escape(framework)}
            </div>

            <div style="
                padding:0.24rem 0.58rem;

                color:#4f51d7;
                background:#eef0ff;

                border-radius:999px;

                font-size:0.76rem;
                font-weight:750;
            ">
                {escape(license_name)}
            </div>

        </div>
        """
    )


def render_version_compare(
    title: str,
    subtitle: str,
    items: list[str],
) -> None:

    items_html = "".join(
        f"<li>{escape(str(item))}</li>"
        for item in items
    )

    render_html(
        f"""
        <div style="
            padding:1rem 1.05rem;

            background:#f8f9fc;
            border:1px solid #e7eaf1;
            border-radius:14px;

            min-height:260px;
        ">

            <div style="
                color:#172033;
                font-size:1rem;
                font-weight:800;
                margin-bottom:0.2rem;
            ">
                {escape(title)}
            </div>

            <div style="
                color:#98a2b3;
                font-size:0.78rem;
                margin-bottom:0.6rem;
            ">
                {escape(subtitle)}
            </div>

            <ul style="
                margin:0.25rem 0 0 1rem;
                padding:0;
            ">
                {items_html}
            </ul>

        </div>
        """
    )


# =========================================================
# 4-1 데이터
# =========================================================

metadata_4_1 = LESSON_4_1["metadata"]

gui_overview = LESSON_4_1["gui_overview"]
gui_frameworks = LESSON_4_1["gui_frameworks"]
licenses = LESSON_4_1["licenses"]

nano_x = LESSON_4_1["nano_x"]
directfb = LESSON_4_1["directfb"]
gtk = LESSON_4_1["gtk"]
qt = LESSON_4_1["qt"]

pyqt = LESSON_4_1["pyqt"]
qt_designer = LESSON_4_1["qt_designer"]

interface_implementation = LESSON_4_1[
    "interface_implementation"
]

arduino_mapping_4_1 = LESSON_4_1[
    "arduino_mapping"
]

practice_4_1 = LESSON_4_1[
    "practice"
]


# =========================================================
# 4-2 데이터
# =========================================================

metadata_4_2 = LESSON_4_2["metadata"]

version_control_overview = LESSON_4_2[
    "version_control_overview"
]

version_control_types = LESSON_4_2[
    "version_control_types"
]

cvs = LESSON_4_2["cvs"]
svn = LESSON_4_2["svn"]
git = LESSON_4_2["git"]
github = LESSON_4_2["github"]
repository = LESSON_4_2["repository"]
svn_practice = LESSON_4_2["svn_practice"]
collaboration = LESSON_4_2["collaboration"]

configuration_management = LESSON_4_2[
    "configuration_management"
]

case_tools = LESSON_4_2[
    "case_tools"
]

arduino_mapping_4_2 = LESSON_4_2[
    "arduino_mapping"
]

practice_4_2 = LESSON_4_2[
    "practice"
]


# =========================================================
# 진도
# =========================================================

lesson_4_progress = get_lesson_progress(
    "4"
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
    "🔗 **학습 4 · 애플리케이션 인터페이스 구현하기**"
)


# =========================================================
# Breadcrumb
# =========================================================

render_breadcrumb(
    "홈",
    "학습 4",
    "인터페이스 구현하기",
)


# =========================================================
# HERO
# =========================================================

render_html(
    """
    <div class="edu-hero">

        <div class="edu-hero-eyebrow">
            INTERFACE & VERSION CONTROL
        </div>

        <div class="edu-hero-title">
            학습 4. 애플리케이션 인터페이스 구현하기
        </div>

        <div class="edu-hero-desc">
            Embedded GUI와 Interface 구현 환경을 이해하고,
            Source Code 저장 및 Version Control,
            Configuration Management를 학습합니다.
        </div>

    </div>
    """
)


# =========================================================
# 진도
# =========================================================

render_progress_bar(
    lesson_4_progress,
    label="학습 4 전체 진도",
)

if is_lesson_completed("4"):

    st.success(
        "🎉 학습 4의 모든 소단원을 완료했습니다!"
    )


# =========================================================
# 학습 내용 선택
# =========================================================

st.markdown(
    "## 학습 내용 선택"
)

lesson_tab_1, lesson_tab_2 = st.tabs(
    [
        "4-1. 환경 준비 후 인터페이스 구현",
        "4-2. 소스 코드 저장 및 버전 관리",
    ],
    key="lesson_4_main_tabs",
    on_change="rerun",
)


# =========================================================
# 4-1
# =========================================================

if lesson_tab_1.open:

    with lesson_tab_1:

        st.markdown(
            f"## {metadata_4_1['section']}. "
            f"{metadata_4_1['title']}"
        )

        st.caption(
            "Embedded GUI와 Framework를 이해하고 "
            "PyQt · Qt Designer를 이용한 Interface 구현 환경과 "
            "User / Module Interface를 학습합니다."
        )


        # -------------------------------------------------
        # 학습 목표
        # -------------------------------------------------

        with st.container(
            key="edu_section_4_1_objectives"
        ):

            render_surface_header(
                "학습 목표",
                (
                    "GUI Framework와 Interface 구현 환경의 "
                    "핵심 개념을 이해합니다."
                ),
                label="LEARNING GOALS",
            )

            for objective in LESSON_4_1[
                "objectives"
            ]:
                st.markdown(
                    f"- {objective}"
                )


        # -------------------------------------------------
        # 내부 탭
        # -------------------------------------------------

        (
            gui_tab,
            framework_tab,
            license_tab,
            framework_detail_tab,
            qt_tab,
            designer_tab,
            interface_tab,
            arduino_tab_4_1,
            practice_tab_4_1,
            formative_tab_4_1,
            exam_tab_4_1,
        ) = st.tabs(
            [
                "① Embedded GUI",
                "② GUI Framework",
                "③ Framework License",
                "④ 주요 Framework",
                "⑤ QT · PyQt",
                "⑥ Qt Designer",
                "⑦ Interface 구현",
                "⑧ Arduino 연결",
                "⑨ 개념 체험",
                "⑩ 형성평가",
                "⑪ 중간고사 대비",
            ],
            key="lesson_4_1_inner_tabs",
            on_change="rerun",
        )


        # =================================================
        # ① Embedded GUI
        # =================================================

        if gui_tab.open:

            with gui_tab:

                st.markdown(
                    "## Embedded GUI"
                )

                st.caption(
                    "Embedded System에서 GUI를 구현할 때 "
                    "고려해야 하는 특징을 학습합니다."
                )


                with st.container(
                    key="edu_section_gui_core"
                ):

                    render_surface_header(
                        gui_overview[
                            "title"
                        ],
                        gui_overview[
                            "definition"
                        ],
                        label="GRAPHIC USER INTERFACE",
                    )

                    render_concept(
                        "Embedded GUI란?",
                        gui_overview[
                            "embedded_definition"
                        ],
                    )


                # -----------------------------------------
                # 주요 특성
                # -----------------------------------------

                with st.container(
                    key="edu_section_gui_characteristics"
                ):

                    render_surface_header(
                        "Embedded GUI 주요 특성",
                        (
                            "Desktop GUI와 달리 Resource 제약과 "
                            "안정성을 함께 고려해야 합니다."
                        ),
                        label="KEY FEATURES",
                    )

                    for item in gui_overview[
                        "characteristics"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                # -----------------------------------------
                # Design Point
                # -----------------------------------------

                with st.container(
                    key="edu_section_gui_design"
                ):

                    render_surface_header(
                        "GUI Design Point",
                        (
                            "Embedded GUI 설계에서 기억해야 할 "
                            "핵심 네 가지입니다."
                        ),
                        label="DESIGN",
                    )

                    render_pills(
                        gui_overview[
                            "design_points"
                        ]
                    )


                # -----------------------------------------
                # Display / FSE
                # -----------------------------------------

                with st.container(
                    key="edu_section_gui_display"
                ):

                    render_surface_header(
                        "Display 환경과 FSE",
                        gui_overview[
                            "display_requirement"
                        ],
                        label="DISPLAY",
                    )

                    fse = gui_overview[
                        "fse"
                    ]

                    render_concept(
                        (
                            f"{fse['term']} · "
                            f"{fse['full_name']}"
                        ),
                        fse[
                            "description"
                        ],
                    )


                render_exam_panel(
                    gui_overview[
                        "exam_points"
                    ]
                )


        # =================================================
        # ② GUI Framework
        # =================================================

        if framework_tab.open:

            with framework_tab:

                st.markdown(
                    "## Embedded GUI Framework"
                )


                with st.container(
                    key="edu_section_framework_core"
                ):

                    render_surface_header(
                        gui_frameworks[
                            "title"
                        ],
                        gui_frameworks[
                            "definition"
                        ],
                        label="FRAMEWORK",
                    )


                # -----------------------------------------
                # Low / High Level
                # -----------------------------------------

                with st.container(
                    key="edu_section_framework_levels"
                ):

                    render_surface_header(
                        "Low-level vs High-level",
                        (
                            "학습모듈에서 제시하는 GUI 기술을 "
                            "두 그룹으로 구분합니다."
                        ),
                        label="CLASSIFICATION",
                    )

                    low_col, high_col = st.columns(
                        2
                    )

                    with low_col:

                        with st.container(
                            key="edu_subsection_low_level_gui"
                        ):

                            st.markdown(
                                "### Low-level"
                            )

                            for item in gui_frameworks[
                                "low_level"
                            ]:

                                st.markdown(
                                    f"**{item['name']}**"
                                )

                                st.caption(
                                    item[
                                        "description"
                                    ]
                                )


                    with high_col:

                        with st.container(
                            key="edu_subsection_high_level_gui"
                        ):

                            st.markdown(
                                "### High-level"
                            )

                            for item in gui_frameworks[
                                "high_level"
                            ]:

                                st.markdown(
                                    f"**{item['name']}**"
                                )

                                st.caption(
                                    item[
                                        "description"
                                    ]
                                )


                # -----------------------------------------
                # 한눈에 보기
                # -----------------------------------------

                with st.container(
                    key="edu_section_framework_quick"
                ):

                    render_surface_header(
                        "Framework 빠른 구분",
                        (
                            "시험에서 자주 비교되는 "
                            "Framework 분류를 한 번에 확인합니다."
                        ),
                        label="QUICK VIEW",
                    )

                    col1, col2 = st.columns(
                        2
                    )

                    with col1:
                        st.markdown(
                            "**Low-level**"
                        )

                        render_pills(
                            gui_frameworks[
                                "classification"
                            ][
                                "low_level"
                            ]
                        )

                    with col2:
                        st.markdown(
                            "**High-level**"
                        )

                        render_pills(
                            gui_frameworks[
                                "classification"
                            ][
                                "high_level"
                            ]
                        )


                # -----------------------------------------
                # 선정 요소
                # -----------------------------------------

                with st.container(
                    key="edu_section_framework_selection"
                ):

                    render_surface_header(
                        "Framework 선정 기준",
                        (
                            "기능뿐 아니라 Target Resource와 "
                            "License까지 함께 검토해야 합니다."
                        ),
                        label="SELECTION",
                    )

                    render_pills(
                        gui_frameworks[
                            "selection_points"
                        ]
                    )


                render_exam_panel(
                    gui_frameworks[
                        "exam_points"
                    ]
                )


        # =================================================
        # ③ License
        # =================================================

        if license_tab.open:

            with license_tab:

                st.markdown(
                    "## GUI Framework와 License"
                )

                st.caption(
                    "시험 범위에서는 Framework와 License의 "
                    "대응 관계를 정확하게 구분해야 합니다."
                )


                with st.container(
                    key="edu_section_gui_license"
                ):

                    render_surface_header(
                        licenses[
                            "title"
                        ],
                        licenses[
                            "definition"
                        ],
                        label="LICENSE",
                    )

                    items = licenses[
                        "items"
                    ]

                    left_col, right_col = st.columns(
                        2
                    )

                    half = (
                        len(items) + 1
                    ) // 2

                    with left_col:

                        for item in items[
                            :half
                        ]:
                            render_framework_license(
                                item[
                                    "framework"
                                ],
                                item[
                                    "license"
                                ],
                            )

                    with right_col:

                        for item in items[
                            half:
                        ]:
                            render_framework_license(
                                item[
                                    "framework"
                                ],
                                item[
                                    "license"
                                ],
                            )


                st.warning(
                    licenses[
                        "important_point"
                    ]
                )

                render_exam_panel(
                    licenses[
                        "exam_points"
                    ]
                )


        # =================================================
        # ④ 주요 Framework
        # =================================================

        if framework_detail_tab.open:

            with framework_detail_tab:

                st.markdown(
                    "## 주요 GUI Framework"
                )

                st.caption(
                    "Nano-X, DirectFB, GTK, QT의 특징을 "
                    "Framework별로 살펴봅니다."
                )


                framework_data = [
                    (
                        "NANO-X",
                        nano_x,
                    ),
                    (
                        "DIRECT FRAME BUFFER",
                        directfb,
                    ),
                    (
                        "GTK",
                        gtk,
                    ),
                    (
                        "QT",
                        qt,
                    ),
                ]


                for index, (
                    label,
                    framework,
                ) in enumerate(
                    framework_data
                ):

                    with st.container(
                        key=(
                            "edu_section_framework_detail_"
                            f"{index}"
                        )
                    ):

                        description = framework[
                            "definition"
                        ]

                        render_surface_header(
                            framework[
                                "title"
                            ],
                            description,
                            label=label,
                        )

                        if framework.get(
                            "full_name"
                        ):
                            st.caption(
                                framework[
                                    "full_name"
                                ]
                            )

                        render_pills(
                            framework[
                                "features"
                            ]
                        )

                        st.markdown(
                            f"**License:** "
                            f"`{framework['license']}`"
                        )

                        if framework.get(
                            "components"
                        ):

                            st.markdown(
                                "**주요 Component**"
                            )

                            render_pills(
                                framework[
                                    "components"
                                ]
                            )

                        render_exam_panel(
                            framework[
                                "exam_points"
                            ],
                            title=(
                                f"{framework['title']} "
                                "시험 포인트"
                            ),
                        )


        # =================================================
        # ⑤ QT · PyQt
        # =================================================

        if qt_tab.open:

            with qt_tab:

                st.markdown(
                    "## QT와 PyQt"
                )


                # -----------------------------------------
                # QT
                # -----------------------------------------

                with st.container(
                    key="edu_section_qt_core"
                ):

                    render_surface_header(
                        qt[
                            "title"
                        ],
                        qt[
                            "definition"
                        ],
                        label="QT FRAMEWORK",
                    )

                    render_pills(
                        qt[
                            "components"
                        ]
                    )

                    st.markdown(
                        "**주요 특징**"
                    )

                    for item in qt[
                        "features"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                # -----------------------------------------
                # PyQt
                # -----------------------------------------

                with st.container(
                    key="edu_section_pyqt_core"
                ):

                    render_surface_header(
                        pyqt[
                            "title"
                        ],
                        pyqt[
                            "definition"
                        ],
                        label="PYTHON BINDING",
                    )

                    for item in pyqt[
                        "features"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                # -----------------------------------------
                # PyQt Flow
                # -----------------------------------------

                with st.container(
                    key="edu_section_pyqt_flow"
                ):

                    render_surface_header(
                        "PyQt GUI 구현 흐름",
                        (
                            "Qt Designer에서 화면을 만든 뒤 "
                            "Python Application에 연결합니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        pyqt[
                            "basic_flow"
                        ]
                    )


                render_exam_panel(
                    [
                        *qt[
                            "exam_points"
                        ],
                        *pyqt[
                            "exam_points"
                        ],
                    ]
                )


        # =================================================
        # ⑥ Qt Designer
        # =================================================

        if designer_tab.open:

            with designer_tab:

                st.markdown(
                    "## Qt Designer"
                )


                with st.container(
                    key="edu_section_qt_designer_core"
                ):

                    render_surface_header(
                        qt_designer[
                            "title"
                        ],
                        qt_designer[
                            "definition"
                        ],
                        label="GUI DESIGN TOOL",
                    )

                    render_concept(
                        "실습 Form Type",
                        qt_designer[
                            "project_type"
                        ],
                    )


                # -----------------------------------------
                # Widget
                # -----------------------------------------

                with st.container(
                    key="edu_section_qt_widgets"
                ):

                    render_surface_header(
                        "주요 Widget",
                        (
                            "Qt Designer에서 화면에 배치할 수 "
                            "있는 대표 Widget입니다."
                        ),
                        label="WIDGET",
                    )

                    render_pills(
                        qt_designer[
                            "widgets"
                        ]
                    )


                # -----------------------------------------
                # Procedure
                # -----------------------------------------

                with st.container(
                    key="edu_section_qt_designer_process"
                ):

                    render_surface_header(
                        "GUI 설계 과정",
                        (
                            "Form 생성부터 .ui File 저장까지의 "
                            "전체 흐름입니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        qt_designer[
                            "procedure"
                        ]
                    )


                # -----------------------------------------
                # UI File
                # -----------------------------------------

                ui_file = qt_designer[
                    "ui_file"
                ]

                with st.container(
                    key="edu_section_ui_file"
                ):

                    render_surface_header(
                        ".ui File",
                        ui_file[
                            "description"
                        ],
                        label="XML",
                    )

                    col1, col2 = st.columns(
                        2
                    )

                    with col1:

                        render_feature(
                            "확장자",
                            ui_file[
                                "extension"
                            ],
                        )

                    with col2:

                        render_feature(
                            "저장 형식",
                            ui_file[
                                "format"
                            ],
                        )

                    st.markdown(
                        "**XML 예제**"
                    )

                    st.code(
                        qt_designer[
                            "xml_example"
                        ],
                        language="xml",
                    )


                render_exam_panel(
                    qt_designer[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑦ Interface 구현
        # =================================================

        if interface_tab.open:

            with interface_tab:

                st.markdown(
                    "## User Interface와 Module Interface"
                )


                with st.container(
                    key="edu_section_interface_core"
                ):

                    render_surface_header(
                        interface_implementation[
                            "title"
                        ],
                        interface_implementation[
                            "definition"
                        ],
                        label="INTERFACE",
                    )


                    user_interface = (
                        interface_implementation[
                            "user_interface"
                        ]
                    )

                    module_interface = (
                        interface_implementation[
                            "module_interface"
                        ]
                    )


                    user_col, module_col = st.columns(
                        2
                    )

                    with user_col:

                        with st.container(
                            key="edu_subsection_user_interface"
                        ):

                            st.markdown(
                                "### 👤 User Interface"
                            )

                            st.write(
                                user_interface[
                                    "description"
                                ]
                            )

                            render_pills(
                                user_interface[
                                    "examples"
                                ]
                            )


                    with module_col:

                        with st.container(
                            key="edu_subsection_module_interface"
                        ):

                            st.markdown(
                                "### 🧩 Module Interface"
                            )

                            st.write(
                                module_interface[
                                    "description"
                                ]
                            )

                            render_pills(
                                module_interface[
                                    "examples"
                                ]
                            )


                # -----------------------------------------
                # 환경 준비
                # -----------------------------------------

                with st.container(
                    key="edu_section_interface_environment"
                ):

                    render_surface_header(
                        "Interface 구현 환경 준비",
                        (
                            "구현 전 Target, OS, Display, "
                            "Framework 등을 확인합니다."
                        ),
                        label="ENVIRONMENT",
                    )

                    render_pills(
                        interface_implementation[
                            "environment_preparation"
                        ]
                    )


                # -----------------------------------------
                # 구현 과정
                # -----------------------------------------

                with st.container(
                    key="edu_section_interface_process"
                ):

                    render_surface_header(
                        "Interface 구현 과정",
                        (
                            "요구사항 분석부터 실제 기능 검증까지의 "
                            "전체 흐름입니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        interface_implementation[
                            "implementation_process"
                        ]
                    )


                # -----------------------------------------
                # 중요 사항
                # -----------------------------------------

                with st.container(
                    key="edu_section_interface_points"
                ):

                    render_surface_header(
                        "Interface 구현 시 확인 사항",
                        (
                            "사용성과 Module 간 연결을 동시에 "
                            "검증해야 합니다."
                        ),
                        label="CHECK POINT",
                    )

                    for item in interface_implementation[
                        "important_points"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                render_exam_panel(
                    interface_implementation[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑧ Arduino 연결
        # =================================================

        if arduino_tab_4_1.open:

            with arduino_tab_4_1:

                st.markdown(
                    "## NCS Interface와 Arduino 연결"
                )


                with st.container(
                    key="edu_section_arduino_mapping_4_1"
                ):

                    render_surface_header(
                        arduino_mapping_4_1[
                            "title"
                        ],
                        arduino_mapping_4_1[
                            "note"
                        ],
                        label="ARDUINO CONNECTION",
                    )


                    mapping = arduino_mapping_4_1[
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

                        for index, (
                            col,
                            item,
                        ) in enumerate(
                            zip(
                                cols,
                                current,
                            )
                        ):

                            with col:

                                with st.container(
                                    key=(
                                        "edu_subsection_arduino41_"
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
                # Project
                # -----------------------------------------

                project = arduino_mapping_4_1[
                    "project_example"
                ]

                with st.container(
                    key="edu_section_arduino_project_4_1"
                ):

                    render_surface_header(
                        project[
                            "project"
                        ],
                        (
                            "User Interface와 Module Interface를 "
                            "스마트 화분 프로젝트에 적용합니다."
                        ),
                        label="PROJECT EXAMPLE",
                    )

                    col1, col2 = st.columns(
                        2
                    )

                    with col1:

                        st.markdown(
                            "**User Interface**"
                        )

                        render_pills(
                            project[
                                "user_interface"
                            ]
                        )

                    with col2:

                        st.markdown(
                            "**Module Interface**"
                        )

                        for item in project[
                            "module_interface"
                        ]:
                            st.markdown(
                                f"- {item}"
                            )


                st.warning(
                    arduino_mapping_4_1[
                        "important_distinction"
                    ]
                )


        # =================================================
        # ⑨ 개념 체험
        # =================================================

        if practice_tab_4_1.open:

            with practice_tab_4_1:

                st.markdown(
                    "## GUI와 Interface 개념 체험"
                )


                # -----------------------------------------
                # Framework 분류
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_framework"
                ):

                    render_surface_header(
                        "Framework 분류하기",
                        practice_4_1[
                            "activities"
                        ][0][
                            "instruction"
                        ],
                        label="ACTIVITY 01",
                    )

                    framework_case = st.selectbox(
                        "Framework를 선택하세요.",
                        [
                            "선택하세요",
                            "Nano-X",
                            "DirectFB",
                            "KDrive",
                            "SDL",
                            "Gtk",
                            "QT",
                            "FLTK",
                            "MiniGUI",
                        ],
                        key="4_1_framework_case",
                    )

                    low_level = {
                        "Nano-X",
                        "DirectFB",
                        "KDrive",
                        "SDL",
                    }

                    high_level = {
                        "Gtk",
                        "QT",
                        "FLTK",
                        "MiniGUI",
                    }

                    if framework_case != "선택하세요":

                        classification = st.radio(
                            "어느 그룹인가요?",
                            [
                                "Low-level",
                                "High-level",
                            ],
                            index=None,
                            key="4_1_framework_class",
                        )

                        if classification:

                            expected = (
                                "Low-level"
                                if framework_case in low_level
                                else "High-level"
                            )

                            if (
                                classification
                                == expected
                            ):
                                st.success(
                                    "정답입니다! ✅"
                                )

                            else:
                                st.error(
                                    "다시 확인해보세요."
                                )


                # -----------------------------------------
                # License
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_license"
                ):

                    render_surface_header(
                        "Framework와 License",
                        practice_4_1[
                            "activities"
                        ][1][
                            "instruction"
                        ],
                        label="ACTIVITY 02",
                    )

                    license_framework = st.selectbox(
                        "Framework",
                        [
                            "선택하세요",
                            "Nano-X",
                            "DirectFB",
                            "KDrive",
                            "SDL",
                            "Gtk",
                            "QT",
                            "FLTK",
                            "MiniGUI",
                        ],
                        key="4_1_license_framework",
                    )

                    license_answers = {
                        "Nano-X": (
                            "Mozilla Public License"
                        ),
                        "DirectFB": "LGPL",
                        "KDrive": "X11 License",
                        "SDL": "LGPL",
                        "Gtk": "GPL",
                        "QT": "GPL",
                        "FLTK": "LGPL",
                        "MiniGUI": "GPL",
                    }

                    if (
                        license_framework
                        != "선택하세요"
                    ):

                        answer = st.selectbox(
                            "License",
                            [
                                "선택하세요",
                                "Mozilla Public License",
                                "LGPL",
                                "X11 License",
                                "GPL",
                            ],
                            key="4_1_license_answer",
                        )

                        if answer != "선택하세요":

                            if (
                                answer
                                == license_answers[
                                    license_framework
                                ]
                            ):
                                st.success(
                                    "정답입니다! ✅"
                                )

                            else:
                                st.error(
                                    "Framework와 License를 "
                                    "다시 확인해보세요."
                                )


                # -----------------------------------------
                # Qt Designer
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_designer"
                ):

                    render_surface_header(
                        "Qt Designer",
                        practice_4_1[
                            "activities"
                        ][2][
                            "instruction"
                        ],
                        label="ACTIVITY 03",
                    )

                    designer_question = st.radio(
                        (
                            "Qt Designer 실습에서 선택하는 "
                            "Form Type은?"
                        ),
                        [
                            "Dialog without Buttons",
                            "Main Window only",
                            "Console Application",
                        ],
                        index=None,
                        key="4_1_designer_question",
                    )

                    if (
                        designer_question
                        == "Dialog without Buttons"
                    ):
                        st.success(
                            "정답입니다! ✅"
                        )

                    elif designer_question:
                        st.error(
                            "학습모듈 실습 Form Type을 "
                            "다시 확인해보세요."
                        )


                # -----------------------------------------
                # Interface 구분
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_interface"
                ):

                    render_surface_header(
                        "User / Module Interface 구분",
                        practice_4_1[
                            "activities"
                        ][3][
                            "instruction"
                        ],
                        label="ACTIVITY 04",
                    )

                    interface_case = st.selectbox(
                        "사례를 선택하세요.",
                        [
                            "선택하세요",
                            "사용자가 Button을 누른다.",
                            "화면에 상태 Message를 출력한다.",
                            "함수 Parameter로 Sensor 값을 전달한다.",
                            "함수 Return Value를 다른 Module에서 사용한다.",
                        ],
                        key="4_1_interface_case",
                    )

                    user_examples = {
                        "사용자가 Button을 누른다.",
                        "화면에 상태 Message를 출력한다.",
                    }

                    if interface_case != "선택하세요":

                        interface_answer = st.radio(
                            "어떤 Interface인가요?",
                            [
                                "User Interface",
                                "Module Interface",
                            ],
                            index=None,
                            key="4_1_interface_answer",
                        )

                        if interface_answer:

                            expected = (
                                "User Interface"
                                if interface_case
                                in user_examples
                                else "Module Interface"
                            )

                            if (
                                interface_answer
                                == expected
                            ):
                                st.success(
                                    "정답입니다! ✅"
                                )

                            else:
                                st.error(
                                    "다시 판단해보세요."
                                )


        # =================================================
        # ⑩ 형성평가
        # =================================================

        if formative_tab_4_1.open:

            with formative_tab_4_1:

                render_quiz(
                    FORMATIVE_QUIZ_4_1,
                    title="✅ 4-1 형성평가",
                    description=(
                        "Embedded GUI, Framework, License, "
                        "QT, PyQt, Qt Designer와 "
                        "Interface 구현 내용을 확인합니다."
                    ),
                )


        # =================================================
        # ⑪ 중간고사
        # =================================================

        if exam_tab_4_1.open:

            with exam_tab_4_1:

                render_exam_practice(
                    EXAM_PRACTICE_4_1
                )


        if is_section_completed(
            "4-1"
        ):

            st.success(
                "✅ 4-1 학습 완료"
            )


# =========================================================
# 4-2
# =========================================================

if lesson_tab_2.open:

    with lesson_tab_2:

        st.markdown(
            f"## {metadata_4_2['section']}. "
            f"{metadata_4_2['title']}"
        )

        st.caption(
            "CVS · SVN · GIT의 Version Control 방식을 비교하고 "
            "Repository, Commit, Configuration Management와 "
            "CASE Tool을 학습합니다."
        )


        # -------------------------------------------------
        # 학습 목표
        # -------------------------------------------------

        with st.container(
            key="edu_section_4_2_objectives"
        ):

            render_surface_header(
                "학습 목표",
                (
                    "Source Code의 Version과 변경 이력을 "
                    "체계적으로 관리하는 방법을 이해합니다."
                ),
                label="LEARNING GOALS",
            )

            for objective in LESSON_4_2[
                "objectives"
            ]:
                st.markdown(
                    f"- {objective}"
                )


        # -------------------------------------------------
        # 내부 탭
        # -------------------------------------------------

        (
            version_tab,
            type_tab,
            vcs_tab,
            github_tab,
            repository_tab,
            svn_practice_tab,
            collaboration_tab,
            configuration_tab,
            case_tab,
            arduino_tab_4_2,
            practice_tab_4_2,
            formative_tab_4_2,
            exam_tab_4_2,
        ) = st.tabs(
            [
                "① Version Control",
                "② 중앙형 · 분산형",
                "③ CVS · SVN · GIT",
                "④ GitHub",
                "⑤ Repository",
                "⑥ SVN 실습",
                "⑦ 협업",
                "⑧ Configuration",
                "⑨ CASE",
                "⑩ Arduino · Git",
                "⑪ 개념 체험",
                "⑫ 형성평가",
                "⑬ 중간고사 대비",
            ],
            key="lesson_4_2_inner_tabs",
            on_change="rerun",
        )


        # =================================================
        # ① Version Control
        # =================================================

        if version_tab.open:

            with version_tab:

                st.markdown(
                    "## Version Control"
                )


                with st.container(
                    key="edu_section_version_core"
                ):

                    render_surface_header(
                        version_control_overview[
                            "title"
                        ],
                        version_control_overview[
                            "definition"
                        ],
                        label="VERSION CONTROL",
                    )


                # -----------------------------------------
                # 필요성
                # -----------------------------------------

                with st.container(
                    key="edu_section_version_needed"
                ):

                    render_surface_header(
                        "왜 Version Control이 필요한가?",
                        (
                            "변경 이력, 복구, 협업, 결과물 관리를 "
                            "체계적으로 수행할 수 있습니다."
                        ),
                        label="WHY",
                    )

                    for item in version_control_overview[
                        "why_needed"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                # -----------------------------------------
                # 관리 대상
                # -----------------------------------------

                with st.container(
                    key="edu_section_version_items"
                ):

                    render_surface_header(
                        "Version 관리 대상",
                        (
                            "Source Code만 관리하는 것이 아닙니다."
                        ),
                        label="MANAGED ITEM",
                    )

                    render_pills(
                        version_control_overview[
                            "managed_items"
                        ]
                    )


                # -----------------------------------------
                # 기본 용어
                # -----------------------------------------

                with st.container(
                    key="edu_section_version_terms"
                ):

                    render_surface_header(
                        "기본 용어",
                        (
                            "Repository · Commit · Update · "
                            "Working Copy를 구분합니다."
                        ),
                        label="TERMS",
                    )

                    terms = version_control_overview[
                        "basic_terms"
                    ]

                    for start in range(
                        0,
                        len(terms),
                        2,
                    ):

                        current = terms[
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

                                render_feature(
                                    item[
                                        "term"
                                    ],
                                    item[
                                        "description"
                                    ],
                                )


                render_exam_panel(
                    version_control_overview[
                        "exam_points"
                    ]
                )


        # =================================================
        # ② 중앙 / 분산
        # =================================================

        if type_tab.open:

            with type_tab:

                st.markdown(
                    "## Version Control System의 유형"
                )


                centralized = version_control_types[
                    "centralized"
                ]

                distributed = version_control_types[
                    "distributed"
                ]


                with st.container(
                    key="edu_section_version_types"
                ):

                    render_surface_header(
                        version_control_types[
                            "title"
                        ],
                        (
                            "Repository를 관리하는 위치와 "
                            "작업 방식에 따라 구분할 수 있습니다."
                        ),
                        label="ARCHITECTURE",
                    )


                    col1, col2 = st.columns(
                        2
                    )

                    with col1:

                        render_version_compare(
                            centralized[
                                "title"
                            ],
                            "Central Repository",
                            centralized[
                                "characteristics"
                            ],
                        )

                        render_pills(
                            centralized[
                                "examples"
                            ]
                        )


                    with col2:

                        render_version_compare(
                            distributed[
                                "title"
                            ],
                            "Local Repository",
                            distributed[
                                "characteristics"
                            ],
                        )

                        render_pills(
                            distributed[
                                "examples"
                            ]
                        )


                # -----------------------------------------
                # 비교
                # -----------------------------------------

                with st.container(
                    key="edu_section_version_type_compare"
                ):

                    render_surface_header(
                        "중앙 집중형 vs 분산형",
                        (
                            "Repository 구조와 Network 의존성, "
                            "대표 시스템을 한눈에 비교합니다."
                        ),
                        label="COMPARISON",
                    )

                    render_html(
                        """
                        <div style="
                            display:grid;
                            grid-template-columns:1.2fr 2fr 2fr;
                            gap:0;
                            overflow:hidden;

                            border:1px solid #e2e7ef;
                            border-radius:13px;
                        ">

                            <div style="
                                padding:0.8rem 0.9rem;
                                background:#f4f5fa;
                                font-weight:800;
                                color:#172033;
                            ">
                                비교 항목
                            </div>

                            <div style="
                                padding:0.8rem 0.9rem;
                                background:#f4f5fa;
                                font-weight:800;
                                color:#172033;
                            ">
                                Centralized
                            </div>

                            <div style="
                                padding:0.8rem 0.9rem;
                                background:#f4f5fa;
                                font-weight:800;
                                color:#172033;
                            ">
                                Distributed
                            </div>

                            <div style="
                                padding:0.9rem;
                                border-top:1px solid #e7eaf1;
                                font-weight:750;
                            ">
                                Repository
                            </div>

                            <div style="
                                padding:0.9rem;
                                border-top:1px solid #e7eaf1;
                                color:#4c5a6d;
                            ">
                                중앙 Repository 중심
                            </div>

                            <div style="
                                padding:0.9rem;
                                border-top:1px solid #e7eaf1;
                                color:#4c5a6d;
                            ">
                                각 개발자가 Repository 정보를 보유
                            </div>

                            <div style="
                                padding:0.9rem;
                                border-top:1px solid #e7eaf1;
                                font-weight:750;
                            ">
                                Network 의존
                            </div>

                            <div style="
                                padding:0.9rem;
                                border-top:1px solid #e7eaf1;
                                color:#4c5a6d;
                            ">
                                상대적으로 큼
                            </div>

                            <div style="
                                padding:0.9rem;
                                border-top:1px solid #e7eaf1;
                                color:#4c5a6d;
                            ">
                                Local 작업 가능
                            </div>

                            <div style="
                                padding:0.9rem;
                                border-top:1px solid #e7eaf1;
                                font-weight:750;
                            ">
                                대표 시스템
                            </div>

                            <div style="
                                padding:0.9rem;
                                border-top:1px solid #e7eaf1;
                                color:#4c5a6d;
                            ">
                                CVS · SVN
                            </div>

                            <div style="
                                padding:0.9rem;
                                border-top:1px solid #e7eaf1;
                                color:#4c5a6d;
                            ">
                                GIT
                            </div>

                        </div>
                        """
                    )

                    render_surface_header(
                        "중앙 집중형 vs 분산형",
                        (
                            "Repository와 Network 의존성을 "
                            "비교합니다."
                        ),
                        label="COMPARISON",
                    )

                    for item in version_control_types[
                        "comparison"
                    ]:

                        category_col, central_col, distributed_col = (
                            st.columns(
                                [1.5, 3, 3]
                            )
                        )

                        with category_col:
                            st.markdown(
                                f"**{item['category']}**"
                            )

                        with central_col:
                            st.write(
                                item[
                                    "centralized"
                                ]
                            )

                        with distributed_col:
                            st.write(
                                item[
                                    "distributed"
                                ]
                            )


                render_exam_panel(
                    version_control_types[
                        "exam_points"
                    ]
                )


        # =================================================
        # ③ CVS / SVN / GIT
        # =================================================

        if vcs_tab.open:

            with vcs_tab:

                st.markdown(
                    "## CVS · SVN · GIT 비교"
                )

                st.caption(
                    "시험에서 가장 중요한 Version Control "
                    "비교 영역입니다."
                )


                with st.container(
                    key="edu_section_vcs_compare"
                ):

                    render_surface_header(
                        "세 가지 Version Control System",
                        (
                            "관리 방식과 관리 단위, 지원 File의 "
                            "차이를 비교합니다."
                        ),
                        label="VCS COMPARISON",
                    )


                    cvs_col, svn_col, git_col = st.columns(
                        3
                    )


                    with cvs_col:

                        with st.container(
                            key="edu_subsection_cvs"
                        ):

                            st.markdown(
                                "### CVS"
                            )

                            st.caption(
                                cvs[
                                    "full_name"
                                ]
                            )

                            st.write(
                                cvs[
                                    "definition"
                                ]
                            )

                            st.markdown(
                                f"**관리 단위:** "
                                f"{cvs['management_unit']}"
                            )

                            st.markdown(
                                f"**File:** "
                                f"{cvs['file_support']}"
                            )


                    with svn_col:

                        with st.container(
                            key="edu_subsection_svn"
                        ):

                            st.markdown(
                                "### SVN"
                            )

                            st.caption(
                                svn[
                                    "full_name"
                                ]
                            )

                            st.write(
                                svn[
                                    "definition"
                                ]
                            )

                            st.markdown(
                                f"**관리 단위:** "
                                f"{svn['management_unit']}"
                            )

                            st.markdown(
                                f"**File:** "
                                f"{svn['file_support']}"
                            )


                    with git_col:

                        with st.container(
                            key="edu_subsection_git"
                        ):

                            st.markdown(
                                "### GIT"
                            )

                            st.caption(
                                "Distributed Version Control"
                            )

                            st.write(
                                git[
                                    "definition"
                                ]
                            )

                            st.markdown(
                                f"**관리 방식:** "
                                f"{git['management_unit']}"
                            )

                            st.markdown(
                                "**Repository:** Local Copy"
                            )


                # -----------------------------------------
                # 핵심 비교표
                # -----------------------------------------

                with st.container(
                    key="edu_section_vcs_summary"
                ):

                    render_surface_header(
                        "시험 핵심 비교",
                        (
                            "CVS · SVN · GIT의 차이를 "
                            "최소 키워드로 기억합니다."
                        ),
                        label="EXAM MEMORY",
                    )

                    render_html(
                        """
                        <div style="
                            display:grid;
                            grid-template-columns:1fr 1fr 1fr;
                            gap:0.75rem;
                        ">

                            <div style="
                                padding:1rem;
                                background:#f8f9fc;
                                border:1px solid #e7eaf1;
                                border-radius:13px;
                            ">
                                <div style="font-weight:800;margin-bottom:0.45rem;">
                                    CVS
                                </div>
                                <div style="font-size:0.86rem;color:#4c5a6d;">
                                    중앙 집중형<br>
                                    개별 File<br>
                                    ASCII 중심
                                </div>
                            </div>

                            <div style="
                                padding:1rem;
                                background:#f8f9fc;
                                border:1px solid #e7eaf1;
                                border-radius:13px;
                            ">
                                <div style="font-weight:800;margin-bottom:0.45rem;">
                                    SVN
                                </div>
                                <div style="font-size:0.86rem;color:#4c5a6d;">
                                    중앙 집중형<br>
                                    작업 단위<br>
                                    ASCII + Binary
                                </div>
                            </div>

                            <div style="
                                padding:1rem;
                                background:#f8f9fc;
                                border:1px solid #e7eaf1;
                                border-radius:13px;
                            ">
                                <div style="font-weight:800;margin-bottom:0.45rem;">
                                    GIT
                                </div>
                                <div style="font-size:0.86rem;color:#4c5a6d;">
                                    분산형<br>
                                    Snapshot<br>
                                    Repository Local Copy
                                </div>
                            </div>

                        </div>
                        """
                    )


                # -----------------------------------------
                # 각 특징
                # -----------------------------------------

                with st.expander(
                    "CVS 특징 자세히 보기"
                ):
                    for item in cvs[
                        "characteristics"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )

                with st.expander(
                    "SVN 특징 자세히 보기"
                ):
                    for item in svn[
                        "characteristics"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )

                with st.expander(
                    "GIT 특징 자세히 보기"
                ):
                    for item in git[
                        "characteristics"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                render_exam_panel(
                    [
                        *cvs[
                            "exam_points"
                        ],
                        *svn[
                            "exam_points"
                        ],
                        *git[
                            "exam_points"
                        ],
                    ]
                )


        # =================================================
        # ④ GitHub
        # =================================================

        if github_tab.open:

            with github_tab:

                st.markdown(
                    "## GIT과 GitHub"
                )


                with st.container(
                    key="edu_section_github_core"
                ):

                    render_surface_header(
                        github[
                            "title"
                        ],
                        github[
                            "definition"
                        ],
                        label="REMOTE SERVICE",
                    )


                    git_col, github_col = st.columns(
                        2
                    )

                    comparison = github[
                        "git_vs_github"
                    ]


                    with git_col:

                        with st.container(
                            key="edu_subsection_git_compare"
                        ):

                            render_feature(
                                comparison[0][
                                    "name"
                                ],
                                comparison[0][
                                    "description"
                                ],
                            )


                    with github_col:

                        with st.container(
                            key="edu_subsection_github_compare"
                        ):

                            render_feature(
                                comparison[1][
                                    "name"
                                ],
                                comparison[1][
                                    "description"
                                ],
                            )


                st.info(
                    github[
                        "important_point"
                    ]
                )


                with st.container(
                    key="edu_section_github_uses"
                ):

                    render_surface_header(
                        "GitHub 활용",
                        (
                            "Remote Repository 저장과 협업에 "
                            "활용할 수 있습니다."
                        ),
                        label="USE CASE",
                    )

                    render_pills(
                        github[
                            "uses"
                        ]
                    )


                render_exam_panel(
                    github[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑤ Repository
        # =================================================

        if repository_tab.open:

            with repository_tab:

                st.markdown(
                    "## Repository"
                )


                with st.container(
                    key="edu_section_repository_core"
                ):

                    render_surface_header(
                        repository[
                            "title"
                        ],
                        repository[
                            "definition"
                        ],
                        label="REPOSITORY",
                    )


                with st.container(
                    key="edu_section_repository_types"
                ):

                    render_surface_header(
                        "Repository 유형",
                        (
                            "Central · Local · Remote Repository를 "
                            "구분합니다."
                        ),
                        label="TYPE",
                    )

                    cols = st.columns(
                        3
                    )

                    for col, item in zip(
                        cols,
                        repository[
                            "types"
                        ],
                    ):

                        with col:

                            with st.container(
                                key=(
                                    "edu_subsection_repo_"
                                    f"{item['name']}"
                                )
                            ):

                                render_feature(
                                    item[
                                        "name"
                                    ],
                                    item[
                                        "description"
                                    ],
                                )


                with st.container(
                    key="edu_section_repository_flow"
                ):

                    render_surface_header(
                        "Version 저장 흐름",
                        (
                            "Source 작성부터 Repository에 "
                            "변경 이력이 쌓이는 과정을 확인합니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        repository[
                            "repository_flow"
                        ]
                    )


                render_exam_panel(
                    repository[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑥ SVN 실습
        # =================================================

        if svn_practice_tab.open:

            with svn_practice_tab:

                st.markdown(
                    "## SVN Source Code 관리 실습"
                )


                with st.container(
                    key="edu_section_svn_practice_core"
                ):

                    render_surface_header(
                        svn_practice[
                            "title"
                        ],
                        svn_practice[
                            "purpose"
                        ],
                        label="SVN PRACTICE",
                    )

                    render_concept(
                        "실습 Source File",
                        svn_practice[
                            "source_file"
                        ],
                    )


                # -----------------------------------------
                # Process
                # -----------------------------------------

                with st.container(
                    key="edu_section_svn_process"
                ):

                    render_surface_header(
                        "SVN 실습 흐름",
                        (
                            "Working Copy에서 Source를 수정하고 "
                            "Commit하여 Repository에 반영합니다."
                        ),
                        label="PROCESS",
                    )

                    render_process(
                        [
                            item[
                                "title"
                            ]
                            for item in svn_practice[
                                "procedure"
                            ]
                        ]
                    )

                    with st.expander(
                        "단계별 설명 보기"
                    ):

                        for item in svn_practice[
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
                                "file"
                            ):
                                st.code(
                                    item[
                                        "file"
                                    ]
                                )


                # -----------------------------------------
                # Commit
                # -----------------------------------------

                commit = svn_practice[
                    "commit"
                ]

                with st.container(
                    key="edu_section_commit"
                ):

                    render_surface_header(
                        "Commit",
                        commit[
                            "definition"
                        ],
                        label="CORE TERM",
                    )

                    st.info(
                        commit[
                            "important_point"
                        ]
                    )


                render_exam_panel(
                    svn_practice[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑦ 협업
        # =================================================

        if collaboration_tab.open:

            with collaboration_tab:

                st.markdown(
                    "## Version Control과 협업"
                )


                with st.container(
                    key="edu_section_collaboration_core"
                ):

                    render_surface_header(
                        collaboration[
                            "title"
                        ],
                        collaboration[
                            "definition"
                        ],
                        label="COLLABORATION",
                    )


                with st.container(
                    key="edu_section_collaboration_flow"
                ):

                    render_surface_header(
                        "협업 Workflow",
                        (
                            "Repository 준비부터 Integration과 "
                            "Test까지의 흐름입니다."
                        ),
                        label="WORKFLOW",
                    )

                    render_process(
                        collaboration[
                            "workflow"
                        ]
                    )


                with st.container(
                    key="edu_section_collaboration_points"
                ):

                    render_surface_header(
                        "협업 시 주의 사항",
                        (
                            "Version Control을 사용해도 "
                            "팀 규칙이 필요합니다."
                        ),
                        label="CHECK POINT",
                    )

                    for item in collaboration[
                        "important_points"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                render_exam_panel(
                    collaboration[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑧ Configuration Management
        # =================================================

        if configuration_tab.open:

            with configuration_tab:

                st.markdown(
                    "## Software Configuration Management"
                )


                with st.container(
                    key="edu_section_configuration_core"
                ):

                    render_surface_header(
                        configuration_management[
                            "title"
                        ],
                        configuration_management[
                            "definition"
                        ],
                        label="CONFIGURATION MANAGEMENT",
                    )


                # -----------------------------------------
                # Configuration Item
                # -----------------------------------------

                with st.container(
                    key="edu_section_configuration_items"
                ):

                    render_surface_header(
                        "Configuration Item",
                        (
                            "Source Code뿐 아니라 Document, Library, "
                            "Build File, Test 결과도 관리 대상입니다."
                        ),
                        label="CI",
                    )

                    render_pills(
                        configuration_management[
                            "configuration_items"
                        ]
                    )


                # -----------------------------------------
                # 주요 활동
                # -----------------------------------------

                with st.container(
                    key="edu_section_configuration_activities"
                ):

                    render_surface_header(
                        "Configuration Management 활동",
                        (
                            "식별 → Version 관리 → 변경 통제 → "
                            "상태 관리의 관점으로 이해합니다."
                        ),
                        label="ACTIVITY",
                    )

                    activities = configuration_management[
                        "activities"
                    ]

                    for start in range(
                        0,
                        len(activities),
                        2,
                    ):

                        current = activities[
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

                                render_feature(
                                    item[
                                        "name"
                                    ],
                                    item[
                                        "description"
                                    ],
                                )


                # -----------------------------------------
                # 목적
                # -----------------------------------------

                with st.container(
                    key="edu_section_configuration_purpose"
                ):

                    render_surface_header(
                        "Configuration Management의 목적",
                        (
                            "변경과 Version을 통제하여 "
                            "Software Quality를 유지합니다."
                        ),
                        label="PURPOSE",
                    )

                    render_pills(
                        configuration_management[
                            "purpose"
                        ]
                    )


                render_exam_panel(
                    configuration_management[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑨ CASE
        # =================================================

        if case_tab.open:

            with case_tab:

                st.markdown(
                    "## CASE Tool"
                )


                with st.container(
                    key="edu_section_case_core"
                ):

                    render_surface_header(
                        case_tools[
                            "title"
                        ],
                        case_tools[
                            "definition"
                        ],
                        label=case_tools[
                            "full_name"
                        ],
                    )


                # -----------------------------------------
                # 개발 단계
                # -----------------------------------------

                with st.container(
                    key="edu_section_case_stages"
                ):

                    render_surface_header(
                        "지원 가능한 개발 단계",
                        (
                            "CASE는 특정 한 단계만을 의미하지 않습니다."
                        ),
                        label="DEVELOPMENT LIFE CYCLE",
                    )

                    render_process(
                        case_tools[
                            "development_stages"
                        ]
                    )


                # -----------------------------------------
                # 역할
                # -----------------------------------------

                with st.container(
                    key="edu_section_case_roles"
                ):

                    render_surface_header(
                        "CASE Tool의 역할",
                        (
                            "개발, 문서, Modeling, Source, "
                            "Project와 Quality 관리를 지원합니다."
                        ),
                        label="ROLE",
                    )

                    render_pills(
                        case_tools[
                            "roles"
                        ]
                    )


                # -----------------------------------------
                # 장점
                # -----------------------------------------

                with st.container(
                    key="edu_section_case_benefits"
                ):

                    render_surface_header(
                        "CASE 활용 효과",
                        (
                            "자동화와 체계적인 결과물 관리로 "
                            "생산성과 품질 향상을 지원합니다."
                        ),
                        label="BENEFIT",
                    )

                    for item in case_tools[
                        "benefits"
                    ]:
                        st.markdown(
                            f"- {item}"
                        )


                render_exam_panel(
                    case_tools[
                        "exam_points"
                    ]
                )


        # =================================================
        # ⑩ Arduino / Git
        # =================================================

        if arduino_tab_4_2.open:

            with arduino_tab_4_2:

                st.markdown(
                    "## NCS Version Control과 Arduino 프로젝트 연결"
                )


                with st.container(
                    key="edu_section_arduino_mapping_4_2"
                ):

                    render_surface_header(
                        arduino_mapping_4_2[
                            "title"
                        ],
                        arduino_mapping_4_2[
                            "note"
                        ],
                        label="ARDUINO + GIT",
                    )


                    mapping = arduino_mapping_4_2[
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

                        for index, (
                            col,
                            item,
                        ) in enumerate(
                            zip(
                                cols,
                                current,
                            )
                        ):

                            with col:

                                with st.container(
                                    key=(
                                        "edu_subsection_arduino42_"
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
                # Version Timeline
                # -----------------------------------------

                project = arduino_mapping_4_2[
                    "project_example"
                ]

                with st.container(
                    key="edu_section_arduino_versions"
                ):

                    render_surface_header(
                        project[
                            "project"
                        ],
                        (
                            "기능이 추가될 때마다 Version을 "
                            "남기는 예시입니다."
                        ),
                        label="VERSION HISTORY",
                    )

                    render_process(
                        [
                            item[
                                "version"
                            ]
                            for item in project[
                                "versions"
                            ]
                        ]
                    )

                    for item in project[
                        "versions"
                    ]:

                        st.markdown(
                            f"**{item['version']}** "
                            f"— {item['change']}"
                        )


                # -----------------------------------------
                # Git Flow
                # -----------------------------------------

                with st.container(
                    key="edu_section_arduino_git_flow"
                ):

                    render_surface_header(
                        "Arduino Git Workflow",
                        (
                            "Project Folder를 Repository로 관리하는 "
                            "기본 흐름입니다."
                        ),
                        label="WORKFLOW",
                    )

                    render_process(
                        arduino_mapping_4_2[
                            "git_example_flow"
                        ]
                    )


                st.warning(
                    arduino_mapping_4_2[
                        "important_distinction"
                    ]
                )


        # =================================================
        # ⑪ 개념 체험
        # =================================================

        if practice_tab_4_2.open:

            with practice_tab_4_2:

                st.markdown(
                    "## Version Control 개념 체험"
                )


                # -----------------------------------------
                # VCS 분류
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_vcs_type"
                ):

                    render_surface_header(
                        "중앙 집중형 · 분산형",
                        practice_4_2[
                            "activities"
                        ][1][
                            "instruction"
                        ],
                        label="ACTIVITY 01",
                    )

                    vcs_name = st.selectbox(
                        "Version Control System",
                        [
                            "선택하세요",
                            "CVS",
                            "SVN",
                            "GIT",
                        ],
                        key="4_2_vcs_name",
                    )

                    if vcs_name != "선택하세요":

                        vcs_type = st.radio(
                            "어떤 방식인가요?",
                            [
                                "중앙 집중형",
                                "분산형",
                            ],
                            index=None,
                            key="4_2_vcs_type",
                        )

                        expected = (
                            "분산형"
                            if vcs_name == "GIT"
                            else "중앙 집중형"
                        )

                        if vcs_type:

                            if vcs_type == expected:
                                st.success(
                                    "정답입니다! ✅"
                                )

                            else:
                                st.error(
                                    "다시 확인해보세요."
                                )


                # -----------------------------------------
                # 관리 단위
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_vcs_unit"
                ):

                    render_surface_header(
                        "CVS · SVN · GIT 특징",
                        practice_4_2[
                            "activities"
                        ][0][
                            "instruction"
                        ],
                        label="ACTIVITY 02",
                    )

                    unit_question = st.selectbox(
                        "설명을 선택하세요.",
                        [
                            "선택하세요",
                            "개별 File 단위",
                            "작업 단위",
                            "Snapshot 방식",
                        ],
                        key="4_2_unit_question",
                    )

                    unit_answers = {
                        "개별 File 단위": "CVS",
                        "작업 단위": "SVN",
                        "Snapshot 방식": "GIT",
                    }

                    if unit_question != "선택하세요":

                        unit_answer = st.selectbox(
                            "어떤 System인가요?",
                            [
                                "선택하세요",
                                "CVS",
                                "SVN",
                                "GIT",
                            ],
                            key="4_2_unit_answer",
                        )

                        if unit_answer != "선택하세요":

                            if (
                                unit_answer
                                == unit_answers[
                                    unit_question
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
                # Commit
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_commit"
                ):

                    render_surface_header(
                        "Commit 이해하기",
                        practice_4_2[
                            "activities"
                        ][2][
                            "instruction"
                        ],
                        label="ACTIVITY 03",
                    )

                    commit_question = st.radio(
                        (
                            "Working Copy에서 수정한 내용을 "
                            "Repository에 반영하는 작업은?"
                        ),
                        [
                            "Commit",
                            "Compile",
                            "Debug",
                            "Link",
                        ],
                        index=None,
                        key="4_2_commit_question",
                    )

                    if commit_question == "Commit":

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif commit_question:

                        st.error(
                            "Version Control 기본 용어를 "
                            "다시 확인해보세요."
                        )


                # -----------------------------------------
                # Git / GitHub
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_git_github"
                ):

                    render_surface_header(
                        "GIT과 GitHub 구분",
                        practice_4_2[
                            "activities"
                        ][3][
                            "instruction"
                        ],
                        label="ACTIVITY 04",
                    )

                    github_question = st.radio(
                        (
                            "GIT Repository를 Network 환경에서 "
                            "저장하고 공유하도록 지원하는 Service는?"
                        ),
                        [
                            "GitHub",
                            "GCC",
                            "GDB",
                            "Make",
                        ],
                        index=None,
                        key="4_2_github_question",
                    )

                    if github_question == "GitHub":

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif github_question:

                        st.error(
                            "GIT과 GitHub의 차이를 "
                            "다시 확인해보세요."
                        )


                # -----------------------------------------
                # CASE
                # -----------------------------------------

                with st.container(
                    key="edu_section_practice_case"
                ):

                    render_surface_header(
                        "CASE",
                        (
                            "CASE의 전체 이름을 "
                            "확인합니다."
                        ),
                        label="ACTIVITY 05",
                    )

                    case_question = st.radio(
                        "CASE의 전체 이름은?",
                        [
                            (
                                "Computer Aided "
                                "Software Engineering"
                            ),
                            (
                                "Computer Application "
                                "System Environment"
                            ),
                            (
                                "Central Application "
                                "Software Engine"
                            ),
                        ],
                        index=None,
                        key="4_2_case_question",
                    )

                    if case_question == (
                        "Computer Aided "
                        "Software Engineering"
                    ):

                        st.success(
                            "정답입니다! ✅"
                        )

                    elif case_question:

                        st.error(
                            "CASE의 전체 이름을 "
                            "다시 확인해보세요."
                        )


        # =================================================
        # ⑫ 형성평가
        # =================================================

        if formative_tab_4_2.open:

            with formative_tab_4_2:

                render_quiz(
                    FORMATIVE_QUIZ_4_2,
                    title="✅ 4-2 형성평가",
                    description=(
                        "Version Control, CVS/SVN/GIT, "
                        "GitHub, Repository, Configuration "
                        "Management와 CASE를 확인합니다."
                    ),
                )


        # =================================================
        # ⑬ 중간고사
        # =================================================

        if exam_tab_4_2.open:

            with exam_tab_4_2:

                render_exam_practice(
                    EXAM_PRACTICE_4_2
                )


        if is_section_completed(
            "4-2"
        ):

            st.success(
                "✅ 4-2 학습 완료"
            )


# =========================================================
# 학습 4 전체 완료
# =========================================================

if is_lesson_completed(
    "4"
):

    st.divider()

    st.success(
        "🎉 학습 4 · 애플리케이션 인터페이스 구현하기를 "
        "모두 완료했습니다!"
    )

    with st.expander(
        "📚 학습 4 핵심 내용 다시 보기"
    ):

        st.markdown(
            "### 4-1 핵심 정리"
        )

        render_summary(
            LESSON_4_1[
                "summary"
            ]
        )

        st.divider()

        st.markdown(
            "### 4-2 핵심 정리"
        )

        render_summary(
            LESSON_4_2[
                "summary"
            ]
        )