from __future__ import annotations

from utils.quiz import QuizQuestion


# =========================================================
# 학습 4-1 형성평가
# 환경 준비 후 인터페이스 구현
# =========================================================

FORMATIVE_QUIZ_4_1 = [

    # -----------------------------------------------------
    # 1. 임베디드 GUI 기본 개념
    # -----------------------------------------------------
    QuizQuestion(
        id="4_1_f01",
        type="multiple_choice",
        question="GUI의 영문 전체 명칭은?",
        options=[
            "Graphical User Interface",
            "General User Internet",
            "Graphic Unit Input",
            "Global Utility Interface",
        ],
        answer="Graphical User Interface",
        explanation=(
            "GUI는 Graphical User Interface의 약자로 "
            "그래픽 요소를 이용하여 사용자와 시스템이 "
            "상호작용하는 인터페이스입니다."
        ),
        topic="GUI 개요",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_1_f02",
        type="multiple_choice",
        question=(
            "PDF에서 멀티미디어 임베디드 시스템의 GUI가 "
            "지원해야 한다고 제시한 해상도 기준은?"
        ),
        options=[
            "640×480 이상",
            "320×240 이하",
            "1920×1080만",
            "128×64만",
        ],
        answer="640×480 이상",
        explanation=(
            "PDF에서는 640×480 이상의 고해상도를 "
            "지원해야 한다고 설명합니다."
        ),
        topic="GUI 특성",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_1_f03",
        type="multiple_choice",
        question=(
            "임베디드 GUI에서 요구되는 화면 방식으로 "
            "PDF에 제시된 것은?"
        ),
        options=[
            "전체 화면 기반(FSE)",
            "텍스트 전용 화면",
            "명령행만 사용",
            "프린터 기반 화면",
        ],
        answer="전체 화면 기반(FSE)",
        explanation=(
            "PDF에서는 전체 화면 기반(FSE)의 "
            "사용자 인터페이스를 지원해야 한다고 설명합니다."
        ),
        topic="GUI 특성",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_1_f04",
        type="multiple_choice",
        question=(
            "임베디드 GUI의 특성으로 가장 적절하지 않은 것은?"
        ),
        options=[
            "단순성",
            "직관성",
            "경량성",
            "가능한 한 복잡한 인터페이스",
        ],
        answer="가능한 한 복잡한 인터페이스",
        explanation=(
            "임베디드 환경에서는 PC GUI보다 다소 단순하면서 "
            "직관적인 인터페이스가 요구됩니다."
        ),
        topic="GUI 특성",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_1_f05",
        type="true_false",
        question=(
            "임베디드 시스템은 사용자 인터페이스 처리 성능이 "
            "상대적으로 낮을 수 있으므로 경량성과 안정성을 "
            "갖춘 GUI 플랫폼이 필요할 수 있다."
        ),
        answer=True,
        explanation=(
            "PDF에서 임베디드 GUI 플랫폼의 "
            "경량성과 안정성을 강조합니다."
        ),
        topic="GUI 특성",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 2. GUI 라이브러리 분류
    # -----------------------------------------------------
    QuizQuestion(
        id="4_1_f06",
        type="multiple_choice",
        question=(
            "다음 중 PDF에서 저수준 GUI 라이브러리로 "
            "분류된 것은?"
        ),
        options=[
            "Nano-X",
            "QT",
            "Gtk",
            "MiniGUI",
        ],
        answer="Nano-X",
        explanation=(
            "Nano-X, DirectFB, KDrive, SDL은 "
            "저수준 GUI 라이브러리로 분류되어 있습니다."
        ),
        topic="GUI 라이브러리",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f07",
        type="multiple_choice",
        question=(
            "다음 중 PDF에서 고수준 GUI 라이브러리로 "
            "분류된 것은?"
        ),
        options=[
            "QT",
            "Nano-X",
            "DirectFB",
            "KDrive",
        ],
        answer="QT",
        explanation=(
            "Gtk, QT, FLTK, MiniGUI는 "
            "고수준 GUI 라이브러리로 분류됩니다."
        ),
        topic="GUI 라이브러리",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f08",
        type="multiple_choice",
        question=(
            "다음 중 모두 저수준 GUI 라이브러리로 "
            "구성된 것은?"
        ),
        options=[
            "Nano-X, DirectFB, KDrive, SDL",
            "Gtk, QT, FLTK, MiniGUI",
            "Nano-X, QT, FLTK, SDL",
            "Gtk, DirectFB, KDrive, MiniGUI",
        ],
        answer="Nano-X, DirectFB, KDrive, SDL",
        explanation=(
            "PDF의 표에서 네 항목 모두 "
            "저수준 GUI 라이브러리로 분류됩니다."
        ),
        topic="GUI 라이브러리",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f09",
        type="multiple_choice",
        question=(
            "다음 중 모두 고수준 GUI 라이브러리로 "
            "구성된 것은?"
        ),
        options=[
            "Gtk, QT, FLTK, MiniGUI",
            "Nano-X, DirectFB, KDrive, SDL",
            "QT, SDL, KDrive, FLTK",
            "Gtk, Nano-X, MiniGUI, DirectFB",
        ],
        answer="Gtk, QT, FLTK, MiniGUI",
        explanation=(
            "PDF에서 Gtk, QT, FLTK, MiniGUI를 "
            "고수준 GUI 라이브러리로 분류합니다."
        ),
        topic="GUI 라이브러리",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 3. 라이선스
    # -----------------------------------------------------
    QuizQuestion(
        id="4_1_f10",
        type="multiple_choice",
        question="Nano-X의 라이선스는?",
        options=[
            "Mozilla Public License",
            "LGPL",
            "GPL",
            "X11 License",
        ],
        answer="Mozilla Public License",
        explanation=(
            "PDF의 표에서 Nano-X는 "
            "Mozilla Public License로 제시됩니다."
        ),
        topic="GUI 라이선스",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f11",
        type="multiple_choice",
        question="DirectFB의 라이선스는?",
        options=[
            "LGPL",
            "GPL",
            "X11 License",
            "Mozilla Public License",
        ],
        answer="LGPL",
        explanation="PDF에서는 DirectFB의 라이선스를 LGPL로 제시합니다.",
        topic="GUI 라이선스",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f12",
        type="multiple_choice",
        question="KDrive의 라이선스는?",
        options=[
            "X11 License",
            "GPL",
            "LGPL",
            "Mozilla Public License",
        ],
        answer="X11 License",
        explanation="PDF에서는 KDrive를 X11 License로 제시합니다.",
        topic="GUI 라이선스",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f13",
        type="multiple_choice",
        question="SDL의 라이선스는?",
        options=[
            "LGPL",
            "GPL",
            "X11 License",
            "Mozilla Public License",
        ],
        answer="LGPL",
        explanation="PDF의 표에서 SDL은 LGPL입니다.",
        topic="GUI 라이선스",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f14",
        type="multiple_choice",
        question="Gtk의 라이선스는?",
        options=[
            "GPL",
            "LGPL",
            "X11 License",
            "Mozilla Public License",
        ],
        answer="GPL",
        explanation="PDF 표에서는 Gtk 라이선스를 GPL로 제시합니다.",
        topic="GUI 라이선스",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f15",
        type="multiple_choice",
        question="QT의 라이선스는?",
        options=[
            "GPL",
            "LGPL",
            "X11 License",
            "Mozilla Public License",
        ],
        answer="GPL",
        explanation="PDF 표에서는 QT의 라이선스를 GPL로 제시합니다.",
        topic="GUI 라이선스",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f16",
        type="multiple_choice",
        question="FLTK의 라이선스는?",
        options=[
            "LGPL",
            "GPL",
            "X11 License",
            "Mozilla Public License",
        ],
        answer="LGPL",
        explanation="PDF에서는 FLTK 라이선스를 LGPL로 제시합니다.",
        topic="GUI 라이선스",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f17",
        type="multiple_choice",
        question="MiniGUI의 라이선스는?",
        options=[
            "GPL",
            "LGPL",
            "X11 License",
            "Mozilla Public License",
        ],
        answer="GPL",
        explanation="PDF에서는 MiniGUI의 라이선스를 GPL로 제시합니다.",
        topic="GUI 라이선스",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 4. Nano-X
    # -----------------------------------------------------
    QuizQuestion(
        id="4_1_f18",
        type="multiple_choice",
        question=(
            "소형 장치를 위한 경량 그래픽 윈도 시스템을 "
            "제공하는 프레임워크는?"
        ),
        options=[
            "Nano-X",
            "DirectFB",
            "GTK",
            "QT",
        ],
        answer="Nano-X",
        explanation=(
            "Nano-X는 소형 장치용 경량 그래픽 "
            "윈도 시스템을 제공하는 오픈 소스 프로젝트입니다."
        ),
        topic="Nano-X",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_1_f19",
        type="multiple_choice",
        question=(
            "Nano-X가 제공하는 두 가지 형식의 API는?"
        ),
        options=[
            "Xlib, Win32",
            "SPI, I2C",
            "HTML, CSS",
            "TCP, UDP",
        ],
        answer="Xlib, Win32",
        explanation=(
            "PDF에서는 Nano-X가 Xlib과 Win32 "
            "두 형식의 API를 제공한다고 설명합니다."
        ),
        topic="Nano-X",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f20",
        type="true_false",
        question=(
            "Nano-X는 Client/Server 모델로 동작한다."
        ),
        answer=True,
        explanation=(
            "Nano-X는 client/server 모델로 동작한다고 "
            "PDF에 제시되어 있습니다."
        ),
        topic="Nano-X",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f21",
        type="multiple_choice",
        question=(
            "Nano-X에 대한 설명으로 옳지 않은 것은?"
        ),
        options=[
            "Widget Library를 지원한다.",
            "Client/Server 모델로 동작한다.",
            "Window Manager를 제공한다.",
            "소형 장치를 목표로 한다.",
        ],
        answer="Widget Library를 지원한다.",
        explanation=(
            "Nano-X는 Window Manager는 제공하지만 "
            "Widget Library는 지원하지 않습니다."
        ),
        topic="Nano-X",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 5. DirectFB
    # -----------------------------------------------------
    QuizQuestion(
        id="4_1_f22",
        type="multiple_choice",
        question=(
            "Linux 커널의 프레임버퍼 디바이스에 대한 "
            "추상 레이어 형태의 기술은?"
        ),
        options=[
            "DirectFB",
            "Nano-X",
            "GTK",
            "QT",
        ],
        answer="DirectFB",
        explanation=(
            "DirectFB는 Linux Framebuffer Device에 대한 "
            "추상 레이어 형태의 기술입니다."
        ),
        topic="DirectFB",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f23",
        type="true_false",
        question=(
            "DirectFB는 X Window를 대체할 수 있다."
        ),
        answer=True,
        explanation=(
            "PDF에서는 DirectFB가 X Window를 "
            "대체할 수 있다고 설명합니다."
        ),
        topic="DirectFB",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f24",
        type="multiple_choice",
        question=(
            "DirectFB에 대한 설명으로 가장 적절한 것은?"
        ),
        options=[
            "GDK로 포팅되었으며 GTK+ 애플리케이션을 지원한다.",
            "Widget Library를 반드시 자체 제공한다.",
            "Windows에서만 사용할 수 있다.",
            "Python 전용 라이브러리이다.",
        ],
        answer="GDK로 포팅되었으며 GTK+ 애플리케이션을 지원한다.",
        explanation=(
            "PDF에서 DirectFB는 GDK로 포팅되었으며 "
            "GTK+ 애플리케이션을 지원한다고 설명합니다."
        ),
        topic="DirectFB",
        difficulty="어려움",
    ),

    # -----------------------------------------------------
    # 6. GTK
    # -----------------------------------------------------
    QuizQuestion(
        id="4_1_f25",
        type="multiple_choice",
        question="GTK의 전체 명칭으로 PDF에 제시된 것은?",
        options=[
            "The Gimp Toolkit",
            "General Tool Kit",
            "Graphic Target Kernel",
            "GNU Transfer Kit",
        ],
        answer="The Gimp Toolkit",
        explanation=(
            "PDF에서는 GTK를 The Gimp Toolkit으로 "
            "표기하고 있습니다."
        ),
        topic="GTK",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f26",
        type="multiple_choice",
        question=(
            "GTK에 대한 설명으로 가장 적절한 것은?"
        ),
        options=[
            "GUI 제작을 위한 멀티 플랫폼 프레임워크이다.",
            "오직 ARM에서만 동작한다.",
            "NFS 전송 도구이다.",
            "GDB용 디버거이다.",
        ],
        answer="GUI 제작을 위한 멀티 플랫폼 프레임워크이다.",
        explanation=(
            "GTK는 GNU 프로젝트의 오픈 소스 "
            "멀티 플랫폼 GUI 프레임워크입니다."
        ),
        topic="GTK",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_1_f27",
        type="multiple_choice",
        question=(
            "GTK에서 다양한 프로그래밍 언어를 "
            "사용할 수 있게 해주는 것으로 PDF가 설명한 것은?"
        ),
        options=[
            "Wrapper",
            "NFS",
            "gdbserver",
            "Linker",
        ],
        answer="Wrapper",
        explanation=(
            "Wrapper를 이용하여 C++, Java, Perl, Python 등 "
            "다양한 언어를 사용할 수 있다고 설명합니다."
        ),
        topic="GTK",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 7. QT
    # -----------------------------------------------------
    QuizQuestion(
        id="4_1_f28",
        type="multiple_choice",
        question=(
            "PDF에서 설명하는 QT의 특징으로 옳은 것은?"
        ),
        options=[
            "X Window가 필요하지 않다.",
            "반드시 X Window가 필요하다.",
            "CLI 프로그램만 만들 수 있다.",
            "NFS 설정에만 사용한다.",
        ],
        answer="X Window가 필요하지 않다.",
        explanation=(
            "PDF에서는 임베디드 QT가 X Window를 "
            "필요로 하지 않는다고 설명합니다."
        ),
        topic="QT",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f29",
        type="multiple_choice",
        question=(
            "PDF에서 QT의 개발 흐름으로 제시한 순서는?"
        ),
        options=[
            "Trolltech → Nokia → Qt Company",
            "Nokia → Trolltech → Microsoft",
            "GNU → Nokia → Apple",
            "Riverbank → Trolltech → GNU",
        ],
        answer="Trolltech → Nokia → Qt Company",
        explanation=(
            "PDF에서는 Trolltech에서 개발을 시작하여 Nokia를 거쳐 "
            "Qt Company에 의해 릴리즈되고 있다고 설명합니다."
        ),
        topic="QT",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f30",
        type="true_false",
        question=(
            "PDF에서는 QT가 컴파일 시 매우 작은 크기로 "
            "컴파일 가능하다고 설명한다."
        ),
        answer=True,
        explanation=(
            "임베디드 환경에서의 QT 특징 중 하나로 "
            "작은 크기의 컴파일 결과가 제시됩니다."
        ),
        topic="QT",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 8. PyQt
    # -----------------------------------------------------
    QuizQuestion(
        id="4_1_f31",
        type="multiple_choice",
        question="PyQt에 대한 설명으로 가장 적절한 것은?",
        options=[
            "Qt의 Python 바인딩",
            "Linux Kernel",
            "NFS 서버",
            "ARM 전용 디버거",
        ],
        answer="Qt의 Python 바인딩",
        explanation=(
            "PDF에서는 PyQt를 크로스 플랫폼 GUI 툴킷 Qt의 "
            "Python 바인딩이라고 설명합니다."
        ),
        topic="PyQt",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_1_f32",
        type="multiple_choice",
        question="PyQt를 개발한 회사로 PDF에 제시된 것은?",
        options=[
            "Riverbank Computing",
            "Trolltech",
            "Microsoft",
            "GNU Foundation",
        ],
        answer="Riverbank Computing",
        explanation=(
            "PDF에서는 영국 회사 Riverbank Computing이 "
            "PyQt를 개발했다고 설명합니다."
        ),
        topic="PyQt",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f33",
        type="true_false",
        question=(
            "PDF에서는 PyQt가 Microsoft Windows와 "
            "여러 Unix 계열 운영체제를 지원한다고 설명한다."
        ),
        answer=True,
        explanation=(
            "Windows, Linux, macOS 등을 포함한 다양한 "
            "운영체제를 지원한다고 설명합니다."
        ),
        topic="PyQt",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 9. Qt Designer
    # -----------------------------------------------------
    QuizQuestion(
        id="4_1_f34",
        type="multiple_choice",
        question=(
            "PDF의 PyQt Designer 실습에서 선택하는 "
            "기본 Form Template은?"
        ),
        options=[
            "Dialog without Buttons",
            "Main Window with Toolbar",
            "Console Only",
            "Empty Terminal",
        ],
        answer="Dialog without Buttons",
        explanation=(
            "PDF 수행 내용에서는 "
            "'Dialog without Buttons' 템플릿을 선택합니다."
        ),
        topic="Qt Designer",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f35",
        type="multiple_choice",
        question=(
            "Qt Designer에서 GUI Widget을 확인하는 "
            "위치로 PDF에 제시된 것은?"
        ),
        options=[
            "좌측 패널",
            "작업 표시줄",
            "BIOS 화면",
            "터미널만",
        ],
        answer="좌측 패널",
        explanation=(
            "PDF에서는 Designer 좌측 패널의 위젯을 "
            "선택하여 Form 위에 배치하도록 합니다."
        ),
        topic="Qt Designer",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_1_f36",
        type="multiple_choice",
        question=(
            "Qt Designer 실습의 흐름으로 가장 적절한 것은?"
        ),
        options=[
            (
                "Designer 실행 → Form 선택 → Widget 선택 → "
                "Form에 배치 → GUI 확인"
            ),
            (
                "GUI 실행 → PyQt 삭제 → Form 생성"
            ),
            (
                "NFS 설정 → GPIO 작성 → Widget 삭제"
            ),
            (
                "Target 종료 → Designer 삭제 → Compile"
            ),
        ],
        answer=(
            "Designer 실행 → Form 선택 → Widget 선택 → "
            "Form에 배치 → GUI 확인"
        ),
        explanation=(
            "Designer에서 폼을 선택하고 위젯을 배치한 뒤 "
            "GUI를 실행하여 확인합니다."
        ),
        topic="Qt Designer",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f37",
        type="multiple_choice",
        question=(
            "Qt Designer에서 작성한 작업을 저장했을 때 "
            "PDF에서 설명하는 파일 형식은?"
        ),
        options=[
            "UI 확장자를 가진 XML 형식",
            "EXE 형식만",
            "JPG 형식",
            "CSV 형식만",
        ],
        answer="UI 확장자를 가진 XML 형식",
        explanation=(
            "PDF에서는 저장하면 UI 확장자를 가진 "
            "XML 형식의 파일이 만들어진다고 설명합니다."
        ),
        topic="Qt Designer",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 10. 인터페이스 / 환경
    # -----------------------------------------------------
    QuizQuestion(
        id="4_1_f38",
        type="multiple_choice",
        question=(
            "사용자가 프로그램을 조작하고 상태를 확인할 수 있도록 "
            "제공되는 인터페이스는?"
        ),
        options=[
            "사용자 인터페이스",
            "교차 컴파일러",
            "Linker",
            "Object File",
        ],
        answer="사용자 인터페이스",
        explanation=(
            "Button, Label, Input 등은 사용자가 시스템과 "
            "상호작용하도록 하는 사용자 인터페이스 요소입니다."
        ),
        topic="인터페이스",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_1_f39",
        type="multiple_choice",
        question=(
            "Host System과 Target System을 직접 연결하기 위한 "
            "네트워크 케이블로 수행 환경에 제시된 것은?"
        ),
        options=[
            "Cross Cable",
            "HDMI Cable",
            "Power Cable",
            "VGA Cable",
        ],
        answer="Cross Cable",
        explanation=(
            "PDF의 재료·자료 항목에서 Cross Cable을 "
            "Host와 Target 직접 연결용 Network Cable로 제시합니다."
        ),
        topic="실습 환경",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_f40",
        type="true_false",
        question=(
            "무상 소프트웨어라면 사용 기간이나 "
            "라이선스 문제를 확인할 필요가 없다."
        ),
        answer=False,
        explanation=(
            "PDF에서는 무상 버전이라도 기간 문제 등이 "
            "발생할 수 있으므로 라이선스를 확인하도록 합니다."
        ),
        topic="실습 환경",
        difficulty="보통",
    ),
]


# =========================================================
# 학습 4-1 중간고사 대비
# =========================================================

EXAM_PRACTICE_4_1 = [

    QuizQuestion(
        id="4_1_e01",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 임베디드 GUI의 특성은?"
        ),
        passage=(
            "사용자 인터페이스 처리 성능이 상대적으로 낮은 "
            "환경에서도 신속하게 GUI를 처리할 수 있도록 "
            "가볍게 구성하는 특성"
        ),
        options=[
            "경량성",
            "실시간성",
            "보안성",
            "이식성",
        ],
        answer="경량성",
        explanation=(
            "PDF에서는 임베디드 GUI 플랫폼에 "
            "경량성(light-weight)이 필요하다고 설명합니다."
        ),
        topic="GUI 특성",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e02",
        type="multiple_choice",
        question=(
            "다음 중 GUI 라이브러리의 수준별 분류가 "
            "올바른 것은?"
        ),
        options=[
            "Nano-X - 저수준 / QT - 고수준",
            "QT - 저수준 / DirectFB - 고수준",
            "Gtk - 저수준 / SDL - 고수준",
            "MiniGUI - 저수준 / Nano-X - 고수준",
        ],
        answer="Nano-X - 저수준 / QT - 고수준",
        explanation=(
            "Nano-X는 저수준, QT는 고수준 GUI "
            "라이브러리로 표에 제시됩니다."
        ),
        topic="GUI 라이브러리",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e03",
        type="multiple_choice",
        question=(
            "다음 GUI Library와 License 연결이 "
            "올바르지 않은 것은?"
        ),
        options=[
            "Nano-X - Mozilla Public License",
            "DirectFB - LGPL",
            "KDrive - X11 License",
            "QT - X11 License",
        ],
        answer="QT - X11 License",
        explanation=(
            "PDF의 표에서는 QT를 GPL로 제시합니다."
        ),
        topic="GUI 라이선스",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="4_1_e04",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 GUI Framework는?"
        ),
        passage=(
            "소형 장치를 위한 경량 그래픽 윈도 시스템이며 "
            "Xlib과 Win32 형식의 API를 제공한다. "
            "Client/Server 모델로 동작하고 Window Manager를 "
            "제공하지만 Widget Library는 지원하지 않는다."
        ),
        options=[
            "Nano-X",
            "DirectFB",
            "GTK",
            "QT",
        ],
        answer="Nano-X",
        explanation=(
            "Nano-X의 주요 특징을 종합한 설명입니다."
        ),
        topic="Nano-X",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e05",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 GUI Framework는?"
        ),
        passage=(
            "Linux Kernel의 Framebuffer Device에 대한 "
            "추상 레이어 형태의 기술이며 X Window를 "
            "대체할 수 있고 GTK+ Application을 지원한다."
        ),
        options=[
            "DirectFB",
            "Nano-X",
            "QT",
            "MiniGUI",
        ],
        answer="DirectFB",
        explanation=(
            "Linux Framebuffer 기반의 추상 레이어라는 설명은 "
            "DirectFB의 특징입니다."
        ),
        topic="DirectFB",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e06",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 GUI Framework는?"
        ),
        passage=(
            "GNU 프로젝트의 오픈 소스 멀티 플랫폼 GUI "
            "프레임워크이며 Wrapper를 이용하여 C++, Java, "
            "Perl, Python 등의 언어에서 활용할 수 있다."
        ),
        options=[
            "GTK",
            "Nano-X",
            "DirectFB",
            "KDrive",
        ],
        answer="GTK",
        explanation=(
            "The Gimp Toolkit인 GTK의 특징입니다."
        ),
        topic="GTK",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e07",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 GUI Framework는?"
        ),
        passage=(
            "Trolltech에서 개발을 시작하였으며 Nokia를 거쳐 "
            "Qt Company에서 지속적으로 릴리즈되고 있다. "
            "X Window가 필요하지 않고 작은 크기로 컴파일할 수 있다."
        ),
        options=[
            "QT",
            "GTK",
            "Nano-X",
            "DirectFB",
        ],
        answer="QT",
        explanation=(
            "PDF에서 설명하는 QT의 특징입니다."
        ),
        topic="QT",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e08",
        type="multiple_choice",
        question=(
            "다음 중 PDF에서 LGPL로 제시된 "
            "GUI Library만으로 구성된 것은?"
        ),
        options=[
            "DirectFB, SDL, FLTK",
            "Nano-X, QT, Gtk",
            "KDrive, QT, MiniGUI",
            "Gtk, MiniGUI, Nano-X",
        ],
        answer="DirectFB, SDL, FLTK",
        explanation=(
            "PDF 표에서 DirectFB, SDL, FLTK가 LGPL로 제시됩니다."
        ),
        topic="GUI 라이선스",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="4_1_e09",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 도구는?"
        ),
        passage=(
            "크로스 플랫폼 GUI Toolkit인 Qt를 "
            "Python에서 사용할 수 있도록 제공하는 바인딩이며 "
            "Riverbank Computing이 개발하였다."
        ),
        options=[
            "PyQt",
            "GDB",
            "GCC",
            "Nano-X",
        ],
        answer="PyQt",
        explanation=(
            "PDF에서 PyQt를 Qt의 Python Binding으로 설명합니다."
        ),
        topic="PyQt",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e10",
        type="multiple_choice",
        question=(
            "다음 PyQt Designer 실습 순서의 빈칸에 "
            "들어갈 내용으로 가장 적절한 것은?"
        ),
        passage=(
            "PyQt 설치 → Designer 실행 → "
            "(               ) → Widget 배치 → GUI 실행 확인"
        ),
        options=[
            "Dialog without Buttons 선택",
            "NFS 서버 삭제",
            "GDB Breakpoint 설정",
            "ARM Cross Compiler 삭제",
        ],
        answer="Dialog without Buttons 선택",
        explanation=(
            "PDF에서는 Designer 실행 후 기본 템플릿에서 "
            "Dialog without Buttons를 선택합니다."
        ),
        topic="Qt Designer",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e11",
        type="multiple_choice",
        question=(
            "다음 Qt Designer 작업에 대한 설명으로 "
            "가장 적절한 것은?"
        ),
        passage=(
            "좌측 패널에서 Text Label을 선택하여 "
            "Form 위의 원하는 위치에 배치하였다."
        ),
        options=[
            "GUI Widget을 Form에 배치한 것이다.",
            "프로그램을 교차 컴파일한 것이다.",
            "NFS 공유 폴더를 생성한 것이다.",
            "GDB로 변수를 출력한 것이다.",
        ],
        answer="GUI Widget을 Form에 배치한 것이다.",
        explanation=(
            "Qt Designer에서는 좌측 Widget 패널의 요소를 "
            "Form에 배치하여 GUI를 설계합니다."
        ),
        topic="Qt Designer",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_1_e12",
        type="multiple_choice",
        question=(
            "Qt Designer에서 작성한 GUI를 저장했을 때 "
            "생성되는 파일에 대한 PDF의 설명으로 옳은 것은?"
        ),
        options=[
            "UI 확장자를 가진 XML 형식",
            "반드시 EXE 파일",
            "ARM ELF 파일",
            "CSV 파일",
        ],
        answer="UI 확장자를 가진 XML 형식",
        explanation=(
            "PDF에서는 GUI 작업 저장 시 UI 확장자를 가진 "
            "XML 형식 파일이 생성된다고 설명합니다."
        ),
        topic="Qt Designer",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e13",
        type="multiple_choice",
        question=(
            "오픈 소스 GUI 도구의 성능 평가 시 "
            "PDF 수행 Tip에서 테스트 대상으로 제시한 것은?"
        ),
        options=[
            "Widget 출력 기능과 Image 출력 기능",
            "NFS와 GDB만",
            "GPIO와 ADC만",
            "Compiler Version만",
        ],
        answer="Widget 출력 기능과 Image 출력 기능",
        explanation=(
            "PDF 수행 Tip에서는 자주 사용되는 Widget 출력과 "
            "Image 출력 기능을 테스트하여 성능을 측정한다고 설명합니다."
        ),
        topic="GUI 테스트",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="4_1_e14",
        type="multiple_choice",
        question=(
            "인터페이스 구현 과정의 순서로 "
            "가장 적절한 것은?"
        ),
        options=[
            (
                "GUI Framework 확인 → License 확인 → "
                "도구 선정 → 환경 구성 → GUI 작성 → 테스트"
            ),
            (
                "GUI 테스트 → 도구 삭제 → 라이선스 확인"
            ),
            (
                "Target 삭제 → Widget 작성 → GCC 삭제"
            ),
            (
                "NFS 구성 → GDB 실행 → Form 삭제"
            ),
        ],
        answer=(
            "GUI Framework 확인 → License 확인 → "
            "도구 선정 → 환경 구성 → GUI 작성 → 테스트"
        ),
        explanation=(
            "GUI 도구와 라이선스를 검토하고 환경을 구성한 뒤 "
            "GUI를 작성하고 정상 동작을 테스트하는 흐름입니다."
        ),
        topic="인터페이스 구현",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e15",
        type="multiple_choice",
        question=(
            "다음 Arduino 프로젝트 상황을 "
            "사용자 인터페이스 관점에서 가장 잘 설명한 것은?"
        ),
        passage=(
            "LCD에 현재 토양 수분값을 표시하고 "
            "사용자가 버튼을 누르면 물 펌프가 작동한다."
        ),
        options=[
            (
                "LCD와 버튼을 통해 사용자가 시스템 상태를 확인하고 "
                "기능을 조작하는 사용자 인터페이스이다."
            ),
            "교차 컴파일러의 기능이다.",
            "Linker의 동작이다.",
            "GDB의 원격 디버깅이다.",
        ],
        answer=(
            "LCD와 버튼을 통해 사용자가 시스템 상태를 확인하고 "
            "기능을 조작하는 사용자 인터페이스이다."
        ),
        explanation=(
            "GUI뿐 아니라 물리적인 표시 장치와 입력 장치도 "
            "사용자와 시스템의 상호작용 관점에서 연결하여 "
            "이해할 수 있습니다."
        ),
        topic="Arduino 연결",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_1_e16",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 PyQt Designer의 "
            "기본 Form Template 이름을 쓰시오."
        ),
        passage=(
            "PDF 실습에서 작은 빈 창을 기본으로 제공하며 "
            "GUI 디자인을 시작할 때 선택한다."
        ),
        answer=[
            "Dialog without Buttons",
            "dialog without buttons",
        ],
        explanation=(
            "PDF에서는 Dialog without Buttons를 선택하여 "
            "GUI 작성 실습을 시작합니다."
        ),
        topic="Qt Designer",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="4_1_e17",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 GUI Framework를 쓰시오."
        ),
        passage=(
            "소형 장치를 위한 경량 그래픽 윈도 시스템이며 "
            "Client/Server 모델로 동작하고 Widget Library는 "
            "지원하지 않는다."
        ),
        answer=[
            "Nano-X",
            "Nano-x",
            "nano-x",
        ],
        explanation="해당 특징은 Nano-X에 대한 설명입니다.",
        topic="Nano-X",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="4_1_e18",
        type="short_answer",
        question=(
            "PDF의 GUI Library 표에서 KDrive에 "
            "적용된 라이선스 이름을 쓰시오."
        ),
        answer=[
            "X11 License",
            "X11 license",
            "x11 license",
        ],
        explanation=(
            "PDF에서는 KDrive의 라이선스를 "
            "X11 License로 제시합니다."
        ),
        topic="GUI 라이선스",
        difficulty="어려움",
    ),
]


# =========================================================
# 전체 문제
# =========================================================

ALL_QUIZ_4_1 = (
    FORMATIVE_QUIZ_4_1
    + EXAM_PRACTICE_4_1
)