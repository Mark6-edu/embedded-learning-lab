from __future__ import annotations

from html import escape
from typing import Iterable, Sequence

import streamlit as st


# =========================================================
# 내부 공통 함수
# =========================================================

def _clean_items(items: Sequence[str] | None) -> list[str]:
    """빈 문자열을 제거하고 문자열 목록으로 정리한다."""
    if not items:
        return []

    return [
        str(item).strip()
        for item in items
        if str(item).strip()
    ]


# =========================================================
# 기본 페이지 UI
# =========================================================

def set_page_title(title: str) -> None:
    """페이지 제목을 출력한다."""
    st.title(title)


def render_breadcrumb(*items: str) -> None:
    """현재 학습 위치를 간단히 표시한다."""
    clean_items = [
        item.strip()
        for item in items
        if item and item.strip()
    ]

    if not clean_items:
        return

    st.caption(" › ".join(clean_items))


def render_section_header(
    title: str,
    subtitle: str | None = None,
) -> None:
    """
    학습 내용의 큰 Section 제목.

    페이지 내부에서 너무 많은 대제목이 생기지 않도록
    h2까지만 사용한다.
    """
    st.markdown(f"## {title}")

    if subtitle:
        st.caption(subtitle)


# =========================================================
# 학습 목표
# =========================================================

def render_learning_objectives(
    objectives: Sequence[str],
    title: str = "🎯 학습 목표",
) -> None:
    """
    학습 목표를 카드가 아닌 간결한 목록으로 표시한다.

    기존 pages/01~04와의 호환성을 위해
    함수 이름을 변경하지 않는다.
    """
    items = _clean_items(objectives)

    if not items:
        return

    st.markdown(f"### {title}")

    for objective in items:
        st.markdown(f"- {objective}")


def render_learning_objectives_checklist(
    objectives: Sequence[str],
    title: str = "🎯 학습 목표",
) -> None:
    """
    기존 리팩터링 코드와의 호환용 함수.

    render_learning_objectives와 동일한 방식으로 출력한다.
    """
    render_learning_objectives(
        objectives,
        title=title,
    )


# =========================================================
# 학습 카드
# =========================================================

def render_learning_card(
    title: str,
    description: str,
    tags: Iterable[str] | None = None,
) -> None:
    """
    정말 카드가 필요한 개념에만 사용하는 기본 카드.

    지나치게 큰 제목과 여백을 사용하지 않는다.
    """
    with st.container(border=True):
        st.markdown(f"**{title}**")
        st.write(description)

        if tags:
            clean_tags = [
                str(tag).strip()
                for tag in tags
                if str(tag).strip()
            ]

            if clean_tags:
                st.caption(
                    " · ".join(clean_tags)
                )


# =========================================================
# 핵심 이론
# =========================================================

def render_theory_box(
    title: str,
    content: str,
    source_note: str | None = None,
) -> None:
    """
    핵심 이론.

    모든 내용을 큰 카드로 감싸지 않고
    제목 + 본문 중심의 온라인 교과서 형태로 표시한다.
    """
    st.markdown(f"### {title}")
    st.write(content)

    if source_note:
        st.caption(source_note)


# =========================================================
# 쉬운 설명
# =========================================================

def render_easy_explanation(
    content: str,
    title: str = "쉽게 이해하기",
) -> None:
    """학생 눈높이 설명."""
    if not content:
        return

    st.info(
        f"💡 **{title}**\n\n{content}"
    )


# =========================================================
# 핵심 개념
# =========================================================

def render_key_points(
    points: Sequence[str],
    title: str = "🔑 핵심 개념",
) -> None:
    """
    핵심 개념을 카드 Grid가 아닌
    간결한 핵심 목록으로 보여준다.
    """
    items = _clean_items(points)

    if not items:
        return

    st.markdown(f"### {title}")

    for point in items:
        st.markdown(f"- {point}")


# =========================================================
# 시험 핵심
# =========================================================

def render_exam_points(
    points: Sequence[str],
    title: str = "🎯 중간고사 핵심 포인트",
) -> None:
    """
    시험 핵심은 하나의 강조 영역 안에서 보여준다.

    각각을 카드로 만들지 않는다.
    """
    items = _clean_items(points)

    if not items:
        return

    body = "\n".join(
        f"- {item}"
        for item in items
    )

    st.warning(
        f"**{title}**\n\n{body}"
    )


# =========================================================
# Arduino 연결
# =========================================================

def render_arduino_connection(
    content: str,
    title: str = "Arduino에서는 어떻게 연결될까?",
) -> None:
    """NCS 이론과 Arduino 프로젝트 연결."""
    if not content:
        return

    st.success(
        f"🤖 **{title}**\n\n{content}"
    )


