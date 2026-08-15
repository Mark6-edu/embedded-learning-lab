# 임베디드 애플리케이션 구현 LAB

## 프로젝트 목적
이 프로젝트는 특성화고등학교 시스템 프로그래밍 수업에서 사용할 수 있는 NCS 기반 임베디드 애플리케이션 구현 학습용 Streamlit 웹 애플리케이션입니다.

학생들은 핵심 이론 학습, 개념 확인, 미니 실습, Arduino 연계 내용을 순서대로 학습할 수 있으며, 향후 실제 프로젝트와 연결할 수 있는 기반 구조를 마련하는 것이 목표입니다.

## 대상 교과 및 학생
- 교과: 시스템 프로그래밍
- 대상: 특성화고등학교 2학년
- 학습 영역: NCS 임베디드 애플리케이션 구현

## 주요 기능
- 메인 홈 화면 및 학습 영역 소개
- 학습 1~4 기본 페이지 골격 구성
- 학습 이론, 핵심 개념, 실습 영역 구조화
- 향후 확장을 고려한 퀴즈 데이터 구조 설계
- 공통 UI 함수 기반 재사용 구조

## 프로젝트 구조
```text
embedded-learning-lab/
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
├── data/
│   ├── __init__.py
│   ├── lessons/
│   │   ├── __init__.py
│   │   └── lesson_1_1.py
│   └── quizzes/
│       ├── __init__.py
│       └── quiz_1_1.py
├── pages/
│   ├── 01_학습1_기술명세.py
│   ├── 02_학습2_개발환경.py
│   ├── 03_학습3_모듈구현.py
│   └── 04_학습4_인터페이스.py
└── utils/
    ├── __init__.py
    ├── ui.py
    ├── quiz.py
    └── progress.py
```

## 로컬 실행 방법
1. 가상 환경 생성

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

2. 의존성 설치

```bash
pip install -r requirements.txt
```

3. 앱 실행

```bash
streamlit run streamlit_app.py
```

## 참고
현재 단계는 기본 구조와 학습 페이지 골격을 구축한 초기 버전입니다. 향후 학습 1-1의 실제 NCS 콘텐츠를 확장할 수 있도록 데이터와 UI를 분리해 설계하였습니다.
