# 시간제한 2초, n <= 5*10^5, n^2 안됨
from collections import defaultdict 
n = int(input())

li = [int(input()) for _ in range(n)]

def mean(li):
    sum = 0
    for i in li:
        sum += i
    return round(sum / len(li))

def mid(li):
    li.sort()
    return li[len(li)//2]


def count(li):
    dic = dict()
    an = []

    for i in li:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in dic:
        if dic[i] == max(dic.values()):
            an.append(i)

    an.sort()

    if len(an) >= 2:
        return an[1]
    else:
        return an[0]


def width(li):
    li.sort()
    return li[-1] - li[0]

print(mean(li))
print(mid(li))
print(count(li))
print(width(li))