# =========================================================
# 실습
# =========================================================

def render_practice_box(
    instruction: str,
    title: str = "미니 실습",
    hint: str | None = None,
) -> None:
    """학생 활동 안내."""
    st.markdown(f"### 🧪 {title}")
    st.write(instruction)

    if hint:
        st.caption(f"힌트 · {hint}")


# =========================================================
# 참고 / 주의
# =========================================================

def render_note(
    content: str,
    title: str = "참고",
) -> None:
    if not content:
        return

    st.info(
        f"ℹ️ **{title}**\n\n{content}"
    )


def render_warning(
    content: str,
    title: str = "주의",
) -> None:
    if not content:
        return

    st.warning(
        f"⚠️ **{title}**\n\n{content}"
    )


# =========================================================
# 학습 정리
# =========================================================

def render_summary(
    points: Sequence[str],
    title: str = "📝 오늘의 핵심 정리",
) -> None:
    """학습 정리를 번호 목록으로 표시한다."""
    items = _clean_items(points)

    if not items:
        return

    st.markdown(f"### {title}")

    for index, point in enumerate(
        items,
        start=1,
    ):
        st.markdown(
            f"**{index}.** {point}"
        )


# =========================================================
# 비교 UI
# =========================================================

def render_comparison_panel(
    left_title: str,
    left_items: Sequence[str],
    right_title: str,
    right_items: Sequence[str],
) -> None:
    """
    두 개념을 비교할 때만 사용하는 UI.

    예:
    Host vs Target
    RISC vs CISC
    Error vs Warning
    """
    left = _clean_items(left_items)
    right = _clean_items(right_items)

    col_left, col_arrow, col_right = st.columns(
        [5, 1, 5]
    )

    with col_left:
        with st.container(border=True):
            st.markdown(f"**{left_title}**")

            for item in left:
                st.markdown(f"- {item}")

    with col_arrow:
        st.markdown("")
        st.markdown("### →")

    with col_right:
        with st.container(border=True):
            st.markdown(f"**{right_title}**")

            for item in right:
                st.markdown(f"- {item}")


def render_comparison_cards(
    rows: Sequence[dict[str, str]],
    title: str = "비교",
) -> None:
    """
    과거 리팩터링 코드와의 호환용 비교 함수.

    2개 항목 비교에 맞춰 가볍게 출력한다.
    """
    if not rows:
        return

    st.markdown(f"### {title}")

    cols = st.columns(
        min(2, len(rows))
    )

    for index, row in enumerate(rows):
        with cols[index % len(cols)]:
            with st.container(border=True):
                for key, value in row.items():
                    st.caption(str(key))
                    st.markdown(f"**{value}**")


# =========================================================
# Badge / 짧은 항목
# =========================================================

def render_badge_row(
    items: Sequence[str],
    label: str | None = None,
) -> None:
    """
    Serial · Ethernet · JTAG · USB처럼
    짧은 용어를 한 줄로 보여준다.

    CSS Badge를 사용하지 않고 Markdown code 표현을 사용한다.
    """
    clean = _clean_items(items)

    if not clean:
        return

    if label:
        st.markdown(f"**{label}**")

    st.markdown(
        "  ".join(
            f"`{item}`"
            for item in clean
        )
    )


# =========================================================
# Compact Grid
# =========================================================

def render_compact_grid(
    items: Sequence[str | dict[str, str]],
    columns: int = 3,
    title: str | None = None,
) -> None:
    """
    짧은 분류 항목에만 사용하는 Compact Grid.

    학습 목표에는 사용하지 않는다.
    """
    if not items:
        return

    if title:
        st.markdown(f"### {title}")

    column_count = min(
        max(1, columns),
        len(items),
    )

    cols = st.columns(column_count)

    for index, item in enumerate(items):

        if isinstance(item, dict):
            label = (
                item.get("name")
                or item.get("title")
                or item.get("term")
                or item.get("label")
                or "개념"
            )

            description = (
                item.get("description")
                or item.get("meaning")
                or item.get("detail")
                or item.get("summary")
                or ""
            )

        else:
            label = str(item)
            description = ""

        with cols[index % column_count]:
            st.markdown(f"**{label}**")

            if description:
                st.caption(description)


# =========================================================
# 정의 카드
# =========================================================

def render_definition_cards(
    items: Sequence[dict[str, str]],
    title: str = "개념 정리",
    key_field: str = "name",
    value_field: str = "description",
) -> None:
    """용어 + 설명을 2열 정도로 정리한다."""
    if not items:
        return

    compact_items = [
        {
            "name": item.get(
                key_field,
                "",
            ),
            "description": item.get(
                value_field,
                "",
            ),
        }
        for item in items
    ]

    render_compact_grid(
        compact_items,
        columns=2,
        title=title,
    )


