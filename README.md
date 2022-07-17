# Function

Crawling - 실제 사용할 땐 crawling_return.py 사용

Agent 자동화 설치 - 실제 사용할 땐 agent_install_bat.py 사용
 
 

Batch 파일을 활용한 Zabbix Monitoring Agent 설치 자동화

- agent 자동화 설치 방법

vm/cloud server에서 

'yum install python3' 하고

'python3 -m pip install boto3' 한 뒤에

https://github.com/OIDC-JT/Function/blob/master/agent_install_test.py 이 파일을 서버에 깔고

'python3 agent_install_test.py' 해서 py 파일 실행 시키고


---위 code는 우리 django 서버에서 실행/아래코드는 고객 서버에서 실행---

#1. 서버에서 curl -O(centos), wget(ubuntu) 's3 url' 을 입력하여 bat 파일 다운로드

#2. chmod 755 'bat file명' -->bat file 권한을 access 할 수 있게 변경

#3. ./'file명'으로 실행(agent 설치&설정)

하면 vm/cloud server에 agent 설치 및 설정이 완료되서 passta로 바로 모니터링 가능

-----------------------------------------------------------------------------------

방식 설명(백엔드)

1. crawwling_return.py(Server Migration Helper) - 사용자가 요구한 서버 환경에 가장 적합한 서버를 각 CSP 사이트에서 서버 정보를 크롤링함

2. agent_install_bat.py(IaaS Hybrid monitoring Service) - 사용자가 서버 추가 시 입력받은 (ID, OS, Server ID)를 해당 함수에 대입하여 적합한 batch 자동화 파일을 S3에 업로드함

3. security_bat.py(IaaS Security Management Service) - 사용자가 서버 추가시 입력받은 (OS와 Server ID)를 해당 함수에 대입하여 적합한 batch 자동화 파일을 S3에 업로드함
