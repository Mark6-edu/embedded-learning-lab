from __future__ import annotations

from utils.quiz import QuizQuestion


# =========================================================
# 학습 1-2 형성평가
# 임베디드 시스템의 평가
# =========================================================

FORMATIVE_QUIZ_1_2 = [

    # -----------------------------------------------------
    # 1. 오픈 소스 라이선스
    # -----------------------------------------------------
    QuizQuestion(
        id="1_2_f01",
        type="true_false",
        question=(
            "무료로 사용할 수 있는 소프트웨어라면 "
            "라이선스 조건을 확인하지 않아도 된다."
        ),
        answer=False,
        explanation=(
            "오픈 소스나 무료 소프트웨어도 사용 및 배포 조건, "
            "소스 공개 의무, 저작권 표시 등 라이선스 조건을 "
            "확인해야 합니다."
        ),
        topic="오픈 소스 라이선스",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="1_2_f02",
        type="multiple_choice",
        question=(
            "오픈 소스 소프트웨어를 임베디드 시스템에 적용하기 전에 "
            "확인해야 할 사항으로 가장 거리가 먼 것은?"
        ),
        options=[
            "소프트웨어의 출처",
            "사용 및 배포 조건",
            "라이선스 제한 사항",
            "개발자의 개인 취미",
        ],
        answer="개발자의 개인 취미",
        explanation=(
            "오픈 소스 활용 시에는 소프트웨어 출처, 구현 주체, "
            "사용 및 배포 조건, 라이선스 제한 등을 확인해야 합니다."
        ),
        topic="오픈 소스 라이선스",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 2. 신뢰성과 RAM
    # -----------------------------------------------------
    QuizQuestion(
        id="1_2_f03",
        type="multiple_choice",
        question=(
            "제품의 신뢰성 분석, 정비성 및 가용성을 분석하는 것을 "
            "무엇이라고 하는가?"
        ),
        options=[
            "RAM 분석",
            "SRS 분석",
            "QoS 분석",
            "API 분석",
        ],
        answer="RAM 분석",
        explanation=(
            "RAM은 Reliability, Availability, Maintainability를 "
            "의미하며 제품의 신뢰성, 가용성, 정비성을 분석합니다."
        ),
        topic="임베디드 SW 신뢰성",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_f04",
        type="short_answer",
        question=(
            "RAM에서 R이 의미하는 영문 용어를 쓰시오."
        ),
        answer=[
            "Reliability",
            "reliability",
        ],
        explanation=(
            "RAM의 R은 Reliability, 즉 신뢰성을 의미합니다."
        ),
        topic="임베디드 SW 신뢰성",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 3. 신뢰성 예측 모델
    # -----------------------------------------------------
    QuizQuestion(
        id="1_2_f05",
        type="multiple_choice",
        question=(
            "다음 중 NCS 학습모듈에서 제시한 "
            "임베디드 SW 신뢰성 예측 평가 모델이 아닌 것은?"
        ),
        options=[
            "MUSA Model",
            "Putnam Model",
            "SoftRel Prediction Model",
            "Waterfall Model",
        ],
        answer="Waterfall Model",
        explanation=(
            "NCS에서는 RL-TR-92-52, MUSA, Putnam, "
            "SoftRel Prediction Model을 신뢰성 예측 모델로 제시합니다."
        ),
        topic="신뢰성 예측 모델",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_f06",
        type="true_false",
        question=(
            "임베디드 SW 신뢰성 예측 평가 모델들은 "
            "과거 데이터를 활용하여 개발 초기에 예측하는 데 "
            "사용될 수 있다."
        ),
        answer=True,
        explanation=(
            "NCS에서는 각 모델의 통계적 가정과 특징은 다르지만 "
            "과거 데이터를 활용하여 개발 초기에 예측한다는 "
            "공통점이 있다고 설명합니다."
        ),
        topic="신뢰성 예측 모델",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_f07",
        type="multiple_choice",
        question=(
            "신뢰성 평가에서 외부 전문가와 내부 개발자의 평가 결과를 "
            "수치화하기 위해 사용할 수 있는 방법은?"
        ),
        options=[
            "리커트 척도",
            "DFS",
            "VLSM",
            "FIFO",
        ],
        answer="리커트 척도",
        explanation=(
            "평가 지표의 부합성을 전문가가 리커트 척도로 평가한 후 "
            "평균 점수를 산정할 수 있습니다."
        ),
        topic="신뢰성 평가 방법",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="1_2_f08",
        type="multiple_choice",
        question=(
            "전문가 집단의 의견과 판단을 수집하는 방법으로 "
            "NCS에서 제시한 것은?"
        ),
        options=[
            "델파이 방법",
            "버블 정렬",
            "라운드 로빈",
            "체크섬",
        ],
        answer="델파이 방법",
        explanation=(
            "전문가 의견 수렴 방법으로 델파이 방법과 "
            "브레인스토밍법을 활용할 수 있습니다."
        ),
        topic="신뢰성 평가 방법",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 4. Skill-Set
    # -----------------------------------------------------
    QuizQuestion(
        id="1_2_f09",
        type="multiple_choice",
        question=(
            "임베디드 SW 적용 인력의 Skill-Set 평가 항목 중 "
            "운영체제 API를 활용하는 시스템 소프트웨어 개발 기술을 "
            "평가하는 항목은?"
        ),
        options=[
            "시스템 프로그래밍",
            "프로그래밍 언어",
            "개발 도구",
            "소프트웨어 공학",
        ],
        answer="시스템 프로그래밍",
        explanation=(
            "시스템 프로그래밍은 운영체제의 API를 활용하는 "
            "시스템 소프트웨어 개발 기술 수준을 평가합니다."
        ),
        topic="Skill-Set",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_f10",
        type="multiple_choice",
        question=(
            "Linux Device Driver, Windows CE Device Driver, "
            "RTOS 등의 경험을 평가하는 Skill-Set 항목은?"
        ),
        options=[
            "운영체제 커널 프로그래밍",
            "미들웨어 및 응용 프로그래밍",
            "개발 도구",
            "프로그래밍 언어",
        ],
        answer="운영체제 커널 프로그래밍",
        explanation=(
            "운영체제 커널 프로그래밍은 운영체제 커널의 일부를 "
            "수행한 경험과 기술 수준을 평가합니다."
        ),
        topic="Skill-Set",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_f11",
        type="multiple_choice",
        question=(
            "다음 중 임베디드 SW 적용 인력의 Skill-Set 평가 항목에 "
            "해당하지 않는 것은?"
        ),
        options=[
            "하드웨어 제어 프로그래밍",
            "소프트웨어 공학 및 개발 프로세스",
            "미들웨어 및 응용 프로그래밍",
            "학교 급식 관리",
        ],
        answer="학교 급식 관리",
        explanation=(
            "NCS에서는 프로그래밍 언어, 개발 도구, 시스템 프로그래밍, "
            "OS 커널 프로그래밍, 하드웨어 제어 프로그래밍, "
            "SW 공학 및 개발 프로세스, 미들웨어 및 응용 프로그래밍의 "
            "7개 영역을 제시합니다."
        ),
        topic="Skill-Set",
        difficulty="쉬움",
    ),

    # -----------------------------------------------------
    # 5. 시험 인증
    # -----------------------------------------------------
    QuizQuestion(
        id="1_2_f12",
        type="true_false",
        question=(
            "임베디드 SW 테스팅은 하드웨어와 함께 고려해야 하므로 "
            "기존 패키지 SW 테스팅과 다른 적용이 필요할 수 있다."
        ),
        answer=True,
        explanation=(
            "NCS에서는 임베디드 SW 시험이 하드웨어와 함께 "
            "고려되어야 한다고 설명합니다."
        ),
        topic="임베디드 SW 시험 인증",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="1_2_f13",
        type="multiple_choice",
        question=(
            "이동통신 분야에서 수행되는 시험 인증의 예로 "
            "가장 적절한 것은?"
        ),
        options=[
            "RF 및 프로토콜 시험",
            "기계 가공 시험",
            "토양 성분 시험",
            "건축 구조 시험",
        ],
        answer="RF 및 프로토콜 시험",
        explanation=(
            "이동통신 분야에서는 RF와 프로토콜 시험 인증 등이 "
            "수행되고 있습니다."
        ),
        topic="임베디드 SW 시험 인증",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="1_2_f14",
        type="multiple_choice",
        question=(
            "홈네트워크 SW 시험에서 확보하고자 하는 것으로 "
            "NCS에서 제시한 항목은?"
        ),
        options=[
            "서비스 수용성, 안정성, 신뢰성",
            "교실 좌석 수",
            "인터넷 검색 순위",
            "제품 색상 선호도",
        ],
        answer="서비스 수용성, 안정성, 신뢰성",
        explanation=(
            "홈네트워크 분야에서는 서비스의 수용성, 안정성, "
            "신뢰성 확보를 위한 SW 시험을 수행합니다."
        ),
        topic="임베디드 SW 시험 인증",
        difficulty="보통",
    ),

    # -----------------------------------------------------
    # 6. 기능성 평가
    # -----------------------------------------------------
    QuizQuestion(
        id="1_2_f15",
        type="multiple_choice",
        question=(
            "ISO/IEC 9126에서 제시한 소프트웨어 품질 평가 기준에 "
            "해당하지 않는 것은?"
        ),
        options=[
            "기능성",
            "신뢰성",
            "사용성",
            "가격성",
        ],
        answer="가격성",
        explanation=(
            "NCS 자료에서는 기능성, 신뢰성, 이식성, 사용성, "
            "유지보수성, 효율성을 제시합니다."
        ),
        topic="소프트웨어 품질 평가",
        difficulty="쉬움",
    ),

    QuizQuestion(
        id="1_2_f16",
        type="short_answer",
        question=(
            "애플리케이션에 의존적인 부분을 나타내는 "
            "영문 약어를 쓰시오."
        ),
        answer=[
            "AP",
            "ap",
        ],
        explanation=(
            "AP는 Application dependent Part를 의미합니다."
        ),
        topic="기능성 평가",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_f17",
        type="short_answer",
        question=(
            "운영체제에 의존적인 부분을 나타내는 "
            "영문 약어를 쓰시오."
        ),
        answer=[
            "OP",
            "op",
        ],
        explanation=(
            "OP는 OS dependent Part를 의미합니다."
        ),
        topic="기능성 평가",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_f18",
        type="short_answer",
        question=(
            "하드웨어 제어에 의존적인 부분을 나타내는 "
            "영문 약어를 쓰시오."
        ),
        answer=[
            "HP",
            "hp",
        ],
        explanation=(
            "HP는 Hardware dependent Part를 의미합니다."
        ),
        topic="기능성 평가",
        difficulty="보통",
    ),
]


# =========================================================
# 학습 1-2 중간고사 대비
# =========================================================

EXAM_PRACTICE_1_2 = [

    QuizQuestion(
        id="1_2_e01",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 분석은?"
        ),
        passage=(
            "제품의 신뢰성, 가용성, 정비성을 분석하여 "
            "제품 개발 타당성과 설계 개선 사항을 도출한다."
        ),
        options=[
            "RAM 분석",
            "SRS 분석",
            "QoS 분석",
            "UML 분석",
        ],
        answer="RAM 분석",
        explanation=(
            "RAM은 Reliability, Availability, Maintainability의 "
            "약자로 신뢰성, 가용성, 정비성을 분석합니다."
        ),
        topic="신뢰성 평가",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_e02",
        type="multiple_choice",
        question=(
            "다음 중 임베디드 SW 신뢰성 예측 평가 모델만으로 "
            "구성된 것은?"
        ),
        options=[
            "RL-TR-92-52, MUSA, Putnam, SoftRel Prediction",
            "MUSA, TCP/IP, UML, Putnam",
            "FIFO, LIFO, MUSA, SoftRel",
            "Putnam, VLSM, QoS, RTOS",
        ],
        answer=(
            "RL-TR-92-52, MUSA, Putnam, SoftRel Prediction"
        ),
        explanation=(
            "NCS에서 제시한 4가지 신뢰성 예측 모델은 "
            "RL-TR-92-52, MUSA, Putnam, SoftRel Prediction입니다."
        ),
        topic="신뢰성 예측 모델",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="1_2_e03",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 Skill-Set 평가 항목은?"
        ),
        passage=(
            "개발 프로세스, 모델링, 문서 작업 등 "
            "구현 기술 외의 비정형 기술 수준을 평가한다."
        ),
        options=[
            "소프트웨어 공학 및 개발 프로세스",
            "시스템 프로그래밍",
            "개발 도구",
            "하드웨어 제어 프로그래밍",
        ],
        answer="소프트웨어 공학 및 개발 프로세스",
        explanation=(
            "이 항목은 개발 프로세스, 모델링, 문서 작업 등의 "
            "기술 수준을 평가합니다."
        ),
        topic="Skill-Set",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_e04",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 임베디드 SW 구성 요소는?"
        ),
        passage=(
            "운영체제 모듈 자체 또는 운영체제의 기능을 "
            "사용하기 위해 구현된 부분"
        ),
        options=[
            "AP",
            "OP",
            "HP",
            "QoS",
        ],
        answer="OP",
        explanation=(
            "OP는 OS dependent Part로 운영체제에 "
            "의존적인 부분을 의미합니다."
        ),
        topic="기능성 평가",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_e05",
        type="multiple_choice",
        question=(
            "다음 중 ISO/IEC 9126의 품질 평가 기준을 "
            "올바르게 묶은 것은?"
        ),
        options=[
            (
                "기능성 · 신뢰성 · 이식성 · 사용성 · "
                "유지보수성 · 효율성"
            ),
            (
                "실시간성 · 경량성 · 저전력 · 보안성 · "
                "QoS · 확장성"
            ),
            (
                "프로그래밍 · 모델링 · 컴파일 · 링크 · "
                "디버깅 · 배포"
            ),
            (
                "AP · OP · HP · RAM · SRS · QoS"
            ),
        ],
        answer=(
            "기능성 · 신뢰성 · 이식성 · 사용성 · "
            "유지보수성 · 효율성"
        ),
        explanation=(
            "NCS 자료에서는 ISO/IEC 9126의 소프트웨어 품질 "
            "평가 기준으로 이 6개 항목을 제시합니다."
        ),
        topic="소프트웨어 품질 평가",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_e06",
        type="multiple_choice",
        question=(
            "다음 설명에 해당하는 시험 인증 분야는?"
        ),
        passage=(
            "에너지 관리, 원격진료, 홈 관리, 자동차 연계 서비스 등을 "
            "대상으로 서비스 수용성, 안정성, 신뢰성을 확보하기 위한 "
            "소프트웨어 시험을 수행한다."
        ),
        options=[
            "홈네트워크",
            "디지털방송",
            "이동통신",
            "항공",
        ],
        answer="홈네트워크",
        explanation=(
            "NCS에서는 홈네트워크 분야에서 이러한 SW 시험을 "
            "수행한다고 설명합니다."
        ),
        topic="임베디드 SW 시험 인증",
        difficulty="보통",
    ),

    QuizQuestion(
        id="1_2_e07",
        type="short_answer",
        question=(
            "다음 설명에 해당하는 전문가 의견 수렴 방법을 쓰시오."
        ),
        passage=(
            "전문가 집단의 의견과 판단을 반복적으로 수집하여 "
            "의견을 정리하는 방법"
        ),
        answer=[
            "델파이 방법",
            "델파이",
            "Delphi",
            "delphi",
        ],
        explanation=(
            "NCS에서는 전문가 의견 수렴 방법으로 "
            "델파이 방법과 브레인스토밍법을 제시합니다."
        ),
        topic="신뢰성 평가 방법",
        difficulty="어려움",
    ),

    QuizQuestion(
        id="1_2_e08",
        type="multiple_choice",
        question=(
            "다음 중 학습 1의 평가 항목과 가장 관련이 없는 것은?"
        ),
        options=[
            "오픈 소스 라이선스 파악",
            "신뢰성 평가 모델 파악",
            "Skill-Set 평가 항목 파악",
            "VLSM 서브넷 주소 계산",
        ],
        answer="VLSM 서브넷 주소 계산",
        explanation=(
            "학습 1에서는 기술 스펙 검토와 임베디드 시스템 평가를 "
            "중심으로 라이선스, 신뢰성 모델, Skill-Set, "
            "기능성 및 품질 평가 등을 다룹니다."
        ),
        topic="학습 1 종합",
        difficulty="쉬움",
    ),
]


# =========================================================
# 전체 문제
# =========================================================

ALL_QUIZ_1_2 = (
    FORMATIVE_QUIZ_1_2
    + EXAM_PRACTICE_1_2
)