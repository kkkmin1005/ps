# 2295

# 접근방식 리스트의 최대 크기가 10^3 이므로 O(N^2) 이어도 문제 x 
# 따라서 x+y+z=k -> x+y = k-z 로 변형
# 투포인터 두번 사용

n = int(input())

li = []

for _ in range(n):
    li.append(int(input()))

li.sort()

sum_set = set()

for i in range(n-1, -1, -1): #오른쪽 포인터
    for j in range(i+1): # 왼쪽 포인터
        sum_set.add(li[i] + li[j])

def a():
    for i in range(n-1, -1, -1): #오른쪽 포인터
        for j in range(i+1): # 왼쪽 포인터
            if li[i] - li[j] in sum_set:
                return li[i]
            
print(a())