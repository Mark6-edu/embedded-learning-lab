from __future__ import annotations

from utils.quiz import QuizQuestion


# =========================================================
# 학습 2-1 형성평가
# 개발 도구 선정
# =========================================================

FORMATIVE_QUIZ_2_1 = [

    # -----------------------------------------------------
    # 1. 교차 개발 환경
    # -----------------------------------------------------
    QuizQuestion(
        id="2_1_f01",
        type="multiple_choice",
        question=(
            "임베디드 애플리케이션을 개발하기 위해 "
            "타깃 시스템과 별도로 호스트 시스템에 구성하는 "
            "개발 환경을 무엇이라고 하는가?"
        ),
        options=[
            "교차 개발 환경",
            "분산 처리 환경",
            "웹 개발 환경",
            "가상 네트워크 환경",
        ],
        answer="교차 개발 환경",
        explanation=(
            "임베디드 시스템은 타깃 장치 자체에서 개발하기 어려운 경우가 많아 "
            "호스트 시스템에서 개발한 뒤 타깃 시스템으로 전송하는 "
            "교차 개발 환경을 사용합니다."
        ),
        topic="교차 개발 환경",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f02",
        type="multiple_choice",
        question=(
            "교차 개발 환경에서 프로그램을 작성하고 컴파일하며 "
            "타깃 시스템을 모니터링하는 시스템은?"
        ),
        options=[
            "Host System",
            "Target System",
            "Sensor System",
            "Database System",
        ],
        answer="Host System",
        explanation=(
            "Host System은 프로그램 작성, 컴파일, 디버깅 및 "
            "타깃 시스템 모니터링 등에 사용되는 개발용 시스템입니다."
        ),
        topic="Host / Target",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f03",
        type="multiple_choice",
        question=(
            "개발된 운영체제, 디바이스 드라이버, 애플리케이션 등이 "
            "실제로 실행되는 시스템은?"
        ),
        options=[
            "Target System",
            "Host System",
            "Cloud System",
            "Database System",
        ],
        answer="Target System",
        explanation=(
            "Target System은 개발 결과물이 실제로 동작하는 "
            "임베디드 하드웨어 시스템입니다."
        ),
        topic="Host / Target",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f04",
        type="true_false",
        question=(
            "교차 개발 환경에서는 Host System과 Target System이 "
            "항상 동일한 프로세서와 운영체제를 사용해야 한다."
        ),
        answer=False,
        explanation=(
            "교차 개발 환경에서는 Host System과 Target System의 "
            "프로세서나 운영체제가 서로 다를 수 있습니다."
        ),
        topic="교차 개발 환경",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 2. 인터페이스
    # -----------------------------------------------------
    QuizQuestion(
        id="2_1_f05",
        type="multiple_choice",
        question=(
            "Host System과 Target System 사이에서 "
            "타깃 시스템의 동작을 모니터링하는 용도로 "
            "사용할 수 있는 인터페이스는?"
        ),
        options=[
            "Serial",
            "HDMI",
            "VGA",
            "PS/2",
        ],
        answer="Serial",
        explanation=(
            "Serial 인터페이스는 타깃 시스템의 상태나 "
            "동작 결과를 모니터링하는 데 활용할 수 있습니다."
        ),
        topic="개발 인터페이스",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f06",
        type="multiple_choice",
        question=(
            "Host System과 Target System 사이의 "
            "고속 데이터 전송에 활용될 수 있는 인터페이스는?"
        ),
        options=[
            "Ethernet",
            "Serial",
            "GPIO",
            "PWM",
        ],
        answer="Ethernet",
        explanation=(
            "Ethernet은 TFTP, NFS 등을 활용하여 "
            "호스트와 타깃 사이의 고속 데이터 전송에 사용할 수 있습니다."
        ),
        topic="개발 인터페이스",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_f07",
        type="multiple_choice",
        question=(
            "타깃 시스템을 디버깅하기 위해 사용하는 "
            "대표적인 인터페이스는?"
        ),
        options=[
            "JTAG",
            "PWM",
            "ADC",
            "GPIO",
        ],
        answer="JTAG",
        explanation=(
            "JTAG는 타깃 시스템의 내부 상태를 확인하고 "
            "디버깅하는 데 활용되는 대표적인 인터페이스입니다."
        ),
        topic="개발 인터페이스",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f08",
        type="multiple_choice",
        question=(
            "타깃 시스템의 이미지 업데이트 등에 "
            "활용할 수 있는 인터페이스는?"
        ),
        options=[
            "USB",
            "GPIO",
            "PWM",
            "ADC",
        ],
        answer="USB",
        explanation=(
            "NCS 학습모듈에서는 USB를 이미지 업데이트 등의 "
            "용도로 사용할 수 있다고 설명합니다."
        ),
        topic="개발 인터페이스",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 3. Tool Chain
    # -----------------------------------------------------
    QuizQuestion(
        id="2_1_f09",
        type="multiple_choice",
        question=(
            "교차 개발 환경을 위한 여러 개발 도구의 집합을 "
            "무엇이라고 하는가?"
        ),
        options=[
            "Tool Chain",
            "Data Chain",
            "Process Tree",
            "File System",
        ],
        answer="Tool Chain",
        explanation=(
            "Tool Chain은 교차 컴파일러, 어셈블러, 링커, "
            "디버거 등의 개발 도구 집합을 의미합니다."
        ),
        topic="Tool Chain",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f10",
        type="multiple_choice",
        question=(
            "Host System에서 Target System의 CPU와 운영체제에 맞는 "
            "실행 코드를 생성하는 개발 도구는?"
        ),
        options=[
            "Cross Compiler",
            "Debugger",
            "Editor",
            "Loader",
        ],
        answer="Cross Compiler",
        explanation=(
            "Cross Compiler는 호스트 시스템에서 실행되지만 "
            "타깃 시스템용 실행 코드를 생성합니다."
        ),
        topic="Tool Chain",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_f11",
        type="multiple_choice",
        question=(
            "여러 오브젝트 파일과 라이브러리를 결합하여 "
            "실행 가능한 결과물을 만드는 도구는?"
        ),
        options=[
            "Linker",
            "Assembler",
            "Debugger",
            "Editor",
        ],
        answer="Linker",
        explanation=(
            "Linker는 여러 오브젝트 파일과 라이브러리를 연결해 "
            "최종 실행 결과물을 만듭니다."
        ),
        topic="Tool Chain",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_f12",
        type="multiple_choice",
        question=(
            "어셈블리 언어로 작성된 코드를 "
            "기계어 형태로 변환하는 도구는?"
        ),
        options=[
            "Assembler",
            "Linker",
            "Debugger",
            "Editor",
        ],
        answer="Assembler",
        explanation=(
            "Assembler는 어셈블리 언어를 기계어 또는 "
            "오브젝트 코드 형태로 변환합니다."
        ),
        topic="Tool Chain",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_f13",
        type="multiple_choice",
        question=(
            "프로그램의 실행 상태와 오류를 분석하는 데 "
            "사용하는 개발 도구는?"
        ),
        options=[
            "Debugger",
            "Linker",
            "Assembler",
            "Compiler",
        ],
        answer="Debugger",
        explanation=(
            "Debugger는 프로그램 실행 상태를 확인하고 "
            "오류 원인을 분석하는 데 사용합니다."
        ),
        topic="Tool Chain",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 4. 타깃 보드
    # -----------------------------------------------------
    QuizQuestion(
        id="2_1_f14",
        type="multiple_choice",
        question=(
            "개발된 운영체제, 디바이스 드라이버, 애플리케이션을 "
            "다운로드하여 실행할 수 있는 하드웨어 시스템은?"
        ),
        options=[
            "타깃 보드",
            "호스트 PC",
            "웹 서버",
            "데이터베이스",
        ],
        answer="타깃 보드",
        explanation=(
            "타깃 보드는 임베디드 소프트웨어가 실제로 "
            "실행되는 하드웨어입니다."
        ),
        topic="타깃 보드",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f15",
        type="true_false",
        question=(
            "타깃 보드의 개발 환경을 구성할 때 "
            "회로도, 메모리 맵, I/O 맵, 디버깅 포트 등을 "
            "확인할 필요가 있다."
        ),
        answer=True,
        explanation=(
            "타깃 보드의 하드웨어 구조를 정확히 이해해야 "
            "적절한 개발 환경을 구성할 수 있습니다."
        ),
        topic="타깃 보드",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 5. RISC / CISC
    # -----------------------------------------------------
    QuizQuestion(
        id="2_1_f16",
        type="multiple_choice",
        question=(
            "복잡한 명령어를 줄이고 사용 빈도가 높은 "
            "단순한 명령어 중심으로 구성된 프로세서 구조는?"
        ),
        options=[
            "RISC",
            "CISC",
            "FIFO",
            "LIFO",
        ],
        answer="RISC",
        explanation=(
            "RISC는 Reduced Instruction Set Computer의 개념으로 "
            "단순하고 사용 빈도가 높은 명령어를 중심으로 구성됩니다."
        ),
        topic="RISC / CISC",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f17",
        type="multiple_choice",
        question=(
            "명령어의 수가 많고 명령어 길이와 실행 사이클이 "
            "다양할 수 있는 프로세서 구조는?"
        ),
        options=[
            "CISC",
            "RISC",
            "UART",
            "GPIO",
        ],
        answer="CISC",
        explanation=(
            "CISC는 복잡한 명령어를 다수 포함하며 "
            "명령어 길이나 실행 사이클이 다양할 수 있습니다."
        ),
        topic="RISC / CISC",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f18",
        type="true_false",
        question=(
            "RISC 구조는 일반적으로 Load / Store 중심으로 "
            "메모리에 접근한다."
        ),
        answer=True,
        explanation=(
            "RISC에서는 메모리 접근을 Load와 Store 명령 중심으로 "
            "구성하는 특징이 있습니다."
        ),
        topic="RISC / CISC",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 6. Interrupt / GPIO / 통신
    # -----------------------------------------------------
    QuizQuestion(
        id="2_1_f19",
        type="multiple_choice",
        question=(
            "CPU가 현재 처리 중인 작업을 잠시 중단하고 "
            "다른 처리를 수행하도록 알리는 방식은?"
        ),
        options=[
            "Interrupt",
            "Polling",
            "Linking",
            "Compiling",
        ],
        answer="Interrupt",
        explanation=(
            "Interrupt는 특정 사건 발생 시 CPU가 현재 작업을 잠시 중단하고 "
            "해당 처리를 수행하도록 하는 방식입니다."
        ),
        topic="Interrupt",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f20",
        type="short_answer",
        question=(
            "GPIO의 영문 전체 명칭을 쓰시오."
        ),
        answer=[
            "General Purpose Input/Output",
            "general purpose input/output",
            "General Purpose Input Output",
            "general purpose input output",
        ],
        explanation=(
            "GPIO는 General Purpose Input/Output의 약자입니다."
        ),
        topic="GPIO",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_f21",
        type="multiple_choice",
        question=(
            "GPIO에 대한 설명으로 가장 적절한 것은?"
        ),
        options=[
            "입력 또는 출력으로 사용할 수 있는 범용 디지털 신호 핀",
            "운영체제를 설치하기 위한 저장 장치",
            "프로그램을 컴파일하는 소프트웨어",
            "네트워크 주소를 자동으로 할당하는 프로토콜",
        ],
        answer="입력 또는 출력으로 사용할 수 있는 범용 디지털 신호 핀",
        explanation=(
            "GPIO는 사용 목적에 따라 입력 또는 출력으로 설정해 "
            "주변 장치를 제어하는 데 사용할 수 있습니다."
        ),
        topic="GPIO",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f22",
        type="multiple_choice",
        question=(
            "다음 중 임베디드 시스템에서 주변 장치와의 "
            "통신에 사용되는 방식으로만 구성된 것은?"
        ),
        options=[
            "I2C, SPI, UART",
            "HTTP, HTML, CSS",
            "FIFO, LIFO, DFS",
            "RAM, ROM, SSD",
        ],
        answer="I2C, SPI, UART",
        explanation=(
            "I2C, SPI, UART는 프로세서와 주변 장치 사이의 "
            "통신에 널리 사용되는 방식입니다."
        ),
        topic="통신 인터페이스",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 7. Arduino 연결
    # -----------------------------------------------------
    QuizQuestion(
        id="2_1_f23",
        type="multiple_choice",
        question=(
            "Arduino 수업 환경에서 Host System에 "
            "해당하는 것으로 가장 적절한 것은?"
        ),
        options=[
            "학생이 사용하는 PC",
            "Arduino UNO",
            "초음파 센서",
            "서보모터",
        ],
        answer="학생이 사용하는 PC",
        explanation=(
            "PC에서 코드를 작성하고 컴파일한 뒤 Arduino로 전송하므로 "
            "PC를 Host System으로 이해할 수 있습니다."
        ),
        topic="Arduino 연결",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_f24",
        type="multiple_choice",
        question=(
            "Arduino 수업 환경에서 Target System에 "
            "해당하는 것으로 가장 적절한 것은?"
        ),
        options=[
            "Arduino UNO",
            "학생 PC",
            "웹 브라우저",
            "문서 작성 프로그램",
        ],
        answer="Arduino UNO",
        explanation=(
            "작성한 프로그램이 실제로 실행되는 Arduino 보드는 "
            "Target System으로 해석할 수 있습니다."
        ),
        topic="Arduino 연결",
        difficulty="쉬움",
    ),
]


# =========================================================
# 학습 2-1 중간고사 대비
# =========================================================

EXAM_PRACTICE_2_1 = [

    QuizQuestion(
        id="2_1_e01",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 시스템은?"
        ),
        passage=(
            "프로그램을 작성하고 컴파일한 뒤 "
            "타깃 시스템으로 전송하며, 타깃 시스템의 "
            "동작을 모니터링하는 데 사용된다."
        ),
        options=[
            "Host System",
            "Target System",
            "Sensor System",
            "Storage System",
        ],
        answer="Host System",
        explanation=(
            "Host System은 임베디드 프로그램을 개발하는 "
            "개발용 시스템입니다."
        ),
        topic="교차 개발 환경",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_e02",
        type="multiple_choice",
        question=(
            "다음 연결 중 가장 적절하지 않은 것은?"
        ),
        options=[
            "Serial - 타깃 시스템 모니터링",
            "Ethernet - 고속 데이터 전송",
            "JTAG - 디버깅",
            "GPIO - 프로그램 컴파일",
        ],
        answer="GPIO - 프로그램 컴파일",
        explanation=(
            "GPIO는 범용 입출력 핀으로 주변 장치를 제어하거나 "
            "상태를 입력받는 데 사용됩니다."
        ),
        topic="개발 인터페이스",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_e03",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 개발 도구는?"
        ),
        passage=(
            "호스트 시스템에서 실행되지만 "
            "타깃 시스템의 프로세서와 운영체제에 맞는 "
            "실행 코드를 생성한다."
        ),
        options=[
            "Cross Compiler",
            "Debugger",
            "Linker",
            "Text Editor",
        ],
        answer="Cross Compiler",
        explanation=(
            "Cross Compiler는 개발 환경과 실행 대상 환경이 "
            "서로 다른 교차 개발 환경에서 핵심적인 도구입니다."
        ),
        topic="Tool Chain",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_e04",
        type="multiple_choice",
        question=(
            "다음 중 Tool Chain에 포함되는 개발 도구를 "
            "올바르게 묶은 것은?"
        ),
        options=[
            "Cross Compiler · Assembler · Linker · Debugger",
            "Sensor · Motor · LED · Buzzer",
            "HTML · CSS · HTTP · DNS",
            "Stack · Queue · Tree · Graph",
        ],
        answer="Cross Compiler · Assembler · Linker · Debugger",
        explanation=(
            "Tool Chain은 컴파일, 어셈블, 링크, 디버깅 등에 "
            "필요한 여러 개발 도구로 구성됩니다."
        ),
        topic="Tool Chain",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_e05",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 프로세서 구조는?"
        ),
        passage=(
            "사용 빈도가 높은 단순한 명령어를 중심으로 구성하고 "
            "Load / Store 방식으로 메모리에 접근한다."
        ),
        options=[
            "RISC",
            "CISC",
            "UART",
            "JTAG",
        ],
        answer="RISC",
        explanation=(
            "RISC는 단순한 명령어와 Load / Store 중심의 "
            "구조가 대표적인 특징입니다."
        ),
        topic="RISC / CISC",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_e06",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 개념은?"
        ),
        passage=(
            "현재 처리 중인 작업을 잠시 중단시키고 "
            "특정 사건에 대한 처리를 우선 수행하도록 "
            "CPU에 알린다."
        ),
        options=[
            "Interrupt",
            "Linking",
            "Compiling",
            "Caching",
        ],
        answer="Interrupt",
        explanation=(
            "Interrupt는 특정 사건 발생 시 CPU가 "
            "별도의 처리를 수행하도록 하는 방식입니다."
        ),
        topic="Interrupt",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_e07",
        type="multiple_choice",
        question=(
            "다음 중 Arduino 수업 환경과 "
            "교차 개발 환경의 연결이 가장 적절한 것은?"
        ),
        options=[
            "학생 PC = Host System / Arduino UNO = Target System",
            "Arduino UNO = Host System / 학생 PC = Target System",
            "초음파 센서 = Host System / LED = Target System",
            "Arduino IDE = Target System / Arduino UNO = Compiler",
        ],
        answer="학생 PC = Host System / Arduino UNO = Target System",
        explanation=(
            "PC에서 프로그램을 작성하고 컴파일한 뒤 "
            "Arduino 보드에서 실행하므로 이런 식으로 대응할 수 있습니다."
        ),
        topic="Arduino 연결",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_e08",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 영문 약어를 쓰시오."
        ),
        passage=(
            "입력 또는 출력으로 사용할 수 있으며 "
            "사용자가 제어할 수 있는 범용 디지털 신호 핀"
        ),
        answer=[
            "GPIO",
            "gpio",
        ],
        explanation=(
            "GPIO는 General Purpose Input/Output의 약자입니다."
        ),
        topic="GPIO",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_1_e09",
        type="multiple_choice",
        question=(
            "다음 중 타깃 보드를 분석할 때 "
            "검토 대상으로 가장 거리가 먼 것은?"
        ),
        options=[
            "회로도",
            "메모리 맵",
            "I/O 맵",
            "학생의 좌석 배치",
        ],
        answer="학생의 좌석 배치",
        explanation=(
            "타깃 보드 분석에서는 회로도, 메모리 맵, "
            "I/O 맵, 디버깅 포트 등 하드웨어 관련 정보를 확인합니다."
        ),
        topic="타깃 보드",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_1_e10",
        type="multiple_choice",
        question=(
            "다음 중 프로세서와 주변 장치 사이의 "
            "통신 방식으로 적절한 것은?"
        ),
        options=[
            "I2C · SPI · UART",
            "HTTP · FTP · SMTP",
            "HTML · CSS · JavaScript",
            "DFS · BFS · Dijkstra",
        ],
        answer="I2C · SPI · UART",
        explanation=(
            "I2C, SPI, UART는 임베디드 시스템에서 "
            "프로세서와 주변 장치 사이의 통신에 활용됩니다."
        ),
        topic="통신 인터페이스",
        difficulty="쉬움",
    ),
]


# =========================================================
# 전체 문제
# =========================================================

ALL_QUIZ_2_1 = (
    FORMATIVE_QUIZ_2_1
    + EXAM_PRACTICE_2_1
)