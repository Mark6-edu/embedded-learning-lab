from __future__ import annotations

from utils.quiz import QuizQuestion


# =========================================================
# 학습 3-1 형성평가
# 애플리케이션 구현 및 오류 제거
# =========================================================

FORMATIVE_QUIZ_3_1 = [

    # -----------------------------------------------------
    # 1. GCC 개요
    # -----------------------------------------------------
    QuizQuestion(
        id="3_1_f01",
        type="multiple_choice",
        question=(
            "GCC의 현재 의미로 가장 적절한 것은?"
        ),
        options=[
            "GNU Compiler Collection",
            "General Computer Control",
            "Global Code Converter",
            "GNU Communication Client",
        ],
        answer="GNU Compiler Collection",
        explanation=(
            "GCC는 GNU Compiler Collection을 의미하며 "
            "여러 프로그래밍 언어를 지원하는 컴파일러 모음입니다."
        ),
        topic="GCC 개요",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f02",
        type="true_false",
        question=(
            "GCC는 처음부터 여러 프로그래밍 언어를 "
            "지원하는 Compiler Collection으로 시작하였다."
        ),
        answer=False,
        explanation=(
            "초기에는 GNU C Compiler로 시작하였고, "
            "이후 여러 언어를 지원하면서 "
            "GNU Compiler Collection으로 확장되었습니다."
        ),
        topic="GCC 개요",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f03",
        type="multiple_choice",
        question=(
            "다음 중 GCC가 지원하는 프로그래밍 언어의 "
            "예로 가장 적절한 것은?"
        ),
        options=[
            "C",
            "HTML",
            "CSS",
            "SQL 문서만",
        ],
        answer="C",
        explanation=(
            "GCC는 C를 비롯하여 C++, Fortran 등 "
            "여러 프로그래밍 언어를 지원합니다."
        ),
        topic="GCC 개요",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 2. GCC 동작 원리
    # -----------------------------------------------------
    QuizQuestion(
        id="3_1_f04",
        type="multiple_choice",
        question=(
            "GCC 내부 처리 과정에서 전처리를 담당하는 도구는?"
        ),
        options=[
            "cpp",
            "cc1",
            "as",
            "ld",
        ],
        answer="cpp",
        explanation=(
            "cpp는 헤더 파일 포함과 매크로 처리 등의 "
            "전처리 작업을 수행합니다."
        ),
        topic="GCC 동작 과정",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f05",
        type="multiple_choice",
        question=(
            "GCC 내부 처리 과정에서 실제 컴파일을 담당하는 도구는?"
        ),
        options=[
            "cc1",
            "cpp",
            "as",
            "ld",
        ],
        answer="cc1",
        explanation=(
            "cc1은 전처리된 C 소스 코드를 "
            "컴파일하는 과정에 사용됩니다."
        ),
        topic="GCC 동작 과정",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f06",
        type="multiple_choice",
        question=(
            "어셈블리 코드를 오브젝트 파일로 변환하는 도구는?"
        ),
        options=[
            "as",
            "cpp",
            "cc1",
            "ld",
        ],
        answer="as",
        explanation=(
            "as는 assembler로서 어셈블리 코드를 "
            "오브젝트 파일 형태로 변환합니다."
        ),
        topic="GCC 동작 과정",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f07",
        type="multiple_choice",
        question=(
            "오브젝트 파일과 라이브러리를 결합하여 "
            "최종 실행 파일을 생성하는 도구는?"
        ),
        options=[
            "ld",
            "cpp",
            "cc1",
            "as",
        ],
        answer="ld",
        explanation=(
            "ld는 linker로서 여러 오브젝트 파일과 "
            "라이브러리를 연결하여 실행 파일을 생성합니다."
        ),
        topic="GCC 동작 과정",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f08",
        type="multiple_choice",
        question=(
            "GCC의 처리 순서로 가장 적절한 것은?"
        ),
        options=[
            "cpp → cc1 → as → ld",
            "ld → as → cc1 → cpp",
            "cc1 → cpp → ld → as",
            "as → cpp → cc1 → ld",
        ],
        answer="cpp → cc1 → as → ld",
        explanation=(
            "소스 코드는 전처리(cpp) → 컴파일(cc1) → "
            "어셈블링(as) → 링크(ld) 순서로 처리됩니다."
        ),
        topic="GCC 동작 과정",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 3. GCC 옵션
    # -----------------------------------------------------
    QuizQuestion(
        id="3_1_f09",
        type="multiple_choice",
        question=(
            "GCC에서 전처리 단계까지만 수행하는 옵션은?"
        ),
        options=[
            "-E",
            "-c",
            "-o",
            "-L",
        ],
        answer="-E",
        explanation=(
            "-E 옵션은 전처리까지만 수행한 뒤 "
            "이후 컴파일 과정을 진행하지 않습니다."
        ),
        topic="GCC 옵션",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f10",
        type="multiple_choice",
        question=(
            "GCC에서 링크를 수행하지 않고 "
            "오브젝트 파일까지만 생성하는 옵션은?"
        ),
        options=[
            "-c",
            "-E",
            "-o",
            "-I",
        ],
        answer="-c",
        explanation=(
            "-c 옵션은 소스 코드를 컴파일하여 "
            "오브젝트 파일을 생성하지만 링크는 수행하지 않습니다."
        ),
        topic="GCC 옵션",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f11",
        type="multiple_choice",
        question=(
            "생성되는 실행 파일의 이름을 지정하는 GCC 옵션은?"
        ),
        options=[
            "-o",
            "-c",
            "-E",
            "-O",
        ],
        answer="-o",
        explanation=(
            "-o 옵션은 출력 파일의 이름을 지정합니다."
        ),
        topic="GCC 옵션",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f12",
        type="multiple_choice",
        question=(
            "헤더 파일을 검색할 경로를 지정하는 GCC 옵션은?"
        ),
        options=[
            "-I",
            "-L",
            "-l",
            "-O",
        ],
        answer="-I",
        explanation=(
            "-I 옵션은 헤더 파일을 검색할 디렉터리를 지정합니다."
        ),
        topic="GCC 옵션",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f13",
        type="multiple_choice",
        question=(
            "라이브러리 파일을 검색할 경로를 지정하는 GCC 옵션은?"
        ),
        options=[
            "-L",
            "-I",
            "-l",
            "-c",
        ],
        answer="-L",
        explanation=(
            "-L 옵션은 라이브러리를 검색할 경로를 지정합니다."
        ),
        topic="GCC 옵션",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f14",
        type="multiple_choice",
        question=(
            "특정 라이브러리를 링크할 때 사용하는 GCC 옵션은?"
        ),
        options=[
            "-l",
            "-L",
            "-I",
            "-E",
        ],
        answer="-l",
        explanation=(
            "-l 옵션은 사용할 라이브러리를 지정할 때 사용합니다."
        ),
        topic="GCC 옵션",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f15",
        type="multiple_choice",
        question=(
            "컴파일 최적화와 관련된 GCC 옵션은?"
        ),
        options=[
            "-O",
            "-o",
            "-c",
            "-E",
        ],
        answer="-O",
        explanation=(
            "-O는 최적화와 관련된 옵션입니다."
        ),
        topic="GCC 옵션",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f16",
        type="multiple_choice",
        question=(
            "정적 라이브러리를 이용하여 링크하는 옵션은?"
        ),
        options=[
            "-static",
            "-dynamic",
            "-source",
            "-target",
        ],
        answer="-static",
        explanation=(
            "-static 옵션은 정적 라이브러리를 이용하여 "
            "링크할 때 사용합니다."
        ),
        topic="GCC 옵션",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 4. 모듈 구현
    # -----------------------------------------------------
    QuizQuestion(
        id="3_1_f17",
        type="multiple_choice",
        question=(
            "특정 하나의 기능이나 역할을 수행하도록 "
            "구현한 프로그램 단위로 가장 적절한 것은?"
        ),
        options=[
            "단위 모듈",
            "공통 모듈",
            "운영체제",
            "툴체인",
        ],
        answer="단위 모듈",
        explanation=(
            "단위 모듈은 특정 기능이나 역할을 "
            "수행하도록 구현된 프로그램 단위로 볼 수 있습니다."
        ),
        topic="모듈 구현",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f18",
        type="multiple_choice",
        question=(
            "여러 프로그램에서 반복적으로 사용할 기능을 "
            "분리하여 구현한 모듈은?"
        ),
        options=[
            "공통 모듈",
            "단위 모듈",
            "Target System",
            "Object File",
        ],
        answer="공통 모듈",
        explanation=(
            "여러 기능에서 공통으로 사용하는 기능은 "
            "공통 모듈로 분리하여 구현할 수 있습니다."
        ),
        topic="모듈 구현",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f19",
        type="true_false",
        question=(
            "모듈 구현에서는 요구사항과 관계없이 "
            "개발자가 원하는 기능을 자유롭게 추가하는 것이 "
            "가장 중요하다."
        ),
        answer=False,
        explanation=(
            "구현 코드는 요구사항을 반영해야 하며 "
            "각 모듈의 역할과 입력·출력을 명확하게 해야 합니다."
        ),
        topic="모듈 구현",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 5. 오류와 경고
    # -----------------------------------------------------
    QuizQuestion(
        id="3_1_f20",
        type="multiple_choice",
        question=(
            "프로그램의 정상적인 컴파일을 방해하여 "
            "소스 수정이 필요한 문제를 무엇이라고 하는가?"
        ),
        options=[
            "Error",
            "Warning",
            "Comment",
            "Option",
        ],
        answer="Error",
        explanation=(
            "Error는 정상적인 컴파일을 방해하는 문제로 "
            "원인을 찾아 코드를 수정해야 합니다."
        ),
        topic="오류와 경고",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f21",
        type="multiple_choice",
        question=(
            "컴파일이 계속될 수 있지만 "
            "잠재적인 문제 가능성을 알려주는 메시지는?"
        ),
        options=[
            "Warning",
            "Error",
            "Linker",
            "Header",
        ],
        answer="Warning",
        explanation=(
            "Warning은 컴파일을 반드시 중단시키지는 않지만 "
            "잠재적인 문제가 있음을 알려주는 메시지입니다."
        ),
        topic="오류와 경고",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f22",
        type="multiple_choice",
        question=(
            "컴파일 오류를 발견한 후의 올바른 처리 과정은?"
        ),
        options=[
            (
                "오류 메시지 확인 → 소스 수정 → "
                "재컴파일 → 결과 확인"
            ),
            (
                "소스 삭제 → 컴퓨터 종료 → 다시 작성"
            ),
            (
                "경고 무시 → Target 전송 → 실행"
            ),
            (
                "컴파일러 삭제 → 소스 수정 → NFS 종료"
            ),
        ],
        answer=(
            "오류 메시지 확인 → 소스 수정 → "
            "재컴파일 → 결과 확인"
        ),
        explanation=(
            "오류 위치와 원인을 확인하고 소스를 수정한 뒤 "
            "다시 컴파일하여 문제가 제거됐는지 확인해야 합니다."
        ),
        topic="오류 제거",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f23",
        type="true_false",
        question=(
            "컴파일 과정에서 Error가 없다면 "
            "Warning은 모두 무시해도 된다."
        ),
        answer=False,
        explanation=(
            "학습 목표에서는 컴파일 결과의 오류뿐 아니라 "
            "경고도 확인하고 소스를 수정하여 제거하도록 요구합니다."
        ),
        topic="오류와 경고",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 6. Arduino 오류 연결
    # -----------------------------------------------------
    QuizQuestion(
        id="3_1_f24",
        type="multiple_choice",
        question=(
            "다음 Arduino 코드가 컴파일되지 않는 "
            "가장 직접적인 원인은?"
        ),
        passage=(
            "pinMode(13, OUTPUT)"
        ),
        options=[
            "문장 끝의 세미콜론(;)이 없다.",
            "13번 핀은 사용할 수 없다.",
            "OUTPUT은 문자열이어야 한다.",
            "pinMode 함수는 loop에서만 사용할 수 있다.",
        ],
        answer="문장 끝의 세미콜론(;)이 없다.",
        explanation=(
            "C/C++ 문장 끝에는 일반적으로 세미콜론이 필요합니다."
        ),
        topic="Arduino 오류",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f25",
        type="multiple_choice",
        question=(
            "Arduino IDE에서 컴파일 오류가 발생했을 때 "
            "가장 먼저 해야 할 행동으로 적절한 것은?"
        ),
        options=[
            "오류 메시지와 발생 위치를 확인한다.",
            "모든 코드를 삭제한다.",
            "Arduino 보드를 교체한다.",
            "프로그램을 제출한다.",
        ],
        answer="오류 메시지와 발생 위치를 확인한다.",
        explanation=(
            "오류 해결은 컴파일러가 알려주는 메시지와 "
            "코드 위치를 확인하는 것에서 시작하는 것이 좋습니다."
        ),
        topic="Arduino 오류",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 7. ECHO SERVER
    # -----------------------------------------------------
    QuizQuestion(
        id="3_1_f26",
        type="multiple_choice",
        question=(
            "NCS의 ECHO SERVER 실습에서 "
            "Host System의 역할은?"
        ),
        options=[
            "Client",
            "Server",
            "Router",
            "Sensor",
        ],
        answer="Client",
        explanation=(
            "ECHO SERVER 실습에서 Host System의 "
            "pc_client 프로그램은 Client 역할을 수행합니다."
        ),
        topic="ECHO SERVER",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f27",
        type="multiple_choice",
        question=(
            "NCS의 ECHO SERVER 실습에서 "
            "Target System의 역할은?"
        ),
        options=[
            "Server",
            "Client",
            "Compiler",
            "Editor",
        ],
        answer="Server",
        explanation=(
            "Target System에서 arm_server를 실행하여 "
            "ECHO Server 역할을 수행합니다."
        ),
        topic="ECHO SERVER",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f28",
        type="multiple_choice",
        question=(
            "Host에서 실행할 pc_client 프로그램을 "
            "컴파일할 때 사용하는 것으로 가장 적절한 것은?"
        ),
        options=[
            "gcc",
            "ARM Cross Compiler",
            "JTAG",
            "NFS",
        ],
        answer="gcc",
        explanation=(
            "Host에서 실행하는 pc_client는 "
            "Host용 gcc를 이용해 컴파일합니다."
        ),
        topic="ECHO SERVER",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f29",
        type="multiple_choice",
        question=(
            "Target에서 실행할 arm_server 프로그램을 "
            "컴파일할 때 사용하는 것은?"
        ),
        options=[
            "ARM Cross Compiler",
            "Host용 gcc만",
            "NFS",
            "Serial Monitor",
        ],
        answer="ARM Cross Compiler",
        explanation=(
            "arm_server는 Target System의 ARM 프로세서에서 "
            "실행되므로 ARM용 교차 컴파일러를 이용합니다."
        ),
        topic="ECHO SERVER",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f30",
        type="true_false",
        question=(
            "ECHO SERVER 실습의 핵심 목적은 "
            "복잡한 네트워크 프로그래밍 기술 자체를 "
            "깊게 학습하는 것이다."
        ),
        answer=False,
        explanation=(
            "이 실습에서는 네트워크 프로그래밍 자체보다는 "
            "Host와 Target을 이용한 교차 개발 환경의 "
            "활용 과정에 초점을 둡니다."
        ),
        topic="ECHO SERVER",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f31",
        type="multiple_choice",
        question=(
            "Target용 arm_server 실행 파일을 "
            "Target System으로 전달하는 데 활용할 수 있는 것은?"
        ),
        options=[
            "NFS",
            "GPIO",
            "PWM",
            "ADC",
        ],
        answer="NFS",
        explanation=(
            "PDF 실습에서는 NFS 등을 이용하여 "
            "arm_server 실행 파일을 Target으로 전달합니다."
        ),
        topic="ECHO SERVER",
        difficulty="쉬움",
    ),

        # -----------------------------------------------------
    # 8. make / Makefile
    # -----------------------------------------------------

    QuizQuestion(
        id="3_1_f32",
        type="multiple_choice",
        question=(
            "Makefile의 기본 구성 요소로 "
            "가장 적절한 것은?"
        ),
        options=[
            "target, dependencies, command",
            "host, target, server",
            "cpp, cc1, as",
            "GPIO, SPI, UART",
        ],
        answer="target, dependencies, command",
        explanation=(
            "Makefile은 기본적으로 target, dependencies, "
            "command의 관계를 이용하여 빌드 작업을 정의합니다."
        ),
        topic="make",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_f33",
        type="multiple_choice",
        question=(
            "Makefile에서 target을 생성하는 데 필요한 "
            "파일 목록을 무엇이라고 하는가?"
        ),
        options=[
            "dependencies",
            "command",
            "compiler",
            "debugger",
        ],
        answer="dependencies",
        explanation=(
            "dependencies는 target을 생성하는 데 필요한 "
            "파일 목록입니다."
        ),
        topic="make",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f34",
        type="multiple_choice",
        question=(
            "Makefile에서 command의 역할로 "
            "가장 적절한 것은?"
        ),
        options=[
            (
                "target을 생성하기 위해 "
                "실행할 명령을 정의한다."
            ),
            "Target System의 IP 주소를 정의한다.",
            "GCC의 버전을 저장한다.",
            "디버거의 중단점을 설정한다.",
        ],
        answer=(
            "target을 생성하기 위해 "
            "실행할 명령을 정의한다."
        ),
        explanation=(
            "command는 일반적으로 컴파일러 등을 호출하여 "
            "target을 생성하는 명령입니다."
        ),
        topic="make",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f35",
        type="multiple_choice",
        question=(
            "다음 Makefile 구문에서 target은 무엇인가?"
        ),
        passage=(
            "test: test1.o test2.o test3.o"
        ),
        options=[
            "test",
            "test1.o",
            "test2.o",
            "test3.o",
        ],
        answer="test",
        explanation=(
            "콜론(:) 왼쪽의 test가 target이고, "
            "오른쪽 파일들은 dependencies입니다."
        ),
        topic="make",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_f36",
        type="multiple_choice",
        question=(
            "다음 Makefile 구문에서 dependencies는?"
        ),
        passage=(
            "test1.o: test1.c test1.h"
        ),
        options=[
            "test1.c와 test1.h",
            "test1.o만",
            "gcc만",
            "test만",
        ],
        answer="test1.c와 test1.h",
        explanation=(
            "콜론 왼쪽의 test1.o가 target이며 "
            "오른쪽의 test1.c와 test1.h가 dependencies입니다."
        ),
        topic="make",
        difficulty="보통",
    ),

        QuizQuestion(
        id="3_1_e15",
        type="multiple_choice",
        question=(
            "다음 Makefile의 구성 요소를 "
            "올바르게 분석한 것은?"
        ),
        passage=(
            "test: test1.o test2.o test3.o"
        ),
        options=[
            (
                "test는 target이고 "
                "test1.o, test2.o, test3.o는 dependencies이다."
            ),
            (
                "test는 command이고 "
                "나머지는 target이다."
            ),
            (
                "모든 항목이 command이다."
            ),
            (
                "모든 항목이 compiler option이다."
            ),
        ],
        answer=(
            "test는 target이고 "
            "test1.o, test2.o, test3.o는 dependencies이다."
        ),
        explanation=(
            "Makefile에서 콜론 왼쪽에는 target, "
            "오른쪽에는 target 생성에 필요한 "
            "dependencies를 작성합니다."
        ),
        topic="make",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_e16",
        type="multiple_choice",
        question=(
            "다음 중 make의 동작을 가장 잘 설명한 것은?"
        ),
        options=[
            (
                "Makefile의 target과 dependencies를 확인하고 "
                "필요한 command를 실행한다."
            ),
            (
                "소스 코드의 모든 오류를 자동으로 수정한다."
            ),
            (
                "Target System의 하드웨어를 자동 교체한다."
            ),
            (
                "GDB의 breakpoint를 자동 생성한다."
            ),
        ],
        answer=(
            "Makefile의 target과 dependencies를 확인하고 "
            "필요한 command를 실행한다."
        ),
        explanation=(
            "make는 Makefile에 정의된 의존 관계와 "
            "명령을 이용하여 프로그램 빌드 작업을 수행합니다."
        ),
        topic="make",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_e17",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 Makefile의 "
            "구성 요소를 영문으로 쓰시오."
        ),
        passage=(
            "최종 target을 생성하기 위해 필요한 "
            "파일들의 목록"
        ),
        answer=[
            "dependencies",
            "dependency",
            "Dependencies",
        ],
        explanation=(
            "Makefile에서는 target 생성에 필요한 "
            "파일 목록을 dependencies라고 합니다."
        ),
        topic="make",
        difficulty="어려움",
    ),
]


# =========================================================
# 학습 3-1 중간고사 대비
# =========================================================

EXAM_PRACTICE_3_1 = [

    QuizQuestion(
        id="3_1_e01",
        type="multiple_choice",
        question=(
            "다음 GCC 처리 과정의 빈칸에 들어갈 도구는?"
        ),
        passage=(
            "소스 코드 → cpp → (      ) → as → ld → 실행 파일"
        ),
        options=[
            "cc1",
            "gdb",
            "NFS",
            "JTAG",
        ],
        answer="cc1",
        explanation=(
            "GCC 처리 순서는 cpp → cc1 → as → ld입니다."
        ),
        topic="GCC 동작 과정",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_e02",
        type="multiple_choice",
        question=(
            "다음 GCC 내부 도구와 역할의 연결이 "
            "올바르지 않은 것은?"
        ),
        options=[
            "cpp - 전처리",
            "cc1 - 컴파일",
            "as - 어셈블링",
            "ld - 소스 코드 편집",
        ],
        answer="ld - 소스 코드 편집",
        explanation=(
            "ld는 Linker이며 오브젝트 파일과 라이브러리를 "
            "연결해 실행 파일을 생성합니다."
        ),
        topic="GCC 동작 과정",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_e03",
        type="multiple_choice",
        question=(
            "다음 명령의 결과로 가장 적절한 것은?"
        ),
        passage="gcc -c test.c",
        options=[
            "링크 없이 오브젝트 파일을 생성한다.",
            "전처리만 수행한다.",
            "실행 파일 이름을 test로 지정한다.",
            "Target으로 파일을 전송한다.",
        ],
        answer="링크 없이 오브젝트 파일을 생성한다.",
        explanation=(
            "-c 옵션은 컴파일을 수행하되 "
            "링크 단계는 수행하지 않습니다."
        ),
        topic="GCC 옵션",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_e04",
        type="multiple_choice",
        question=(
            "다음 명령의 의미로 가장 적절한 것은?"
        ),
        passage="gcc test.c -o test",
        options=[
            "test라는 이름의 실행 파일을 생성한다.",
            "test.c를 삭제한다.",
            "전처리까지만 수행한다.",
            "라이브러리 검색 경로를 test로 지정한다.",
        ],
        answer="test라는 이름의 실행 파일을 생성한다.",
        explanation=(
            "-o 뒤에는 생성할 출력 파일 이름을 지정합니다."
        ),
        topic="GCC 옵션",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_e05",
        type="multiple_choice",
        question=(
            "다음 GCC 옵션의 연결이 올바른 것은?"
        ),
        options=[
            "-I - 헤더 파일 검색 경로",
            "-L - 전처리까지만 수행",
            "-E - 출력 파일 이름 지정",
            "-c - 최적화 수행",
        ],
        answer="-I - 헤더 파일 검색 경로",
        explanation=(
            "-I는 헤더 검색 경로, -L은 라이브러리 검색 경로, "
            "-E는 전처리까지만 수행, -c는 링크 없이 "
            "오브젝트 파일을 생성합니다."
        ),
        topic="GCC 옵션",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="3_1_e06",
        type="multiple_choice",
        question=(
            "다음 상황에서 가장 적절한 조치는?"
        ),
        passage=(
            "소스 코드를 컴파일하였더니 컴파일러가 "
            "특정 줄에서 Error 메시지를 출력하였다."
        ),
        options=[
            (
                "메시지와 코드 위치를 확인하고 "
                "소스를 수정한 뒤 재컴파일한다."
            ),
            "Error를 무시하고 Target으로 전송한다.",
            "컴파일러를 삭제한다.",
            "프로젝트 전체를 처음부터 다시 작성한다.",
        ],
        answer=(
            "메시지와 코드 위치를 확인하고 "
            "소스를 수정한 뒤 재컴파일한다."
        ),
        explanation=(
            "컴파일 오류 제거는 오류 메시지를 분석하고 "
            "소스를 수정한 뒤 재컴파일하는 반복 과정입니다."
        ),
        topic="오류 제거",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_e07",
        type="multiple_choice",
        question=(
            "다음 Arduino 코드의 문제로 가장 적절한 것은?"
        ),
        passage=(
            "void setup() {\n"
            "    pinMode(13, OUTPUT)\n"
            "}"
        ),
        options=[
            "세미콜론 누락",
            "setup 함수 사용 불가",
            "13번 핀 사용 불가",
            "OUTPUT 자료형 오류",
        ],
        answer="세미콜론 누락",
        explanation=(
            "pinMode(13, OUTPUT) 문장 끝에 "
            "세미콜론이 누락되었습니다."
        ),
        topic="Arduino 오류",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_1_e08",
        type="multiple_choice",
        question=(
            "다음 중 ECHO SERVER 실습의 역할과 "
            "컴파일러 연결이 올바른 것은?"
        ),
        options=[
            "Host Client - gcc / Target Server - ARM Cross Compiler",
            "Host Server - ARM Cross Compiler / Target Client - gcc",
            "Host Client - NFS / Target Server - JTAG",
            "Host Target - GPIO / Target Host - UART",
        ],
        answer=(
            "Host Client - gcc / Target Server - ARM Cross Compiler"
        ),
        explanation=(
            "Host에서는 pc_client를 gcc로 컴파일하고, "
            "Target에서 실행할 arm_server는 "
            "ARM용 교차 컴파일러로 생성합니다."
        ),
        topic="ECHO SERVER",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="3_1_e09",
        type="multiple_choice",
        question=(
            "다음 과정의 올바른 순서는?"
        ),
        passage=(
            "Target에서 동작할 ECHO Server 프로그램을 "
            "구현하여 실행하려고 한다."
        ),
        options=[
            (
                "소스 작성 → ARM 교차 컴파일 → "
                "Target 전송 → Target 실행"
            ),
            (
                "Target 실행 → 소스 작성 → gcc 삭제"
            ),
            (
                "NFS 삭제 → 소스 작성 → Host 종료"
            ),
            (
                "GPIO 설정 → Linker 삭제 → Target 실행"
            ),
        ],
        answer=(
            "소스 작성 → ARM 교차 컴파일 → "
            "Target 전송 → Target 실행"
        ),
        explanation=(
            "Target용 프로그램은 Host에서 작성하고 "
            "교차 컴파일한 뒤 Target으로 전달하여 실행합니다."
        ),
        topic="교차 개발 환경",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_e10",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 프로그램은?"
        ),
        passage=(
            "Host System에서 실행되며 사용자가 입력한 문자열을 "
            "Target의 ECHO Server에 전달하고 반환된 문자열을 확인한다."
        ),
        options=[
            "pc_client",
            "arm_server",
            "cpp",
            "ld",
        ],
        answer="pc_client",
        explanation=(
            "pc_client는 Host에서 실행되는 Client 프로그램입니다."
        ),
        topic="ECHO SERVER",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_e11",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 프로그램은?"
        ),
        passage=(
            "ARM용 교차 컴파일러로 생성하고 Target System에서 "
            "실행하여 Client가 보낸 문자열을 다시 돌려보낸다."
        ),
        options=[
            "arm_server",
            "pc_client",
            "gcc",
            "cpp",
        ],
        answer="arm_server",
        explanation=(
            "arm_server는 Target System에서 실행되는 "
            "ECHO Server 프로그램입니다."
        ),
        topic="ECHO SERVER",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_e12",
        type="multiple_choice",
        question=(
            "다음 중 학습 3-1의 핵심 학습 흐름으로 "
            "가장 적절한 것은?"
        ),
        options=[
            (
                "요구사항 확인 → 모듈 구현 → 컴파일 → "
                "오류·경고 확인 → 수정 → 재컴파일"
            ),
            (
                "코드 작성 → 오류 무시 → 바로 제출"
            ),
            (
                "Target 삭제 → Host 종료 → 소스 작성"
            ),
            (
                "라이선스 확인 → RISC 변경 → NFS 삭제"
            ),
        ],
        answer=(
            "요구사항 확인 → 모듈 구현 → 컴파일 → "
            "오류·경고 확인 → 수정 → 재컴파일"
        ),
        explanation=(
            "3-1에서는 요구사항에 따라 모듈을 구현하고 "
            "컴파일 과정에서 발견된 오류와 경고를 "
            "수정하는 과정이 핵심입니다."
        ),
        topic="학습 3-1 종합",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_1_e13",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 GCC 내부 도구의 이름을 쓰시오."
        ),
        passage=(
            "오브젝트 파일과 필요한 라이브러리를 연결하여 "
            "최종 실행 파일을 생성한다."
        ),
        answer=[
            "ld",
            "LD",
        ],
        explanation=(
            "ld는 GCC 처리 과정의 Linker입니다."
        ),
        topic="GCC 동작 과정",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="3_1_e14",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 GCC 옵션을 쓰시오."
        ),
        passage=(
            "컴파일 후 링크를 수행하지 않고 "
            "오브젝트 파일까지만 생성한다."
        ),
        answer=[
            "-c",
            "c",
        ],
        explanation=(
            "-c 옵션은 오브젝트 파일을 생성한 뒤 "
            "링크 단계는 수행하지 않습니다."
        ),
        topic="GCC 옵션",
        difficulty="어려움",
    ),
]


# =========================================================
# 전체 문제
# =========================================================

ALL_QUIZ_3_1 = (
    FORMATIVE_QUIZ_3_1
    + EXAM_PRACTICE_3_1
)

