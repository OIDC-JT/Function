# Function

### 1. Repo에 대한 설명
  - 이 Repo에는 정통 팀에서 제공하는 서비스들에 대해 꼭 필요한 기능들을 개발한 Code들이 있다.
  - Code들은 주로 Python으로 개발되었으며, Python 외에도 C, Shell 언어 등이 사용되었다.
  - 이 Repo에서 개발한 기능들을 Django 기반의 "NBP_back_pub" Repo와 "OIDC_FRONT_BP" Repo와 연동하여 사용한다.

### 2. 서비스 별 기능 설명
  (1) Server Migration Helper Service
  - 사용자가 원하는 서버 환경 또는 사용중인 IaaS 환경에 대해 Cloud로 Migration 시 최적의 Cloud 서버 환경을 분석해줌(analysis.py)
  - 분석 후 얻은 최적의 Cloud 서버 환경에 대해, CSP 별로 가장 적합한 Server의 정보를 Crawling하여 실시간으로 제공함(craw_return_test.py)

  (2) IaaS Hybrid Cloud Monitoring Service
  - 대시보드에서 회원가입, 로그인 시 Zabbix Database에도 자동적으로 정보 연동해줌(receive_host.py)
  - 모니터링한 Data들을 Proxy, Monitering Server로 전송해주는 Agent에 대해 Batch 파일을 활용하여 고객 Server에 가능한 간단한 방식으로 자동 설치해줌(agent_install_bat.py)

  (3) Iaas Security Management Service
  - Batch 파일을 활용하여 보안 검사를 위한 Tool(ClamAV) 설치/설정 자동화, 매일 00시마다 Server의 Virus 검사, Virus 검사 결과를 소켓 프로그래밍을 활용하여 매일 00시 10분마다 Main Server에 전달(security_bat.py)
  - Main server에서 여러 고객들의 보안 검사 결과를 소켓 프로그래밍을 통해 실시간으로 자동적으로 받게 해줌(server.c)

### 3. Monitoring Agent, 보안 검사 Tool(ClamAV), Socket 통신 자동화 설치/설정 방법
#### 관리자 Server에서 실행
    vm/cloud server에서
    yum install python3 (Python 설치)
    python3 -m pip install boto3 (S3 관리 설치)
    python3 function.py (사용자에 맞는 기능 실행/생성 후 S3에 업로드)    
#### 사용자 Server에서 실행
    curl -O(centos), wget(ubuntu) 's3 url' (S3에 업로드된 생성된 기능을 서버에 다운로드)
    chmod 755 file.bat  (bat file 권한을 access 할 수 있게 변경)
    ./file.bat  (Batch 파일을 활용한 원하는 기능 실행 밒 설정)


vm/cloud server에 agent 설치 및 설정이 완료되서 passta로 바로 모니터링 가능

+보안 실시간 점검(매일 00시 00분)이 가능하며 점검 결과를 Django Server로 소켓 전송 함

(백그라운드에서 'nohup,  ./file &' 기능 사용-터미널이 꺼져도 언제든 수신할 수 있게)

-----------------------------------------------------------------------------------

방식 설명(백엔드 개발 참고) 

1. crawwling_return.py(Server Migration Helper) - 사용자가 요구한 서버 환경에 가장 적합한 서버를 각 CSP 사이트에서 서버 정보를 크롤링함

2. agent_install_bat.py(IaaS Hybrid monitoring Service) - 사용자가 서버 추가 시 입력받은 (ID, OS, Server ID)를 해당 함수에 대입하여 적합한 batch 자동화 파일을 S3에 업로드함

3. security_bat.py(IaaS Security Management Service) - 사용자가 서버 추가시 입력받은 (OS와 Server ID)를 해당 함수에 대입하여 적합한 batch 자동화 파일과 Socket Setting Code C파일을 S3에 업로드함
