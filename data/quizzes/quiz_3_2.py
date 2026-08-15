from __future__ import annotations

from utils.quiz import QuizQuestion


# =========================================================
# 학습 3-2 형성평가
# 디버깅 및 프로그램 통합
# =========================================================

FORMATIVE_QUIZ_3_2 = [

    # -----------------------------------------------------
    # 1. GDB 개요
    # -----------------------------------------------------
    QuizQuestion(
        id="3_2_f01",
        type="multiple_choice",
        question="GDB의 영문 전체 명칭은?",
        options=[
            "GNU Debugger",
            "General Data Builder",
            "GNU Device Board",
            "Global Debug Binary",
        ],
        answer="GNU Debugger",
        explanation=(
            "GDB는 GNU Debugger의 약자로 "
            "GNU 소프트웨어 시스템의 기본 디버거입니다."
        ),
        topic="GDB 개요",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f02",
        type="true_false",
        question=(
            "GDB를 이용하면 프로그램 실행 과정을 추적하고 "
            "프로그램 내부 변수의 값을 확인하거나 변경할 수 있다."
        ),
        answer=True,
        explanation=(
            "GDB는 프로그램의 실행을 추적하고 "
            "변수 값을 확인하거나 변경하는 기능을 제공합니다."
        ),
        topic="GDB 개요",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f03",
        type="multiple_choice",
        question=(
            "GDB 자체의 기본 사용자 인터페이스에 대한 설명으로 "
            "가장 적절한 것은?"
        ),
        options=[
            "기본적으로 명령행 인터페이스를 사용한다.",
            "반드시 웹 브라우저에서만 실행된다.",
            "기본적으로 그래픽 편집기만 제공한다.",
            "Arduino IDE에서만 실행된다.",
        ],
        answer="기본적으로 명령행 인터페이스를 사용한다.",
        explanation=(
            "GDB 자체에는 기본 GUI가 포함되지 않고 "
            "명령행 인터페이스를 이용합니다."
        ),
        topic="GDB 개요",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f04",
        type="multiple_choice",
        question=(
            "GDB를 GUI 형태로 사용할 수 있게 해주는 "
            "프런트엔드의 예는?"
        ),
        options=[
            "DDD",
            "NFS",
            "GPIO",
            "UART",
        ],
        answer="DDD",
        explanation=(
            "DDD는 GDB와 함께 사용할 수 있는 "
            "그래픽 기반 프런트엔드의 예입니다."
        ),
        topic="GDB 개요",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 2. 원격 디버깅
    # -----------------------------------------------------
    QuizQuestion(
        id="3_2_f05",
        type="multiple_choice",
        question=(
            "GDB가 실행되는 시스템과 디버깅 대상 프로그램이 "
            "실행되는 시스템이 서로 다른 경우 사용하는 방식은?"
        ),
        options=[
            "원격 모드 디버깅",
            "정적 링크",
            "전처리",
            "로컬 파일 복사",
        ],
        answer="원격 모드 디버깅",
        explanation=(
            "임베디드 교차 개발 환경에서는 Host와 Target이 "
            "분리되어 있기 때문에 원격 모드 디버깅을 활용할 수 있습니다."
        ),
        topic="원격 디버깅",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f06",
        type="multiple_choice",
        question=(
            "원격 모드 디버깅에서 Target System에 "
            "설치할 수 있는 프로그램은?"
        ),
        options=[
            "gdbserver",
            "DDD",
            "gcc만",
            "cpp",
        ],
        answer="gdbserver",
        explanation=(
            "Target System에는 gdbserver를 설치하고 "
            "Host의 GDB와 연결할 수 있습니다."
        ),
        topic="원격 디버깅",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_f07",
        type="multiple_choice",
        question=(
            "원격 모드 디버깅에서 Host System에 "
            "구성할 수 있는 도구 조합은?"
        ),
        options=[
            "ARM 전용 GDB와 DDD",
            "GPIO와 PWM",
            "NFS와 ADC",
            "UART와 SPI만",
        ],
        answer="ARM 전용 GDB와 DDD",
        explanation=(
            "NCS 예시에서는 Host에 ARM 전용 GDB와 DDD, "
            "Target에 gdbserver를 구성합니다."
        ),
        topic="원격 디버깅",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_f08",
        type="true_false",
        question=(
            "임베디드 시스템에서는 Host와 Target이 분리되는 "
            "교차 개발 환경의 특성 때문에 원격 디버깅이 활용될 수 있다."
        ),
        answer=True,
        explanation=(
            "Host와 Target이 서로 다른 시스템에서 동작하는 "
            "교차 개발 환경과 원격 디버깅은 밀접하게 연결됩니다."
        ),
        topic="원격 디버깅",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 3. -g 옵션
    # -----------------------------------------------------
    QuizQuestion(
        id="3_2_f09",
        type="multiple_choice",
        question=(
            "GDB로 소스 수준 디버깅을 수행하기 위해 "
            "gcc 컴파일 시 사용하는 옵션은?"
        ),
        options=[
            "-g",
            "-o",
            "-E",
            "-L",
        ],
        answer="-g",
        explanation=(
            "-g 옵션은 GDB에서 활용할 디버깅 정보를 "
            "실행 파일에 포함합니다."
        ),
        topic="디버깅 컴파일",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f10",
        type="multiple_choice",
        question=(
            "다음 명령의 의미로 가장 적절한 것은?"
        ),
        passage="gcc -g gdb_test.c -o gdb_test",
        options=[
            "디버깅 정보를 포함하여 gdb_test 실행 파일을 생성한다.",
            "GDB를 종료한다.",
            "breakpoint를 설정한다.",
            "Target으로 파일을 전송한다.",
        ],
        answer="디버깅 정보를 포함하여 gdb_test 실행 파일을 생성한다.",
        explanation=(
            "-g는 디버깅 정보를 포함하고, "
            "-o gdb_test는 출력 파일 이름을 지정합니다."
        ),
        topic="디버깅 컴파일",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_f11",
        type="multiple_choice",
        question=(
            "다음 GDB 실행 문법에서 pid의 의미는?"
        ),
        passage="gdb [prog] [core|pid]",
        options=[
            "현재 실행 중인 프로그램의 프로세스 ID",
            "프로그램 소스 파일의 줄 번호",
            "Target System의 IP 주소",
            "라이브러리 파일 이름",
        ],
        answer="현재 실행 중인 프로그램의 프로세스 ID",
        explanation=(
            "pid를 이용하면 현재 실행 중인 프로세스를 "
            "디버깅 대상으로 지정할 수 있습니다."
        ),
        topic="GDB 실행",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_f12",
        type="multiple_choice",
        question=(
            "프로그램이 비정상 종료되었을 때 생성된 정보를 이용하여 "
            "디버깅할 수 있는 파일은?"
        ),
        options=[
            "core dump 파일",
            "Makefile",
            "header 파일",
            "NFS 설정 파일",
        ],
        answer="core dump 파일",
        explanation=(
            "core 파일은 프로그램이 비정상적으로 종료되었을 때 "
            "생성된 정보를 활용하여 디버깅하는 데 사용할 수 있습니다."
        ),
        topic="GDB 실행",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 4. GDB 기본 명령
    # -----------------------------------------------------
    QuizQuestion(
        id="3_2_f13",
        type="multiple_choice",
        question="소스 파일의 내용을 확인하는 GDB 명령은?",
        options=[
            "list",
            "run",
            "print",
            "quit",
        ],
        answer="list",
        explanation="list는 소스 파일의 내용을 출력합니다.",
        topic="GDB 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f14",
        type="multiple_choice",
        question="Breakpoint를 지정하는 GDB 명령은?",
        options=[
            "break",
            "clear",
            "run",
            "print",
        ],
        answer="break",
        explanation=(
            "break 명령으로 특정 라인 또는 함수에 "
            "breakpoint를 설정할 수 있습니다."
        ),
        topic="GDB 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f15",
        type="multiple_choice",
        question="설정한 breakpoint를 제거하는 명령은?",
        options=[
            "clear",
            "break",
            "next",
            "continue",
        ],
        answer="clear",
        explanation="clear는 설정된 breakpoint를 제거합니다.",
        topic="GDB 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f16",
        type="multiple_choice",
        question="GDB에서 프로그램을 실행하는 명령은?",
        options=[
            "run",
            "list",
            "quit",
            "clear",
        ],
        answer="run",
        explanation="run 명령으로 디버깅 대상 프로그램을 실행합니다.",
        topic="GDB 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f17",
        type="multiple_choice",
        question="변수나 식의 현재 값을 확인하는 명령은?",
        options=[
            "print",
            "break",
            "clear",
            "quit",
        ],
        answer="print",
        explanation=(
            "print expr 형식으로 변수 또는 식의 값을 확인합니다."
        ),
        topic="GDB 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f18",
        type="multiple_choice",
        question=(
            "Breakpoint에서 멈춘 프로그램의 실행을 "
            "계속하는 명령은?"
        ),
        options=[
            "continue",
            "list",
            "break",
            "return",
        ],
        answer="continue",
        explanation=(
            "continue 또는 축약 명령 c를 사용하면 "
            "프로그램 실행을 계속할 수 있습니다."
        ),
        topic="GDB 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f19",
        type="multiple_choice",
        question=(
            "멈춘 프로그램에서 다음 문장을 실행하는 명령은?"
        ),
        options=[
            "next",
            "break",
            "clear",
            "quit",
        ],
        answer="next",
        explanation=(
            "next 또는 n을 사용하여 다음 문장을 실행합니다."
        ),
        topic="GDB 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f20",
        type="multiple_choice",
        question=(
            "호출되는 함수 내부로 진입하여 "
            "한 문장씩 실행하는 명령은?"
        ),
        options=[
            "step",
            "next",
            "continue",
            "list",
        ],
        answer="step",
        explanation=(
            "step은 호출되는 함수 내부로 진입하여 "
            "실행 과정을 확인할 수 있습니다."
        ),
        topic="GDB 명령어",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_f21",
        type="multiple_choice",
        question="GDB 프로그램을 종료하는 명령은?",
        options=[
            "quit",
            "clear",
            "return",
            "list",
        ],
        answer="quit",
        explanation="quit 명령으로 GDB를 종료합니다.",
        topic="GDB 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f22",
        type="multiple_choice",
        question=(
            "프로그램 실행 중 특정 식의 값을 "
            "계속 출력하는 GDB 명령은?"
        ),
        options=[
            "disp",
            "list",
            "run",
            "clear",
        ],
        answer="disp",
        explanation=(
            "disp expr은 프로그램 실행 중 "
            "지정한 식의 값을 계속 표시합니다."
        ),
        topic="GDB 명령어",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 5. Breakpoint / next / step
    # -----------------------------------------------------
    QuizQuestion(
        id="3_2_f23",
        type="multiple_choice",
        question=(
            "프로그램 실행을 특정 코드 위치에서 "
            "일시적으로 멈추도록 지정한 지점을 무엇이라고 하는가?"
        ),
        options=[
            "Breakpoint",
            "Target",
            "Dependency",
            "Linker",
        ],
        answer="Breakpoint",
        explanation=(
            "Breakpoint는 특정 코드 위치에서 프로그램을 "
            "멈추고 상태를 확인하기 위해 사용합니다."
        ),
        topic="Breakpoint",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f24",
        type="multiple_choice",
        question=(
            "next와 step의 차이에 대한 설명으로 "
            "가장 적절한 것은?"
        ),
        options=[
            (
                "step은 함수 내부로 진입할 수 있고 "
                "next는 일반적으로 함수 내부로 들어가지 않고 진행한다."
            ),
            "next는 GDB를 종료하고 step은 프로그램을 삭제한다.",
            "두 명령은 breakpoint를 삭제하는 명령이다.",
            "두 명령은 완전히 동일한 기능만 수행한다.",
        ],
        answer=(
            "step은 함수 내부로 진입할 수 있고 "
            "next는 일반적으로 함수 내부로 들어가지 않고 진행한다."
        ),
        explanation=(
            "next와 step 모두 단계 실행에 사용하지만 "
            "함수 호출 시 동작 방식에 차이가 있습니다."
        ),
        topic="Breakpoint",
        difficulty="어려움",
    ),

    # -----------------------------------------------------
    # 6. 변수 확인과 변경
    # -----------------------------------------------------
    QuizQuestion(
        id="3_2_f25",
        type="multiple_choice",
        question=(
            "변수의 자료형을 확인하기 위해 "
            "실습에서 사용한 GDB 명령은?"
        ),
        options=[
            "whatis",
            "print",
            "break",
            "run",
        ],
        answer="whatis",
        explanation=(
            "실습에서는 whatis sum을 이용해 "
            "sum 변수의 자료형이 int임을 확인합니다."
        ),
        topic="변수 확인",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_f26",
        type="multiple_choice",
        question=(
            "디버깅 도중 sum 변수의 값을 1000으로 "
            "변경하는 명령은?"
        ),
        options=[
            "set variable sum=1000",
            "print sum=1000",
            "break sum=1000",
            "list sum=1000",
        ],
        answer="set variable sum=1000",
        explanation=(
            "set variable 명령을 이용하면 "
            "디버깅 중 변수의 값을 변경할 수 있습니다."
        ),
        topic="변수 변경",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_f27",
        type="true_false",
        question=(
            "디버깅 도중 변수 값을 변경하면 "
            "프로그램의 이후 실행 결과도 달라질 수 있다."
        ),
        answer=True,
        explanation=(
            "변수 상태를 변경하면 이후 계산에 영향을 주기 때문에 "
            "최종 실행 결과도 달라질 수 있습니다."
        ),
        topic="변수 변경",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 7. GDB 실습
    # -----------------------------------------------------
    QuizQuestion(
        id="3_2_f28",
        type="multiple_choice",
        question=(
            "실습에서 15번째 라인에 breakpoint를 "
            "설정하기 위해 사용한 명령은?"
        ),
        options=[
            "br 15",
            "run 15",
            "print 15",
            "list 15",
        ],
        answer="br 15",
        explanation=(
            "PDF 실습에서는 br 15를 이용하여 "
            "15번째 라인에 breakpoint를 설정합니다."
        ),
        topic="GDB 실습",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_f29",
        type="multiple_choice",
        question=(
            "Breakpoint에서 sum 변수의 값을 확인하기 위해 "
            "사용한 명령은?"
        ),
        options=[
            "print sum",
            "break sum",
            "list sum",
            "quit sum",
        ],
        answer="print sum",
        explanation=(
            "print sum을 이용하여 현재 sum 값을 확인합니다."
        ),
        topic="GDB 실습",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f30",
        type="multiple_choice",
        question=(
            "실습에서 처음 확인한 sum의 값과 자료형의 "
            "올바른 조합은?"
        ),
        options=[
            "0 / int",
            "100 / float",
            "1000 / char",
            "5050 / double",
        ],
        answer="0 / int",
        explanation=(
            "Breakpoint에서 print sum 결과는 0, "
            "whatis sum 결과는 int로 확인됩니다."
        ),
        topic="GDB 실습",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 8. 프로그램 통합
    # -----------------------------------------------------
    QuizQuestion(
        id="3_2_f31",
        type="multiple_choice",
        question=(
            "모듈별 프로그램을 통합하기 전에 "
            "가장 적절한 작업은?"
        ),
        options=[
            "각 모듈의 정상 동작을 디버깅하여 확인한다.",
            "모든 오류를 무시한다.",
            "소스 파일을 모두 삭제한다.",
            "Target System을 변경한다.",
        ],
        answer="각 모듈의 정상 동작을 디버깅하여 확인한다.",
        explanation=(
            "각 모듈의 문제를 먼저 확인하고 수정한 뒤 "
            "정상 동작하는 모듈을 통합하는 것이 적절합니다."
        ),
        topic="프로그램 통합",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f32",
        type="multiple_choice",
        question=(
            "프로그램 통합 흐름으로 가장 적절한 것은?"
        ),
        options=[
            (
                "모듈 구현 → 모듈별 컴파일 → 디버깅 → "
                "오류 수정 → 정상 동작 확인 → 프로그램 통합"
            ),
            (
                "프로그램 통합 → 오류 무시 → 코드 삭제"
            ),
            (
                "Target 삭제 → Host 종료 → 프로그램 통합"
            ),
            (
                "NFS 삭제 → breakpoint 삭제 → 프로그램 작성"
            ),
        ],
        answer=(
            "모듈 구현 → 모듈별 컴파일 → 디버깅 → "
            "오류 수정 → 정상 동작 확인 → 프로그램 통합"
        ),
        explanation=(
            "각 모듈을 확인한 뒤 통합하고 "
            "통합 결과를 다시 확인해야 합니다."
        ),
        topic="프로그램 통합",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 9. Arduino 연결
    # -----------------------------------------------------
    QuizQuestion(
        id="3_2_f33",
        type="multiple_choice",
        question=(
            "Arduino 환경에서 GDB의 print와 가장 비슷한 목적으로 "
            "활용할 수 있는 것은?"
        ),
        options=[
            "Serial.print()",
            "pinMode()",
            "delay()",
            "analogWrite()만",
        ],
        answer="Serial.print()",
        explanation=(
            "Serial.print()를 이용하면 센서값이나 변수 값을 "
            "Serial Monitor에서 확인하여 디버깅할 수 있습니다."
        ),
        topic="Arduino 디버깅",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_f34",
        type="multiple_choice",
        question=(
            "Arduino 프로젝트에서 센서와 출력 장치가 함께 "
            "정상 동작하지 않을 때 가장 적절한 접근은?"
        ),
        options=[
            (
                "센서 모듈과 출력 모듈을 각각 확인한 뒤 "
                "정상 동작하면 통합한다."
            ),
            "모든 코드를 한 번에 수정한다.",
            "컴파일 메시지는 확인하지 않는다.",
            "새 보드를 구입하는 것부터 시작한다.",
        ],
        answer=(
            "센서 모듈과 출력 모듈을 각각 확인한 뒤 "
            "정상 동작하면 통합한다."
        ),
        explanation=(
            "문제를 모듈 단위로 분리하여 확인하면 "
            "원인을 더 쉽게 좁힐 수 있습니다."
        ),
        topic="Arduino 디버깅",
        difficulty="보통",
    ),
]


# =========================================================
# 학습 3-2 중간고사 대비
# =========================================================

EXAM_PRACTICE_3_2 = [

    QuizQuestion(
        id="3_2_e01",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 도구는?"
        ),
        passage=(
            "GNU 소프트웨어 시스템의 기본 디버거이며 "
            "프로그램 실행 과정을 추적하고 내부 변수의 "
            "값을 확인하거나 변경할 수 있다."
        ),
        options=[
            "GDB",
            "GCC",
            "NFS",
            "Makefile",
        ],
        answer="GDB",
        explanation=(
            "GDB는 GNU Debugger이며 프로그램 실행을 "
            "추적하고 내부 상태를 조사할 수 있습니다."
        ),
        topic="GDB 개요",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_e02",
        type="multiple_choice",
        question=(
            "다음 중 원격 모드 디버깅 환경의 "
            "구성이 올바른 것은?"
        ),
        options=[
            "Host - ARM GDB / Target - gdbserver",
            "Host - gdbserver / Target - DDD만",
            "Host - GPIO / Target - GCC",
            "Host - NFS / Target - Makefile",
        ],
        answer="Host - ARM GDB / Target - gdbserver",
        explanation=(
            "NCS의 예에서는 Host에 ARM용 GDB와 DDD, "
            "Target에 gdbserver를 구성합니다."
        ),
        topic="원격 디버깅",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_e03",
        type="multiple_choice",
        question=(
            "다음 gcc 명령에서 -g 옵션을 사용하는 이유는?"
        ),
        passage="gcc -g gdb_test.c -o gdb_test",
        options=[
            "GDB가 사용할 디버깅 정보를 포함하기 위해",
            "소스 파일을 삭제하기 위해",
            "NFS 서버를 실행하기 위해",
            "프로그램을 최적화하기 위해서만",
        ],
        answer="GDB가 사용할 디버깅 정보를 포함하기 위해",
        explanation=(
            "-g 옵션을 주어 컴파일하면 GDB에서 필요한 "
            "부가적인 디버깅 정보가 포함됩니다."
        ),
        topic="디버깅 컴파일",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_e04",
        type="multiple_choice",
        question=(
            "다음 명령과 기능의 연결이 올바르지 않은 것은?"
        ),
        options=[
            "list - 소스 파일 확인",
            "break - breakpoint 설정",
            "print - 변수 값 확인",
            "quit - 프로그램 단계 실행",
        ],
        answer="quit - 프로그램 단계 실행",
        explanation=(
            "quit는 GDB 종료 명령입니다."
        ),
        topic="GDB 명령어",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_e05",
        type="multiple_choice",
        question=(
            "다음 상황에 사용할 명령으로 가장 적절한 것은?"
        ),
        passage=(
            "15번째 코드에서 프로그램의 실행을 멈추고 "
            "변수 상태를 조사하려고 한다."
        ),
        options=[
            "break 15",
            "print 15",
            "continue 15",
            "quit 15",
        ],
        answer="break 15",
        explanation=(
            "break 명령을 사용하여 특정 라인에 "
            "breakpoint를 설정할 수 있습니다."
        ),
        topic="Breakpoint",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_e06",
        type="multiple_choice",
        question=(
            "다음 상황에서 사용할 명령은?"
        ),
        passage=(
            "Breakpoint에서 프로그램이 멈췄다. "
            "현재 sum 변수의 값을 확인하려고 한다."
        ),
        options=[
            "print sum",
            "list sum",
            "run sum",
            "clear sum",
        ],
        answer="print sum",
        explanation=(
            "print 명령으로 변수나 식의 값을 확인합니다."
        ),
        topic="GDB 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_e07",
        type="multiple_choice",
        question=(
            "함수 호출문을 만났을 때 함수 내부의 "
            "실행 과정을 직접 추적하려면 어떤 명령이 적절한가?"
        ),
        options=[
            "step",
            "next",
            "quit",
            "clear",
        ],
        answer="step",
        explanation=(
            "step은 호출되는 함수 내부로 진입하여 "
            "한 문장씩 실행합니다."
        ),
        topic="단계 실행",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_e08",
        type="multiple_choice",
        question=(
            "Breakpoint 이후 프로그램 실행을 "
            "계속하려고 할 때 사용하는 명령은?"
        ),
        options=[
            "continue",
            "break",
            "list",
            "whatis",
        ],
        answer="continue",
        explanation=(
            "continue 또는 c 명령을 사용합니다."
        ),
        topic="GDB 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="3_2_e09",
        type="multiple_choice",
        question=(
            "다음 실습 결과에 대한 설명으로 가장 적절한 것은?"
        ),
        passage=(
            "(gdb) print sum\n"
            "$2 = 0\n"
            "(gdb) whatis sum\n"
            "type = int"
        ),
        options=[
            "sum의 현재 값은 0이고 자료형은 int이다.",
            "sum의 값은 int이고 자료형은 0이다.",
            "sum은 breakpoint 이름이다.",
            "프로그램에 오류가 발생했다.",
        ],
        answer="sum의 현재 값은 0이고 자료형은 int이다.",
        explanation=(
            "print는 값, whatis는 자료형을 확인하는 데 사용됩니다."
        ),
        topic="GDB 실습",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_e10",
        type="multiple_choice",
        question=(
            "다음 명령의 실행 결과로 가장 적절한 것은?"
        ),
        passage="set variable sum=1000",
        options=[
            "디버깅 중 sum 변수의 값이 1000으로 변경된다.",
            "sum이라는 breakpoint가 생성된다.",
            "프로그램이 종료된다.",
            "sum의 자료형이 변경된다.",
        ],
        answer="디버깅 중 sum 변수의 값이 1000으로 변경된다.",
        explanation=(
            "set variable을 사용하면 프로그램 실행 중 "
            "변수 상태를 변경하여 결과 변화를 확인할 수 있습니다."
        ),
        topic="변수 변경",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_e11",
        type="multiple_choice",
        question=(
            "다음 GDB 디버깅 과정의 순서로 가장 적절한 것은?"
        ),
        options=[
            (
                "-g 옵션으로 컴파일 → GDB 실행 → "
                "breakpoint 설정 → run → 변수 확인"
            ),
            (
                "quit → 소스 삭제 → breakpoint 설정 → compile"
            ),
            (
                "Target 종료 → print → gcc 삭제 → run"
            ),
            (
                "NFS 삭제 → step → 소스 작성 → Host 종료"
            ),
        ],
        answer=(
            "-g 옵션으로 컴파일 → GDB 실행 → "
            "breakpoint 설정 → run → 변수 확인"
        ),
        explanation=(
            "디버깅 정보를 포함해 컴파일한 뒤 GDB에서 "
            "중단점을 설정하고 실행하여 상태를 조사합니다."
        ),
        topic="GDB 실습",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="3_2_e12",
        type="multiple_choice",
        question=(
            "next와 step의 차이를 가장 잘 설명한 것은?"
        ),
        options=[
            (
                "next는 함수 호출을 한 단계로 처리하고, "
                "step은 함수 내부로 진입하여 확인할 수 있다."
            ),
            "next는 종료 명령이고 step은 breakpoint 삭제 명령이다.",
            "next는 변수 값을 출력하고 step은 자료형을 출력한다.",
            "두 명령 모두 NFS 파일 전송용이다.",
        ],
        answer=(
            "next는 함수 호출을 한 단계로 처리하고, "
            "step은 함수 내부로 진입하여 확인할 수 있다."
        ),
        explanation=(
            "단계 실행에서 자주 구분해야 하는 핵심 차이입니다."
        ),
        topic="단계 실행",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="3_2_e13",
        type="multiple_choice",
        question=(
            "모듈 통합에 대한 설명으로 가장 적절한 것은?"
        ),
        options=[
            (
                "각 모듈을 디버깅하여 정상 동작을 확인한 뒤 "
                "프로그램을 통합하고 통합 결과를 다시 확인한다."
            ),
            "오류가 있는 모듈도 즉시 모두 통합한다.",
            "통합한 이후에는 디버깅할 필요가 없다.",
            "모듈별 테스트는 필요하지 않다.",
        ],
        answer=(
            "각 모듈을 디버깅하여 정상 동작을 확인한 뒤 "
            "프로그램을 통합하고 통합 결과를 다시 확인한다."
        ),
        explanation=(
            "3-2의 학습 목표는 모듈별 소스 코드를 디버깅하고 "
            "개발된 프로그램을 통합하는 것입니다."
        ),
        topic="프로그램 통합",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_e14",
        type="multiple_choice",
        question=(
            "Arduino 프로젝트에서 다음 상황의 "
            "디버깅 방법으로 가장 적절한 것은?"
        ),
        passage=(
            "초음파 센서 값에 따라 LED가 켜져야 하지만 "
            "예상대로 동작하지 않는다."
        ),
        options=[
            (
                "Serial Monitor에서 센서값을 먼저 확인하고 "
                "조건문과 LED 출력 부분을 단계적으로 점검한다."
            ),
            "모든 코드를 무작위로 수정한다.",
            "컴파일 결과를 확인하지 않는다.",
            "센서와 LED를 동시에 교체한다.",
        ],
        answer=(
            "Serial Monitor에서 센서값을 먼저 확인하고 "
            "조건문과 LED 출력 부분을 단계적으로 점검한다."
        ),
        explanation=(
            "디버깅은 관찰 가능한 값을 이용해 "
            "문제 범위를 단계적으로 좁히는 과정입니다."
        ),
        topic="Arduino 디버깅",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_e15",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 GDB 명령어를 쓰시오."
        ),
        passage=(
            "프로그램을 특정 코드 위치에서 멈추도록 "
            "중단점을 설정한다."
        ),
        answer=[
            "break",
            "br",
            "BREAK",
        ],
        explanation=(
            "break 명령을 이용하여 breakpoint를 설정합니다."
        ),
        topic="GDB 명령어",
        difficulty="보통",
    ),

    QuizQuestion(
        id="3_2_e16",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 GDB 명령어를 쓰시오."
        ),
        passage=(
            "변수의 자료형을 확인한다."
        ),
        answer=[
            "whatis",
            "WHATIS",
        ],
        explanation=(
            "실습에서는 whatis sum을 이용하여 "
            "sum 변수의 자료형을 확인합니다."
        ),
        topic="GDB 실습",
        difficulty="어려움",
    ),
]


# =========================================================
# 전체 문제
# =========================================================

ALL_QUIZ_3_2 = (
    FORMATIVE_QUIZ_3_2
    + EXAM_PRACTICE_3_2
)