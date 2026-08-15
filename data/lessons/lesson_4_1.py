from __future__ import annotations


# =========================================================
# 학습 4-1
# 환경 준비 후 인터페이스 구현
# =========================================================

LESSON_4_1 = {

    # =====================================================
    # 기본 정보
    # =====================================================

    "metadata": {
        "lesson": "학습 4",
        "section": "4-1",
        "title": "환경 준비 후 인터페이스 구현",
        "page_range": "NCS 학습모듈 기준",
        "ncs_module": "임베디드 애플리케이션 구현",
    },


    # =====================================================
    # 학습 목표
    # =====================================================

    "objectives": [
        (
            "임베디드 시스템에서 사용되는 GUI의 특징을 "
            "설명할 수 있다."
        ),
        (
            "대표적인 Embedded GUI Framework의 종류와 "
            "특징을 구분할 수 있다."
        ),
        (
            "GUI Framework의 License를 확인하고 "
            "개발 환경에 적절한 Framework를 선택할 수 있다."
        ),
        (
            "PyQt와 Qt Designer를 이용한 GUI 구현 환경을 "
            "설명할 수 있다."
        ),
        (
            "User Interface와 Module Interface의 개념을 "
            "구분하여 설명할 수 있다."
        ),
        (
            "인터페이스 구현을 위한 환경을 준비하고 "
            "요구사항에 맞게 Interface를 구현할 수 있다."
        ),
    ],


    # =====================================================
    # 1. Embedded GUI 개요
    # =====================================================

    "gui_overview": {

        "title": "Embedded GUI",

        "definition": (
            "GUI는 Graphic User Interface의 약자로, "
            "사용자가 문자 명령만 입력하는 방식이 아니라 "
            "Button, Icon, Menu, Window 등의 Graphic 요소를 "
            "이용하여 시스템과 상호작용할 수 있도록 하는 "
            "User Interface이다."
        ),

        "embedded_definition": (
            "Embedded GUI는 임베디드 시스템의 제한된 "
            "Hardware Resource와 Display 환경을 고려하여 "
            "구현되는 Graphic User Interface이다."
        ),

        "characteristics": [
            (
                "작고 제한된 Memory와 Processor Resource를 "
                "고려해야 한다."
            ),
            (
                "사용자가 쉽게 이해할 수 있도록 "
                "단순하고 직관적으로 구성해야 한다."
            ),
            (
                "빠른 응답성과 안정적인 동작이 중요하다."
            ),
            (
                "Embedded System의 Display Resolution과 "
                "Input Device를 고려해야 한다."
            ),
            (
                "불필요하게 무거운 기능을 줄이고 "
                "가볍게 동작하도록 구현해야 한다."
            ),
        ],

        "display_requirement": (
            "학습모듈에서는 Graphic Interface 환경의 예로 "
            "640 × 480 이상의 해상도를 고려한다."
        ),

        "fse": {
            "term": "FSE",
            "full_name": "Full Screen Environment",
            "description": (
                "Embedded System의 화면 전체를 Application이 "
                "사용하는 형태의 환경을 의미한다."
            ),
        },

        "design_points": [
            "Simple",
            "Intuitive",
            "Lightweight",
            "Stable",
        ],

        "exam_points": [
            "GUI는 Graphic User Interface의 약자이다.",
            (
                "Embedded GUI는 제한된 Hardware Resource를 "
                "고려하여 가볍고 안정적으로 구현해야 한다."
            ),
            (
                "사용자가 쉽게 사용할 수 있도록 "
                "단순하고 직관적인 Interface가 중요하다."
            ),
            (
                "FSE는 Full Screen Environment를 의미한다."
            ),
            (
                "학습모듈에서는 GUI 환경 예로 "
                "640 × 480 이상의 해상도를 고려한다."
            ),
        ],
    },


    # =====================================================
    # 2. GUI Framework
    # =====================================================

    "gui_frameworks": {

        "title": "Embedded GUI Framework",

        "definition": (
            "GUI Framework는 Window, Button, Menu, Text, "
            "Event 처리 등의 Graphic Interface 기능을 "
            "쉽게 구현할 수 있도록 제공되는 "
            "Software Framework이다."
        ),

        "low_level": [
            {
                "name": "Nano-X",
                "description": (
                    "소형 Embedded System에서 사용할 수 있도록 "
                    "가볍게 설계된 Graphic Window System이다."
                ),
            },
            {
                "name": "DirectFB",
                "description": (
                    "Linux Framebuffer를 기반으로 Graphic 기능을 "
                    "제공하는 Library이다."
                ),
            },
            {
                "name": "KDrive",
                "description": (
                    "Memory와 Resource 사용을 줄인 "
                    "소형 X Server 계열이다."
                ),
            },
            {
                "name": "SDL",
                "description": (
                    "Graphic, Audio, Input 기능을 제공하는 "
                    "Multimedia Library이다."
                ),
            },
        ],

        "high_level": [
            {
                "name": "Gtk",
                "description": (
                    "Widget 기반으로 GUI Application을 "
                    "구현할 수 있는 Graphic Toolkit이다."
                ),
            },
            {
                "name": "QT",
                "description": (
                    "다양한 Platform에서 사용할 수 있는 "
                    "GUI Application Framework이다."
                ),
            },
            {
                "name": "FLTK",
                "description": (
                    "비교적 가볍고 빠른 GUI Toolkit이다."
                ),
            },
            {
                "name": "MiniGUI",
                "description": (
                    "Embedded System 환경을 위한 "
                    "경량 GUI System이다."
                ),
            },
        ],

        "classification": {
            "low_level": [
                "Nano-X",
                "DirectFB",
                "KDrive",
                "SDL",
            ],
            "high_level": [
                "Gtk",
                "QT",
                "FLTK",
                "MiniGUI",
            ],
        },

        "selection_points": [
            "Target Hardware Resource",
            "Operating System",
            "Display Resolution",
            "GUI 기능 요구사항",
            "Development Language",
            "License",
            "Maintenance",
            "Development Tool 지원 여부",
        ],

        "exam_points": [
            (
                "Nano-X, DirectFB, KDrive, SDL은 "
                "Low-level 계열 GUI 기술로 구분할 수 있다."
            ),
            (
                "Gtk, QT, FLTK, MiniGUI는 "
                "High-level GUI Framework로 구분할 수 있다."
            ),
            (
                "GUI Framework 선정 시 기능뿐 아니라 "
                "License도 함께 확인해야 한다."
            ),
        ],
    },


    # =====================================================
    # 3. GUI Framework License
    # =====================================================

    "licenses": {

        "title": "GUI Framework와 License",

        "definition": (
            "Open Source GUI Framework를 사용하는 경우에는 "
            "Framework의 기능뿐 아니라 Software License를 "
            "확인하여 사용 조건을 검토해야 한다."
        ),

        "items": [
            {
                "framework": "Nano-X",
                "license": "Mozilla Public License",
            },
            {
                "framework": "DirectFB",
                "license": "LGPL",
            },
            {
                "framework": "KDrive",
                "license": "X11 License",
            },
            {
                "framework": "SDL",
                "license": "LGPL",
            },
            {
                "framework": "Gtk",
                "license": "GPL",
            },
            {
                "framework": "QT",
                "license": "GPL",
            },
            {
                "framework": "FLTK",
                "license": "LGPL",
            },
            {
                "framework": "MiniGUI",
                "license": "GPL",
            },
        ],

        "important_point": (
            "시험 범위에서는 학습모듈에 제시된 "
            "Framework와 License의 대응 관계를 그대로 "
            "기억하는 것이 중요하다."
        ),

        "exam_points": [
            "Nano-X → Mozilla Public License",
            "DirectFB → LGPL",
            "KDrive → X11 License",
            "SDL → LGPL",
            "Gtk → GPL",
            "QT → GPL",
            "FLTK → LGPL",
            "MiniGUI → GPL",
        ],
    },


    # =====================================================
    # 4. Nano-X
    # =====================================================

    "nano_x": {

        "title": "Nano-X",

        "definition": (
            "Nano-X는 Embedded System을 위해 설계된 "
            "경량 Graphic Window System이다."
        ),

        "features": [
            "작은 Memory 환경을 고려한다.",
            "Embedded System에 적합한 경량 구조를 가진다.",
            "Window와 Graphic 기능을 제공한다.",
            "Client / Server 구조로 사용할 수 있다.",
        ],

        "license": "Mozilla Public License",

        "exam_points": [
            (
                "Nano-X는 Embedded System에서 사용할 수 있는 "
                "경량 Graphic System이다."
            ),
            "Nano-X의 License는 Mozilla Public License이다.",
        ],
    },


    # =====================================================
    # 5. DirectFB
    # =====================================================

    "directfb": {

        "title": "DirectFB",

        "full_name": "Direct Frame Buffer",

        "definition": (
            "DirectFB는 Linux Framebuffer Device를 이용하여 "
            "Graphic 기능을 제공하는 Library이다."
        ),

        "features": [
            "Linux Framebuffer를 기반으로 한다.",
            "Graphic 출력 기능을 제공한다.",
            "Hardware Acceleration을 활용할 수 있다.",
            "Embedded Graphic Application 구현에 사용할 수 있다.",
        ],

        "license": "LGPL",

        "exam_points": [
            "DirectFB는 Linux Framebuffer 기반 Graphic Library이다.",
            "DirectFB의 License는 LGPL이다.",
        ],
    },


    # =====================================================
    # 6. GTK
    # =====================================================

    "gtk": {

        "title": "GTK",

        "definition": (
            "GTK는 다양한 Widget을 이용하여 GUI Application을 "
            "구현할 수 있도록 지원하는 Graphic Toolkit이다."
        ),

        "features": [
            "Widget 기반의 GUI를 구성할 수 있다.",
            "Button, Label, Window 등의 UI Component를 제공한다.",
            "Event 기반 Application을 구현할 수 있다.",
        ],

        "license": "GPL",

        "exam_points": [
            "GTK는 Widget 기반 GUI Toolkit이다.",
            "학습모듈 기준 GTK의 License는 GPL이다.",
        ],
    },


    # =====================================================
    # 7. QT
    # =====================================================

    "qt": {

        "title": "QT",

        "definition": (
            "QT는 GUI Application을 개발할 수 있도록 "
            "다양한 Widget, Event, Layout 등의 기능을 "
            "제공하는 Application Framework이다."
        ),

        "features": [
            "다양한 GUI Widget을 제공한다.",
            "Event 기반 Application 구현이 가능하다.",
            "Layout을 이용하여 화면 요소를 배치할 수 있다.",
            "다양한 Platform에서 Application을 개발할 수 있다.",
            "Qt Designer와 함께 사용할 수 있다.",
        ],

        "license": "GPL",

        "components": [
            "Widget",
            "Signal",
            "Slot",
            "Layout",
            "Event",
        ],

        "exam_points": [
            "QT는 GUI Application Framework이다.",
            "QT에서는 Widget과 Layout을 이용하여 GUI를 구성할 수 있다.",
            "QT의 License는 학습모듈 기준 GPL이다.",
            "Qt Designer를 이용하면 GUI 화면을 시각적으로 설계할 수 있다.",
        ],
    },


    # =====================================================
    # 8. PyQt
    # =====================================================

    "pyqt": {

        "title": "PyQt",

        "definition": (
            "PyQt는 Python에서 QT Framework를 사용할 수 있도록 "
            "제공되는 Python Binding이다."
        ),

        "features": [
            "Python으로 QT GUI Application을 구현할 수 있다.",
            "QT에서 제공하는 Widget을 사용할 수 있다.",
            "Qt Designer와 함께 사용할 수 있다.",
            ".ui File을 활용하여 GUI 구조를 관리할 수 있다.",
        ],

        "basic_flow": [
            "Qt Designer에서 UI 설계",
            ".ui File 저장",
            "Python Program에서 UI 사용",
            "Signal / Slot 연결",
            "Application 실행",
        ],

        "exam_points": [
            "PyQt는 Python에서 QT를 사용할 수 있도록 지원한다.",
            (
                "Qt Designer에서 만든 .ui File을 "
                "PyQt Application에서 활용할 수 있다."
            ),
        ],
    },


    # =====================================================
    # 9. Qt Designer
    # =====================================================

    "qt_designer": {

        "title": "Qt Designer",

        "definition": (
            "Qt Designer는 QT 기반 GUI 화면을 "
            "Drag & Drop 방식으로 설계할 수 있는 "
            "Graphic Interface 설계 도구이다."
        ),

        "project_type": "Dialog without Buttons",

        "widgets": [
            "Label",
            "Push Button",
            "Line Edit",
            "Text Edit",
            "Combo Box",
            "Check Box",
            "Radio Button",
        ],

        "procedure": [
            "Qt Designer 실행",
            "New Form 선택",
            "Dialog without Buttons 선택",
            "필요한 Widget 배치",
            "Widget의 Property 설정",
            "Signal / Slot 관계 확인",
            ".ui File 저장",
            "Application에서 .ui File 활용",
        ],

        "ui_file": {
            "extension": ".ui",
            "format": "XML",
            "description": (
                "Qt Designer에서 설계한 GUI 정보는 "
                ".ui 확장자의 File로 저장할 수 있으며, "
                "내부적으로 XML 형식으로 GUI 구조를 표현한다."
            ),
        },

        "xml_example": (
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
            "<ui version=\"4.0\">\n"
            "    <class>Dialog</class>\n"
            "    <widget class=\"QDialog\" name=\"Dialog\">\n"
            "    </widget>\n"
            "</ui>"
        ),

        "exam_points": [
            (
                "Qt Designer는 Drag & Drop 방식으로 "
                "GUI 화면을 설계할 수 있는 도구이다."
            ),
            (
                "학습모듈 실습에서는 "
                "`Dialog without Buttons`를 선택한다."
            ),
            ".ui File은 XML 형식으로 GUI 정보를 저장한다.",
            (
                "Qt Designer에서는 Label, Push Button 등 "
                "다양한 Widget을 배치할 수 있다."
            ),
        ],
    },


    # =====================================================
    # 10. Interface 구현
    # =====================================================

    "interface_implementation": {

        "title": "User Interface와 Module Interface 구현",

        "definition": (
            "Application Interface는 사용자와 프로그램 사이의 "
            "User Interface뿐 아니라 Program 내부 Module 사이에서 "
            "Data와 기능을 연결하는 Module Interface도 포함한다."
        ),

        "user_interface": {
            "title": "User Interface",
            "description": (
                "사용자가 Application과 상호작용할 수 있도록 "
                "입력과 출력 기능을 제공하는 Interface이다."
            ),
            "examples": [
                "Button",
                "Menu",
                "Text Input",
                "Display",
                "Status Message",
            ],
        },

        "module_interface": {
            "title": "Module Interface",
            "description": (
                "Program 내부의 서로 다른 Module 사이에서 "
                "함수 호출, Data 전달, 상태 공유 등이 "
                "가능하도록 정의하는 Interface이다."
            ),
            "examples": [
                "Function Parameter",
                "Return Value",
                "Shared Data",
                "Module API",
            ],
        },

        "environment_preparation": [
            "Target System 확인",
            "Operating System 확인",
            "Display 환경 확인",
            "Input Device 확인",
            "GUI Framework 선정",
            "Development Tool 설치",
            "Library 확인",
            "License 확인",
        ],

        "implementation_process": [
            "Interface 요구사항 확인",
            "사용자 입력과 출력 정의",
            "Module 간 Data 흐름 정의",
            "GUI Framework 선정",
            "개발 환경 준비",
            "GUI 화면 설계",
            "Event와 기능 연결",
            "Module Interface 연결",
            "실행 및 기능 확인",
            "오류 수정",
        ],

        "important_points": [
            "사용자가 쉽게 이해할 수 있도록 구성한다.",
            "Input과 Output의 의미를 명확하게 한다.",
            "Module 간 Data 형식을 일치시킨다.",
            "Event와 실제 기능의 연결을 확인한다.",
            "Target Hardware Resource를 고려한다.",
            "Interface 구현 후 실제 동작을 검증한다.",
        ],

        "exam_points": [
            (
                "User Interface는 사용자와 Application 사이의 "
                "상호작용을 지원한다."
            ),
            (
                "Module Interface는 Program 내부 Module 사이의 "
                "Data와 기능 연결을 지원한다."
            ),
            (
                "Interface 구현 전 Hardware, OS, GUI Framework, "
                "Development Tool 등의 환경을 준비해야 한다."
            ),
        ],
    },


    # =====================================================
    # 11. Arduino 연결
    # =====================================================

    "arduino_mapping": {

        "title": "NCS Interface와 Arduino 프로젝트 연결",

        "note": (
            "NCS 학습모듈에서는 GUI Framework와 QT 기반 "
            "Interface 구현을 다루지만, Arduino 프로젝트에서도 "
            "사용자 입력·출력과 Module 사이의 Interface를 "
            "비슷한 관점에서 이해할 수 있다."
        ),

        "mapping": [
            {
                "ncs": "User Interface",
                "arduino": "Button, LCD, LED, Buzzer",
            },
            {
                "ncs": "Input Widget",
                "arduino": "Button / Sensor 입력",
            },
            {
                "ncs": "Output Widget",
                "arduino": "LCD / LED / Buzzer 출력",
            },
            {
                "ncs": "Module Interface",
                "arduino": "함수 Parameter / Return Value",
            },
            {
                "ncs": "Event 처리",
                "arduino": "Button 입력 / Sensor 조건 처리",
            },
            {
                "ncs": "GUI 상태 표시",
                "arduino": "LCD / Serial Monitor 상태 표시",
            },
        ],

        "project_example": {
            "project": "Arduino 스마트 화분",
            "user_interface": [
                "Button",
                "LCD",
                "LED",
            ],
            "module_interface": [
                "Sensor Module → Control Module",
                "Control Module → Pump Module",
                "Control Module → Display Module",
            ],
        },

        "important_distinction": (
            "Arduino의 LCD와 Button은 QT GUI를 그대로 "
            "대체하는 것이 아니라, User Interface와 "
            "Module Interface의 개념을 학생이 실제 Hardware에서 "
            "체험하기 위한 연결 사례이다."
        ),
    },


    # =====================================================
    # 12. 미니 실습
    # =====================================================

    "practice": {

        "title": "GUI와 Interface 구현 미니 실습",

        "activities": [
            {
                "title": "Framework 분류하기",
                "instruction": (
                    "Nano-X, DirectFB, KDrive, SDL과 "
                    "Gtk, QT, FLTK, MiniGUI를 "
                    "Low-level / High-level로 구분한다."
                ),
            },
            {
                "title": "Framework와 License 연결하기",
                "instruction": (
                    "각 GUI Framework에 해당하는 "
                    "License를 올바르게 연결한다."
                ),
            },
            {
                "title": "Qt Designer 화면 구성하기",
                "instruction": (
                    "Dialog without Buttons에 "
                    "Label과 Push Button 등을 배치한다."
                ),
            },
            {
                "title": "User / Module Interface 구분하기",
                "instruction": (
                    "주어진 Interface 사례가 User Interface인지 "
                    "Module Interface인지 판단한다."
                ),
            },
            {
                "title": "Arduino Interface 분석하기",
                "instruction": (
                    "Arduino 프로젝트에서 Button, LCD, Sensor, "
                    "함수 사이의 관계를 Interface 관점에서 분석한다."
                ),
            },
        ],

        "example_questions": [
            {
                "question": (
                    "Nano-X의 License는?"
                ),
                "answer": "Mozilla Public License",
            },
            {
                "question": (
                    "DirectFB의 License는?"
                ),
                "answer": "LGPL",
            },
            {
                "question": (
                    "Qt Designer의 .ui File은 어떤 형식으로 "
                    "저장되는가?"
                ),
                "answer": "XML",
            },
            {
                "question": (
                    "Qt Designer 실습에서 선택하는 "
                    "Form Type은?"
                ),
                "answer": "Dialog without Buttons",
            },
            {
                "question": (
                    "사용자와 Application 사이의 상호작용을 "
                    "지원하는 Interface는?"
                ),
                "answer": "User Interface",
            },
            {
                "question": (
                    "Program 내부 Module 간 Data를 전달하는 "
                    "Interface는?"
                ),
                "answer": "Module Interface",
            },
        ],
    },


    # =====================================================
    # 13. 핵심 정리
    # =====================================================

    "summary": [
        (
            "GUI는 Graphic User Interface이며 Graphic 요소를 "
            "통해 사용자가 시스템과 상호작용하도록 한다."
        ),
        (
            "Embedded GUI는 제한된 Hardware Resource를 고려하여 "
            "단순하고 직관적이며 가볍고 안정적으로 구현해야 한다."
        ),
        (
            "FSE는 Full Screen Environment를 의미한다."
        ),
        (
            "Nano-X, DirectFB, KDrive, SDL은 "
            "Low-level GUI 기술로 구분할 수 있다."
        ),
        (
            "Gtk, QT, FLTK, MiniGUI는 "
            "High-level GUI Framework로 구분할 수 있다."
        ),
        (
            "Nano-X의 License는 Mozilla Public License이다."
        ),
        (
            "DirectFB와 SDL, FLTK의 License는 "
            "학습모듈 기준 LGPL이다."
        ),
        (
            "KDrive의 License는 X11 License이다."
        ),
        (
            "Gtk, QT, MiniGUI의 License는 "
            "학습모듈 기준 GPL이다."
        ),
        (
            "Nano-X는 Embedded System용 경량 Graphic System이다."
        ),
        (
            "DirectFB는 Linux Framebuffer를 기반으로 "
            "Graphic 기능을 제공한다."
        ),
        (
            "QT는 Widget, Layout, Event 등을 이용하여 "
            "GUI Application을 구현할 수 있다."
        ),
        (
            "PyQt는 Python에서 QT를 사용할 수 있도록 지원한다."
        ),
        (
            "Qt Designer는 Drag & Drop 방식으로 "
            "GUI 화면을 설계할 수 있다."
        ),
        (
            "Qt Designer 실습에서는 "
            "Dialog without Buttons를 사용할 수 있다."
        ),
        (
            ".ui File은 XML 형식으로 GUI 구조를 저장한다."
        ),
        (
            "User Interface는 사용자와 Application 사이의 "
            "상호작용을 지원한다."
        ),
        (
            "Module Interface는 Program 내부 Module 사이의 "
            "Data와 기능 연결을 지원한다."
        ),
        (
            "Interface 구현 전 Target, OS, GUI Framework, "
            "Development Tool, License 등을 확인해야 한다."
        ),
        (
            "Arduino 프로젝트에서도 Button, LCD 등의 User Interface와 "
            "함수 간 Data 전달 형태의 Module Interface를 "
            "연결하여 이해할 수 있다."
        ),
    ],
}