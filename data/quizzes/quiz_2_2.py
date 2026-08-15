from __future__ import annotations

from utils.quiz import QuizQuestion


# =========================================================
# 학습 2-2 형성평가
# 애플리케이션 개발 환경 구축
# =========================================================

FORMATIVE_QUIZ_2_2 = [

    # -----------------------------------------------------
    # 1. 개발 환경 기본 구조
    # -----------------------------------------------------
    QuizQuestion(
        id="2_2_f01",
        type="multiple_choice",
        question=(
            "임베디드 애플리케이션 개발 환경에서 "
            "프로그램을 작성하고 컴파일하는 시스템은?"
        ),
        options=[
            "Host System",
            "Target System",
            "Sensor System",
            "Storage System",
        ],
        answer="Host System",
        explanation=(
            "Host System에서 소스 코드를 작성하고 "
            "Target System용 실행 파일을 생성합니다."
        ),
        topic="개발 환경 구성",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_2_f02",
        type="multiple_choice",
        question=(
            "Host System에서 생성된 프로그램이 "
            "실제로 실행되는 시스템은?"
        ),
        options=[
            "Target System",
            "Host System",
            "Virtual Machine",
            "Text Editor",
        ],
        answer="Target System",
        explanation=(
            "Target System은 교차 컴파일된 프로그램이 "
            "실제로 실행되는 임베디드 시스템입니다."
        ),
        topic="개발 환경 구성",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 2. 가상 머신
    # -----------------------------------------------------
    QuizQuestion(
        id="2_2_f03",
        type="multiple_choice",
        question=(
            "Host PC에서 Linux 개발 환경을 구성하기 위해 "
            "사용할 수 있는 가상화 소프트웨어의 예는?"
        ),
        options=[
            "VirtualBox",
            "Notepad",
            "PowerPoint",
            "Paint",
        ],
        answer="VirtualBox",
        explanation=(
            "PDF에서는 VMware나 Oracle VM VirtualBox 등을 "
            "이용하여 Linux 기반 Host 환경을 구성할 수 있다고 설명합니다."
        ),
        topic="가상 머신",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_2_f04",
        type="true_false",
        question=(
            "Host System의 Linux 환경은 반드시 "
            "PC에 직접 설치해야만 한다."
        ),
        answer=False,
        explanation=(
            "Linux를 직접 설치할 수도 있지만 "
            "VirtualBox나 VMware 등의 가상화 환경을 이용할 수도 있습니다."
        ),
        topic="가상 머신",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 3. NFS
    # -----------------------------------------------------
    QuizQuestion(
        id="2_2_f05",
        type="short_answer",
        question=(
            "NFS의 영문 전체 명칭을 쓰시오."
        ),
        answer=[
            "Network File System",
            "network file system",
        ],
        explanation=(
            "NFS는 Network File System의 약자입니다."
        ),
        topic="NFS",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_f06",
        type="multiple_choice",
        question=(
            "NFS를 사용하는 가장 적절한 목적은?"
        ),
        options=[
            (
                "네트워크를 통해 다른 시스템의 "
                "파일이나 디렉터리를 공유하기 위해"
            ),
            "프로그램의 문법 오류를 자동 수정하기 위해",
            "CPU의 명령어 수를 늘리기 위해",
            "디지털 핀의 전압을 측정하기 위해",
        ],
        answer=(
            "네트워크를 통해 다른 시스템의 "
            "파일이나 디렉터리를 공유하기 위해"
        ),
        explanation=(
            "NFS는 네트워크를 통해 파일 시스템을 공유하는 방식이며, "
            "Host에서 만든 실행 파일을 Target에서 접근하는 데 활용할 수 있습니다."
        ),
        topic="NFS",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_2_f07",
        type="multiple_choice",
        question=(
            "NFS 서버에서 공유 디렉터리를 설정하기 위해 "
            "수정하는 파일은?"
        ),
        options=[
            "/etc/exports",
            "/etc/passwd",
            "/etc/hosts",
            "/etc/profile",
        ],
        answer="/etc/exports",
        explanation=(
            "/etc/exports 파일에는 NFS로 공유할 "
            "디렉터리와 접근 조건을 설정합니다."
        ),
        topic="NFS",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_f08",
        type="true_false",
        question=(
            "NFS 설정 파일을 수정한 뒤에는 "
            "NFS 서비스를 재시작하여 변경 내용을 "
            "반영할 수 있다."
        ),
        answer=True,
        explanation=(
            "PDF에서도 /etc/exports 수정 후 "
            "NFS 데몬을 재시작하여 설정값을 반영합니다."
        ),
        topic="NFS",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 4. Linux 명령어
    # -----------------------------------------------------
    QuizQuestion(
        id="2_2_f09",
        type="multiple_choice",
        question=(
            "Linux에서 새로운 디렉터리를 생성하는 명령어는?"
        ),
        options=[
            "mkdir",
            "cp",
            "tar",
            "file",
        ],
        answer="mkdir",
        explanation=(
            "mkdir은 Make Directory의 의미로 "
            "새로운 디렉터리를 생성합니다."
        ),
        topic="Linux 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_2_f10",
        type="multiple_choice",
        question=(
            "Linux에서 파일 또는 디렉터리를 복사하는 명령어는?"
        ),
        options=[
            "cp",
            "mkdir",
            "source",
            "env",
        ],
        answer="cp",
        explanation=(
            "cp 명령은 파일이나 디렉터리를 복사할 때 사용합니다."
        ),
        topic="Linux 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_2_f11",
        type="multiple_choice",
        question=(
            "압축된 교차 컴파일러 파일을 해제할 때 "
            "사용할 수 있는 명령어는?"
        ),
        options=[
            "tar",
            "env",
            "source",
            "file",
        ],
        answer="tar",
        explanation=(
            "PDF 예시에서는 tar xvfj 명령을 이용해 "
            "교차 컴파일러 압축 파일을 해제합니다."
        ),
        topic="Linux 명령어",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_f12",
        type="multiple_choice",
        question=(
            "텍스트 파일을 편집하기 위해 "
            "PDF 예시에서 사용하는 명령어는?"
        ),
        options=[
            "vi",
            "cp",
            "mkdir",
            "file",
        ],
        answer="vi",
        explanation=(
            "PDF에서는 vi /root/.bashrc, vi /etc/exports와 같이 "
            "vi 편집기를 사용합니다."
        ),
        topic="Linux 명령어",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_2_f13",
        type="multiple_choice",
        question=(
            "변경한 .bashrc 내용을 현재 셸에 "
            "즉시 적용하기 위해 사용하는 명령어는?"
        ),
        options=[
            "source",
            "tar",
            "file",
            "mkdir",
        ],
        answer="source",
        explanation=(
            "source /root/.bashrc를 실행하면 "
            "변경된 환경 설정을 현재 셸에 적용할 수 있습니다."
        ),
        topic="환경 변수",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_f14",
        type="multiple_choice",
        question=(
            "현재 PATH 환경 변수를 확인하기 위해 "
            "사용할 수 있는 명령은?"
        ),
        options=[
            "env | grep PATH",
            "mkdir PATH",
            "tar PATH",
            "cp PATH",
        ],
        answer="env | grep PATH",
        explanation=(
            "PDF에서는 env | grep PATH 명령을 이용해 "
            "PATH 환경 변수 설정 결과를 확인합니다."
        ),
        topic="환경 변수",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_f15",
        type="multiple_choice",
        question=(
            "생성된 실행 파일이 어떤 프로세서용인지 "
            "파일 형식을 확인할 때 사용하는 명령어는?"
        ),
        options=[
            "file",
            "mkdir",
            "source",
            "vi",
        ],
        answer="file",
        explanation=(
            "file tc_test를 실행하면 실행 파일이 "
            "ARM용 ELF 파일인지 확인할 수 있습니다."
        ),
        topic="Linux 명령어",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 5. 교차 컴파일러 / PATH
    # -----------------------------------------------------
    QuizQuestion(
        id="2_2_f16",
        type="multiple_choice",
        question=(
            "교차 컴파일러가 설치된 위치를 "
            "명령어 검색 경로에 추가하기 위해 사용하는 환경 변수는?"
        ),
        options=[
            "PATH",
            "HOME",
            "USER",
            "SHELL",
        ],
        answer="PATH",
        explanation=(
            "교차 컴파일러 실행 파일이 있는 디렉터리를 "
            "PATH 환경 변수에 추가합니다."
        ),
        topic="교차 컴파일러",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_2_f17",
        type="multiple_choice",
        question=(
            "PDF 예시에서 PATH 환경 변수를 수정하기 위해 "
            "편집하는 파일은?"
        ),
        options=[
            "/root/.bashrc",
            "/etc/exports",
            "/etc/passwd",
            "/boot/config",
        ],
        answer="/root/.bashrc",
        explanation=(
            "PDF에서는 /root/.bashrc 파일에 "
            "교차 컴파일러의 경로를 추가합니다."
        ),
        topic="교차 컴파일러",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_f18",
        type="multiple_choice",
        question=(
            "교차 컴파일러가 정상 설치되었는지 "
            "버전과 설정을 확인하기 위해 사용하는 명령은?"
        ),
        options=[
            "arm-unknown-linux-gnueabi-gcc -v",
            "mkdir gcc",
            "source gcc",
            "file gcc",
        ],
        answer="arm-unknown-linux-gnueabi-gcc -v",
        explanation=(
            "gcc -v 옵션을 사용하면 컴파일러 정보와 "
            "설치 상태를 확인할 수 있습니다."
        ),
        topic="교차 컴파일러",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 6. 교차 컴파일
    # -----------------------------------------------------
    QuizQuestion(
        id="2_2_f19",
        type="multiple_choice",
        question=(
            "다음 명령의 역할로 가장 적절한 것은?"
        ),
        passage=(
            "arm-unknown-linux-gnueabi-gcc "
            "tc_test.c -o tc_test"
        ),
        options=[
            "tc_test.c를 ARM용 실행 파일 tc_test로 컴파일한다.",
            "tc_test 파일을 삭제한다.",
            "NFS 서버를 재시작한다.",
            "PATH 환경 변수를 출력한다.",
        ],
        answer=(
            "tc_test.c를 ARM용 실행 파일 tc_test로 컴파일한다."
        ),
        explanation=(
            "ARM용 교차 컴파일러를 이용해 "
            "tc_test.c를 tc_test라는 실행 파일로 생성합니다."
        ),
        topic="교차 컴파일",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_f20",
        type="multiple_choice",
        question=(
            "gcc 명령에서 -o 옵션의 역할로 가장 적절한 것은?"
        ),
        options=[
            "생성할 결과 파일의 이름을 지정한다.",
            "NFS 서버를 실행한다.",
            "환경 변수를 삭제한다.",
            "디렉터리를 생성한다.",
        ],
        answer="생성할 결과 파일의 이름을 지정한다.",
        explanation=(
            "예를 들어 -o tc_test는 최종 결과 파일의 이름을 "
            "tc_test로 지정합니다."
        ),
        topic="교차 컴파일",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_f21",
        type="true_false",
        question=(
            "ARM용으로 교차 컴파일된 실행 파일은 "
            "x86 기반 Host System에서 정상 실행되지 않을 수 있다."
        ),
        answer=True,
        explanation=(
            "실행 파일이 Target System의 ARM 프로세서용으로 "
            "생성되었기 때문에 Host와 프로세서 구조가 다르면 "
            "실행되지 않을 수 있습니다."
        ),
        topic="교차 컴파일",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_f22",
        type="multiple_choice",
        question=(
            "file tc_test 명령 결과로 ARM용 실행 파일임을 "
            "판단할 수 있는 핵심 단어는?"
        ),
        options=[
            "ARM",
            "JPEG",
            "HTML",
            "ASCII only",
        ],
        answer="ARM",
        explanation=(
            "PDF의 예에서는 'ELF 32-bit LSB executable, ARM' "
            "형태로 실행 파일의 구조가 표시됩니다."
        ),
        topic="실행 파일 확인",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 7. Target 전송 및 실행
    # -----------------------------------------------------
    QuizQuestion(
        id="2_2_f23",
        type="multiple_choice",
        question=(
            "Host System에서 생성한 실행 파일을 "
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
            "NFS를 이용하면 Host에서 생성된 실행 파일을 "
            "Target에서 접근하여 실행할 수 있습니다."
        ),
        topic="Target 실행",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_2_f24",
        type="multiple_choice",
        question=(
            "교차 개발 환경에서 가장 올바른 개발 순서는?"
        ),
        options=[
            (
                "소스 작성 → 교차 컴파일 → 파일 형식 확인 → "
                "Target 전달 → Target 실행"
            ),
            (
                "Target 실행 → 소스 작성 → 파일 삭제 → 컴파일"
            ),
            (
                "NFS 삭제 → Host 종료 → 프로그램 작성"
            ),
            (
                "GPIO 설정 → 웹 브라우저 실행 → 데이터베이스 생성"
            ),
        ],
        answer=(
            "소스 작성 → 교차 컴파일 → 파일 형식 확인 → "
            "Target 전달 → Target 실행"
        ),
        explanation=(
            "Host에서 코드를 작성하고 Target용으로 컴파일한 후 "
            "실행 파일을 Target으로 전달하여 실행하는 것이 "
            "기본적인 흐름입니다."
        ),
        topic="개발 환경 흐름",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 8. 문제 해결
    # -----------------------------------------------------
    QuizQuestion(
        id="2_2_f25",
        type="multiple_choice",
        question=(
            "교차 컴파일러 명령어를 입력했는데 "
            "'command not found'가 발생했다. "
            "가장 먼저 확인할 항목은?"
        ),
        options=[
            "PATH 환경 변수",
            "센서의 색상",
            "모터의 회전 방향",
            "웹 브라우저 기록",
        ],
        answer="PATH 환경 변수",
        explanation=(
            "컴파일러가 설치되어 있어도 해당 디렉터리가 "
            "PATH에 포함되지 않으면 명령을 찾지 못할 수 있습니다."
        ),
        topic="문제 해결",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_f26",
        type="multiple_choice",
        question=(
            "NFS 공유 디렉터리에 Target System이 "
            "접근하지 못할 때 우선 확인할 사항은?"
        ),
        options=[
            "/etc/exports 설정과 NFS 서비스 상태",
            "CISC 명령어 개수",
            "GPIO 핀 번호만 확인",
            "HTML 문법",
        ],
        answer="/etc/exports 설정과 NFS 서비스 상태",
        explanation=(
            "NFS 접근 문제에서는 공유 설정 파일과 "
            "NFS 서비스의 정상 동작 여부를 확인해야 합니다."
        ),
        topic="문제 해결",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 9. Arduino 연결
    # -----------------------------------------------------
    QuizQuestion(
        id="2_2_f27",
        type="multiple_choice",
        question=(
            "NCS의 'Target으로 실행 파일 전송' 과정과 "
            "Arduino 환경에서 가장 유사한 과정은?"
        ),
        options=[
            "Upload",
            "새 파일 만들기",
            "브라우저 새로고침",
            "문서 인쇄",
        ],
        answer="Upload",
        explanation=(
            "Arduino IDE의 Upload는 Host에서 생성한 프로그램을 "
            "Arduino Target Board로 전달하는 과정으로 볼 수 있습니다."
        ),
        topic="Arduino 연결",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="2_2_f28",
        type="multiple_choice",
        question=(
            "Arduino 환경에서 프로그램 실행 결과를 "
            "확인하는 방법으로 가장 적절한 것은?"
        ),
        options=[
            "Serial Monitor 또는 실제 하드웨어 동작 확인",
            "NFS 설정 파일만 확인",
            "파일 이름만 변경",
            "가상 머신만 종료",
        ],
        answer="Serial Monitor 또는 실제 하드웨어 동작 확인",
        explanation=(
            "Arduino에서는 Serial Monitor 또는 LED, 센서, "
            "모터 등의 실제 동작을 통해 실행 결과를 확인할 수 있습니다."
        ),
        topic="Arduino 연결",
        difficulty="쉬움",
    ),
]


# =========================================================
# 학습 2-2 중간고사 대비
# =========================================================

EXAM_PRACTICE_2_2 = [

    QuizQuestion(
        id="2_2_e01",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 시스템은?"
        ),
        passage=(
            "소스 코드를 작성하고 Target System용 실행 파일을 "
            "생성하기 위해 교차 컴파일러가 설치되어 있다."
        ),
        options=[
            "Host System",
            "Target System",
            "Sensor",
            "Actuator",
        ],
        answer="Host System",
        explanation=(
            "교차 컴파일러와 개발 도구는 일반적으로 "
            "Host System에 구성됩니다."
        ),
        topic="개발 환경 구성",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_e02",
        type="multiple_choice",
        question=(
            "다음 명령과 기능의 연결이 올바르지 않은 것은?"
        ),
        options=[
            "mkdir - 디렉터리 생성",
            "cp - 파일 복사",
            "source - 설정 적용",
            "file - NFS 서버 재시작",
        ],
        answer="file - NFS 서버 재시작",
        explanation=(
            "file 명령은 파일의 형식과 종류를 확인하는 명령입니다."
        ),
        topic="Linux 명령어",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_e03",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 파일은?"
        ),
        passage=(
            "NFS로 공유할 디렉터리와 접근 조건을 설정하기 위해 "
            "Host System에서 수정한다."
        ),
        options=[
            "/etc/exports",
            "/root/.bashrc",
            "/etc/passwd",
            "/etc/shadow",
        ],
        answer="/etc/exports",
        explanation=(
            "/etc/exports는 NFS의 공유 디렉터리와 "
            "접근 설정을 정의하는 파일입니다."
        ),
        topic="NFS",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_e04",
        type="multiple_choice",
        question=(
            "다음 작업의 올바른 순서는?"
        ),
        passage=(
            "교차 컴파일러가 설치된 디렉터리를 "
            "명령어 검색 경로에 추가하려고 한다."
        ),
        options=[
            (
                ".bashrc 수정 → source 실행 → "
                "env | grep PATH로 확인"
            ),
            (
                "env 삭제 → mkdir 실행 → NFS 종료"
            ),
            (
                "file 실행 → tar 삭제 → Target 종료"
            ),
            (
                "NFS 실행 → GPIO 설정 → HTML 작성"
            ),
        ],
        answer=(
            ".bashrc 수정 → source 실행 → "
            "env | grep PATH로 확인"
        ),
        explanation=(
            "PATH를 .bashrc에서 수정한 후 source로 적용하고 "
            "env 명령을 통해 정상 반영 여부를 확인할 수 있습니다."
        ),
        topic="환경 변수",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="2_2_e05",
        type="multiple_choice",
        question=(
            "다음 명령을 실행한 목적은?"
        ),
        passage=(
            "arm-unknown-linux-gnueabi-gcc -v"
        ),
        options=[
            "교차 컴파일러의 설치와 실행 상태 확인",
            "NFS 공유 디렉터리 삭제",
            "ARM 실행 파일 삭제",
            "Target System 재부팅",
        ],
        answer="교차 컴파일러의 설치와 실행 상태 확인",
        explanation=(
            "-v 옵션을 통해 교차 컴파일러의 정보와 "
            "정상 실행 여부를 확인할 수 있습니다."
        ),
        topic="교차 컴파일러",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_e06",
        type="multiple_choice",
        question=(
            "다음 명령을 실행한 결과로 가장 적절한 것은?"
        ),
        passage=(
            "arm-unknown-linux-gnueabi-gcc "
            "tc_test.c -o tc_test"
        ),
        options=[
            "ARM용 실행 파일 tc_test가 생성된다.",
            "/etc/exports가 삭제된다.",
            "PATH가 초기화된다.",
            "NFS 서버가 자동 종료된다.",
        ],
        answer="ARM용 실행 파일 tc_test가 생성된다.",
        explanation=(
            "ARM용 교차 컴파일러가 tc_test.c를 컴파일하여 "
            "tc_test라는 실행 파일을 생성합니다."
        ),
        topic="교차 컴파일",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_e07",
        type="multiple_choice",
        question=(
            "다음 결과를 통해 알 수 있는 내용으로 가장 적절한 것은?"
        ),
        passage=(
            "tc_test: ELF 32-bit LSB executable, ARM"
        ),
        options=[
            "tc_test는 ARM 프로세서용 실행 파일이다.",
            "tc_test는 이미지 파일이다.",
            "tc_test는 HTML 문서이다.",
            "tc_test는 NFS 설정 파일이다.",
        ],
        answer="tc_test는 ARM 프로세서용 실행 파일이다.",
        explanation=(
            "file 명령 결과에서 ARM이라는 표시를 통해 "
            "ARM 아키텍처용 실행 파일임을 확인할 수 있습니다."
        ),
        topic="실행 파일 형식",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_e08",
        type="multiple_choice",
        question=(
            "ARM용으로 컴파일한 tc_test가 Host PC에서 "
            "실행되지 않은 가장 적절한 이유는?"
        ),
        options=[
            (
                "Host와 Target의 프로세서 구조가 달라 "
                "Target용 실행 파일을 Host에서 실행할 수 없기 때문"
            ),
            "소스 코드에 한글이 있기 때문",
            "NFS 이름이 너무 짧기 때문",
            "GPIO 핀이 연결되지 않았기 때문",
        ],
        answer=(
            "Host와 Target의 프로세서 구조가 달라 "
            "Target용 실행 파일을 Host에서 실행할 수 없기 때문"
        ),
        explanation=(
            "교차 컴파일은 Target 프로세서용 실행 파일을 생성하므로 "
            "Host 아키텍처와 다르면 실행되지 않을 수 있습니다."
        ),
        topic="교차 개발 환경",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="2_2_e09",
        type="multiple_choice",
        question=(
            "다음 개발 과정의 빈칸에 들어갈 내용으로 "
            "가장 적절한 것은?"
        ),
        passage=(
            "소스 작성 → 교차 컴파일 → 파일 형식 확인 → "
            "(        ) → Target에서 실행"
        ),
        options=[
            "NFS 등을 이용해 Target으로 실행 파일 전달",
            "소스 코드 삭제",
            "PATH 제거",
            "Host System 포맷",
        ],
        answer="NFS 등을 이용해 Target으로 실행 파일 전달",
        explanation=(
            "Host에서 생성한 실행 파일은 NFS 등을 이용해 "
            "Target으로 전달한 후 Target에서 실행합니다."
        ),
        topic="개발 환경 흐름",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_e10",
        type="multiple_choice",
        question=(
            "다음 증상에 대한 확인 항목으로 가장 적절한 것은?"
        ),
        passage=(
            "교차 컴파일러가 정상 설치되어 있지만 "
            "터미널에서 명령어를 입력하면 command not found가 발생한다."
        ),
        options=[
            "PATH 환경 변수",
            "RISC 명령어 수",
            "GPIO 출력 전압",
            "서보모터 각도",
        ],
        answer="PATH 환경 변수",
        explanation=(
            "실행 파일이 존재해도 해당 위치가 PATH에 포함되지 않으면 "
            "쉘이 명령어를 찾지 못할 수 있습니다."
        ),
        topic="문제 해결",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="2_2_e11",
        type="multiple_choice",
        question=(
            "다음 중 NCS 개발 환경과 Arduino 환경의 대응으로 "
            "가장 적절하지 않은 것은?"
        ),
        options=[
            "Host System - 학생 PC",
            "Target System - Arduino UNO",
            "Target 전송 - Upload",
            "NFS 설정 파일 - digitalWrite()",
        ],
        answer="NFS 설정 파일 - digitalWrite()",
        explanation=(
            "digitalWrite()는 Arduino GPIO 출력 함수이며 "
            "NFS 설정 파일과 직접적인 대응 관계가 없습니다."
        ),
        topic="Arduino 연결",
        difficulty="보통",
    ),

    QuizQuestion(
        id="2_2_e12",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 Linux 명령어를 쓰시오."
        ),
        passage=(
            "실행 파일이 ARM용인지 x86용인지와 같은 "
            "파일의 형식을 확인할 때 사용한다."
        ),
        answer=[
            "file",
            "FILE",
        ],
        explanation=(
            "file 명령은 파일의 종류와 실행 파일의 "
            "아키텍처 등을 확인할 때 사용합니다."
        ),
        topic="Linux 명령어",
        difficulty="보통",
    ),
]


# =========================================================
# 전체 문제
# =========================================================

ALL_QUIZ_2_2 = (
    FORMATIVE_QUIZ_2_2
    + EXAM_PRACTICE_2_2
)