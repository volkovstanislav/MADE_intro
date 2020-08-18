x = input()
k_list = []
for i in range(int(x)):
    i = input()
    k_list.append(int(i))

k = 0
flag = False
k1 = max(k_list)
answer = []
for i in range(2, 1500):
    for j in range(1, i):
        num = (pow(2, i-1, 35184372089371) + pow(2, j-1, 35184372089371)) % 35184372089371
        answer.append(num)
        k = k + 1
        if k == k1:
            flag = True
            break

    if flag:
        i = 1501

for a in k_list:
    print(answer[a-1])

