from __future__ import annotations


# =========================================================
# 학습 4-2
# 소스 코드 저장 및 버전 관리
# =========================================================

LESSON_4_2 = {

    # =====================================================
    # 기본 정보
    # =====================================================

    "metadata": {
        "lesson": "학습 4",
        "section": "4-2",
        "title": "소스 코드 저장 및 버전 관리",
        "page_range": "NCS 학습모듈 기준",
        "ncs_module": "임베디드 애플리케이션 구현",
    },


    # =====================================================
    # 학습 목표
    # =====================================================

    "objectives": [
        (
            "소스 코드 저장 및 버전 관리의 필요성을 "
            "설명할 수 있다."
        ),
        (
            "중앙 집중형과 분산형 버전 관리 시스템의 "
            "특징을 구분할 수 있다."
        ),
        (
            "CVS, SVN, GIT의 특징을 비교할 수 있다."
        ),
        (
            "Repository와 Commit의 개념을 설명할 수 있다."
        ),
        (
            "SVN을 이용한 Source Code 저장 및 "
            "Commit 과정을 설명할 수 있다."
        ),
        (
            "Git과 GitHub의 차이를 설명할 수 있다."
        ),
        (
            "Configuration Management의 목적과 "
            "주요 관리 대상을 설명할 수 있다."
        ),
        (
            "CASE Tool의 개념과 Software Development "
            "지원 역할을 설명할 수 있다."
        ),
    ],


    # =====================================================
    # 1. Version Control 개요
    # =====================================================

    "version_control_overview": {

        "title": "Version Control",

        "definition": (
            "Version Control은 Software 개발 과정에서 "
            "Source Code와 관련 File의 변경 내용을 저장하고 "
            "관리하여 필요한 시점의 상태를 확인하거나 "
            "이전 Version으로 복구할 수 있도록 하는 "
            "관리 방법이다."
        ),

        "why_needed": [
            (
                "Source Code가 언제 어떻게 변경되었는지 "
                "확인할 수 있다."
            ),
            (
                "잘못된 수정이 발생했을 때 "
                "이전 상태를 확인하거나 복구할 수 있다."
            ),
            (
                "여러 개발자가 공동으로 Source Code를 "
                "관리할 수 있다."
            ),
            (
                "개발 과정에서 Version별 결과물을 "
                "체계적으로 관리할 수 있다."
            ),
            (
                "Software Configuration Management와 "
                "연계하여 개발 결과물의 품질을 관리할 수 있다."
            ),
        ],

        "managed_items": [
            "Source Code",
            "Header File",
            "Configuration File",
            "Document",
            "Library 정보",
            "Build 관련 File",
        ],

        "basic_terms": [
            {
                "term": "Repository",
                "description": (
                    "Version 관리 대상과 변경 이력을 "
                    "저장하는 저장 공간이다."
                ),
            },
            {
                "term": "Commit",
                "description": (
                    "작업한 변경 내용을 Repository에 "
                    "하나의 Version으로 반영하는 작업이다."
                ),
            },
            {
                "term": "Update",
                "description": (
                    "Repository의 최신 변경 내용을 "
                    "Working Copy에 반영하는 작업이다."
                ),
            },
            {
                "term": "Working Copy",
                "description": (
                    "개발자가 실제로 수정 작업을 수행하는 "
                    "Local 작업 공간이다."
                ),
            },
        ],

        "exam_points": [
            (
                "Version Control은 Source Code 등의 변경 이력을 "
                "저장하고 관리하기 위해 사용한다."
            ),
            (
                "Version Control을 사용하면 변경 내용 확인, "
                "이전 Version 복구, 공동 개발이 가능하다."
            ),
            (
                "Repository는 Version 관리 대상과 "
                "변경 이력을 저장하는 공간이다."
            ),
            (
                "Commit은 변경 내용을 Repository에 "
                "반영하는 작업이다."
            ),
        ],
    },


    # =====================================================
    # 2. Version Control 방식
    # =====================================================

    "version_control_types": {

        "title": "Version Control System의 유형",

        "centralized": {
            "title": "Centralized Version Control",
            "description": (
                "하나의 중앙 Repository를 중심으로 "
                "여러 개발자가 Source Code를 공유하고 "
                "Version을 관리하는 방식이다."
            ),
            "characteristics": [
                "중앙 Server에 Repository가 존재한다.",
                "개발자는 중앙 Repository와 연결하여 작업한다.",
                "관리 구조를 이해하기 쉽다.",
                (
                    "중앙 Repository 또는 Network에 문제가 생기면 "
                    "작업에 영향을 받을 수 있다."
                ),
            ],
            "examples": [
                "CVS",
                "SVN",
            ],
        },

        "distributed": {
            "title": "Distributed Version Control",
            "description": (
                "각 개발자가 Repository의 정보를 "
                "자신의 Local 환경에 가지고 작업할 수 있는 "
                "분산형 Version 관리 방식이다."
            ),
            "characteristics": [
                "각 개발자가 Repository 정보를 Local에 가진다.",
                "Local에서 Version 기록 작업을 수행할 수 있다.",
                (
                    "Remote Repository 연결을 최소화하면서 "
                    "작업할 수 있다."
                ),
                "분산된 환경에서 협업하기에 유리하다.",
            ],
            "examples": [
                "GIT",
            ],
        },

        "comparison": [
            {
                "category": "Repository",
                "centralized": "중앙 Repository 중심",
                "distributed": "각 개발자가 Repository 정보를 보유",
            },
            {
                "category": "Network 의존",
                "centralized": "상대적으로 큼",
                "distributed": "Local 작업 가능",
            },
            {
                "category": "대표 시스템",
                "centralized": "CVS, SVN",
                "distributed": "GIT",
            },
        ],

        "exam_points": [
            "CVS와 SVN은 중앙 집중형 Version 관리 방식이다.",
            "GIT은 분산형 Version 관리 방식이다.",
            (
                "중앙 집중형은 하나의 중앙 Repository를 "
                "중심으로 Version을 관리한다."
            ),
            (
                "분산형은 개발자가 Repository 정보를 "
                "Local 환경에 가지고 작업할 수 있다."
            ),
        ],
    },


    # =====================================================
    # 3. CVS
    # =====================================================

    "cvs": {

        "title": "CVS",

        "full_name": "Concurrent Versions System",

        "definition": (
            "CVS는 중앙 Repository를 이용하여 "
            "여러 개발자가 Source Code의 Version을 "
            "관리할 수 있도록 하는 Version Control System이다."
        ),

        "characteristics": [
            "중앙 집중형 Version 관리 방식이다.",
            "개별 File 단위로 Version을 관리한다.",
            "ASCII File 중심의 관리 방식으로 설명된다.",
            (
                "여러 개발자가 하나의 Repository를 "
                "공동으로 사용할 수 있다."
            ),
        ],

        "management_unit": "개별 File",

        "file_support": "ASCII 중심",

        "exam_points": [
            "CVS는 Concurrent Versions System의 약자이다.",
            "CVS는 중앙 집중형 Version 관리 시스템이다.",
            "CVS는 개별 File 단위로 Version을 관리한다.",
            "학습모듈 비교 기준에서 CVS는 ASCII File 중심이다.",
        ],
    },


    # =====================================================
    # 4. SVN
    # =====================================================

    "svn": {

        "title": "SVN",

        "full_name": "Subversion",

        "definition": (
            "SVN은 중앙 Repository를 이용하여 "
            "Software Project의 Source Code와 File을 "
            "Version별로 관리할 수 있는 "
            "중앙 집중형 Version Control System이다."
        ),

        "characteristics": [
            "중앙 집중형 Version 관리 방식이다.",
            "작업 단위 중심으로 Version을 관리할 수 있다.",
            "ASCII와 Binary File을 관리할 수 있다.",
            "Repository에 변경 내용을 Commit할 수 있다.",
            "Working Copy를 이용하여 Local에서 File을 수정한다.",
        ],

        "management_unit": "작업 단위",

        "file_support": "ASCII + Binary",

        "basic_flow": [
            "Repository 준비",
            "Working Copy 준비",
            "Source Code 수정",
            "변경 내용 확인",
            "Commit",
            "Repository에 새로운 Version 반영",
        ],

        "exam_points": [
            "SVN은 Subversion을 의미한다.",
            "SVN은 중앙 집중형 Version 관리 시스템이다.",
            (
                "학습모듈 비교 기준에서 SVN은 "
                "작업 단위로 Version을 관리한다."
            ),
            "SVN은 ASCII와 Binary File을 관리할 수 있다.",
            "변경 내용은 Commit을 통해 Repository에 반영한다.",
        ],
    },


    # =====================================================
    # 5. GIT
    # =====================================================

    "git": {

        "title": "GIT",

        "definition": (
            "GIT은 분산형 Version Control System으로, "
            "각 개발자가 Repository의 정보를 Local 환경에 "
            "보유하면서 Source Code의 Version을 "
            "관리할 수 있다."
        ),

        "characteristics": [
            "분산형 Version 관리 방식이다.",
            (
                "각 개발자가 Repository 전체의 정보를 "
                "Local 환경에 가지고 작업할 수 있다."
            ),
            (
                "Remote Repository와 계속 연결하지 않아도 "
                "Local에서 Version 관리 작업을 수행할 수 있다."
            ),
            (
                "File의 변경 내용을 Snapshot 개념으로 "
                "관리하는 방식으로 설명할 수 있다."
            ),
            (
                "여러 개발자의 분산 협업 환경에 "
                "적합하게 사용할 수 있다."
            ),
        ],

        "management_unit": "Snapshot",

        "repository_style": (
            "Repository의 정보를 Local에 복사하여 관리"
        ),

        "remote_connection": (
            "Remote Repository 연결을 최소화하면서 "
            "Local 작업 가능"
        ),

        "basic_terms": [
            "Repository",
            "Working Directory",
            "Commit",
            "Snapshot",
            "Remote Repository",
        ],

        "exam_points": [
            "GIT은 분산형 Version Control System이다.",
            (
                "GIT에서는 각 개발자가 Repository 정보를 "
                "Local 환경에 보유할 수 있다."
            ),
            (
                "학습모듈 비교 기준에서 GIT은 "
                "Snapshot 방식으로 Version을 관리한다."
            ),
            (
                "GIT은 Remote Repository 연결을 최소화하면서 "
                "Local 작업을 수행할 수 있다."
            ),
        ],
    },


    # =====================================================
    # 6. GitHub
    # =====================================================

    "github": {

        "title": "GitHub",

        "definition": (
            "GitHub는 GIT Repository를 Network 환경에서 "
            "저장하고 공유하며 협업할 수 있도록 지원하는 "
            "Service이다."
        ),

        "git_vs_github": [
            {
                "name": "GIT",
                "description": (
                    "Source Code의 Version을 관리하는 "
                    "분산형 Version Control System이다."
                ),
            },
            {
                "name": "GitHub",
                "description": (
                    "GIT Repository를 저장하고 공유하며 "
                    "협업할 수 있도록 지원하는 Service이다."
                ),
            },
        ],

        "important_point": (
            "GIT과 GitHub는 같은 개념이 아니다. "
            "GIT은 Version Control System이고, "
            "GitHub는 GIT Repository를 활용할 수 있도록 "
            "지원하는 Network 기반 Service이다."
        ),

        "uses": [
            "Remote Repository 저장",
            "Source Code 공유",
            "개발자 협업",
            "변경 이력 확인",
            "Project Source 관리",
        ],

        "exam_points": [
            (
                "GIT은 Version Control System이고 "
                "GitHub는 GIT Repository를 활용하는 Service이다."
            ),
            "GIT과 GitHub는 동일한 개념이 아니다.",
            (
                "GitHub는 GIT Repository를 저장하고 "
                "공유하는 데 활용할 수 있다."
            ),
        ],
    },


    # =====================================================
    # 7. Repository
    # =====================================================

    "repository": {

        "title": "Repository",

        "definition": (
            "Repository는 Source Code와 관련 File의 "
            "Version 정보 및 변경 이력을 저장하고 "
            "관리하는 공간이다."
        ),

        "types": [
            {
                "name": "Central Repository",
                "description": (
                    "CVS와 SVN처럼 중앙 Server에서 "
                    "공동으로 사용하는 Repository이다."
                ),
            },
            {
                "name": "Local Repository",
                "description": (
                    "GIT과 같은 분산형 Version Control에서 "
                    "개발자의 Local 환경에 존재하는 Repository이다."
                ),
            },
            {
                "name": "Remote Repository",
                "description": (
                    "Network를 통해 여러 개발자가 "
                    "공유할 수 있는 Repository이다."
                ),
            },
        ],

        "repository_flow": [
            "Source Code 작성",
            "변경 내용 확인",
            "Version 저장",
            "Repository에 변경 이력 축적",
            "필요 시 이전 Version 확인",
        ],

        "exam_points": [
            (
                "Repository는 Version 관리 대상과 "
                "변경 이력을 저장하는 공간이다."
            ),
            (
                "SVN에서는 중앙 Repository를 중심으로 "
                "작업한다."
            ),
            (
                "GIT에서는 Local Repository와 "
                "Remote Repository를 활용할 수 있다."
            ),
        ],
    },


    # =====================================================
    # 8. SVN 실습
    # =====================================================

    "svn_practice": {

        "title": "SVN Source Code 관리 실습",

        "source_file": "scm_test.c",

        "purpose": (
            "Source Code를 수정하고 변경된 내용을 "
            "SVN Repository에 Commit하는 과정을 통해 "
            "Version 관리의 기본 흐름을 학습한다."
        ),

        "procedure": [
            {
                "step": 1,
                "title": "Working Copy 확인",
                "description": (
                    "Version 관리 대상 Source Code가 있는 "
                    "Working Directory를 확인한다."
                ),
            },
            {
                "step": 2,
                "title": "Source Code 확인",
                "description": (
                    "scm_test.c File의 내용을 확인한다."
                ),
                "file": "scm_test.c",
            },
            {
                "step": 3,
                "title": "Source Code 수정",
                "description": (
                    "요구사항에 맞게 scm_test.c의 "
                    "내용을 수정한다."
                ),
            },
            {
                "step": 4,
                "title": "변경 내용 확인",
                "description": (
                    "수정된 Source Code의 변경 상태를 확인한다."
                ),
            },
            {
                "step": 5,
                "title": "Commit",
                "description": (
                    "수정된 Source Code를 Repository에 "
                    "새로운 Version으로 반영한다."
                ),
            },
            {
                "step": 6,
                "title": "Version 확인",
                "description": (
                    "Repository에 변경 내용이 정상적으로 "
                    "저장되었는지 확인한다."
                ),
            },
        ],

        "commit": {
            "definition": (
                "Commit은 Working Copy에서 변경한 내용을 "
                "Repository에 하나의 변경 이력으로 "
                "반영하는 작업이다."
            ),
            "important_point": (
                "Commit하기 전에는 변경된 Source Code의 "
                "내용과 정상 동작 여부를 확인하는 것이 중요하다."
            ),
        },

        "exam_points": [
            "SVN 실습 Source File의 예는 scm_test.c이다.",
            (
                "Working Copy에서 Source를 수정한 뒤 "
                "Commit하여 Repository에 반영한다."
            ),
            (
                "Commit은 변경 내용을 Repository에 "
                "저장하는 작업이다."
            ),
            (
                "Version 관리에서는 변경 내용과 "
                "변경 이력을 함께 관리하는 것이 중요하다."
            ),
        ],
    },


    # =====================================================
    # 9. 협업
    # =====================================================

    "collaboration": {

        "title": "Version Control과 협업",

        "definition": (
            "여러 개발자가 하나의 Software를 공동으로 "
            "개발할 때 Version Control System을 이용하면 "
            "각 개발자의 Source 변경 내용을 체계적으로 "
            "관리할 수 있다."
        ),

        "workflow": [
            "공동 Repository 준비",
            "개발자별 Working Environment 준비",
            "담당 Module 또는 Source 수정",
            "변경 내용 확인",
            "Commit 또는 Version 반영",
            "다른 개발자의 변경 내용 확인",
            "통합",
            "Test",
        ],

        "important_points": [
            "변경 목적을 명확히 한다.",
            "작은 단위로 변경 내용을 관리한다.",
            "Commit 전 정상 동작 여부를 확인한다.",
            "다른 개발자의 변경 내용과 충돌 여부를 확인한다.",
            "공통 Source Code를 임의로 변경하지 않는다.",
            "Version별 결과물을 체계적으로 관리한다.",
        ],

        "exam_points": [
            (
                "Version Control System은 여러 개발자의 "
                "공동 개발을 지원한다."
            ),
            (
                "협업에서는 Source 변경 이력과 "
                "Version을 체계적으로 관리해야 한다."
            ),
            (
                "Commit 전 변경 내용과 프로그램 동작을 "
                "확인하는 것이 중요하다."
            ),
        ],
    },


    # =====================================================
    # 10. Configuration Management
    # =====================================================

    "configuration_management": {

        "title": "Software Configuration Management",

        "definition": (
            "Software Configuration Management는 "
            "Software 개발 과정에서 생성되는 다양한 "
            "Configuration Item의 변경 상태와 Version을 "
            "체계적으로 식별하고 관리하는 활동이다."
        ),

        "configuration_items": [
            "Source Code",
            "Document",
            "Library",
            "Configuration File",
            "Build File",
            "Test 결과",
            "Release Version",
        ],

        "activities": [
            {
                "name": "Configuration Identification",
                "description": (
                    "관리할 Configuration Item을 "
                    "식별하고 구분한다."
                ),
            },
            {
                "name": "Version Control",
                "description": (
                    "Configuration Item의 Version과 "
                    "변경 이력을 관리한다."
                ),
            },
            {
                "name": "Change Control",
                "description": (
                    "변경 요청과 변경 내용을 "
                    "통제하고 관리한다."
                ),
            },
            {
                "name": "Status Management",
                "description": (
                    "각 Configuration Item의 "
                    "현재 상태를 확인하고 관리한다."
                ),
            },
        ],

        "purpose": [
            "Software 변경 이력 관리",
            "Version별 결과물 관리",
            "개발 결과물의 일관성 유지",
            "변경에 따른 오류 감소",
            "Software Quality 유지",
        ],

        "exam_points": [
            (
                "Configuration Management는 Source Code뿐 아니라 "
                "Document와 Configuration File 등도 관리한다."
            ),
            (
                "Version Control은 Configuration Management의 "
                "중요한 활동 중 하나이다."
            ),
            (
                "Configuration Item을 식별하고 변경 상태와 "
                "Version을 관리해야 한다."
            ),
            (
                "Configuration Management는 Software Quality "
                "유지와도 관련된다."
            ),
        ],
    },


    # =====================================================
    # 11. CASE Tool
    # =====================================================

    "case_tools": {

        "title": "CASE",

        "full_name": "Computer Aided Software Engineering",

        "definition": (
            "CASE는 Software Development 과정에서 수행되는 "
            "분석, 설계, 구현, Test, 유지보수 등의 활동을 "
            "Computer Tool을 이용하여 지원하는 "
            "Software Engineering 환경 또는 도구이다."
        ),

        "roles": [
            "Software Development 작업 지원",
            "개발 문서 작성 지원",
            "Modeling 지원",
            "Source Code 관리 지원",
            "Project 관리 지원",
            "Software Quality 향상 지원",
        ],

        "development_stages": [
            "Analysis",
            "Design",
            "Implementation",
            "Testing",
            "Maintenance",
        ],

        "benefits": [
            "반복적인 개발 작업을 자동화할 수 있다.",
            "개발 문서와 결과물을 체계적으로 관리할 수 있다.",
            "개발 생산성을 높이는 데 도움을 줄 수 있다.",
            "Software Quality 관리에 도움을 줄 수 있다.",
        ],

        "exam_points": [
            (
                "CASE는 Computer Aided Software Engineering의 "
                "약자이다."
            ),
            (
                "CASE Tool은 Software Development의 여러 단계를 "
                "지원하는 Computer 기반 도구이다."
            ),
            (
                "CASE는 분석, 설계, 구현, Test, 유지보수 등의 "
                "과정을 지원할 수 있다."
            ),
            (
                "CASE Tool은 개발 생산성과 Software Quality "
                "향상에 도움을 줄 수 있다."
            ),
        ],
    },


    # =====================================================
    # 12. Arduino / Git 연결
    # =====================================================

    "arduino_mapping": {

        "title": "NCS Version Control과 Arduino 프로젝트 연결",

        "note": (
            "NCS 학습모듈에서 다루는 Version Control과 "
            "Configuration Management는 Arduino 프로젝트에서도 "
            "Source Code의 수정 이력과 완성 Version을 "
            "관리하는 데 그대로 적용할 수 있다."
        ),

        "mapping": [
            {
                "ncs": "Source Code Version 관리",
                "arduino": "Arduino .ino File 변경 이력 관리",
            },
            {
                "ncs": "Repository",
                "arduino": "Arduino Project Repository",
            },
            {
                "ncs": "Commit",
                "arduino": "Sketch 수정 내용을 Version으로 저장",
            },
            {
                "ncs": "Configuration Item",
                "arduino": (
                    ".ino, Header, 회로 관련 Document, "
                    "부품 목록 등"
                ),
            },
            {
                "ncs": "Version",
                "arduino": "v1 → v2 → 최종 Version",
            },
            {
                "ncs": "협업",
                "arduino": (
                    "팀원이 Code와 기능을 나누어 개발한 뒤 통합"
                ),
            },
        ],

        "project_example": {
            "project": "Arduino 스마트 화분",
            "versions": [
                {
                    "version": "v1",
                    "change": "토양 수분 Sensor 값 출력",
                },
                {
                    "version": "v2",
                    "change": "Pump 자동 제어 추가",
                },
                {
                    "version": "v3",
                    "change": "LCD 출력 기능 추가",
                },
                {
                    "version": "v4",
                    "change": "전체 기능 통합 및 오류 수정",
                },
            ],
        },

        "git_example_flow": [
            "Arduino Project Folder 준비",
            "GIT Repository 초기화",
            "Source Code 수정",
            "변경 내용 확인",
            "Commit",
            "필요한 경우 Remote Repository와 공유",
        ],

        "important_distinction": (
            "시험 범위에서는 CVS, SVN, GIT의 특징과 "
            "학습모듈의 SVN 실습 흐름을 우선 학습하고, "
            "Arduino와 GIT 연결은 실제 프로젝트에 적용하기 위한 "
            "확장 활동으로 이해한다."
        ),
    },


    # =====================================================
    # 13. 미니 실습
    # =====================================================

    "practice": {

        "title": "Version Control 미니 실습",

        "activities": [
            {
                "title": "CVS · SVN · GIT 구분하기",
                "instruction": (
                    "각 Version Control System의 "
                    "관리 방식과 특징을 구분한다."
                ),
            },
            {
                "title": "중앙 집중형 · 분산형 구분하기",
                "instruction": (
                    "CVS, SVN, GIT을 중앙 집중형과 "
                    "분산형으로 분류한다."
                ),
            },
            {
                "title": "Commit 흐름 이해하기",
                "instruction": (
                    "Working Copy에서 Source를 수정한 뒤 "
                    "Repository에 반영하는 과정을 배열한다."
                ),
            },
            {
                "title": "Git과 GitHub 구분하기",
                "instruction": (
                    "Version Control System과 "
                    "Repository 공유 Service의 차이를 판단한다."
                ),
            },
            {
                "title": "Configuration Item 찾기",
                "instruction": (
                    "Arduino 프로젝트에서 Version 관리가 필요한 "
                    "Source, Document, Configuration File 등을 "
                    "찾아본다."
                ),
            },
        ],

        "example_questions": [
            {
                "question": (
                    "CVS와 SVN은 어떤 형태의 "
                    "Version Control System인가?"
                ),
                "answer": "중앙 집중형",
            },
            {
                "question": (
                    "GIT은 어떤 형태의 "
                    "Version Control System인가?"
                ),
                "answer": "분산형",
            },
            {
                "question": (
                    "학습모듈 비교 기준에서 CVS의 "
                    "Version 관리 단위는?"
                ),
                "answer": "개별 File",
            },
            {
                "question": (
                    "학습모듈 비교 기준에서 SVN의 "
                    "Version 관리 단위는?"
                ),
                "answer": "작업 단위",
            },
            {
                "question": (
                    "학습모듈 비교 기준에서 GIT의 "
                    "Version 관리 방식은?"
                ),
                "answer": "Snapshot",
            },
            {
                "question": (
                    "Working Copy에서 수정한 내용을 "
                    "Repository에 반영하는 작업은?"
                ),
                "answer": "Commit",
            },
            {
                "question": (
                    "GIT Repository를 저장하고 공유할 수 있도록 "
                    "지원하는 Service의 예는?"
                ),
                "answer": "GitHub",
            },
            {
                "question": (
                    "CASE의 전체 이름은?"
                ),
                "answer": (
                    "Computer Aided Software Engineering"
                ),
            },
        ],
    },


    # =====================================================
    # 14. 핵심 정리
    # =====================================================

    "summary": [
        (
            "Version Control은 Source Code와 관련 File의 "
            "변경 이력과 Version을 관리하기 위해 사용한다."
        ),
        (
            "Repository는 Version 관리 대상과 "
            "변경 이력을 저장하는 공간이다."
        ),
        (
            "Commit은 변경 내용을 Repository에 "
            "하나의 Version으로 반영하는 작업이다."
        ),
        (
            "CVS와 SVN은 중앙 집중형 Version Control System이다."
        ),
        (
            "GIT은 분산형 Version Control System이다."
        ),
        (
            "CVS는 학습모듈 비교 기준에서 "
            "개별 File 단위로 Version을 관리한다."
        ),
        (
            "CVS는 학습모듈 비교 기준에서 "
            "ASCII File 중심으로 관리한다."
        ),
        (
            "SVN은 학습모듈 비교 기준에서 "
            "작업 단위로 Version을 관리한다."
        ),
        (
            "SVN은 ASCII와 Binary File을 관리할 수 있다."
        ),
        (
            "GIT은 학습모듈 비교 기준에서 "
            "Snapshot 방식으로 Version을 관리한다."
        ),
        (
            "GIT에서는 각 개발자가 Repository 정보를 "
            "Local 환경에 가지고 작업할 수 있다."
        ),
        (
            "GIT은 Remote Repository 연결을 최소화하면서 "
            "Local Version 관리 작업을 수행할 수 있다."
        ),
        (
            "GIT은 Version Control System이며 "
            "GitHub는 GIT Repository를 저장하고 공유하는 "
            "Service이다."
        ),
        (
            "SVN 실습에서는 scm_test.c와 같은 Source를 "
            "수정한 뒤 Commit하여 Repository에 반영할 수 있다."
        ),
        (
            "Version Control System은 여러 개발자가 "
            "공동으로 Source Code를 관리하는 데 활용할 수 있다."
        ),
        (
            "Software Configuration Management는 Source Code, "
            "Document, Configuration File 등의 Version과 "
            "변경 상태를 체계적으로 관리한다."
        ),
        (
            "Version Control은 Software Configuration "
            "Management의 중요한 활동 중 하나이다."
        ),
        (
            "CASE는 Computer Aided Software Engineering을 "
            "의미한다."
        ),
        (
            "CASE Tool은 Software의 분석, 설계, 구현, Test, "
            "유지보수 등의 개발 활동을 지원할 수 있다."
        ),
        (
            "Arduino 프로젝트에서도 Source Code와 Document를 "
            "Version별로 관리하면 개발 과정과 문제 해결 이력을 "
            "체계적으로 남길 수 있다."
        ),
    ],
}