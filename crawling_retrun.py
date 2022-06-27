import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

def NBP(lst):       #리스트로 변환 Cpu(변수=a), 변환 Mem(변수=b) 값을 받음

    html = urlopen("https://www.ncloud.com/charge/region/ko")
    bsObj = BeautifulSoup(html, "html.parser")

    index = 1

    List = []               #크롤링한 정보

    for child in bsObj.find("tbody").children:
        a1 = str(child).replace('Standard-g2','').replace('High CPU-g2','').replace('High Memory-g2','').replace('<tr><th rowspan="5">', '').replace('<td rowspan="5">일반 데이터베이스 서버<br/>개인 홈페이지 운영</td>','').replace('<td rowspan="5">과학적 모델링<br/>게임 서버</td>','').replace('<td rowspan="5">고성능 데이터베이스 서버<br/>대규모 게임 서비스</td>','').replace('<tr><td>','').replace('</td></tr>','').replace(',','').replace('</td><td>', ', ').replace('</th><td>','').replace('원','W')

        a2 = a1.split(',')
        
        if index < 6:
            a2.insert(0, 'Standard-g2')
        elif index < 11:
            a2.insert(0, 'High CPU-g2')
        elif index < 16:
            a2.insert(0, 'High Memory-g2')
        elif index == 16:
            break

        index += 1

        List.append(a2)
        
    for i in range(len(lst)):
        #여기서 입력받은 lst = [[a,b], [a2,b2], [a3],[b3]) 같은 형식

        #CPU, MEM 크기 비교
        List2 = []          #크기 비교 후 산출된 Server 목록 초기값
        #a = lst[i][0]      #입력받은 리스트 변수 지정
        #b = lst[i][1]      #입력받은 리스트 변수 지정

        a=3                #test를 위해 임의로 지정한 함수 입력 값(cpu)
        b=9                #test를 위해 임의로 지정한 함수 입력 값(mem)
        for i in range(len(List)):
            if a < int(List[i][1]) and b < int(List[i][2]):
                List2.append(List[i])


        c=100000000000000             #초기값
        f=0                           #금액 인덱싱 초기값
        best_server=[]                #적합한 server 정보 초기값

        #가장 저렴한 price를 가진 server 찾기
        for i in range(len(List2)):
            if "/" in List2[i][5]:
                slash = List2[i][5].find("/")
                f = List2[i][5][0:slash]

            if int(re.sub('W','',str(f))) < c:          #금액에서 Won 뺀 int 값
                c = int(re.sub('W','',str(f)))          #c = temp
                best_server = List2[i]                  #가장 적합한 server 정보

    return best_server                              #적합한 서버 정보 반환