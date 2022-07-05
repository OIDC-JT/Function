import boto3

service_name = 's3'
endpoint_url = 'https://kr.object.ncloudstorage.com'
region_name = 'kr-standard'
access_key = 'm5bIyITDeH0kEW8K3sZ4'
secret_key = 'LS6N46NhCZmxOqbbsIDi42gQdbc1Lzk24qIyk12x'

#ID = input("ID는?")
ID = 'passta'       #요청을 받을 때마다 사용자 ID값으로 설정(현재는 예시로 passta로 설정)(back에서 수정해줘야됨)    

data1 = '#!/bin/bash \nrpm -Uvh http://repo.zabbix.com/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm \nyum -y install zabbix-agent zabbix-sender \nsed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"######Zabbix Server IP#######\" \necho \"#############################\" \necho \"Server=175.45.194.199\" >> /etc/zabbix/zabbix_agentd.conf \necho \"ServerActive=175.45.194.199:10051\" >> /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"####### HOSTMetadata #######\" \necho \"#############################\" \necho \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsystemctl start zabbix-agent \nsystemctl enable zabbix-agent \nsystemctl status zabbix-agent'%(ID,ID)

f = open('%s.bat'%ID, 'w')
f.write(data1)
f.close()

if __name__ == "__main__":                                      #NBP S3 Upload Code
    s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key)

    bucket_name = 'oidc'
    object_name = '%s.bat'%ID                                       #파일 이름(파일명 : ID)
    #local_file_path = 'C:/Users/82102/Desktop/OIDC/%s.bat'%ID      #local 위치 
    local_file_path = '/root/%s.bat'%ID                             #서버상 위치

    s3.upload_file(local_file_path, bucket_name, object_name, ExtraArgs={'ACL':'public-read'})


#서버에서 agent 설치하는 법(metadata는 id로 설정되있음)
#1. 서버에서 curl -O(centos), wget(ubuntu) 's3 url' 을 입력하여 bat 파일 다운로드
#2. chmod 755 'bat file명' -->bat file 권한을 access 할 수 있게 변경
#3. ./'file명'으로 실행(agent 설치&설정)