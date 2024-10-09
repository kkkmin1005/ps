n = int(input())
i = n
import sys

def prime(num):
    if num < 2:
        return False
    
    for k in range(2,int(num**0.5)+1):
        if num % k == 0:
            return False
    return True

def parindrom(num):

    count2 = 0

    for t in range(0,len(str(num))//2): #팰린드롬 수 판별
        if str(num)[t] != str(num)[-1-t]:
            return False

    return True
            

while True:
    if prime(i) and parindrom(i):
        print(i)
        break
    else:
        i+=1
