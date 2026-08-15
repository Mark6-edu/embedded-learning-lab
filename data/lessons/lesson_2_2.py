from __future__ import annotations


# =========================================================
# 학습 2-2
# 애플리케이션 개발 환경 구축
# =========================================================

LESSON_2_2 = {

    # =====================================================
    # 기본 정보
    # =====================================================

    "metadata": {
        "lesson": "학습 2",
        "section": "2-2",
        "title": "애플리케이션 개발 환경 구축",
        "page_range": "NCS 학습모듈 기준",
        "ncs_module": "임베디드 애플리케이션 구현",
    },


    # =====================================================
    # 학습 목표
    # =====================================================

    "objectives": [
        (
            "임베디드 애플리케이션 개발에 필요한 "
            "Host와 Target 개발 환경의 구성 요소를 "
            "설명할 수 있다."
        ),
        (
            "가상 머신을 이용하여 Linux 기반 "
            "개발 환경을 구성하는 목적을 설명할 수 있다."
        ),
        (
            "NFS를 이용하여 Host와 Target 사이에서 "
            "파일을 공유하는 방법을 설명할 수 있다."
        ),
        (
            "임베디드 개발 환경에서 사용하는 주요 "
            "Linux 명령어의 기능을 설명할 수 있다."
        ),
        (
            "ARM Cross Compiler를 설치하고 "
            "환경변수를 설정하는 과정을 설명할 수 있다."
        ),
        (
            "Cross Compile을 수행하여 Target Architecture용 "
            "실행 파일을 생성할 수 있다."
        ),
        (
            "생성한 실행 파일을 Target으로 전달하여 "
            "실행하고 결과를 확인할 수 있다."
        ),
    ],


    # =====================================================
    # 1. 개발 환경 개요
    # =====================================================

    "environment_overview": {

        "title": "애플리케이션 개발 환경",

        "definition": (
            "임베디드 애플리케이션 개발 환경은 "
            "프로그램을 작성하고 컴파일하는 Host System과 "
            "완성된 프로그램을 실행하는 Target System으로 "
            "구성된다."
        ),

        "host": [
            "Ubuntu 14.04 LTS",
            "VirtualBox",
            "ARM Cross Compiler",
            "minicom",
            "TFTP",
            "NFS",
        ],

        "target": [
            "Linux Kernel 2.6.29",
            "Bootloader",
            "BSP",
            "Root File System",
            "Target Application",
        ],

        "host_description": (
            "Host System에서는 Source Code 작성, "
            "Cross Compile, File Transfer, Debugging 등의 "
            "개발 작업을 수행한다."
        ),

        "target_description": (
            "Target System에서는 Host에서 만들어진 "
            "Target용 실행 파일을 실제로 실행한다."
        ),

        "network": [
            (
                "Host와 Target은 Ethernet 등의 Network를 "
                "통해 연결할 수 있다."
            ),
            (
                "NFS를 이용하면 Host의 Directory를 "
                "Target에서 Mount하여 사용할 수 있다."
            ),
            (
                "Serial 통신은 Target의 Console 확인 등에 "
                "사용할 수 있다."
            ),
        ],

        "development_flow": [
            "Host 개발 환경 구성",
            "Cross Compiler 설치",
            "Network 및 NFS 구성",
            "Source Code 작성",
            "Cross Compile",
            "Target용 실행 파일 생성",
            "Target으로 전달",
            "Target에서 실행",
            "결과 확인",
        ],

        "important_note": (
            "NCS 학습모듈에 제시된 Ubuntu 14.04 LTS와 "
            "Linux Kernel 2.6.29는 학습모듈의 원문 환경이다. "
            "시험 범위에서는 원문의 용어와 절차를 기준으로 "
            "학습한다."
        ),

        "exam_points": [
            (
                "Host는 Ubuntu 14.04 LTS 기반 개발 환경으로 "
                "제시된다."
            ),
            (
                "Target은 Linux Kernel 2.6.29 기반 환경으로 "
                "제시된다."
            ),
            (
                "Host에는 Cross Compiler, NFS, minicom 등의 "
                "개발 도구를 구성할 수 있다."
            ),
            (
                "Target에는 Bootloader, BSP, Root File System "
                "등이 필요하다."
            ),
        ],
    },


    # =====================================================
    # 2. 가상 머신
    # =====================================================

    "virtual_machine": {

        "title": "가상 머신을 이용한 개발 환경 구성",

        "definition": (
            "가상 머신은 하나의 실제 컴퓨터 안에서 "
            "다른 운영체제를 독립적으로 실행할 수 있도록 "
            "가상의 컴퓨터 환경을 제공하는 기술이다."
        ),

        "description": (
            "Host PC에 VirtualBox와 같은 가상화 프로그램을 "
            "설치하고 Ubuntu를 실행하면 기존 운영체제를 "
            "유지하면서 Linux 기반 임베디드 개발 환경을 "
            "구성할 수 있다."
        ),

        "advantages": [
            "기존 Host OS를 유지할 수 있다.",
            "개발 환경을 독립적으로 구성할 수 있다.",
            "환경을 복제하거나 복구하기 쉽다.",
            "실습 환경을 여러 컴퓨터에 동일하게 배포하기 쉽다.",
        ],

        "steps": [
            {
                "step": 1,
                "title": "VirtualBox 설치",
                "description": (
                    "Host PC에 VirtualBox와 같은 "
                    "가상화 프로그램을 설치한다."
                ),
            },
            {
                "step": 2,
                "title": "Ubuntu 가상 머신 생성",
                "description": (
                    "Ubuntu 설치 이미지를 이용해 "
                    "가상 머신을 생성한다."
                ),
            },
            {
                "step": 3,
                "title": "개발 도구 설치",
                "description": (
                    "Ubuntu 환경에 Compiler, Editor, "
                    "Network Tool 등의 개발 도구를 설치한다."
                ),
            },
            {
                "step": 4,
                "title": "Network 환경 구성",
                "description": (
                    "Host와 Target이 통신할 수 있도록 "
                    "Network 환경을 설정한다."
                ),
            },
        ],

        "exam_points": [
            (
                "가상 머신을 사용하면 하나의 Host PC에서 "
                "별도의 Linux 개발 환경을 구성할 수 있다."
            ),
            (
                "NCS 실습에서는 VirtualBox와 Ubuntu 환경이 "
                "사용된다."
            ),
        ],
    },


    # =====================================================
    # 3. NFS
    # =====================================================

    "nfs": {

        "title": "NFS를 이용한 파일 공유",

        "full_name": "Network File System",

        "definition": (
            "NFS는 Network를 통해 다른 시스템의 "
            "Directory와 File을 자신의 File System처럼 "
            "사용할 수 있도록 하는 파일 공유 방식이다."
        ),

        "purpose": (
            "Host에서 Cross Compile한 실행 파일을 "
            "Target에서 쉽게 접근하고 실행하기 위해 사용할 수 있다."
        ),

        "exports_description": (
            "NFS Server에서 공유할 Directory와 접근 가능한 "
            "Client 조건은 /etc/exports 파일에 설정한다."
        ),

        "exports_example": (
            "/work/filesystem/sys-root "
            "*(rw,sync,no_root_squash)"
        ),

        "restart_command": (
            "/etc/init.d/nfs-kernel-server restart"
        ),

        "procedure": [
            {
                "step": 1,
                "title": "NFS Server 설치 및 확인",
                "description": (
                    "Host Linux에서 NFS Server 기능을 "
                    "사용할 수 있도록 준비한다."
                ),
            },
            {
                "step": 2,
                "title": "/etc/exports 설정",
                "description": (
                    "Target에서 접근할 Host Directory를 "
                    "/etc/exports에 등록한다."
                ),
                "command": (
                    "vi /etc/exports"
                ),
            },
            {
                "step": 3,
                "title": "NFS Server 재시작",
                "description": (
                    "변경된 공유 설정을 적용하기 위해 "
                    "NFS Server를 다시 시작한다."
                ),
                "command": (
                    "/etc/init.d/nfs-kernel-server restart"
                ),
            },
            {
                "step": 4,
                "title": "Target에서 Mount",
                "description": (
                    "Target에서 Host의 NFS 공유 Directory를 "
                    "Mount하여 사용한다."
                ),
            },
            {
                "step": 5,
                "title": "공유 파일 확인",
                "description": (
                    "Host에서 생성한 실행 파일을 "
                    "Target에서 확인하고 실행한다."
                ),
            },
        ],

        "exam_points": [
            "NFS는 Network File System의 약자이다.",
            (
                "NFS의 공유 Directory 설정은 "
                "/etc/exports 파일에서 수행한다."
            ),
            (
                "NFS를 이용하면 Host의 File을 Target에서 "
                "Network를 통해 사용할 수 있다."
            ),
            (
                "/etc/exports 변경 후 NFS Server를 "
                "재시작하여 설정을 적용한다."
            ),
        ],
    },


    # =====================================================
    # 4. Linux 파일 관리
    # =====================================================

    "linux_file_management": {

        "title": "Linux 파일 관리와 환경 설정 명령어",

        "intro": (
            "임베디드 Linux 개발 환경을 구축할 때 "
            "Directory 생성, File 복사, 압축 해제, "
            "환경변수 적용과 실행 파일 확인 등의 작업을 "
            "명령어로 수행한다."
        ),

        "commands": [
            {
                "command": "mkdir",
                "description": "새로운 Directory를 생성한다.",
                "example": (
                    "mkdir /usr/local/arm"
                ),
            },
            {
                "command": "cp",
                "description": "File이나 Directory를 복사한다.",
                "example": (
                    "cp toolchain.tar.gz /usr/local/arm"
                ),
            },
            {
                "command": "tar",
                "description": (
                    "압축 File을 묶거나 해제할 때 사용한다."
                ),
                "example": (
                    "tar xvf toolchain.tar"
                ),
            },
            {
                "command": "vi",
                "description": (
                    "Terminal 환경에서 Text File을 "
                    "편집할 수 있는 Editor이다."
                ),
                "example": (
                    "vi /root/.bashrc"
                ),
            },
            {
                "command": "source",
                "description": (
                    "현재 Shell에서 설정 File의 내용을 "
                    "즉시 다시 읽어 적용한다."
                ),
                "example": (
                    "source /root/.bashrc"
                ),
            },
            {
                "command": "env",
                "description": (
                    "현재 Shell의 환경변수를 확인한다."
                ),
                "example": (
                    "env | grep PATH"
                ),
            },
            {
                "command": "ll",
                "description": (
                    "File과 Directory 정보를 자세하게 확인한다."
                ),
                "example": (
                    "ll"
                ),
            },
            {
                "command": "file",
                "description": (
                    "File의 형식과 Architecture 등의 "
                    "정보를 확인한다."
                ),
                "example": (
                    "file tc_test"
                ),
            },
        ],

        "exam_points": [
            "`mkdir` → Directory 생성",
            "`cp` → File 복사",
            "`tar` → 압축 해제 또는 묶기",
            "`vi` → Text File 편집",
            "`source` → 설정 즉시 적용",
            "`env` → 환경변수 확인",
            "`file` → 실행 파일 형식과 Architecture 확인",
        ],
    },


    # =====================================================
    # 5. Cross Compiler 설치
    # =====================================================

    "cross_compiler_installation": {

        "title": "ARM Cross Compiler 설치",

        "definition": (
            "Cross Compiler는 Host System에서 실행되면서 "
            "Target Processor가 실행할 수 있는 Code를 "
            "생성하는 Compiler이다."
        ),

        "install_directory": (
            "/usr/local/arm"
        ),

        "procedure": [
            {
                "step": 1,
                "title": "설치 Directory 생성",
                "description": (
                    "ARM Tool Chain을 설치할 Directory를 만든다."
                ),
                "command": (
                    "mkdir /usr/local/arm"
                ),
            },
            {
                "step": 2,
                "title": "Tool Chain File 복사",
                "description": (
                    "Cross Compiler 압축 File을 "
                    "설치 Directory로 복사한다."
                ),
                "command": (
                    "cp <toolchain-file> /usr/local/arm"
                ),
            },
            {
                "step": 3,
                "title": "Tool Chain 압축 해제",
                "description": (
                    "복사한 Tool Chain File의 압축을 해제한다."
                ),
                "command": (
                    "tar xvf <toolchain-file>"
                ),
            },
            {
                "step": 4,
                "title": "PATH 환경변수 설정",
                "description": (
                    "/root/.bashrc에 Cross Compiler의 "
                    "실행 경로를 PATH로 추가한다."
                ),
                "command": (
                    "vi /root/.bashrc"
                ),
            },
            {
                "step": 5,
                "title": "환경 설정 적용",
                "description": (
                    "수정된 .bashrc의 내용을 현재 Shell에 "
                    "즉시 적용한다."
                ),
                "command": (
                    "source /root/.bashrc"
                ),
            },
            {
                "step": 6,
                "title": "PATH 확인",
                "description": (
                    "Cross Compiler의 경로가 PATH에 "
                    "정상적으로 추가되었는지 확인한다."
                ),
                "command": (
                    "env | grep PATH"
                ),
            },
            {
                "step": 7,
                "title": "Compiler 동작 확인",
                "description": (
                    "ARM Cross Compiler의 Version 정보를 "
                    "출력하여 설치 상태를 확인한다."
                ),
                "command": (
                    "arm-unknown-linux-gnueabi-gcc -v"
                ),
            },
        ],

        "exam_points": [
            (
                "Cross Compiler 설치 예제 Directory는 "
                "/usr/local/arm이다."
            ),
            (
                "/root/.bashrc에서 PATH 환경변수를 "
                "설정할 수 있다."
            ),
            (
                "`source /root/.bashrc`는 수정한 설정을 "
                "현재 Shell에 적용한다."
            ),
            (
                "`env | grep PATH`를 통해 PATH 설정을 "
                "확인할 수 있다."
            ),
            (
                "`arm-unknown-linux-gnueabi-gcc -v`를 "
                "이용해 Cross Compiler 설치 상태를 확인한다."
            ),
        ],
    },


    # =====================================================
    # 6. Cross Compilation
    # =====================================================

    "cross_compilation": {

        "title": "Cross Compilation",

        "definition": (
            "Cross Compilation은 Host와 다른 Architecture를 가진 "
            "Target에서 실행할 프로그램을 Host에서 "
            "컴파일하는 과정이다."
        ),

        "source_file": (
            "tc_test.c"
        ),

        "command": (
            "arm-unknown-linux-gnueabi-gcc "
            "tc_test.c -o tc_test"
        ),

        "description": (
            "ARM Cross Compiler를 이용하여 tc_test.c를 "
            "ARM Target용 실행 파일 tc_test로 생성한다."
        ),

        "file_command": (
            "file tc_test"
        ),

        "file_result": (
            "ELF 32-bit LSB executable, ARM"
        ),

        "architecture_note": (
            "Cross Compile한 실행 파일은 ARM Architecture용이므로 "
            "x86 기반 Host에서 직접 실행할 수 없을 수 있다. "
            "실제 실행은 ARM Target System에서 수행한다."
        ),

        "comparison": [
            {
                "category": "Host Compiler",
                "description": (
                    "Host Architecture용 실행 파일 생성"
                ),
            },
            {
                "category": "Cross Compiler",
                "description": (
                    "Target Architecture용 실행 파일 생성"
                ),
            },
        ],

        "exam_points": [
            (
                "`arm-unknown-linux-gnueabi-gcc`는 "
                "ARM Target용 Cross Compiler이다."
            ),
            (
                "`-o tc_test`는 출력 실행 파일의 "
                "이름을 tc_test로 지정한다."
            ),
            (
                "`file tc_test`를 이용하여 실행 파일의 "
                "Architecture를 확인할 수 있다."
            ),
            (
                "`ELF 32-bit LSB executable, ARM`이라는 결과는 "
                "해당 File이 ARM용 실행 파일임을 의미한다."
            ),
        ],
    },


    # =====================================================
    # 7. Target 실행
    # =====================================================

    "target_execution": {

        "title": "Target System에서 실행",

        "intro": (
            "Host에서 Cross Compile한 Target용 실행 파일을 "
            "NFS 등의 방법으로 Target에서 접근한 뒤 실행한다."
        ),

        "procedure": [
            {
                "step": 1,
                "title": "실행 파일 생성",
                "description": (
                    "Host에서 ARM Cross Compiler로 "
                    "Target용 실행 파일을 생성한다."
                ),
                "command": (
                    "arm-unknown-linux-gnueabi-gcc "
                    "tc_test.c -o tc_test"
                ),
            },
            {
                "step": 2,
                "title": "실행 파일 형식 확인",
                "description": (
                    "`file` 명령을 이용하여 ARM용 "
                    "실행 파일인지 확인한다."
                ),
                "command": (
                    "file tc_test"
                ),
            },
            {
                "step": 3,
                "title": "공유 Directory로 이동",
                "description": (
                    "NFS로 Target과 공유할 Directory에 "
                    "실행 파일을 위치시킨다."
                ),
            },
            {
                "step": 4,
                "title": "Target에서 파일 확인",
                "description": (
                    "Target System에서 공유된 실행 파일을 확인한다."
                ),
            },
            {
                "step": 5,
                "title": "실행",
                "description": (
                    "Target에서 프로그램을 실행한다."
                ),
                "command": (
                    "./tc_test"
                ),
            },
            {
                "step": 6,
                "title": "결과 확인",
                "description": (
                    "프로그램이 요구한 기능대로 "
                    "동작하는지 확인한다."
                ),
            },
        ],

        "exam_points": [
            (
                "Target용 프로그램은 Host에서 Cross Compile한 뒤 "
                "Target System에서 실행한다."
            ),
            (
                "NFS를 이용하면 Host에서 만든 실행 파일을 "
                "Target이 공유하여 사용할 수 있다."
            ),
            (
                "실행 전 `file` 명령으로 Architecture를 "
                "확인하는 것이 중요하다."
            ),
        ],
    },


    # =====================================================
    # 8. 문제 해결
    # =====================================================

    "troubleshooting": {

        "title": "개발 환경 문제 해결",

        "items": [
            {
                "problem": "Cross Compiler 명령을 찾을 수 없음",
                "cause": (
                    "Tool Chain의 bin Directory가 PATH에 "
                    "등록되지 않았거나 설정이 적용되지 않았다."
                ),
                "solution": (
                    "/root/.bashrc의 PATH를 확인한 뒤 "
                    "`source /root/.bashrc`를 실행한다."
                ),
            },
            {
                "problem": "Target에서 실행 파일이 실행되지 않음",
                "cause": (
                    "실행 파일이 Target Architecture와 "
                    "맞지 않을 수 있다."
                ),
                "solution": (
                    "`file` 명령으로 실행 파일의 "
                    "Architecture를 확인한다."
                ),
            },
            {
                "problem": "NFS 공유 Directory가 보이지 않음",
                "cause": (
                    "/etc/exports 설정 또는 NFS Server 상태, "
                    "Network 연결에 문제가 있을 수 있다."
                ),
                "solution": (
                    "/etc/exports 설정을 확인하고 "
                    "NFS Server를 다시 시작한 뒤 "
                    "Host와 Target의 Network 연결을 확인한다."
                ),
            },
            {
                "problem": "환경변수 수정 후 Compiler가 인식되지 않음",
                "cause": (
                    ".bashrc의 변경 내용을 현재 Shell에서 "
                    "다시 읽지 않았다."
                ),
                "solution": (
                    "`source /root/.bashrc`를 실행한다."
                ),
            },
        ],

        "exam_points": [
            (
                "Compiler를 찾지 못할 때는 PATH 환경변수 설정을 "
                "확인해야 한다."
            ),
            (
                "실행 파일이 실행되지 않으면 Host/Target "
                "Architecture 차이를 확인해야 한다."
            ),
            (
                "NFS 문제가 발생하면 /etc/exports, "
                "Server 상태, Network를 확인한다."
            ),
        ],
    },


    # =====================================================
    # 9. Arduino 연결
    # =====================================================

    "arduino_mapping": {

        "title": "NCS 개발 환경과 Arduino 개발 환경 연결",

        "note": (
            "NCS 학습모듈에서는 Linux Host와 ARM Target을 "
            "중심으로 교차 개발 환경을 설명하지만, "
            "Arduino에서도 Host PC에서 작성하고 Compile한 "
            "프로그램을 Board에 Upload하여 실행한다는 "
            "기본 구조를 경험할 수 있다."
        ),

        "mapping": [
            {
                "ncs": "Host System",
                "arduino": "Arduino IDE가 실행되는 PC",
            },
            {
                "ncs": "Target System",
                "arduino": "Arduino UNO / Nano",
            },
            {
                "ncs": "Source Code",
                "arduino": "Arduino Sketch",
            },
            {
                "ncs": "Cross Compiler / Tool Chain",
                "arduino": "Arduino IDE의 Compile Tool Chain",
            },
            {
                "ncs": "Compile",
                "arduino": "Verify",
            },
            {
                "ncs": "Program Transfer",
                "arduino": "Upload",
            },
            {
                "ncs": "Target Console",
                "arduino": "Serial Monitor",
            },
        ],

        "development_flow": [
            "Arduino IDE에서 Sketch 작성",
            "Board 선택",
            "Port 선택",
            "Verify",
            "Upload",
            "Arduino Board에서 실행",
            "Serial Monitor 등으로 결과 확인",
        ],

        "important_distinction": (
            "Arduino 연결은 원문의 Linux/ARM 개발 환경을 "
            "대체하는 내용이 아니라, 학생이 교차 개발 환경의 "
            "개념을 쉽게 이해하도록 연결하는 보조 설명이다."
        ),
    },


    # =====================================================
    # 10. 미니 실습
    # =====================================================

    "practice": {

        "title": "개발 환경 구축 미니 실습",

        "activities": [
            {
                "title": "Linux 명령어 맞추기",
                "instruction": (
                    "Directory 생성, File 복사, 압축 해제, "
                    "환경변수 확인, File 형식 확인에 필요한 "
                    "명령어를 선택한다."
                ),
            },
            {
                "title": "Cross Compile 흐름 배열하기",
                "instruction": (
                    "Host 환경 구성부터 Target 실행까지 "
                    "올바른 순서로 배열한다."
                ),
            },
            {
                "title": "Architecture 확인하기",
                "instruction": (
                    "`file tc_test` 결과를 보고 "
                    "해당 실행 파일이 어떤 Architecture용인지 "
                    "판단한다."
                ),
            },
            {
                "title": "NFS 문제 해결하기",
                "instruction": (
                    "Target에서 공유 Directory가 보이지 않을 때 "
                    "확인해야 할 설정을 찾는다."
                ),
            },
        ],

        "example_questions": [
            {
                "question": (
                    "새 Directory를 만드는 Linux 명령어는?"
                ),
                "answer": "mkdir",
            },
            {
                "question": (
                    "현재 PATH 환경변수를 확인할 때 "
                    "사용할 수 있는 명령은?"
                ),
                "answer": "env | grep PATH",
            },
            {
                "question": (
                    "실행 파일의 Architecture를 확인하는 명령어는?"
                ),
                "answer": "file",
            },
            {
                "question": (
                    "NFS 공유 Directory 설정 파일은?"
                ),
                "answer": "/etc/exports",
            },
        ],
    },


    # =====================================================
    # 11. 핵심 정리
    # =====================================================

    "summary": [
        (
            "임베디드 개발 환경은 프로그램을 개발하는 Host와 "
            "실행하는 Target으로 구성된다."
        ),
        (
            "NCS 실습 환경에서는 Host의 Ubuntu 14.04 LTS와 "
            "Target의 Linux Kernel 2.6.29가 제시된다."
        ),
        (
            "VirtualBox를 이용하면 Host PC에서 별도의 "
            "Linux 개발 환경을 구성할 수 있다."
        ),
        (
            "NFS는 Network File System의 약자이며 "
            "Host의 Directory를 Target에서 공유할 수 있게 한다."
        ),
        (
            "NFS 공유 설정은 /etc/exports에서 수행한다."
        ),
        (
            "`mkdir`은 Directory 생성, `cp`는 File 복사, "
            "`tar`는 압축 관련 작업에 사용한다."
        ),
        (
            "`source /root/.bashrc`는 변경한 Shell 설정을 "
            "현재 환경에 적용한다."
        ),
        (
            "`env | grep PATH`를 이용해 PATH 설정을 "
            "확인할 수 있다."
        ),
        (
            "ARM Cross Compiler 설치 후 "
            "`arm-unknown-linux-gnueabi-gcc -v`로 "
            "동작 여부를 확인할 수 있다."
        ),
        (
            "`arm-unknown-linux-gnueabi-gcc tc_test.c -o tc_test`는 "
            "ARM Target용 실행 파일을 생성하는 예이다."
        ),
        (
            "`file tc_test` 결과가 "
            "`ELF 32-bit LSB executable, ARM`이라면 "
            "ARM용 실행 파일임을 의미한다."
        ),
        (
            "Cross Compile한 프로그램은 Target Architecture에 "
            "맞는 시스템에서 실행해야 한다."
        ),
        (
            "Host에서 만든 실행 파일은 NFS 등을 통해 "
            "Target으로 전달하여 실행할 수 있다."
        ),
        (
            "Arduino 개발 과정의 Verify와 Upload는 "
            "교차 개발 환경의 Compile과 Program Transfer 개념을 "
            "이해하는 데 도움을 준다."
        ),
    ],
}