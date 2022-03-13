import csv


#2. 데이터 집합 불러오기
table = []
with open("phone_1.csv",'r') as f :
    reader = csv.DictReader(f)
    for row in reader : table.append(row)

#3. 평균과 중앙값 구하기
total = [0,0,0]
keys = list(table[0].keys())
table_sort = [[],[],[]]
for i in range(len(table)) :
    for j in range(len(keys)) :
        table_sort[j].append(float(table[i][keys[j]]))
table = table_sort
for i in range(len(table)) :
    table[i].sort()
print("table :",table)

#평균
mean = []
#중앙값
median = []
for i in range(len(table)) :
    mean.append(sum(table[i])//len(table[i]))
    if len(table[i])%2 == 0 :
        median.append((table[i][len(table[i])//2-1]+table[i][len(table[i])//2])/2)
    else :
        median.append(table[i][len(table[i])//2])
        
print("mean :",mean)
print("median :",median)




