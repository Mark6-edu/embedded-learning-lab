from __future__ import annotations


# =========================================================
# 학습 3-1
# 애플리케이션 구현 및 오류 제거
# =========================================================

LESSON_3_1 = {

    # =====================================================
    # 기본 정보
    # =====================================================

    "metadata": {
        "lesson": "학습 3",
        "section": "3-1",
        "title": "애플리케이션 구현 및 오류 제거",
        "page_range": "NCS 학습모듈 기준",
        "ncs_module": "임베디드 애플리케이션 구현",
    },


    # =====================================================
    # 학습 목표
    # =====================================================

    "objectives": [
        (
            "개발 도구와 프로그래밍 언어를 이용하여 "
            "단위 모듈과 공통 모듈을 구현할 수 있다."
        ),
        (
            "GCC의 특징과 동작 원리를 설명할 수 있다."
        ),
        (
            "GCC의 전처리, 컴파일, 어셈블, 링크 과정을 "
            "순서대로 설명할 수 있다."
        ),
        (
            "GCC의 주요 옵션을 사용하여 "
            "프로그램을 컴파일할 수 있다."
        ),
        (
            "Make와 Makefile의 역할 및 "
            "Make의 동작 과정을 설명할 수 있다."
        ),
        (
            "컴파일 과정에서 발생한 Error와 Warning을 "
            "확인하고 제거할 수 있다."
        ),
        (
            "교차 개발 환경에서 작성한 프로그램을 "
            "Target System에서 실행할 수 있다."
        ),
    ],


    # =====================================================
    # 1. GCC 개요
    # =====================================================

    "gcc_overview": {

        "title": "GCC",

        "full_name": "GNU Compiler Collection",

        "definition": (
            "GCC는 GNU 프로젝트에서 개발한 Compiler Collection으로, "
            "C를 비롯한 여러 프로그래밍 언어의 Source Code를 "
            "컴파일하여 실행 가능한 프로그램을 생성할 수 있다."
        ),

        "features": [
            (
                "GNU 프로젝트에서 개발한 "
                "대표적인 Open Source Compiler Collection이다."
            ),
            (
                "C, C++ 등 여러 프로그래밍 언어를 지원한다."
            ),
            (
                "Linux를 비롯한 다양한 운영체제에서 "
                "사용할 수 있다."
            ),
            (
                "다양한 Processor Architecture를 "
                "지원할 수 있다."
            ),
            (
                "Cross Compiler 환경을 구성하면 "
                "Host와 다른 Architecture의 Target용 "
                "프로그램을 생성할 수 있다."
            ),
            (
                "전처리, 컴파일, 어셈블, 링크 과정을 거쳐 "
                "실행 파일을 생성한다."
            ),
        ],

        "languages": [
            "C",
            "C++",
            "Objective-C",
            "Fortran",
            "Ada",
        ],

        "role": (
            "Source Code를 분석하고 여러 처리 단계를 거쳐 "
            "Processor가 실행할 수 있는 형태의 프로그램으로 "
            "변환하는 역할을 한다."
        ),

        "exam_points": [
            "GCC는 GNU Compiler Collection의 약자이다.",
            (
                "GCC는 하나의 Compiler만을 의미하기보다 "
                "여러 언어를 지원하는 Compiler Collection이다."
            ),
            (
                "GCC는 전처리 → 컴파일 → 어셈블 → 링크 과정을 "
                "통해 실행 파일을 생성한다."
            ),
            (
                "Cross GCC를 이용하면 Host와 다른 Architecture의 "
                "Target용 프로그램을 생성할 수 있다."
            ),
        ],
    },


    # =====================================================
    # 2. GCC 동작 과정
    # =====================================================

    "gcc_process": {

        "title": "GCC 동작 과정",

        "intro": (
            "GCC 명령으로 Source Code를 Compile하면 내부적으로 "
            "전처리기, Compiler, Assembler, Linker가 "
            "순차적으로 동작한다."
        ),

        "flow": [
            "Source Code",
            "cpp",
            "cc1",
            "as",
            "ld",
            "Executable File",
        ],

        "simple_flow": (
            "Source Code → cpp → cc1 → as → ld → Executable File"
        ),

        "stages": [
            {
                "name": "cpp",
                "stage": "전처리",
                "english": "Preprocessing",
                "description": (
                    "#include, #define과 같은 전처리 지시문을 "
                    "처리하여 Compiler가 처리할 Source를 만든다."
                ),
                "output": "전처리가 완료된 Source Code",
            },
            {
                "name": "cc1",
                "stage": "컴파일",
                "english": "Compilation",
                "description": (
                    "전처리된 C Source Code를 분석하여 "
                    "Assembly Code로 변환한다."
                ),
                "output": "Assembly Code",
            },
            {
                "name": "as",
                "stage": "어셈블",
                "english": "Assembly",
                "description": (
                    "Assembly Code를 Object Code로 변환하여 "
                    "Object File을 생성한다."
                ),
                "output": "Object File",
            },
            {
                "name": "ld",
                "stage": "링크",
                "english": "Linking",
                "description": (
                    "Object File과 필요한 Library를 결합하여 "
                    "최종 실행 파일을 생성한다."
                ),
                "output": "Executable File",
            },
        ],

        "target_transfer": (
            "교차 개발 환경에서는 Host에서 생성한 "
            "Target용 실행 파일을 NFS 등의 방법으로 "
            "Target System에 전달하여 실행할 수 있다."
        ),

        "exam_points": [
            "GCC 처리 순서는 cpp → cc1 → as → ld이다.",
            "`cpp`는 전처리를 수행한다.",
            "`cc1`은 C Source를 Assembly Code로 변환한다.",
            "`as`는 Assembly Code를 Object Code로 변환한다.",
            "`ld`는 Object와 Library를 링크하여 실행 파일을 만든다.",
        ],
    },


    # =====================================================
    # 3. GCC 사용법과 주요 옵션
    # =====================================================

    "gcc_usage": {

        "title": "GCC 사용법",

        "basic_syntax": (
            "gcc [option] source_file -o output_file"
        ),

        "description": (
            "GCC는 명령행에서 Source File과 Option을 지정하여 "
            "컴파일 과정을 제어할 수 있다."
        ),

        "options": [
            {
                "option": "-o",
                "description": (
                    "생성할 출력 파일의 이름을 지정한다."
                ),
                "example": (
                    "gcc test.c -o test"
                ),
            },
            {
                "option": "-c",
                "description": (
                    "Link 과정까지 진행하지 않고 "
                    "Object File만 생성한다."
                ),
                "example": (
                    "gcc -c test.c"
                ),
            },
            {
                "option": "-I",
                "description": (
                    "Header File을 검색할 Directory를 지정한다."
                ),
                "example": (
                    "gcc -I./include test.c -o test"
                ),
            },
            {
                "option": "-L",
                "description": (
                    "Library를 검색할 Directory를 지정한다."
                ),
                "example": (
                    "gcc -L./lib test.c -o test"
                ),
            },
            {
                "option": "-l",
                "description": (
                    "Link할 Library를 지정한다."
                ),
                "example": (
                    "gcc test.c -lm -o test"
                ),
            },
            {
                "option": "-g",
                "description": (
                    "GDB 등의 Debugger에서 사용할 수 있도록 "
                    "Debugging 정보를 실행 파일에 포함한다."
                ),
                "example": (
                    "gcc -g test.c -o test"
                ),
            },
            {
                "option": "-Wall",
                "description": (
                    "주요 Warning Message를 활성화하여 "
                    "잠재적인 문제를 확인할 수 있도록 한다."
                ),
                "example": (
                    "gcc -Wall test.c -o test"
                ),
            },
        ],

        "examples": [
            "gcc hello.c -o hello",
            "gcc -c module.c",
            "gcc -Wall test.c -o test",
            "gcc -g debug.c -o debug",
        ],

        "exam_points": [
            "`-o`는 출력 파일 이름을 지정한다.",
            "`-c`는 Object File까지만 생성한다.",
            "`-I`는 Header 검색 경로를 지정한다.",
            "`-L`은 Library 검색 경로를 지정한다.",
            "`-l`은 사용할 Library를 지정한다.",
            "`-g`는 Debugging 정보를 포함한다.",
            "`-Wall`은 주요 Warning을 표시하도록 한다.",
        ],
    },


    # =====================================================
    # 4. Make / Makefile
    # =====================================================

    "make": {

        "title": "Make와 Makefile",

        "definition": (
            "Make는 여러 Source File로 구성된 프로그램을 "
            "효율적으로 Build하기 위한 도구이다. "
            "Makefile에 정의된 Target과 Dependency를 확인하여 "
            "필요한 부분만 다시 Compile할 수 있다."
        ),

        "purpose": (
            "프로그램의 규모가 커지면 Source File마다 직접 "
            "Compiler 명령을 입력하는 방식은 비효율적이다. "
            "Make를 이용하면 파일 간 의존 관계를 바탕으로 "
            "Build 과정을 자동화할 수 있다."
        ),

        "basic_concepts": [
            {
                "name": "Target",
                "description": (
                    "Make가 최종적으로 만들거나 갱신하려는 "
                    "File 또는 작업이다."
                ),
            },
            {
                "name": "Dependency",
                "description": (
                    "Target을 만들기 위해 필요한 "
                    "Source File이나 다른 Target이다."
                ),
            },
            {
                "name": "Command",
                "description": (
                    "Target을 만들기 위해 실제로 실행할 "
                    "Compiler 또는 Shell 명령이다."
                ),
            },
        ],

        "structure": (
            "target: dependencies\n"
            "\tcommand"
        ),

        "example_makefile": (
            "main: main.o module.o\n"
            "\tgcc main.o module.o -o main\n"
            "\n"
            "main.o: main.c\n"
            "\tgcc -c main.c\n"
            "\n"
            "module.o: module.c\n"
            "\tgcc -c module.c"
        ),

        "process": [
            (
                "사용자가 Terminal에서 make 명령을 실행한다."
            ),
            (
                "Make가 Makefile을 읽는다."
            ),
            (
                "Target과 Dependency의 관계를 확인한다."
            ),
            (
                "Target과 Dependency File의 수정 시간을 비교한다."
            ),
            (
                "Dependency가 변경되어 다시 Build가 필요한지 판단한다."
            ),
            (
                "필요한 Command만 실행한다."
            ),
            (
                "변경된 Object 또는 실행 파일을 생성한다."
            ),
        ],

        "advantages": [
            "반복적인 Compile 명령을 자동화할 수 있다.",
            "변경된 Source File을 중심으로 필요한 부분만 다시 Build한다.",
            "여러 Source File의 Dependency를 관리할 수 있다.",
            "복잡한 프로젝트의 Build 작업을 일관되게 수행할 수 있다.",
        ],

        "exam_points": [
            "Make는 프로그램 Build를 자동화하는 도구이다.",
            "Makefile에는 Target, Dependency, Command를 기술한다.",
            (
                "Make는 Target과 Dependency 관계 및 "
                "File 수정 시간을 확인하여 Build 여부를 판단한다."
            ),
            (
                "변경되지 않은 Source를 모두 다시 Compile하는 것이 아니라 "
                "필요한 부분을 중심으로 Build할 수 있다."
            ),
            (
                "Make의 기본 흐름은 Makefile 읽기 → 의존 관계 확인 → "
                "변경 여부 판단 → 필요한 Command 실행이다."
            ),
        ],
    },


    # =====================================================
    # 5. 모듈 구현
    # =====================================================

    "module_implementation": {

        "title": "단위 모듈과 공통 모듈 구현",

        "definition": (
            "애플리케이션은 기능을 여러 Module로 나누어 "
            "구현할 수 있으며, 각각의 Module을 개별적으로 "
            "개발하고 검증한 뒤 최종 프로그램으로 통합한다."
        ),

        "unit_module": {
            "title": "단위 모듈",
            "description": (
                "하나의 독립적인 기능이나 세부 기능을 "
                "수행하도록 구현한 Module이다."
            ),
            "examples": [
                "Sensor 입력 Module",
                "Motor 제어 Module",
                "LCD 출력 Module",
            ],
        },

        "common_module": {
            "title": "공통 모듈",
            "description": (
                "여러 기능이나 Module에서 공통으로 사용하는 "
                "기능을 구현한 Module이다."
            ),
            "examples": [
                "공통 Communication 함수",
                "Error 처리 함수",
                "공통 Utility 함수",
            ],
        },

        "principles": [
            "각 Module의 역할과 기능을 명확하게 구분한다.",
            "Module 간 입력과 출력을 명확하게 정의한다.",
            "중복되는 기능은 공통 Module로 분리할 수 있다.",
            "각 Module을 개별적으로 Compile하고 검증한다.",
            "검증된 Module을 단계적으로 통합한다.",
        ],

        "implementation_flow": [
            "요구 기능 확인",
            "Module 분리",
            "단위 Module 구현",
            "공통 Module 구현",
            "Compile",
            "Error / Warning 제거",
            "Module별 동작 확인",
            "프로그램 통합",
        ],

        "exam_points": [
            (
                "단위 Module은 하나의 독립적인 세부 기능을 "
                "수행하도록 구현한다."
            ),
            (
                "공통 Module은 여러 Module에서 공통으로 "
                "사용하는 기능을 구현한다."
            ),
            (
                "Module 구현 후 Compile하여 Error와 Warning을 "
                "제거해야 한다."
            ),
        ],
    },


    # =====================================================
    # 6. Compile Error / Warning
    # =====================================================

    "compile_error": {

        "title": "컴파일 오류와 경고 제거",

        "error": {
            "title": "Error",
            "description": (
                "Compiler가 프로그램을 정상적으로 처리할 수 없어 "
                "Compile이 실패하는 문제이다."
            ),
            "examples": [
                "문법 오류",
                "정의되지 않은 변수 사용",
                "세미콜론 누락",
                "함수 선언 오류",
            ],
        },

        "warning": {
            "title": "Warning",
            "description": (
                "Compile은 가능할 수 있지만 잠재적인 문제나 "
                "의도하지 않은 동작 가능성이 있음을 "
                "Compiler가 알려주는 Message이다."
            ),
            "examples": [
                "사용하지 않는 변수",
                "자료형 불일치 가능성",
                "잘못된 함수 반환값",
                "초기화되지 않은 변수 사용 가능성",
            ],
        },

        "important_point": (
            "프로그램이 Compile된다는 이유만으로 Warning을 "
            "무시하면 안 되며, 요구사항에 맞는 안정적인 "
            "프로그램을 만들기 위해 Error와 Warning을 모두 "
            "확인하고 제거해야 한다."
        ),

        "process": [
            "Source Code 작성",
            "Compile 실행",
            "Compiler Message 확인",
            "Error 위치와 원인 분석",
            "Source Code 수정",
            "다시 Compile",
            "Warning 확인 및 수정",
            "Error / Warning이 제거될 때까지 반복",
        ],

        "arduino_example": {
            "broken_code": (
                "int ledPin = 13;\n\n"
                "void setup() {\n"
                "    pinMode(ledPin, OUTPUT)\n"
                "}\n\n"
                "void loop() {\n"
                "    digitalWrite(ledPin, HIGH);\n"
                "}"
            ),
            "problem": (
                "pinMode(ledPin, OUTPUT) 문장 끝의 "
                "세미콜론(;)이 누락되어 Compile Error가 발생한다."
            ),
            "fixed_code": (
                "pinMode(ledPin, OUTPUT);"
            ),
        },

        "exam_points": [
            "Error가 발생하면 정상적으로 Compile되지 않을 수 있다.",
            (
                "Warning은 Compile이 가능하더라도 "
                "잠재적인 문제를 의미할 수 있다."
            ),
            (
                "Compiler Message의 File, Line, Message 등을 "
                "확인하여 오류 원인을 찾는다."
            ),
            (
                "성취기준에서는 Compile하여 모든 Error와 Warning을 "
                "제거하는 것이 중요하다."
            ),
        ],
    },


    # =====================================================
    # 7. ECHO Server 실습
    # =====================================================

    "echo_server": {

        "title": "ECHO Server를 이용한 구현 실습",

        "definition": (
            "ECHO Server는 Client가 보낸 데이터를 Server가 "
            "수신한 뒤 동일한 데이터를 다시 Client에게 "
            "전송하는 Network 프로그램이다."
        ),

        "purpose": (
            "ECHO Server 실습을 통해 Source 작성, Compile, "
            "Host/Target 실행, Network 통신 및 결과 확인의 "
            "전체 개발 흐름을 경험할 수 있다."
        ),

        "important_note": (
            "교차 개발 환경에서는 Server와 Client 프로그램을 "
            "Host와 Target 환경에 맞게 Compile하고 실행해야 한다."
        ),

        "host": {
            "role": (
                "Source Code 작성, Compile, 실행 파일 생성 등의 "
                "개발 작업을 수행한다."
            ),
            "environment": (
                "Linux Host Development Environment"
            ),
            "compile_command": (
                "gcc echo_client.c -o echo_client"
            ),
        },

        "target": {
            "role": (
                "Cross Compile된 Target용 ECHO Server 프로그램을 "
                "실행한다."
            ),
            "environment": (
                "ARM Linux Target"
            ),
            "compile_command": (
                "arm-unknown-linux-gnueabi-gcc "
                "echo_server.c -o echo_server"
            ),
        },

        "port": "5100",

        "transfer_method": "NFS",

        "transfer_path": (
            "Host 공유 Directory → NFS → Target"
        ),

        "communication_flow": [
            "Client 실행",
            "Server 연결",
            "Client Data 전송",
            "Server Data 수신",
            "Server 동일 Data 재전송",
            "Client 결과 확인",
        ],

        "development_flow": [
            "ECHO Server Source Code 준비",
            "Cross Compiler로 Target용 실행 파일 생성",
            "Error / Warning 확인",
            "NFS 등을 이용해 Target에서 파일 접근",
            "Target에서 Server 실행",
            "Host에서 Client 실행",
            "Data 송수신 결과 확인",
        ],

        "exam_points": [
            (
                "ECHO Server는 Client가 보낸 데이터를 "
                "그대로 다시 전송하는 Server이다."
            ),
            (
                "Target용 Server 프로그램은 ARM Cross Compiler로 "
                "Compile할 수 있다."
            ),
            (
                "Host에서 생성한 Target용 실행 파일은 "
                "NFS를 이용해 Target에서 사용할 수 있다."
            ),
            (
                "교차 개발 실습에서는 Host와 Target의 역할을 "
                "구분하는 것이 중요하다."
            ),
        ],
    },


    # =====================================================
    # 8. Arduino 연결
    # =====================================================

    "arduino_mapping": {

        "title": "NCS 모듈 구현과 Arduino 프로젝트 연결",

        "note": (
            "NCS 학습모듈에서 다루는 Module 구현, Compile, "
            "Error/Warning 제거 과정은 Arduino 프로젝트에서도 "
            "동일한 문제 해결 흐름으로 경험할 수 있다."
        ),

        "mapping": [
            {
                "ncs": "Source Code 작성",
                "arduino": "Arduino Sketch 작성",
            },
            {
                "ncs": "Compiler",
                "arduino": "Arduino IDE Verify",
            },
            {
                "ncs": "Compile Error",
                "arduino": "Arduino IDE Compiler Error",
            },
            {
                "ncs": "Warning 확인",
                "arduino": "Compiler Warning 확인",
            },
            {
                "ncs": "단위 Module",
                "arduino": "Sensor / Motor / LCD 기능별 함수",
            },
            {
                "ncs": "공통 Module",
                "arduino": "여러 기능에서 사용하는 공통 함수",
            },
            {
                "ncs": "프로그램 실행",
                "arduino": "Upload 후 Board에서 실행",
            },
        ],

        "project_example": {
            "project": "자동 물주기 스마트 화분",
            "modules": [
                "토양 수분 Sensor 입력 Module",
                "Pump 제어 Module",
                "온습도 측정 Module",
                "LCD 출력 Module",
            ],
            "integration": (
                "각 기능을 개별적으로 구현·검증한 뒤 "
                "하나의 Arduino 프로그램으로 통합한다."
            ),
        },
    },


    # =====================================================
    # 9. 미니 실습
    # =====================================================

    "practice": {

        "title": "GCC와 모듈 구현 미니 실습",

        "activities": [
            {
                "title": "GCC 처리 순서 맞추기",
                "instruction": (
                    "cpp, cc1, as, ld를 올바른 순서로 배열한다."
                ),
            },
            {
                "title": "GCC Option 선택하기",
                "instruction": (
                    "출력 파일 지정, Object File 생성, "
                    "Debug 정보 추가 상황에 맞는 Option을 선택한다."
                ),
            },
            {
                "title": "Make 동작 과정 배열하기",
                "instruction": (
                    "Makefile 확인부터 변경된 File Build까지의 "
                    "동작 순서를 배열한다."
                ),
            },
            {
                "title": "Compile Error 찾기",
                "instruction": (
                    "주어진 C 또는 Arduino Code에서 "
                    "Compile Error의 원인을 찾고 수정한다."
                ),
            },
            {
                "title": "Module 나누기",
                "instruction": (
                    "Arduino 프로젝트의 기능을 단위 Module과 "
                    "공통 Module로 나누어 본다."
                ),
            },
        ],

        "example_questions": [
            {
                "question": (
                    "GCC 내부 처리 과정에서 전처리를 담당하는 것은?"
                ),
                "answer": "cpp",
            },
            {
                "question": (
                    "Assembly Code를 Object Code로 변환하는 것은?"
                ),
                "answer": "as",
            },
            {
                "question": (
                    "여러 Object와 Library를 연결하여 "
                    "실행 파일을 만드는 것은?"
                ),
                "answer": "ld",
            },
            {
                "question": (
                    "Object File까지만 생성하는 GCC Option은?"
                ),
                "answer": "-c",
            },
            {
                "question": (
                    "Debug 정보를 포함시키는 GCC Option은?"
                ),
                "answer": "-g",
            },
            {
                "question": (
                    "Make가 Build 순서를 판단하기 위해 확인하는 "
                    "File은?"
                ),
                "answer": "Makefile",
            },
        ],
    },


    # =====================================================
    # 10. 핵심 정리
    # =====================================================

    "summary": [
        (
            "GCC는 GNU Compiler Collection으로 여러 언어와 "
            "Processor Architecture를 지원하는 Compiler Collection이다."
        ),
        (
            "GCC의 내부 처리 과정은 "
            "cpp → cc1 → as → ld 순서이다."
        ),
        (
            "cpp는 전처리, cc1은 컴파일, as는 어셈블, "
            "ld는 링크를 담당한다."
        ),
        (
            "`-o`는 출력 파일의 이름을 지정하고 "
            "`-c`는 Object File까지만 생성한다."
        ),
        (
            "`-I`는 Header 검색 경로, "
            "`-L`은 Library 검색 경로를 지정한다."
        ),
        (
            "`-g`는 Debugging 정보를 포함하고 "
            "`-Wall`은 주요 Warning을 활성화한다."
        ),
        (
            "Make는 Makefile에 정의된 Target, Dependency, "
            "Command를 바탕으로 Build 과정을 자동화한다."
        ),
        (
            "Make는 File의 Dependency와 수정 상태를 확인하여 "
            "필요한 부분을 중심으로 다시 Build한다."
        ),
        (
            "단위 Module은 하나의 세부 기능을 수행하고 "
            "공통 Module은 여러 Module에서 공유하는 기능을 수행한다."
        ),
        (
            "Compile Error는 정상적인 Compile을 방해하며, "
            "Warning은 잠재적인 문제를 알려준다."
        ),
        (
            "프로그램 구현 과정에서는 Compiler Message를 확인하여 "
            "Error와 Warning을 모두 제거해야 한다."
        ),
        (
            "ECHO Server는 Client가 전송한 Data를 "
            "동일하게 다시 Client에게 전송한다."
        ),
        (
            "교차 개발 환경에서는 Host에서 Target용 실행 파일을 "
            "생성한 뒤 NFS 등을 이용하여 Target에서 실행할 수 있다."
        ),
        (
            "Arduino 프로젝트에서도 기능별 Module 구현 → Verify → "
            "Error 수정 → Upload → 통합의 흐름을 적용할 수 있다."
        ),
    ],
}