# =========================================================
# Process
# =========================================================

def render_process_flow(
    items: Sequence[str],
    label: str = "🔄 동작 과정",
) -> None:
    """
    순서가 중요한 내용을
    카드가 아닌 한 줄 Flow로 보여준다.
    """
    clean = _clean_items(items)

    if not clean:
        return

    st.markdown(f"### {label}")

    st.markdown(
        " **→** ".join(clean)
    )


def render_process_steps(
    steps: Sequence[str | dict[str, str]],
    title: str = "🔄 동작 과정",
    columns: int = 3,
) -> None:
    """
    기존 리팩터링 코드와의 호환.

    큰 카드 Grid 대신
    번호 + 제목 + 짧은 설명으로 출력한다.
    """
    if not steps:
        return

    st.markdown(f"### {title}")

    for index, step in enumerate(
        steps,
        start=1,
    ):

        if isinstance(step, dict):
            label = (
                step.get("title")
                or step.get("name")
                or step.get("label")
                or f"단계 {index}"
            )

            detail = (
                step.get("description")
                or step.get("detail")
                or ""
            )

        else:
            label = str(step)
            detail = ""

        st.markdown(
            f"**{index}. {label}**"
        )

        if detail:
            st.caption(detail)


# =========================================================
# 시험 Highlight
# =========================================================

def render_exam_highlight(
    title: str,
    items: Sequence[str],
) -> None:
    """시험 핵심 강조."""
    render_exam_points(
        items,
        title=title,
    )


def render_exam_strip(
    title: str,
    content: str,
) -> None:
    """한두 문장의 시험 핵심."""
    st.warning(
        f"🎯 **{title}**\n\n{content}"
    )


# =========================================================
# 용어 + 의미
# =========================================================

def render_term_with_meaning(
    terms: Sequence[dict[str, str]],
    title: str = "핵심 용어",
) -> None:
    """용어와 의미를 2열로 정리한다."""
    if not terms:
        return

    formatted = []

    for item in terms:
        formatted.append(
            {
                "name": (
                    item.get("term")
                    or item.get("name")
                    or item.get("title")
                    or "용어"
                ),
                "description": (
                    item.get("meaning")
                    or item.get("description")
                    or item.get("detail")
                    or ""
                ),
            }
        )

    render_compact_grid(
        formatted,
        columns=2,
        title=title,
    )


# =========================================================
# Code / Command
# =========================================================

def render_code_panel(
    title: str,
    code: str,
    language: str = "text",
) -> None:
    st.markdown(f"**{title}**")
    st.code(
        code,
        language=language,
    )


def render_command_card(
    command: str,
    description: str,
) -> None:
    """
    명령어는 별도 HTML Card 없이
    Streamlit 기본 Code UI를 사용한다.
    """
    st.code(
        command,
        language="bash",
    )

    if description:
        st.caption(description)


# =========================================================
# Warning / Summary 호환 함수
# =========================================================

def render_warning_box(
    content: str,
    title: str = "주의사항",
) -> None:
    render_warning(
        content,
        title=title,
    )


def render_summary_box(
    content: str,
    title: str = "요약",
) -> None:
    st.success(
        f"**{title}**\n\n{content}"
    )


# =========================================================
# 퀴즈 Preview
# =========================================================

def render_quiz_preview() -> None:
    """
    기존 페이지 호환성을 위해 유지한다.
    """
    st.info(
        "✅ 형성평가 영역입니다."
    )


# =========================================================
# 진도율
# =========================================================

def render_progress_bar(
    progress: float,
    label: str = "진도율",
    show_label: bool = True,
) -> None:
    """0~100 진도율 표시."""
    safe_progress = min(
        100.0,
        max(
            0.0,
            float(progress),
        ),
    )

    if show_label:
        st.caption(
            f"{label} · {safe_progress:.0f}%"
        )

    st.progress(
        int(safe_progress)
    )

def render_block_header(
    title: str,
    description: str | None = None,
    label: str | None = None,
) -> None:
    """
    큰 학습 영역 내부에서 사용하는
    공통 Section Header.
    """

    if label:
        st.markdown(
            f"""
            <div class="edu-block-label">
                {escape(label)}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class="edu-block-title">
            {escape(title)}
        </div>
        """,
        unsafe_allow_html=True,
    )

    if description:
        st.markdown(
            f"""
            <div class="edu-block-desc">
                {escape(description)}
            </div>
            """,
            unsafe_allow_html=True,
        )