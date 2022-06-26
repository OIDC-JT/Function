import math

CPU = input("cpu:")
MEM = input("mem:")
CMAX = input("cpu max:")
MMAX = input("mem max:")

index = 1   #분석 서버 수

Server = []     #서버 정보
Reserv = []     #분석 서버 정보

Server.append([CPU, MEM, CMAX, MMAX])

Click = input("분석하려면 분석을 입력")

if Click == '분석':
    for i in range(index):
        ReCPU = int(Server[i-1][0])*int(Server[i-1][2])/100     #변환된 CPU값(CPU*최대 CPU/100)
        ReMEM = int(Server[i-1][1])*int(Server[i-1][3])/100     #변환된 MEM값(MEM*최대 MEM/100)
        Reserv.append([math.ceil(ReCPU), math.ceil(ReMEM)])             #변환된 값(소수점) 올림
        print (Reserv)