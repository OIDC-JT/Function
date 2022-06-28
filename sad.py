list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst =  [list[i * 2:(i + 1) * 2] for i in range((len(list) - 1 + 2) // 2 )] 

print(lst)