import pprint
import os

def Parsing(ID, ServerID):

    Txtfile_name = ID + '_' + ServerID

    if os.path.exists('C:/Users/82102/Desktop/OIDC/parsing_test.txt'):             
    #if os.path.exists("/root/%s.txt"%(Txtfile_name)):                    #배포용
        result = []
        
        textfile = open("C:/Users/82102/Desktop/OIDC/parsing_test.txt", 'r')
        #textfile = open("/root/%s.txt"%(Txtfile_name), 'r')              #배포용
        index = textfile.readlines()
        textfile.close()

        for i in range(len(index)):
            if "----------- SCAN SUMMARY -----------" in index[i+2]:
                break
            result.append(index[i+1].replace(' FOUND\n',''))

        pprint.pprint(result)

        virus_num = len(result)
        print("Virus 감염수 : %s"%virus_num)
    else :
        virus_num = "파일이 없습니다."
        print(virus_num)


Parsing('ID', 'ServerID')