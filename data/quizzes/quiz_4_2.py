from __future__ import annotations

from utils.quiz import QuizQuestion


# =========================================================
# 학습 4-2 형성평가
# 소스 코드 저장 및 버전 관리
# =========================================================

FORMATIVE_QUIZ_4_2 = [

    # -----------------------------------------------------
    # 1. 버전 관리 기본 개념
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f01",
        type="multiple_choice",
        question=(
            "소스 코드 버전 관리의 목적으로 가장 적절한 것은?"
        ),
        options=[
            "소스 코드의 변경 이력과 여러 버전을 관리한다.",
            "CPU의 동작 주파수를 변경한다.",
            "센서의 전압을 직접 측정한다.",
            "GUI의 해상도만 변경한다.",
        ],
        answer="소스 코드의 변경 이력과 여러 버전을 관리한다.",
        explanation=(
            "버전 관리는 개발 과정에서 변경되는 소스 코드의 "
            "상태와 이력을 저장하고 관리하는 데 사용됩니다."
        ),
        topic="버전 관리 개요",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f02",
        type="true_false",
        question=(
            "버전 관리 체계를 이용하면 이전 버전의 "
            "소스 코드를 다시 확인할 수 있다."
        ),
        answer=True,
        explanation=(
            "버전 관리의 중요한 목적 중 하나는 변경 이력을 "
            "보존하여 이전 상태를 확인할 수 있도록 하는 것입니다."
        ),
        topic="버전 관리 개요",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f03",
        type="multiple_choice",
        question=(
            "소스 코드와 변경 이력을 저장하는 공간을 "
            "일반적으로 무엇이라고 하는가?"
        ),
        options=[
            "Repository",
            "Breakpoint",
            "Framebuffer",
            "Widget",
        ],
        answer="Repository",
        explanation=(
            "Repository는 프로젝트 소스 코드와 "
            "변경 이력을 저장하는 저장소입니다."
        ),
        topic="Repository",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f04",
        type="multiple_choice",
        question=(
            "개발자가 자신의 컴퓨터에서 소스 코드를 "
            "작성하고 수정하는 공간에 가장 가까운 것은?"
        ),
        options=[
            "Local Workspace",
            "Remote Repository",
            "Target Board",
            "gdbserver",
        ],
        answer="Local Workspace",
        explanation=(
            "Local Workspace는 개발자가 자신의 컴퓨터에서 "
            "실제 파일을 작성하고 수정하는 작업 공간입니다."
        ),
        topic="Repository",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 2. 중앙 집중형 / 분산형
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f05",
        type="multiple_choice",
        question=(
            "소스 코드 버전 관리 체계의 유형으로 "
            "가장 적절한 두 가지는?"
        ),
        options=[
            "중앙 집중형과 분산형",
            "저수준과 고수준",
            "전처리형과 링크형",
            "입력형과 출력형",
        ],
        answer="중앙 집중형과 분산형",
        explanation=(
            "NCS 내용에서는 버전 관리 체계를 "
            "중앙 집중형과 분산형으로 구분합니다."
        ),
        topic="버전 관리 유형",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f06",
        type="multiple_choice",
        question=(
            "다음 중 중앙 집중형 버전 관리 체계에 "
            "해당하는 것만 묶은 것은?"
        ),
        options=[
            "CVS, SVN",
            "SVN, GIT",
            "CVS, GIT",
            "GIT, GitHub",
        ],
        answer="CVS, SVN",
        explanation=(
            "CVS와 SVN은 중앙 집중형으로 분류되며 "
            "GIT은 분산형으로 분류됩니다."
        ),
        topic="버전 관리 유형",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f07",
        type="multiple_choice",
        question=(
            "NCS 내용에서 분산형 버전 관리 체계로 "
            "제시된 것은?"
        ),
        options=[
            "GIT",
            "CVS",
            "SVN",
            "Nano-X",
        ],
        answer="GIT",
        explanation=(
            "GIT은 저장소 정보를 각 클라이언트가 "
            "복제할 수 있는 분산형 버전 관리 체계입니다."
        ),
        topic="버전 관리 유형",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f08",
        type="true_false",
        question=(
            "분산형 버전 관리에서는 각 클라이언트가 "
            "저장소 정보를 복제하여 로컬에서도 "
            "버전 관리 작업을 수행할 수 있다."
        ),
        answer=True,
        explanation=(
            "분산형의 핵심 특징은 각 클라이언트가 "
            "저장소 정보를 복제할 수 있다는 것입니다."
        ),
        topic="버전 관리 유형",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 3. CVS
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f09",
        type="multiple_choice",
        question="CVS의 영문 전체 명칭은?",
        options=[
            "Concurrent Version System",
            "Central Virtual Source",
            "Code Version Storage",
            "Computer Verification System",
        ],
        answer="Concurrent Version System",
        explanation=(
            "NCS 자료에서는 CVS를 "
            "Concurrent Version System으로 제시합니다."
        ),
        topic="CVS",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f10",
        type="multiple_choice",
        question=(
            "CVS의 버전 관리 단위로 제시된 것은?"
        ),
        options=[
            "개별 파일 단위",
            "작업 단위",
            "Snapshot 단위",
            "프로세스 단위",
        ],
        answer="개별 파일 단위",
        explanation=(
            "CVS는 개별 파일 단위로 버전을 "
            "관리하는 것으로 제시됩니다."
        ),
        topic="CVS",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f11",
        type="multiple_choice",
        question=(
            "NCS 자료에서 CVS가 지원하는 것으로 "
            "제시된 파일 형태는?"
        ),
        options=[
            "ASCII 파일",
            "Binary 파일만",
            "이미지 파일만",
            "실행 파일만",
        ],
        answer="ASCII 파일",
        explanation=(
            "NCS의 CVS·SVN·GIT 비교 내용에서는 "
            "CVS가 ASCII 파일을 지원하는 것으로 제시됩니다."
        ),
        topic="CVS",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f12",
        type="true_false",
        question=(
            "CVS는 NCS 내용에서 분산형 버전 관리 "
            "시스템으로 분류되어 있다."
        ),
        answer=False,
        explanation=(
            "CVS는 중앙 집중형 버전 관리 체계로 분류됩니다."
        ),
        topic="CVS",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 4. SVN
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f13",
        type="multiple_choice",
        question="SVN의 명칭으로 제시된 것은?",
        options=[
            "Subversion",
            "Source Virtual Network",
            "System Version Node",
            "Software Verification Number",
        ],
        answer="Subversion",
        explanation=(
            "SVN은 Subversion을 의미합니다."
        ),
        topic="SVN",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f14",
        type="multiple_choice",
        question=(
            "SVN의 버전 관리 단위로 NCS에서 "
            "제시된 것은?"
        ),
        options=[
            "작업 단위",
            "개별 파일 단위",
            "Snapshot만",
            "함수 단위",
        ],
        answer="작업 단위",
        explanation=(
            "SVN은 CVS와 달리 개별 파일이 아닌 "
            "작업 단위로 관리한다고 제시됩니다."
        ),
        topic="SVN",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f15",
        type="multiple_choice",
        question=(
            "SVN이 지원하는 파일에 대한 설명으로 "
            "가장 적절한 것은?"
        ),
        options=[
            "ASCII와 Binary 파일을 지원한다.",
            "ASCII 파일만 지원한다.",
            "Binary 파일만 지원한다.",
            "소스 코드 파일은 지원하지 않는다.",
        ],
        answer="ASCII와 Binary 파일을 지원한다.",
        explanation=(
            "NCS 자료에서는 SVN이 ASCII 파일과 "
            "Binary 파일을 모두 지원한다고 제시합니다."
        ),
        topic="SVN",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f16",
        type="multiple_choice",
        question=(
            "CVS와 SVN의 차이에 대한 설명으로 "
            "가장 적절한 것은?"
        ),
        options=[
            (
                "CVS는 개별 파일 단위, "
                "SVN은 작업 단위로 관리한다."
            ),
            (
                "CVS는 분산형, SVN은 중앙 집중형이다."
            ),
            (
                "CVS는 Snapshot, SVN은 개별 파일 단위이다."
            ),
            (
                "두 시스템 모두 GIT의 다른 이름이다."
            ),
        ],
        answer=(
            "CVS는 개별 파일 단위, "
            "SVN은 작업 단위로 관리한다."
        ),
        explanation=(
            "NCS 비교표에서 CVS와 SVN의 관리 단위를 "
            "이와 같이 구분하고 있습니다."
        ),
        topic="CVS / SVN 비교",
        difficulty="어려움",
    ),

    # -----------------------------------------------------
    # 5. GIT
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f17",
        type="multiple_choice",
        question=(
            "GIT에서 버전 관리의 핵심 개념으로 "
            "제시된 것은?"
        ),
        options=[
            "Snapshot",
            "Breakpoint",
            "Widget",
            "Framebuffer",
        ],
        answer="Snapshot",
        explanation=(
            "GIT은 특정 시점의 프로젝트 상태를 "
            "Snapshot 개념으로 관리하는 것으로 설명됩니다."
        ),
        topic="GIT",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f18",
        type="multiple_choice",
        question=(
            "GIT에 대한 설명으로 가장 적절한 것은?"
        ),
        options=[
            "저장소 정보를 모두 복제할 수 있다.",
            "항상 중앙 서버에 연결되어야만 작업할 수 있다.",
            "ASCII 파일만 관리할 수 있다.",
            "GUI를 작성하는 프레임워크이다.",
        ],
        answer="저장소 정보를 모두 복제할 수 있다.",
        explanation=(
            "분산형인 GIT은 저장소 정보를 "
            "클라이언트가 복제할 수 있습니다."
        ),
        topic="GIT",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f19",
        type="true_false",
        question=(
            "GIT은 원격 서버에 접속하는 횟수를 "
            "최소화할 수 있는 특징이 있다."
        ),
        answer=True,
        explanation=(
            "로컬에 저장소 정보가 있으므로 원격 서버와의 "
            "접속을 최소화할 수 있는 특징이 제시됩니다."
        ),
        topic="GIT",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f20",
        type="multiple_choice",
        question=(
            "다음 중 GIT의 특징이 아닌 것은?"
        ),
        options=[
            "개별 ASCII 파일만 관리한다.",
            "분산형이다.",
            "Snapshot을 관리한다.",
            "저장소 정보를 복제할 수 있다.",
        ],
        answer="개별 ASCII 파일만 관리한다.",
        explanation=(
            "개별 파일 단위와 ASCII 중심이라는 특징은 "
            "NCS에서 CVS와 연결되어 제시됩니다."
        ),
        topic="GIT",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 6. CVS / SVN / GIT 종합
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f21",
        type="multiple_choice",
        question=(
            "버전 관리 체계와 특징의 연결이 "
            "올바른 것은?"
        ),
        options=[
            "GIT - 분산형 - Snapshot",
            "CVS - 분산형 - Snapshot",
            "SVN - 분산형 - 개별 파일 단위",
            "GIT - 중앙 집중형 - ASCII 파일만",
        ],
        answer="GIT - 분산형 - Snapshot",
        explanation=(
            "GIT은 분산형이며 Snapshot 개념을 "
            "사용하는 것으로 제시됩니다."
        ),
        topic="버전 관리 비교",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f22",
        type="multiple_choice",
        question=(
            "다음 중 관리 방식의 연결이 올바른 것은?"
        ),
        options=[
            "CVS - 개별 파일 / SVN - 작업 / GIT - Snapshot",
            "CVS - Snapshot / SVN - 파일 / GIT - 작업",
            "CVS - 작업 / SVN - Snapshot / GIT - 파일",
            "CVS - GUI / SVN - CLI / GIT - Framebuffer",
        ],
        answer="CVS - 개별 파일 / SVN - 작업 / GIT - Snapshot",
        explanation=(
            "세 버전 관리 체계의 핵심 관리 방식을 "
            "구분한 연결입니다."
        ),
        topic="버전 관리 비교",
        difficulty="어려움",
    ),

    # -----------------------------------------------------
    # 7. Git과 GitHub
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f23",
        type="multiple_choice",
        question=(
            "GitHub에 대한 설명으로 가장 적절한 것은?"
        ),
        options=[
            "Git 저장소 호스팅을 지원하는 웹 서비스이다.",
            "C 언어용 교차 컴파일러이다.",
            "GUI Framebuffer 라이브러리이다.",
            "GDB의 Target용 서버이다.",
        ],
        answer="Git 저장소 호스팅을 지원하는 웹 서비스이다.",
        explanation=(
            "GitHub는 Git 저장소를 웹에서 "
            "호스팅할 수 있도록 지원하는 서비스입니다."
        ),
        topic="GitHub",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f24",
        type="true_false",
        question=(
            "Git과 GitHub는 완전히 동일한 개념이다."
        ),
        answer=False,
        explanation=(
            "Git은 분산 버전 관리 도구이고 "
            "GitHub는 Git 저장소 호스팅 웹 서비스입니다."
        ),
        topic="GitHub",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f25",
        type="multiple_choice",
        question=(
            "NCS 자료의 GitHub 설명에 포함되는 기능은?"
        ),
        options=[
            "Gist와 Wiki",
            "GPIO와 PWM",
            "GDB와 DDD",
            "cpp와 ld",
        ],
        answer="Gist와 Wiki",
        explanation=(
            "NCS 자료에서는 GitHub 저장소에서 "
            "Gist와 Wiki 등의 기능을 사용할 수 있다고 설명합니다."
        ),
        topic="GitHub",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 8. SVN 실습
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f26",
        type="multiple_choice",
        question=(
            "NCS 4-2에서 소스 코드 버전 관리 "
            "실습에 중심적으로 사용되는 시스템은?"
        ),
        options=[
            "SVN",
            "GDB",
            "Nano-X",
            "DirectFB",
        ],
        answer="SVN",
        explanation=(
            "NCS 4-2 수행 내용에서는 SVN 기반의 "
            "원격 저장소와 Commit 실습을 진행합니다."
        ),
        topic="SVN 실습",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f27",
        type="multiple_choice",
        question=(
            "NCS 버전 관리 실습에서 작성하는 "
            "소스 파일 이름은?"
        ),
        options=[
            "scm_test.c",
            "gdb_test.c",
            "arm_server.c",
            "pc_client.c",
        ],
        answer="scm_test.c",
        explanation=(
            "4-2 SVN 실습에서는 scm_test.c를 "
            "작성하여 버전 관리 과정을 확인합니다."
        ),
        topic="SVN 실습",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f28",
        type="multiple_choice",
        question=(
            "NCS의 SVN 실습에서 소스 코드를 수정한 뒤 "
            "새로운 버전을 저장할 때 사용하는 작업은?"
        ),
        options=[
            "Commit",
            "Breakpoint",
            "Compile only",
            "Framebuffer",
        ],
        answer="Commit",
        explanation=(
            "수정한 소스의 변경 사항을 저장소에 "
            "새로운 버전으로 반영하는 과정이 Commit입니다."
        ),
        topic="SVN 실습",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f29",
        type="multiple_choice",
        question=(
            "PDF의 SVN 실습에서 Windows 파일 탐색기의 "
            "콘텍스트 메뉴에서 선택하는 항목은?"
        ),
        options=[
            "SVN Commit...",
            "GDB Break...",
            "Qt Designer...",
            "Compile Target...",
        ],
        answer="SVN Commit...",
        explanation=(
            "수행 내용에서는 콘텍스트 메뉴의 "
            "SVN Commit...을 이용해 변경 내용을 저장합니다."
        ),
        topic="SVN 실습",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f30",
        type="multiple_choice",
        question=(
            "SVN 버전 관리 실습의 흐름으로 "
            "가장 적절한 것은?"
        ),
        options=[
            (
                "소스 작성 → 원격 저장소 연결 → 수정 → "
                "Commit → 버전 확인"
            ),
            (
                "Commit → 소스 삭제 → 저장소 생성"
            ),
            (
                "GDB 실행 → Breakpoint → Commit"
            ),
            (
                "GUI 작성 → Target 삭제 → SVN 설치 제거"
            ),
        ],
        answer=(
            "소스 작성 → 원격 저장소 연결 → 수정 → "
            "Commit → 버전 확인"
        ),
        explanation=(
            "소스 파일을 저장소와 연결한 뒤 수정 내용을 "
            "Commit하여 여러 버전이 관리되는지 확인합니다."
        ),
        topic="SVN 실습",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 9. Commit
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f31",
        type="multiple_choice",
        question=(
            "Commit의 의미로 가장 적절한 것은?"
        ),
        options=[
            (
                "작업한 변경 사항을 저장소에 "
                "하나의 버전으로 반영한다."
            ),
            "프로그램 실행을 특정 위치에서 정지시킨다.",
            "GUI 위젯을 Form에 배치한다.",
            "Target 보드를 초기화한다.",
        ],
        answer=(
            "작업한 변경 사항을 저장소에 "
            "하나의 버전으로 반영한다."
        ),
        explanation=(
            "Commit은 현재 변경 사항을 버전 관리 "
            "저장소에 새로운 이력으로 반영하는 과정입니다."
        ),
        topic="Commit",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f32",
        type="multiple_choice",
        question=(
            "Commit Message를 작성하는 가장 중요한 이유는?"
        ),
        options=[
            "어떤 내용을 변경했는지 확인하기 위해",
            "컴파일 속도를 높이기 위해",
            "센서 전압을 변경하기 위해",
            "GUI 해상도를 설정하기 위해",
        ],
        answer="어떤 내용을 변경했는지 확인하기 위해",
        explanation=(
            "Commit Message는 각 버전에서 어떤 변화가 "
            "있었는지 알아보기 쉽게 만드는 역할을 합니다."
        ),
        topic="Commit",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f33",
        type="multiple_choice",
        question=(
            "다음 중 의미 있는 Commit Message로 "
            "가장 적절한 것은?"
        ),
        options=[
            "초음파 센서 거리 계산 오류 수정",
            "수정",
            "최종",
            "123",
        ],
        answer="초음파 센서 거리 계산 오류 수정",
        explanation=(
            "변경한 기능이나 오류 수정 내용을 구체적으로 "
            "알 수 있는 메시지가 버전 관리에 유용합니다."
        ),
        topic="Commit",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 10. 협업
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f34",
        type="multiple_choice",
        question=(
            "여러 프로젝트 구성원이 동일한 파일을 "
            "공유하여 작업할 때 버전 관리가 필요한 이유는?"
        ),
        options=[
            (
                "각 구성원의 변경 내용과 "
                "여러 버전을 확인하고 통합하기 위해"
            ),
            "CPU의 명령어를 줄이기 위해",
            "센서를 자동으로 연결하기 위해",
            "GUI를 자동으로 생성하기 위해",
        ],
        answer=(
            "각 구성원의 변경 내용과 "
            "여러 버전을 확인하고 통합하기 위해"
        ),
        explanation=(
            "협업에서는 누가 무엇을 변경했는지와 "
            "버전별 차이를 관리하는 것이 중요합니다."
        ),
        topic="협업",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f35",
        type="true_false",
        question=(
            "여러 사람이 동일한 소스 파일을 수정하는 경우에는 "
            "각 변경 내용을 확인한 뒤 필요한 내용을 "
            "통합하는 과정이 중요하다."
        ),
        answer=True,
        explanation=(
            "여러 버전의 변경 사항을 확인하고 통합하는 것은 "
            "협업 버전 관리의 중요한 과정입니다."
        ),
        topic="협업",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 11. 형상 객체 / 새로운 버전
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f36",
        type="multiple_choice",
        question=(
            "학습 4-2의 학습 목표에 포함된 활동으로 "
            "가장 적절한 것은?"
        ),
        options=[
            (
                "형상 객체를 수집하여 새로운 "
                "소프트웨어 버전을 구축한다."
            ),
            "GUI의 색상만 변경한다.",
            "CPU를 물리적으로 교체한다.",
            "센서 데이터를 삭제한다.",
        ],
        answer=(
            "형상 객체를 수집하여 새로운 "
            "소프트웨어 버전을 구축한다."
        ),
        explanation=(
            "학습 목표에는 형상 객체 수집, 새로운 버전 구축, "
            "소프트웨어 품질 유지가 포함됩니다."
        ),
        topic="형상 관리",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f37",
        type="multiple_choice",
        question=(
            "다음 중 형상 관리 대상의 예로 "
            "가장 적절한 것은?"
        ),
        options=[
            "소스 코드와 관련 프로젝트 파일",
            "모니터의 밝기 설정만",
            "키보드의 색상",
            "교실의 좌석 배치",
        ],
        answer="소스 코드와 관련 프로젝트 파일",
        explanation=(
            "버전 관리와 소프트웨어 구축에 필요한 "
            "프로젝트 산출물은 형상 관리 대상으로 볼 수 있습니다."
        ),
        topic="형상 관리",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f38",
        type="multiple_choice",
        question=(
            "새로운 소프트웨어 버전을 구축하는 "
            "흐름으로 가장 적절한 것은?"
        ),
        options=[
            (
                "형상 객체 확인 → 수집 → 버전 확인 → "
                "통합 → 새 버전 구축 → 결과 확인"
            ),
            (
                "새 버전 삭제 → 소스 삭제 → Target 종료"
            ),
            (
                "GUI 작성 → Breakpoint → NFS 삭제"
            ),
            (
                "Compiler 삭제 → Repository 삭제"
            ),
        ],
        answer=(
            "형상 객체 확인 → 수집 → 버전 확인 → "
            "통합 → 새 버전 구축 → 결과 확인"
        ),
        explanation=(
            "필요한 형상 객체와 버전을 확인하고 "
            "통합한 뒤 새로운 버전을 구축하고 확인하는 흐름입니다."
        ),
        topic="형상 관리",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 12. CASE
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f39",
        type="multiple_choice",
        question="CASE의 영문 전체 명칭은?",
        options=[
            "Computer Aided Software Engineering",
            "Computer Application Source Environment",
            "Code Analysis System Engine",
            "Central Application Software Editor",
        ],
        answer="Computer Aided Software Engineering",
        explanation=(
            "CASE는 Computer Aided Software Engineering의 "
            "약자입니다."
        ),
        topic="CASE",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_f40",
        type="multiple_choice",
        question=(
            "CASE 도구의 역할로 가장 적절한 것은?"
        ),
        options=[
            "소프트웨어 개발 과정을 지원한다.",
            "CPU의 전압을 공급한다.",
            "네트워크 케이블을 대신한다.",
            "센서 데이터를 물리적으로 측정한다.",
        ],
        answer="소프트웨어 개발 과정을 지원한다.",
        explanation=(
            "CASE 도구는 소프트웨어 개발 활동을 "
            "지원하기 위한 도구입니다."
        ),
        topic="CASE",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f41",
        type="multiple_choice",
        question=(
            "학습 4의 평가에서 CASE 도구와 관련하여 "
            "확인하는 내용으로 가장 적절한 것은?"
        ),
        options=[
            "도구 선정, 환경 구성, 설치 및 테스트",
            "서보모터 각도만 측정",
            "GUI 색상만 선택",
            "CPU 명령어만 암기",
        ],
        answer="도구 선정, 환경 구성, 설치 및 테스트",
        explanation=(
            "평가에서는 CASE 도구 선정과 개발 환경 구성, "
            "설치 및 테스트 능력을 확인합니다."
        ),
        topic="CASE",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 13. Arduino 연결
    # -----------------------------------------------------
    QuizQuestion(
        id="4_2_f42",
        type="multiple_choice",
        question=(
            "Arduino 프로젝트에서 버전 관리를 활용하는 "
            "방법으로 가장 적절한 것은?"
        ),
        options=[
            (
                "기능 구현이나 오류 수정이 완료될 때마다 "
                "변경 상태와 내용을 기록한다."
            ),
            "항상 이전 소스 코드를 삭제한다.",
            "파일 이름만 final로 반복해서 변경한다.",
            "정상 코드도 저장하지 않는다.",
        ],
        answer=(
            "기능 구현이나 오류 수정이 완료될 때마다 "
            "변경 상태와 내용을 기록한다."
        ),
        explanation=(
            "기능별 변경 내용을 버전으로 저장하면 "
            "이전 정상 상태를 찾거나 개발 과정을 추적하기 쉽습니다."
        ),
        topic="Arduino 버전 관리",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f43",
        type="multiple_choice",
        question=(
            "Arduino 팀 프로젝트의 Commit Message로 "
            "가장 적절한 것은?"
        ),
        options=[
            "서보모터 초기 위치 설정 추가",
            "진짜최종",
            "최종최종",
            "수정함",
        ],
        answer="서보모터 초기 위치 설정 추가",
        explanation=(
            "구체적으로 어떤 기능을 변경했는지 알 수 있는 "
            "메시지가 변경 이력 관리에 적절합니다."
        ),
        topic="Arduino 버전 관리",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_f44",
        type="multiple_choice",
        question=(
            "Arduino 팀원이 각각 작성한 센서 코드와 모터 코드를 "
            "최종 프로젝트에 합치는 과정과 가장 관련 있는 것은?"
        ),
        options=[
            "변경 버전 확인 및 소스 통합",
            "GDB 종료",
            "GUI Widget 배치",
            "Framebuffer 생성",
        ],
        answer="변경 버전 확인 및 소스 통합",
        explanation=(
            "여러 구성원이 만든 기능을 버전별로 확인한 뒤 "
            "최종 프로그램으로 통합하는 과정과 연결됩니다."
        ),
        topic="Arduino 버전 관리",
        difficulty="보통",
    ),
]


