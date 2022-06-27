import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def NBP(lst):

    html = urlopen("https://www.ncloud.com/charge/region/ko")
    bs = BeautifulSoup(html, "html.parser")

    index = 1

    List = []               #크롤링한 정보
    
    for child in bs.find("tbody").children:
        a1 = str(child).replace('Standard-g2','').replace('High CPU-g2','').replace('High Memory-g2','').replace('<tr><th rowspan="5">', '').replace('<td rowspan="5">일반 데이터베이스 서버<br/>개인 홈페이지 운영</td>','').replace('<td rowspan="5">과학적 모델링<br/>게임 서버</td>','').replace('<td rowspan="5">고성능 데이터베이스 서버<br/>대규모 게임 서비스</td>','').replace('<tr><td>','').replace('</td></tr>','').replace(',','').replace('</td><td>', ', ').replace('</th><td>','').replace('원','W')

        a2 = a1.split(',')
        
        if index < 6:
            a2.insert(0, 'Standard-g2')
            a2.insert(0, index)
        elif index < 11:
            a2.insert(0, 'High CPU-g2')
            a2.insert(0, index)
        elif index < 16:
            a2.insert(0, 'High Memory-g2')
            a2.insert(0, index)
        elif index == 16:
            break

        item_obj = {
            'ID' : index,
            'Name' : a2[1],
            'CPU' : a2[2],
            'MEM' : a2[3],
            'Disk' : a2[4],
            'MPrice' : a2[5],
            'YPrice' : a2[6],
        }

        List.append(item_obj)
        index += 1

    Li = {'server' : List}
    a3 = json.dumps(Li, indent = 7)

    return a3
    

