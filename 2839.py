weight = int(input())
li = []

for i in range((weight//5)+1):
    for k in range((weight//3)+1):
        if (5*i) + (3*k) == weight:
            li.append(i+k)

if len(li) != 0:
    print(min(li))
else:
    print(-1)