# =========================================================
# 학습 4-2 중간고사 대비
# =========================================================

EXAM_PRACTICE_4_2 = [

    QuizQuestion(
        id="4_2_e01",
        type="multiple_choice",
        question=(
            "다음 버전 관리 체계의 분류가 "
            "올바른 것은?"
        ),
        options=[
            "CVS·SVN - 중앙 집중형 / GIT - 분산형",
            "CVS·GIT - 중앙 집중형 / SVN - 분산형",
            "GIT·SVN - 분산형 / CVS - GUI형",
            "CVS·SVN·GIT - 모두 중앙 집중형",
        ],
        answer="CVS·SVN - 중앙 집중형 / GIT - 분산형",
        explanation=(
            "NCS에서는 CVS와 SVN을 중앙 집중형, "
            "GIT을 분산형으로 분류합니다."
        ),
        topic="버전 관리 유형",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e02",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 버전 관리 체계는?"
        ),
        passage=(
            "중앙 집중형이며 개별 파일 단위로 버전을 관리하고 "
            "NCS 비교 내용에서는 ASCII 파일을 지원하는 것으로 제시된다."
        ),
        options=[
            "CVS",
            "SVN",
            "GIT",
            "GitHub",
        ],
        answer="CVS",
        explanation=(
            "개별 파일 단위와 ASCII 지원은 "
            "NCS에서 제시한 CVS의 핵심 특징입니다."
        ),
        topic="CVS",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e03",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 버전 관리 체계는?"
        ),
        passage=(
            "중앙 집중형이며 개별 파일이 아닌 작업 단위로 "
            "버전을 관리하고 ASCII 및 Binary 파일을 지원한다."
        ),
        options=[
            "SVN",
            "CVS",
            "GIT",
            "GitHub",
        ],
        answer="SVN",
        explanation=(
            "작업 단위와 ASCII·Binary 지원은 "
            "SVN의 특징으로 제시됩니다."
        ),
        topic="SVN",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e04",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 버전 관리 체계는?"
        ),
        passage=(
            "분산형이며 Snapshot 개념을 사용한다. "
            "저장소 정보를 모두 복제할 수 있고 "
            "원격 서버와의 접속을 최소화할 수 있다."
        ),
        options=[
            "GIT",
            "CVS",
            "SVN",
            "PyQt",
        ],
        answer="GIT",
        explanation=(
            "Snapshot, 저장소 복제, 분산형이라는 특징은 "
            "GIT과 연결됩니다."
        ),
        topic="GIT",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e05",
        type="multiple_choice",
        question=(
            "다음 버전 관리 시스템과 관리 방식의 "
            "연결이 올바르지 않은 것은?"
        ),
        options=[
            "CVS - 개별 파일 단위",
            "SVN - 작업 단위",
            "GIT - Snapshot",
            "CVS - Snapshot",
        ],
        answer="CVS - Snapshot",
        explanation=(
            "Snapshot 개념은 GIT과 연결되며 "
            "CVS는 개별 파일 단위로 제시됩니다."
        ),
        topic="버전 관리 비교",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="4_2_e06",
        type="multiple_choice",
        question=(
            "Git과 GitHub의 차이를 가장 잘 설명한 것은?"
        ),
        options=[
            (
                "Git은 분산 버전 관리 도구이고 "
                "GitHub는 Git 저장소 호스팅 웹 서비스이다."
            ),
            (
                "Git은 GUI이고 GitHub는 컴파일러이다."
            ),
            (
                "Git은 중앙 집중형이고 GitHub는 분산형이다."
            ),
            (
                "Git과 GitHub는 완전히 같은 프로그램이다."
            ),
        ],
        answer=(
            "Git은 분산 버전 관리 도구이고 "
            "GitHub는 Git 저장소 호스팅 웹 서비스이다."
        ),
        explanation=(
            "Git은 버전 관리 자체를 수행하는 도구이고 "
            "GitHub는 Git 저장소를 호스팅하는 웹 서비스입니다."
        ),
        topic="GitHub",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e07",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 용어는?"
        ),
        passage=(
            "프로젝트의 소스 코드와 변경 이력을 "
            "저장하고 관리하는 공간"
        ),
        options=[
            "Repository",
            "Breakpoint",
            "Widget",
            "Linker",
        ],
        answer="Repository",
        explanation=(
            "소스 코드와 버전 이력을 저장하는 공간을 "
            "Repository라고 합니다."
        ),
        topic="Repository",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_e08",
        type="multiple_choice",
        question=(
            "다음 상황에서 수행해야 할 버전 관리 작업은?"
        ),
        passage=(
            "scm_test.c의 출력 문자열을 수정하였다. "
            "수정된 상태를 새로운 버전으로 원격 저장소에 "
            "반영하려고 한다."
        ),
        options=[
            "Commit",
            "Breakpoint",
            "Preprocessing",
            "Framebuffer",
        ],
        answer="Commit",
        explanation=(
            "변경한 소스를 새로운 버전으로 저장소에 "
            "반영하는 작업이 Commit입니다."
        ),
        topic="Commit",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_e09",
        type="multiple_choice",
        question=(
            "Commit Message의 역할로 가장 적절한 것은?"
        ),
        options=[
            "해당 버전에서 무엇을 변경했는지 기록한다.",
            "프로그램을 자동으로 디버깅한다.",
            "CPU 구조를 변경한다.",
            "저장소를 자동으로 삭제한다.",
        ],
        answer="해당 버전에서 무엇을 변경했는지 기록한다.",
        explanation=(
            "Commit Message는 변경 내용과 이유를 "
            "나중에 식별할 수 있도록 기록하는 데 사용합니다."
        ),
        topic="Commit",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_e10",
        type="multiple_choice",
        question=(
            "NCS SVN 실습의 순서로 가장 적절한 것은?"
        ),
        options=[
            (
                "소스 작성 → 원격 저장소 생성·연결 → "
                "소스 수정 → Commit → 버전 확인"
            ),
            (
                "Commit → 저장소 삭제 → 소스 작성"
            ),
            (
                "GDB 실행 → 소스 작성 → GUI 테스트"
            ),
            (
                "Target 실행 → SVN 제거 → Commit"
            ),
        ],
        answer=(
            "소스 작성 → 원격 저장소 생성·연결 → "
            "소스 수정 → Commit → 버전 확인"
        ),
        explanation=(
            "SVN 실습에서는 소스를 저장소와 연결하고 "
            "수정 후 Commit하여 버전 관리 결과를 확인합니다."
        ),
        topic="SVN 실습",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e11",
        type="multiple_choice",
        question=(
            "다음 중 소스 코드 버전 관리가 "
            "협업에 제공하는 장점으로 가장 적절한 것은?"
        ),
        options=[
            (
                "구성원별 변경 이력을 확인하고 "
                "여러 버전의 내용을 통합할 수 있다."
            ),
            "서보모터의 토크를 증가시킨다.",
            "GUI 해상도를 자동으로 높인다.",
            "네트워크 IP 주소를 자동 생성한다.",
        ],
        answer=(
            "구성원별 변경 이력을 확인하고 "
            "여러 버전의 내용을 통합할 수 있다."
        ),
        explanation=(
            "여러 개발자의 변경 내용을 기록하고 "
            "필요한 버전을 통합할 수 있다는 것이 "
            "협업에서 버전 관리의 중요한 장점입니다."
        ),
        topic="협업",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e12",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 학습 4-2 활동은?"
        ),
        passage=(
            "관리 대상 소스 코드와 프로젝트 파일을 모으고 "
            "각 버전을 확인하여 필요한 내용을 통합한 뒤 "
            "새로운 소프트웨어 버전을 만든다."
        ),
        options=[
            "형상 객체 수집 및 새로운 버전 구축",
            "GDB 원격 디버깅",
            "Qt Designer 작성",
            "NFS 서버 설정",
        ],
        answer="형상 객체 수집 및 새로운 버전 구축",
        explanation=(
            "학습 목표에서 형상 객체를 수집해 "
            "새로운 소프트웨어 버전을 구축하도록 요구합니다."
        ),
        topic="형상 관리",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e13",
        type="multiple_choice",
        question=(
            "CASE의 의미로 가장 적절한 것은?"
        ),
        options=[
            "Computer Aided Software Engineering",
            "Central Application Source Engine",
            "Computer Arduino System Environment",
            "Code Assembly Server Extension",
        ],
        answer="Computer Aided Software Engineering",
        explanation=(
            "CASE는 Computer Aided Software Engineering을 "
            "의미하며 소프트웨어 개발을 지원하는 도구와 관련됩니다."
        ),
        topic="CASE",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e14",
        type="multiple_choice",
        question=(
            "학습 4의 평가 내용에서 CASE 도구와 관련된 "
            "작업 흐름으로 가장 적절한 것은?"
        ),
        options=[
            (
                "도구 선정 → 개발 환경 구성 → "
                "설치 → 동작 테스트"
            ),
            (
                "Target 삭제 → Widget 생성 → Commit 삭제"
            ),
            (
                "Breakpoint 설정 → CPU 교체"
            ),
            (
                "센서 측정 → Qt 삭제 → Repository 삭제"
            ),
        ],
        answer=(
            "도구 선정 → 개발 환경 구성 → "
            "설치 → 동작 테스트"
        ),
        explanation=(
            "CASE 도구 선정 후 개발 환경을 구성하고 "
            "설치한 뒤 정상적으로 동작하는지 테스트합니다."
        ),
        topic="CASE",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e15",
        type="multiple_choice",
        question=(
            "다음 Arduino 프로젝트 버전 이력 중 "
            "버전 관리가 올바르게 활용된 예는?"
        ),
        passage=(
            "스마트 화분 프로젝트를 기능별로 개발하고 있다."
        ),
        options=[
            (
                "v1 센서값 출력 → v2 펌프 제어 추가 → "
                "v3 LCD 표시 추가 → v4 반복 작동 오류 수정"
            ),
            (
                "모든 수정 버전을 삭제하고 final.ino 하나만 유지"
            ),
            (
                "파일 이름만 final1, final2로 변경하고 "
                "변경 내용은 기록하지 않음"
            ),
            (
                "정상 동작한 코드를 매번 삭제한 뒤 다시 작성"
            ),
        ],
        answer=(
            "v1 센서값 출력 → v2 펌프 제어 추가 → "
            "v3 LCD 표시 추가 → v4 반복 작동 오류 수정"
        ),
        explanation=(
            "기능 추가와 오류 수정의 상태를 버전별로 "
            "구분하면 프로젝트의 변경 과정을 추적할 수 있습니다."
        ),
        topic="Arduino 버전 관리",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e16",
        type="multiple_choice",
        question=(
            "다음 중 가장 적절한 Commit Message는?"
        ),
        options=[
            "LCD에 현재 온도 표시 기능 추가",
            "최종",
            "수정",
            "진짜최종",
        ],
        answer="LCD에 현재 온도 표시 기능 추가",
        explanation=(
            "구체적인 변경 기능을 명시하면 "
            "버전 이력을 이해하기 쉽습니다."
        ),
        topic="Commit",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="4_2_e17",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 버전 관리 체계를 쓰시오."
        ),
        passage=(
            "분산형 버전 관리 체계이며 Snapshot 개념으로 "
            "프로젝트의 여러 상태를 시간순으로 관리한다."
        ),
        answer=[
            "GIT",
            "Git",
            "git",
        ],
        explanation=(
            "NCS 자료에서는 GIT을 분산형이며 "
            "Snapshot 기반으로 설명합니다."
        ),
        topic="GIT",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e18",
        type="short_answer",
        question=(
            "소스 코드의 변경 사항을 저장소에 "
            "새로운 버전으로 반영하는 작업의 "
            "영문 용어를 쓰시오."
        ),
        answer=[
            "Commit",
            "commit",
            "COMMIT",
        ],
        explanation=(
            "변경 사항을 하나의 버전으로 저장소에 "
            "반영하는 작업을 Commit이라고 합니다."
        ),
        topic="Commit",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e19",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 용어를 영문으로 쓰시오."
        ),
        passage=(
            "프로젝트의 소스 코드와 변경 이력을 "
            "저장하고 관리하는 저장소"
        ),
        answer=[
            "Repository",
            "repository",
            "REPOSITORY",
        ],
        explanation=(
            "버전 관리에서 소스와 이력을 저장하는 공간을 "
            "Repository라고 합니다."
        ),
        topic="Repository",
        difficulty="보통",
    ),

    QuizQuestion(
        id="4_2_e20",
        type="short_answer",
        question=(
            "CASE의 영문 전체 명칭을 쓰시오."
        ),
        answer=[
            "Computer Aided Software Engineering",
            "computer aided software engineering",
        ],
        explanation=(
            "CASE는 Computer Aided Software Engineering의 "
            "약자입니다."
        ),
        topic="CASE",
        difficulty="어려움",
    ),
]


# =========================================================
# 전체 문제
# =========================================================

ALL_QUIZ_4_2 = (
    FORMATIVE_QUIZ_4_2
    + EXAM_PRACTICE_4_2
)