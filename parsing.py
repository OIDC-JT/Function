import pprint

result = []

textfile = open("C:/Users/82102/Desktop/OIDC/parsing_test.txt", 'r')
#textfile = open("/root/test.txt", 'r')              #배포용
index = textfile.readlines()
textfile.close()

for i in range(len(index)):
    if "----------- SCAN SUMMARY -----------" in index[i+2]:
        break
    result.append(index[i+1].replace(' FOUND\n',''))

pprint.pprint(result)

virus_num = len(result)
print("Virus 감염수 : %s"%virus_num)