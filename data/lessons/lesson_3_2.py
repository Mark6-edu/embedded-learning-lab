from __future__ import annotations


# =========================================================
# 학습 3-2
# 디버깅 및 프로그램 통합
# =========================================================

LESSON_3_2 = {

    # =====================================================
    # 기본 정보
    # =====================================================

    "metadata": {
        "lesson": "학습 3",
        "section": "3-2",
        "title": "디버깅 및 프로그램 통합",
        "page_range": "NCS 학습모듈 기준",
        "ncs_module": "임베디드 애플리케이션 구현",
    },


    # =====================================================
    # 학습 목표
    # =====================================================

    "objectives": [
        (
            "디버깅의 개념과 필요성을 설명할 수 있다."
        ),
        (
            "GDB의 특징과 주요 기능을 설명할 수 있다."
        ),
        (
            "GDB의 실행 모드와 기본 사용 절차를 "
            "설명할 수 있다."
        ),
        (
            "Breakpoint와 Step 실행을 이용하여 "
            "프로그램의 실행 흐름을 분석할 수 있다."
        ),
        (
            "GDB 명령어를 이용하여 변수 값과 "
            "프로그램 상태를 확인할 수 있다."
        ),
        (
            "Host와 Target을 이용한 원격 디버깅 환경을 "
            "설명할 수 있다."
        ),
        (
            "개별적으로 구현한 Module을 검증한 뒤 "
            "하나의 프로그램으로 통합할 수 있다."
        ),
    ],


    # =====================================================
    # 1. 디버깅 개요
    # =====================================================

    "debugging_overview": {

        "title": "디버깅",

        "definition": (
            "디버깅은 프로그램이 의도한 대로 동작하지 않는 "
            "원인을 찾아 분석하고 수정하는 과정이다."
        ),

        "purpose": (
            "Compile Error를 모두 제거한 프로그램이라도 "
            "논리적인 오류나 실행 중 발생하는 문제가 있을 수 있다. "
            "따라서 프로그램을 실행하면서 내부 상태와 실행 흐름을 "
            "확인하여 오류의 원인을 분석해야 한다."
        ),

        "types_of_problem": [
            {
                "name": "Syntax Error",
                "description": (
                    "문법 규칙에 맞지 않아 Compile 단계에서 "
                    "발견되는 오류이다."
                ),
            },
            {
                "name": "Runtime Error",
                "description": (
                    "프로그램 실행 중 발생하는 오류이다."
                ),
            },
            {
                "name": "Logical Error",
                "description": (
                    "프로그램은 실행되지만 결과가 "
                    "의도와 다르게 나타나는 오류이다."
                ),
            },
        ],

        "process": [
            "프로그램 실행",
            "문제 상황 재현",
            "오류 발생 위치 추정",
            "Breakpoint 설정",
            "실행 흐름 확인",
            "변수 및 메모리 상태 확인",
            "오류 원인 분석",
            "Source Code 수정",
            "재실행",
            "정상 동작 확인",
        ],

        "important_point": (
            "디버깅은 단순히 오류가 발생한 줄을 수정하는 것이 아니라 "
            "프로그램의 실행 흐름과 변수 상태를 분석하여 "
            "실제 원인을 찾는 과정이다."
        ),

        "exam_points": [
            (
                "디버깅은 프로그램의 오류 원인을 분석하고 "
                "수정하는 과정이다."
            ),
            (
                "Compile에 성공한 프로그램에서도 Runtime Error나 "
                "Logical Error가 발생할 수 있다."
            ),
            (
                "Breakpoint와 변수 확인은 오류 원인을 찾는 "
                "대표적인 디버깅 방법이다."
            ),
        ],
    },


    # =====================================================
    # 2. GDB 개요
    # =====================================================

    "gdb_overview": {

        "title": "GDB",

        "full_name": "GNU Debugger",

        "definition": (
            "GDB는 GNU 프로젝트에서 제공하는 Debugger로, "
            "프로그램 실행을 제어하면서 Source Code, 변수 값, "
            "함수 호출 상태 등을 확인할 수 있다."
        ),

        "features": [
            (
                "프로그램을 실행하거나 중지할 수 있다."
            ),
            (
                "특정 위치에 Breakpoint를 설정할 수 있다."
            ),
            (
                "한 줄씩 프로그램을 실행할 수 있다."
            ),
            (
                "변수의 현재 값을 확인할 수 있다."
            ),
            (
                "함수 호출 관계와 Stack 상태를 "
                "분석할 수 있다."
            ),
            (
                "Remote Debugging을 이용하면 "
                "Target System의 프로그램도 분석할 수 있다."
            ),
        ],

        "debug_option": {
            "option": "-g",
            "description": (
                "GCC의 -g Option을 사용하면 실행 파일에 "
                "Debugging 정보를 포함할 수 있다."
            ),
            "example": (
                "gcc -g test.c -o test"
            ),
        },

        "basic_procedure": [
            "Source Code 작성",
            "GCC -g Option으로 Compile",
            "GDB 실행",
            "Source 확인",
            "Breakpoint 설정",
            "프로그램 실행",
            "Step 실행",
            "변수 값 확인",
            "오류 원인 분석",
            "GDB 종료",
        ],

        "exam_points": [
            "GDB는 GNU Debugger의 약자이다.",
            (
                "GDB를 이용하면 프로그램 실행을 제어하면서 "
                "변수와 함수 상태를 확인할 수 있다."
            ),
            (
                "GCC의 -g Option은 Debugging 정보를 "
                "실행 파일에 포함한다."
            ),
            (
                "GDB를 사용하기 전 -g Option으로 Compile하는 것이 "
                "중요하다."
            ),
        ],
    },


    # =====================================================
    # 3. GDB 실행 모드
    # =====================================================

    "gdb_modes": {

        "title": "GDB 실행 모드",

        "modes": [
            {
                "name": "Local Debugging",
                "description": (
                    "GDB와 Debugging 대상 프로그램을 "
                    "동일한 시스템에서 실행하는 방식이다."
                ),
                "example": (
                    "Host Linux에서 gcc -g로 Compile한 "
                    "프로그램을 Host의 GDB로 분석"
                ),
            },
            {
                "name": "Remote Debugging",
                "description": (
                    "Debugger는 Host에서 실행하고 "
                    "Debugging 대상 프로그램은 Target에서 실행하는 "
                    "방식이다."
                ),
                "example": (
                    "Target의 gdbserver와 Host의 ARM GDB 연결"
                ),
            },
        ],

        "comparison": [
            {
                "category": "Debugger 실행 위치",
                "local": "Local System",
                "remote": "Host System",
            },
            {
                "category": "대상 프로그램 실행 위치",
                "local": "Local System",
                "remote": "Target System",
            },
            {
                "category": "주요 용도",
                "local": "일반 프로그램 Debugging",
                "remote": "Embedded Target Debugging",
            },
        ],

        "exam_points": [
            (
                "Local Debugging은 Debugger와 대상 프로그램이 "
                "같은 시스템에서 실행된다."
            ),
            (
                "Remote Debugging은 Host와 Target이 "
                "분리되어 동작한다."
            ),
            (
                "임베디드 시스템에서는 Remote Debugging이 "
                "중요하게 사용된다."
            ),
        ],
    },


    # =====================================================
    # 4. GDB 주요 명령어
    # =====================================================

    "gdb_commands": {

        "title": "GDB 주요 명령어",

        "commands": [
            {
                "command": "list",
                "short": "l",
                "description": (
                    "Source Code의 내용을 화면에 출력한다."
                ),
            },
            {
                "command": "break",
                "short": "b",
                "description": (
                    "특정 위치에 Breakpoint를 설정한다."
                ),
                "example": "break main",
            },
            {
                "command": "clear",
                "short": "",
                "description": (
                    "설정한 Breakpoint를 제거한다."
                ),
            },
            {
                "command": "run",
                "short": "r",
                "description": (
                    "프로그램 실행을 시작한다."
                ),
            },
            {
                "command": "print",
                "short": "p",
                "description": (
                    "변수 또는 Expression의 현재 값을 확인한다."
                ),
                "example": "print count",
            },
            {
                "command": "display",
                "short": "disp",
                "description": (
                    "프로그램이 멈출 때마다 특정 변수나 "
                    "Expression 값을 자동으로 표시한다."
                ),
                "example": "display count",
            },
            {
                "command": "continue",
                "short": "c",
                "description": (
                    "중지된 위치부터 프로그램 실행을 계속한다."
                ),
            },
            {
                "command": "next",
                "short": "n",
                "description": (
                    "현재 Source의 다음 줄을 실행한다. "
                    "함수 호출이 있어도 함수 내부로 직접 들어가지 않는다."
                ),
            },
            {
                "command": "step",
                "short": "s",
                "description": (
                    "현재 Source의 다음 줄을 실행한다. "
                    "함수가 호출되면 함수 내부로 진입한다."
                ),
            },
            {
                "command": "up",
                "short": "",
                "description": (
                    "현재 Stack Frame에서 호출한 상위 함수의 "
                    "Frame으로 이동한다."
                ),
            },
            {
                "command": "down",
                "short": "",
                "description": (
                    "상위 Stack Frame에서 다시 하위 Frame으로 "
                    "이동한다."
                ),
            },
            {
                "command": "return",
                "short": "",
                "description": (
                    "현재 함수 실행을 종료하고 "
                    "호출한 함수로 돌아간다."
                ),
            },
            {
                "command": "whatis",
                "short": "",
                "description": (
                    "변수나 Expression의 자료형을 확인한다."
                ),
                "example": "whatis count",
            },
            {
                "command": "set variable",
                "short": "",
                "description": (
                    "Debugging 중 변수 값을 변경한다."
                ),
                "example": "set variable count = 10",
            },
            {
                "command": "quit",
                "short": "q",
                "description": (
                    "GDB를 종료한다."
                ),
            },
        ],

        "command_groups": {
            "source": [
                "list",
            ],
            "breakpoint": [
                "break",
                "clear",
            ],
            "execution": [
                "run",
                "continue",
                "next",
                "step",
                "return",
            ],
            "variable": [
                "print",
                "display",
                "whatis",
                "set variable",
            ],
            "stack": [
                "up",
                "down",
            ],
            "exit": [
                "quit",
            ],
        },

        "exam_points": [
            "`list` → Source Code 확인",
            "`break` → Breakpoint 설정",
            "`clear` → Breakpoint 제거",
            "`run` → 프로그램 실행",
            "`print` → 변수 값 확인",
            "`display` → 변수 값을 계속 표시",
            "`continue` → 실행 계속",
            "`next` → 함수 내부로 들어가지 않고 다음 줄 실행",
            "`step` → 함수 내부로 진입하며 실행",
            "`up` / `down` → Stack Frame 이동",
            "`whatis` → 자료형 확인",
            "`set variable` → 변수 값 변경",
            "`quit` → GDB 종료",
        ],
    },


    # =====================================================
    # 5. Breakpoint
    # =====================================================

    "breakpoint": {

        "title": "Breakpoint",

        "definition": (
            "Breakpoint는 프로그램 실행을 특정 Source 위치에서 "
            "일시적으로 중지시키는 기능이다."
        ),

        "purpose": (
            "오류가 발생할 것으로 예상되는 위치에서 프로그램을 "
            "중지한 뒤 변수 값과 실행 흐름을 확인할 수 있다."
        ),

        "commands": [
            {
                "command": "break main",
                "description": (
                    "main 함수 시작 위치에 Breakpoint를 설정한다."
                ),
            },
            {
                "command": "break 20",
                "description": (
                    "현재 Source File의 20번째 줄에 "
                    "Breakpoint를 설정한다."
                ),
            },
            {
                "command": "clear 20",
                "description": (
                    "20번째 줄의 Breakpoint를 제거한다."
                ),
            },
        ],

        "flow": [
            "GDB 실행",
            "Breakpoint 설정",
            "run 실행",
            "Breakpoint에서 프로그램 중지",
            "변수 및 실행 상태 확인",
            "continue 또는 step/next 실행",
        ],

        "exam_points": [
            (
                "Breakpoint는 프로그램을 특정 위치에서 "
                "일시적으로 중지시킨다."
            ),
            "`break` 명령으로 Breakpoint를 설정한다.",
            "`clear` 명령으로 Breakpoint를 제거할 수 있다.",
            (
                "Breakpoint에서 중지된 상태에서 변수 값과 "
                "프로그램 상태를 분석할 수 있다."
            ),
        ],
    },


    # =====================================================
    # 6. Step Execution
    # =====================================================

    "step_execution": {

        "title": "Step Execution",

        "definition": (
            "Step Execution은 프로그램을 한 단계씩 실행하면서 "
            "각 Source Code가 프로그램 상태에 어떤 영향을 "
            "주는지 확인하는 방법이다."
        ),

        "comparison": [
            {
                "command": "step",
                "description": (
                    "다음 Source Line을 실행하며, "
                    "함수 호출이 있으면 함수 내부로 들어간다."
                ),
                "use_case": (
                    "호출된 함수의 내부 동작까지 확인하고 싶을 때"
                ),
            },
            {
                "command": "next",
                "description": (
                    "다음 Source Line을 실행하지만, "
                    "함수 호출이 있으면 함수 전체를 하나의 "
                    "단계처럼 실행하고 다음 Line으로 이동한다."
                ),
                "use_case": (
                    "함수 내부는 확인하지 않고 현재 함수의 "
                    "흐름만 보고 싶을 때"
                ),
            },
        ],

        "related_commands": [
            {
                "command": "continue",
                "description": (
                    "다음 Breakpoint 또는 프로그램 종료까지 "
                    "실행을 계속한다."
                ),
            },
            {
                "command": "return",
                "description": (
                    "현재 함수의 실행을 끝내고 "
                    "호출한 함수로 돌아간다."
                ),
            },
        ],

        "exam_points": [
            (
                "`step`은 함수가 호출되면 함수 내부로 "
                "진입하여 실행한다."
            ),
            (
                "`next`는 함수 내부로 직접 들어가지 않고 "
                "다음 Source Line으로 진행한다."
            ),
            (
                "`continue`는 다음 Breakpoint 또는 "
                "프로그램 종료까지 실행을 계속한다."
            ),
        ],
    },


    # =====================================================
    # 7. 변수와 프로그램 상태 확인
    # =====================================================

    "variable_memory": {

        "title": "변수와 프로그램 상태 확인",

        "description": (
            "Debugging 과정에서는 변수의 현재 값, 자료형, "
            "변화 과정 등을 확인하여 프로그램의 상태를 분석한다."
        ),

        "commands": [
            {
                "command": "print variable",
                "description": (
                    "변수의 현재 값을 한 번 확인한다."
                ),
                "example": "print count",
            },
            {
                "command": "display variable",
                "description": (
                    "프로그램이 중지될 때마다 변수 값을 "
                    "자동으로 확인한다."
                ),
                "example": "display count",
            },
            {
                "command": "whatis variable",
                "description": (
                    "변수의 자료형을 확인한다."
                ),
                "example": "whatis count",
            },
            {
                "command": "set variable",
                "description": (
                    "Debugging 중 변수의 값을 변경하여 "
                    "동작 변화를 확인할 수 있다."
                ),
                "example": "set variable count = 10",
            },
        ],

        "example": {
            "code": (
                "int count = 0;\n"
                "count = count + 1;"
            ),
            "analysis": [
                "print count로 현재 값을 확인한다.",
                "display count로 실행 단계마다 값을 확인한다.",
                "whatis count로 자료형을 확인한다.",
                (
                    "필요한 경우 set variable count = 10으로 "
                    "값을 임시 변경하여 동작을 분석할 수 있다."
                ),
            ],
        },

        "exam_points": [
            "`print`는 변수 값을 확인한다.",
            "`display`는 변수 값을 자동으로 계속 표시한다.",
            "`whatis`는 변수 또는 Expression의 자료형을 확인한다.",
            (
                "`set variable`을 사용하면 Debugging 과정에서 "
                "변수 값을 변경할 수 있다."
            ),
        ],
    },


    # =====================================================
    # 8. 원격 디버깅
    # =====================================================

    "remote_debugging": {

        "title": "Remote Debugging",

        "definition": (
            "Remote Debugging은 Debugger가 실행되는 Host System과 "
            "Debugging 대상 프로그램이 실행되는 Target System을 "
            "Network 등으로 연결하여 분석하는 방식이다."
        ),

        "why_needed": (
            "임베디드 Target은 화면, Keyboard, 저장 공간, "
            "처리 성능 등이 제한적일 수 있으므로 "
            "Host에서 Debugger를 실행하고 Target에서는 "
            "대상 프로그램만 실행하는 방식이 효율적이다."
        ),

        "host": (
            "ARM용 GDB 또는 DDD 등의 Debugging Tool을 실행한다."
        ),

        "target": (
            "gdbserver를 실행하여 Target Program을 "
            "Host Debugger와 연결한다."
        ),

        "components": [
            {
                "name": "Host GDB",
                "description": (
                    "Target Architecture용 GDB를 이용하여 "
                    "Debugging 명령을 수행한다."
                ),
            },
            {
                "name": "DDD",
                "description": (
                    "GDB를 Graphic Interface 형태로 "
                    "사용할 수 있도록 지원하는 도구이다."
                ),
            },
            {
                "name": "gdbserver",
                "description": (
                    "Target에서 실행되어 Host GDB와 "
                    "Target Program을 연결한다."
                ),
            },
        ],

        "process": [
            "Source Code에 Debugging 정보가 포함되도록 Compile",
            "Target용 실행 파일 생성",
            "Target에 실행 파일 전달",
            "Target에서 gdbserver 실행",
            "Host에서 Target용 GDB 실행",
            "Host GDB와 Target gdbserver 연결",
            "Breakpoint 설정",
            "Target Program 실행",
            "변수 및 실행 흐름 분석",
            "오류 수정 및 재검증",
        ],

        "example_commands": {
            "compile": (
                "arm-unknown-linux-gnueabi-gcc "
                "-g test.c -o test"
            ),
            "target": (
                "gdbserver <host-ip>:<port> ./test"
            ),
            "host": (
                "target remote <target-ip>:<port>"
            ),
        },

        "exam_points": [
            (
                "Remote Debugging에서는 Host에서 Debugger를 "
                "실행하고 Target에서 대상 프로그램을 실행한다."
            ),
            (
                "Target에서는 gdbserver를 이용할 수 있다."
            ),
            (
                "Host에서는 Target Architecture에 맞는 GDB를 "
                "사용해야 한다."
            ),
            (
                "DDD는 GDB를 Graphic Interface 형태로 "
                "사용할 수 있도록 지원하는 도구이다."
            ),
            (
                "Debugging을 위해 -g Option을 이용하여 "
                "Debug 정보를 포함한 실행 파일을 생성한다."
            ),
        ],
    },


    # =====================================================
    # 9. 프로그램 통합
    # =====================================================

    "program_integration": {

        "title": "프로그램 통합",

        "definition": (
            "프로그램 통합은 개별적으로 구현하고 검증한 "
            "단위 Module과 공통 Module을 결합하여 "
            "하나의 완성된 Application으로 만드는 과정이다."
        ),

        "why_needed": (
            "각 Module이 개별적으로 정상 동작하더라도 "
            "Module을 연결했을 때 Interface, Data 전달, "
            "실행 순서 등의 문제로 오류가 발생할 수 있으므로 "
            "통합 과정에서도 충분한 검증이 필요하다."
        ),

        "process": [
            "개별 Module 구현",
            "Module별 Compile",
            "Error / Warning 제거",
            "Module별 단위 기능 확인",
            "Module 간 Interface 확인",
            "Module 통합",
            "통합 프로그램 Compile",
            "통합 프로그램 실행",
            "Debugging",
            "전체 기능 확인",
        ],

        "important_points": [
            "각 Module의 역할이 명확해야 한다.",
            "Module 간 입력과 출력을 확인해야 한다.",
            "공유 변수와 공통 Resource 사용을 확인해야 한다.",
            "통합 후에도 Error와 Warning을 다시 확인해야 한다.",
            "실제 Target에서 전체 기능을 검증해야 한다.",
            "문제가 발생하면 Module별로 분리하여 원인을 분석한다.",
        ],

        "integration_problem_examples": [
            {
                "problem": "각 Module은 정상인데 통합 후 동작하지 않음",
                "possible_cause": (
                    "Module 간 Data 전달 또는 함수 호출 순서에 "
                    "문제가 있을 수 있다."
                ),
            },
            {
                "problem": "Sensor 값은 정상인데 Motor가 이상 동작함",
                "possible_cause": (
                    "조건 처리나 Module 간 Interface에 "
                    "문제가 있을 수 있다."
                ),
            },
            {
                "problem": "통합 후 특정 기능만 멈춤",
                "possible_cause": (
                    "공통 Resource 사용이나 Timing 문제를 "
                    "확인해야 한다."
                ),
            },
        ],

        "exam_points": [
            (
                "Program Integration은 검증된 Module을 결합하여 "
                "하나의 Application으로 만드는 과정이다."
            ),
            (
                "개별 Module이 정상 동작해도 통합 과정에서 "
                "새로운 문제가 발생할 수 있다."
            ),
            (
                "Module 간 Interface, Data 전달, 호출 순서를 "
                "확인해야 한다."
            ),
            (
                "통합 후에도 Compile, Debugging, 전체 기능 검증을 "
                "수행해야 한다."
            ),
        ],
    },


    # =====================================================
    # 10. Arduino 연결
    # =====================================================

    "arduino_mapping": {

        "title": "NCS Debugging과 Arduino 프로젝트 연결",

        "note": (
            "GDB 기반의 Debugging 환경과 Arduino IDE의 "
            "개발 환경은 도구가 완전히 같지는 않지만, "
            "문제를 재현하고 상태를 확인하여 원인을 분석하는 "
            "Debugging 사고 과정은 동일하게 적용할 수 있다."
        ),

        "mapping": [
            {
                "ncs": "Breakpoint",
                "arduino": (
                    "특정 조건에서 상태를 출력하거나 "
                    "동작을 분리하여 확인"
                ),
            },
            {
                "ncs": "print 변수 확인",
                "arduino": "Serial.print()",
            },
            {
                "ncs": "Step Execution",
                "arduino": (
                    "기능을 단계별로 실행하거나 "
                    "Serial 출력으로 흐름 확인"
                ),
            },
            {
                "ncs": "단위 Module Debugging",
                "arduino": (
                    "Sensor, Motor, LCD 기능을 "
                    "각각 별도로 Test"
                ),
            },
            {
                "ncs": "Program Integration",
                "arduino": (
                    "개별 기능을 하나의 Sketch로 통합"
                ),
            },
            {
                "ncs": "통합 Debugging",
                "arduino": (
                    "통합 후 발생하는 문제를 기능별로 "
                    "분리하여 분석"
                ),
            },
        ],

        "project_example": {
            "project": "자동 물주기 스마트 화분",
            "modules": [
                "토양 수분 Sensor",
                "Pump",
                "온습도 Sensor",
                "LCD",
            ],
            "debugging_flow": [
                "Sensor 값만 Serial Monitor로 확인",
                "Pump 단독 동작 확인",
                "LCD 단독 출력 확인",
                "Sensor와 Pump 통합",
                "LCD 추가 통합",
                "전체 기능 실행",
                "문제 발생 시 Module별로 다시 분리하여 확인",
            ],
        },

        "important_distinction": (
            "Arduino에서 Serial Monitor를 이용하는 방식은 "
            "GDB의 Breakpoint와 Step Execution을 그대로 "
            "대체하는 것이 아니라, 학생이 Debugging 원리를 "
            "체험하기 위한 연결 활동이다."
        ),
    },


    # =====================================================
    # 11. 미니 실습
    # =====================================================

    "practice": {

        "title": "GDB와 Debugging 미니 실습",

        "activities": [
            {
                "title": "GDB 명령어 맞추기",
                "instruction": (
                    "Breakpoint 설정, 변수 확인, 실행 계속, "
                    "함수 내부 진입 상황에 맞는 명령어를 선택한다."
                ),
            },
            {
                "title": "step과 next 구분하기",
                "instruction": (
                    "함수 내부를 확인해야 하는 상황과 "
                    "함수를 건너뛰어야 하는 상황을 구분한다."
                ),
            },
            {
                "title": "디버깅 순서 배열하기",
                "instruction": (
                    "GDB 실행부터 Breakpoint, 변수 확인, "
                    "오류 수정까지의 순서를 배열한다."
                ),
            },
            {
                "title": "원격 디버깅 구성하기",
                "instruction": (
                    "Host GDB와 Target gdbserver의 역할을 "
                    "구분한다."
                ),
            },
            {
                "title": "Arduino 통합 문제 분석하기",
                "instruction": (
                    "센서와 Motor가 각각 정상인데 통합 후 "
                    "오류가 발생한 상황에서 어떤 Module부터 "
                    "확인할지 생각한다."
                ),
            },
        ],

        "example_questions": [
            {
                "question": (
                    "GDB에서 Breakpoint를 설정하는 명령어는?"
                ),
                "answer": "break",
            },
            {
                "question": (
                    "변수 값을 확인하는 GDB 명령어는?"
                ),
                "answer": "print",
            },
            {
                "question": (
                    "함수 내부로 진입하며 한 단계 실행하는 명령어는?"
                ),
                "answer": "step",
            },
            {
                "question": (
                    "함수 내부로 들어가지 않고 다음 줄을 "
                    "실행하는 명령어는?"
                ),
                "answer": "next",
            },
            {
                "question": (
                    "Target에서 Remote Debugging을 위해 "
                    "사용할 수 있는 프로그램은?"
                ),
                "answer": "gdbserver",
            },
            {
                "question": (
                    "GCC에서 Debugging 정보를 포함시키는 Option은?"
                ),
                "answer": "-g",
            },
        ],
    },


    # =====================================================
    # 12. 핵심 정리
    # =====================================================

    "summary": [
        (
            "디버깅은 프로그램의 오류 원인을 분석하고 "
            "수정하는 과정이다."
        ),
        (
            "Compile에 성공하더라도 Runtime Error와 "
            "Logical Error가 발생할 수 있다."
        ),
        (
            "GDB는 GNU Debugger로 프로그램 실행 흐름과 "
            "변수 상태를 분석할 수 있다."
        ),
        (
            "GDB 사용을 위해 GCC의 -g Option으로 "
            "Debugging 정보를 포함할 수 있다."
        ),
        (
            "Local Debugging에서는 Debugger와 프로그램이 "
            "같은 시스템에서 실행된다."
        ),
        (
            "Remote Debugging에서는 Host에서 Debugger가 실행되고 "
            "Target에서 대상 프로그램이 실행된다."
        ),
        (
            "`break`는 Breakpoint 설정, `clear`는 "
            "Breakpoint 제거에 사용한다."
        ),
        (
            "`run`은 프로그램 실행, `continue`는 "
            "중지된 프로그램 실행 계속에 사용한다."
        ),
        (
            "`step`은 함수 내부로 진입하며 실행하고 "
            "`next`는 함수 내부로 직접 진입하지 않는다."
        ),
        (
            "`print`는 변수 값을 확인하고 "
            "`display`는 변수 값을 계속 표시한다."
        ),
        (
            "`whatis`는 자료형을 확인하고 "
            "`set variable`은 변수 값을 변경한다."
        ),
        (
            "`up`과 `down`은 Stack Frame 사이를 "
            "이동하는 데 사용할 수 있다."
        ),
        (
            "Remote Debugging에서는 Target의 gdbserver와 "
            "Host의 Target용 GDB를 연결할 수 있다."
        ),
        (
            "DDD는 GDB를 Graphic Interface 형태로 "
            "사용할 수 있도록 지원하는 도구이다."
        ),
        (
            "프로그램 통합은 개별적으로 검증한 Module을 "
            "결합하여 하나의 Application으로 만드는 과정이다."
        ),
        (
            "개별 Module이 정상이어도 통합 과정에서 "
            "Interface와 Data 전달 문제 등이 발생할 수 있다."
        ),
        (
            "Arduino에서도 기능별 단위 Test → 통합 → "
            "Serial Monitor를 이용한 상태 확인 → 문제 수정의 "
            "Debugging 과정을 적용할 수 있다."
        ),
    ],
}