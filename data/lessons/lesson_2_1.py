from __future__ import annotations


# =========================================================
# 학습 2-1
# 개발 도구 선정
# =========================================================

LESSON_2_1 = {

    # =====================================================
    # 기본 정보
    # =====================================================

    "metadata": {
        "lesson": "학습 2",
        "section": "2-1",
        "title": "개발 도구 선정",
        "page_range": "NCS 학습모듈 기준",
        "ncs_module": "임베디드 애플리케이션 구현",
    },


    # =====================================================
    # 학습 목표
    # =====================================================

    "objectives": [
        (
            "임베디드 애플리케이션 개발에 필요한 "
            "개발 환경과 개발 도구의 종류를 설명할 수 있다."
        ),
        (
            "Host System과 Target System으로 구성되는 "
            "교차 개발 환경의 특징을 설명할 수 있다."
        ),
        (
            "Cross Compiler, Assembler, Linker, Debugger 등 "
            "Tool Chain의 역할을 구분할 수 있다."
        ),
        (
            "Target Board와 Reference Board의 개념을 "
            "설명할 수 있다."
        ),
        (
            "RISC와 CISC 프로세서 구조의 특징을 "
            "비교할 수 있다."
        ),
        (
            "Interrupt, GPIO, I2C, SPI, UART 등 "
            "주요 하드웨어 인터페이스의 특징을 "
            "설명할 수 있다."
        ),
    ],


    # =====================================================
    # 1. 교차 개발 환경
    # =====================================================

    "cross_development": {

        "title": "교차 개발 환경",

        "definition": (
            "임베디드 시스템은 일반적으로 프로그램을 개발하는 "
            "Host System과 실제 프로그램이 실행되는 "
            "Target System이 서로 다르다. "
            "따라서 Host에서 Target용 프로그램을 개발하고 "
            "Target에서 실행·검증하는 교차 개발 환경을 사용한다."
        ),

        "why_needed": (
            "Target System은 메모리, 저장장치, 입력 장치 등의 "
            "자원이 제한적이기 때문에 Target 자체에서 모든 "
            "개발 작업을 수행하기 어렵다. "
            "따라서 개발 기능이 충분한 Host System을 이용한다."
        ),

        "host": {
            "title": "Host System",
            "description": (
                "소스 코드 작성, 컴파일, 링크, 디버깅 등 "
                "개발 작업을 수행하는 시스템이다."
            ),
            "roles": [
                "소스 코드 작성",
                "Cross Compile",
                "실행 파일 생성",
                "디버깅",
                "Target System으로 프로그램 전송",
            ],
            "examples": [
                "Windows PC",
                "Linux PC",
                "Ubuntu 개발 환경",
            ],
        },

        "target": {
            "title": "Target System",
            "description": (
                "Host에서 개발한 프로그램을 실제로 실행하는 "
                "임베디드 시스템 또는 Target Board이다."
            ),
            "roles": [
                "Target용 실행 파일 실행",
                "실제 하드웨어 제어",
                "센서 및 장치 동작",
                "실행 결과 확인",
            ],
            "examples": [
                "ARM Target Board",
                "Embedded Linux Board",
                "Arduino UNO / Nano",
            ],
        },

        "interfaces": [
            "Serial",
            "Ethernet",
            "JTAG",
            "USB",
        ],

        "development_flow": [
            "Host에서 소스 코드 작성",
            "Target Architecture에 맞게 Cross Compile",
            "실행 파일 생성",
            "Host에서 Target으로 전송",
            "Target에서 실행",
            "결과 확인 및 디버깅",
        ],

        "exam_points": [
            (
                "Host System은 프로그램을 개발하는 시스템이고 "
                "Target System은 프로그램을 실행하는 시스템이다."
            ),
            (
                "Host와 Target의 CPU Architecture가 다를 수 있으므로 "
                "Cross Compiler가 필요하다."
            ),
            (
                "Host와 Target은 Serial, Ethernet, JTAG, USB 등의 "
                "인터페이스를 이용해 연결할 수 있다."
            ),
        ],
    },


    # =====================================================
    # 2. Tool Chain
    # =====================================================

    "toolchain": {

        "title": "개발 Tool Chain",

        "intro": (
            "임베디드 애플리케이션을 개발하기 위해서는 "
            "소스 코드를 실행 가능한 프로그램으로 변환하고 "
            "오류를 분석하기 위한 여러 개발 도구가 필요하다. "
            "이러한 도구들의 집합을 Tool Chain이라고 한다."
        ),

        "tools": [
            {
                "name": "Cross Compiler",
                "description": (
                    "Host System에서 작성한 소스 코드를 "
                    "Target Processor가 실행할 수 있는 "
                    "기계어 코드로 변환한다."
                ),
            },
            {
                "name": "Assembler",
                "description": (
                    "Assembly Language로 작성된 코드를 "
                    "Object Code로 변환한다."
                ),
            },
            {
                "name": "Linker",
                "description": (
                    "여러 Object File과 Library를 연결하여 "
                    "하나의 실행 파일을 생성한다."
                ),
            },
            {
                "name": "Debugger",
                "description": (
                    "프로그램 실행 과정에서 오류를 찾고 "
                    "변수 값과 프로그램 흐름을 분석한다."
                ),
            },
        ],

        "flow": [
            "Source Code",
            "Cross Compiler",
            "Assembler",
            "Object File",
            "Linker",
            "Executable File",
        ],

        "simple_flow": (
            "Source Code → Compiler → Assembler → "
            "Object File → Linker → Executable File"
        ),

        "exam_points": [
            (
                "Cross Compiler는 Host에서 실행되지만 "
                "Target Processor용 실행 코드를 생성한다."
            ),
            (
                "Assembler는 Assembly Code를 "
                "Object Code로 변환한다."
            ),
            (
                "Linker는 여러 Object File과 Library를 "
                "결합하여 실행 파일을 만든다."
            ),
            (
                "Debugger는 프로그램 실행 상태를 분석하고 "
                "오류의 원인을 찾는 도구이다."
            ),
        ],
    },


    # =====================================================
    # 3. Target Board
    # =====================================================

    "target_board": {

        "title": "Target Board와 Reference Board",

        "target_board": {
            "title": "Target Board",
            "description": (
                "개발한 임베디드 애플리케이션을 실제로 실행하고 "
                "시험하는 하드웨어 시스템이다."
            ),
        },

        "reference_board": {
            "title": "Reference Board",
            "description": (
                "프로세서나 주요 부품 제조사가 제공하는 "
                "참조용 하드웨어 보드로, 새로운 제품을 설계하거나 "
                "기능을 검증할 때 기준으로 활용할 수 있다."
            ),
        },

        "components": [
            "Processor",
            "Memory",
            "Flash Memory",
            "Input / Output Interface",
            "Communication Interface",
            "Power Circuit",
        ],

        "selection_points": [
            "Processor Architecture",
            "Memory 용량",
            "입출력 장치",
            "통신 Interface",
            "확장 가능성",
            "개발 Tool 지원 여부",
        ],

        "exam_points": [
            (
                "Target Board는 개발한 프로그램을 실제로 "
                "실행하고 검증하는 하드웨어이다."
            ),
            (
                "Reference Board는 제품 개발 시 "
                "참조할 수 있도록 제공되는 기준 하드웨어이다."
            ),
            (
                "Target Board 선정 시 Processor, Memory, "
                "I/O 및 Communication Interface 등을 검토한다."
            ),
        ],
    },


    # =====================================================
    # 4. Processor Architecture
    # =====================================================

    "processor_architecture": {

        "title": "Processor Architecture",

        "risc": {
            "name": "RISC",
            "full_name": "Reduced Instruction Set Computer",
            "description": (
                "비교적 단순하고 적은 수의 명령어를 사용하여 "
                "빠르고 효율적으로 명령을 처리하는 구조이다."
            ),
            "features": [
                "명령어 구조가 비교적 단순하다.",
                "명령어 수가 상대적으로 적다.",
                "명령어 실행 시간이 비교적 일정하다.",
                "Pipeline 처리에 유리하다.",
                "임베디드 Processor에서 많이 사용된다.",
            ],
            "examples": [
                "ARM",
            ],
        },

        "cisc": {
            "name": "CISC",
            "full_name": "Complex Instruction Set Computer",
            "description": (
                "다양하고 복잡한 명령어를 제공하여 "
                "하나의 명령어로 여러 동작을 수행할 수 있는 구조이다."
            ),
            "features": [
                "명령어 종류가 많다.",
                "복잡한 명령을 지원한다.",
                "명령어 길이와 실행 시간이 다양할 수 있다.",
                "하드웨어 구조가 상대적으로 복잡할 수 있다.",
            ],
            "examples": [
                "x86",
            ],
        },

        "comparison": [
            {
                "category": "명령어",
                "risc": "단순하고 상대적으로 적음",
                "cisc": "복잡하고 상대적으로 많음",
            },
            {
                "category": "명령어 실행",
                "risc": "비교적 단순하고 일정",
                "cisc": "명령에 따라 다양",
            },
            {
                "category": "구조",
                "risc": "단순화된 구조",
                "cisc": "복잡한 구조",
            },
            {
                "category": "대표 예",
                "risc": "ARM",
                "cisc": "x86",
            },
        ],

        "exam_points": [
            "RISC는 Reduced Instruction Set Computer의 약자이다.",
            "CISC는 Complex Instruction Set Computer의 약자이다.",
            "ARM 계열 Processor는 RISC 구조의 대표적인 예이다.",
            (
                "RISC와 CISC는 단순히 우열 관계가 아니라 "
                "명령어 구조와 설계 방식의 차이로 이해해야 한다."
            ),
        ],
    },


    # =====================================================
    # 5. Hardware Interface
    # =====================================================

    "hardware_interfaces": {

        "title": "주요 Hardware Interface",

        "intro": (
            "임베디드 시스템은 Processor와 외부 장치 사이에서 "
            "데이터를 주고받기 위해 다양한 하드웨어 "
            "Interface를 사용한다."
        ),

        "interfaces": [

            # -------------------------------------------------
            # Interrupt
            # -------------------------------------------------

            {
                "name": "Interrupt",
                "full_name": "Interrupt",
                "description": (
                    "CPU가 현재 작업을 수행하는 중에 특정 사건이 "
                    "발생했음을 알려 현재 작업을 잠시 중단하고 "
                    "해당 사건을 우선 처리하도록 하는 방식이다."
                ),
                "features": [
                    "이벤트 발생에 빠르게 대응할 수 있다.",
                    "Polling 방식의 반복 확인을 줄일 수 있다.",
                    "Interrupt Service Routine과 연결된다.",
                ],
                "arduino_example": (
                    "Arduino의 attachInterrupt()를 이용한 "
                    "외부 인터럽트 처리"
                ),
            },


            # -------------------------------------------------
            # GPIO
            # -------------------------------------------------

            {
                "name": "GPIO",
                "full_name": "General Purpose Input / Output",
                "description": (
                    "Processor가 Digital Signal을 입력받거나 "
                    "출력할 수 있도록 제공하는 범용 입출력 Interface이다."
                ),
                "features": [
                    "Digital Input",
                    "Digital Output",
                    "LED, Button 등의 제어에 사용",
                ],
                "arduino_example": (
                    "pinMode(), digitalRead(), digitalWrite()"
                ),
            },


            # -------------------------------------------------
            # I2C
            # -------------------------------------------------

            {
                "name": "I2C",
                "full_name": "Inter-Integrated Circuit",
                "description": (
                    "SDA와 SCL 두 개의 신호선을 이용하여 "
                    "여러 장치와 통신할 수 있는 직렬 통신 방식이다."
                ),
                "features": [
                    "SDA: Data",
                    "SCL: Clock",
                    "장치 Address 사용",
                    "여러 Slave 장치 연결 가능",
                ],
                "arduino_example": (
                    "Wire Library를 이용한 센서 및 LCD 통신"
                ),
            },


            # -------------------------------------------------
            # SPI
            # -------------------------------------------------

            {
                "name": "SPI",
                "full_name": "Serial Peripheral Interface",
                "description": (
                    "Clock과 여러 데이터 신호선을 이용하여 "
                    "고속으로 데이터를 주고받는 동기식 "
                    "직렬 통신 방식이다."
                ),
                "features": [
                    "SCK",
                    "MOSI",
                    "MISO",
                    "SS / CS",
                    "비교적 빠른 통신 속도",
                ],
                "arduino_example": (
                    "SPI Library 및 SPI 기반 모듈 사용"
                ),
            },


            # -------------------------------------------------
            # UART
            # -------------------------------------------------

            {
                "name": "UART",
                "full_name": (
                    "Universal Asynchronous "
                    "Receiver / Transmitter"
                ),
                "description": (
                    "별도의 Clock Signal 없이 TX와 RX 선을 이용하여 "
                    "데이터를 주고받는 비동기식 직렬 통신 방식이다."
                ),
                "features": [
                    "TX",
                    "RX",
                    "비동기 통신",
                    "Baud Rate 설정 필요",
                ],
                "arduino_example": (
                    "Serial.begin(), Serial.print(), Serial.read()"
                ),
            },
        ],

        "comparison": [
            {
                "interface": "GPIO",
                "main_use": "Digital 입출력",
                "arduino": "digitalRead / digitalWrite",
            },
            {
                "interface": "I2C",
                "main_use": "2선식 장치 통신",
                "arduino": "Wire",
            },
            {
                "interface": "SPI",
                "main_use": "고속 동기식 통신",
                "arduino": "SPI",
            },
            {
                "interface": "UART",
                "main_use": "비동기 직렬 통신",
                "arduino": "Serial",
            },
            {
                "interface": "Interrupt",
                "main_use": "이벤트 즉시 처리",
                "arduino": "attachInterrupt",
            },
        ],

        "exam_points": [
            (
                "GPIO는 General Purpose Input / Output의 약자이다."
            ),
            (
                "I2C는 SDA와 SCL 두 개의 주요 신호선을 사용한다."
            ),
            (
                "SPI의 주요 신호는 SCK, MOSI, MISO, SS/CS이다."
            ),
            (
                "UART는 TX와 RX를 이용하는 비동기 직렬 통신이다."
            ),
            (
                "Interrupt는 특정 사건 발생 시 CPU가 "
                "해당 사건을 우선 처리하도록 하는 방식이다."
            ),
        ],
    },


    # =====================================================
    # 6. Arduino 연결
    # =====================================================

    "arduino_mapping": {

        "title": "NCS 개발 도구와 Arduino 연결",

        "note": (
            "NCS에서 설명하는 Host, Target, Tool Chain과 "
            "Hardware Interface 개념은 Arduino 개발 과정에서도 "
            "비슷한 구조로 경험할 수 있다."
        ),

        "mapping": [
            {
                "ncs": "Host System",
                "arduino": "Arduino IDE가 실행되는 PC",
            },
            {
                "ncs": "Target System",
                "arduino": "Arduino UNO / Nano Board",
            },
            {
                "ncs": "Compiler / Tool Chain",
                "arduino": "Arduino IDE의 Verify 과정",
            },
            {
                "ncs": "Program Transfer",
                "arduino": "Upload",
            },
            {
                "ncs": "UART",
                "arduino": "Serial Monitor",
            },
            {
                "ncs": "GPIO",
                "arduino": "Digital Pin",
            },
            {
                "ncs": "I2C",
                "arduino": "Wire Library",
            },
            {
                "ncs": "SPI",
                "arduino": "SPI Library",
            },
            {
                "ncs": "Interrupt",
                "arduino": "attachInterrupt()",
            },
        ],

        "example": {
            "project": "Arduino 온습도 측정기",
            "host": (
                "PC에서 Arduino IDE를 이용해 "
                "Sketch를 작성하고 Compile한다."
            ),
            "target": (
                "Arduino Board에서 프로그램을 실행하고 "
                "Sensor와 LCD를 제어한다."
            ),
            "interfaces": [
                "GPIO",
                "I2C",
                "UART",
            ],
        },
    },


    # =====================================================
    # 7. 미니 실습
    # =====================================================

    "practice": {

        "title": "개발 도구 선정 미니 실습",

        "activities": [
            {
                "title": "Host와 Target 구분하기",
                "instruction": (
                    "소스 코드 작성, Cross Compile, "
                    "실행 파일 실행 등의 작업이 "
                    "Host와 Target 중 어디에서 수행되는지 구분한다."
                ),
            },
            {
                "title": "Tool Chain 연결하기",
                "instruction": (
                    "Compiler, Assembler, Linker, Debugger의 "
                    "역할을 올바르게 연결한다."
                ),
            },
            {
                "title": "Hardware Interface 선택하기",
                "instruction": (
                    "Arduino 프로젝트 상황을 보고 GPIO, I2C, "
                    "SPI, UART 중 적절한 Interface를 선택한다."
                ),
            },
        ],

        "example_questions": [
            {
                "question": (
                    "여러 Object File을 하나의 실행 파일로 "
                    "연결하는 도구는?"
                ),
                "answer": "Linker",
            },
            {
                "question": (
                    "Arduino Serial Monitor와 가장 밀접한 "
                    "Hardware Interface는?"
                ),
                "answer": "UART",
            },
            {
                "question": (
                    "Arduino UNO와 센서 모듈을 SDA와 SCL로 "
                    "연결했다. 사용한 통신 방식은?"
                ),
                "answer": "I2C",
            },
        ],
    },


    # =====================================================
    # 8. 핵심 정리
    # =====================================================

    "summary": [
        (
            "임베디드 개발에서는 프로그램을 개발하는 "
            "Host System과 실행하는 Target System을 "
            "구분하는 교차 개발 환경을 사용한다."
        ),
        (
            "Cross Compiler는 Host에서 실행되지만 "
            "Target Processor용 프로그램을 생성한다."
        ),
        (
            "Tool Chain에는 Cross Compiler, Assembler, "
            "Linker, Debugger 등이 포함된다."
        ),
        (
            "Target Board는 개발한 프로그램을 실제로 "
            "실행하고 검증하는 하드웨어이다."
        ),
        (
            "Reference Board는 제품이나 시스템 설계 시 "
            "참조하기 위한 기준 하드웨어이다."
        ),
        (
            "RISC는 비교적 단순한 명령어 구조를 사용하고, "
            "CISC는 다양하고 복잡한 명령어를 제공한다."
        ),
        (
            "GPIO는 범용 Digital 입출력을 위한 Interface이다."
        ),
        (
            "I2C는 SDA와 SCL을 이용하고 "
            "여러 장치를 Address로 구분한다."
        ),
        (
            "SPI는 SCK, MOSI, MISO, SS/CS 등을 이용하는 "
            "고속 동기식 직렬 통신 방식이다."
        ),
        (
            "UART는 TX와 RX를 이용하는 "
            "비동기식 직렬 통신 방식이다."
        ),
        (
            "Interrupt는 특정 Event가 발생했을 때 "
            "CPU가 해당 사건을 우선적으로 처리하도록 한다."
        ),
        (
            "Arduino 개발 과정에서도 Host, Target, Tool Chain, "
            "GPIO, I2C, SPI, UART 등의 개념을 확인할 수 있다."
        ),
    ],
}