# 1644

# 접근 방식: 투포인터 -> O(N), 아리스토테네스의 체 -> O(N^1/2)
# 자연수의 최대 크기가 4*10^6 -> n*3/2 -> 8*10^9 (X)
# 제한시간 2초 

n = int(input())

# n보다 작은 소수들 찾기
li = [i for i in range(n+1)] # 소수 담을 리스트 제작

# 아리스토테네스의 체 이용해 리스트에서 소수만 찾아주기

mid = int(n ** (1/2))

for i in range(2,mid+1):
    if li[i] == 0:
        continue
    for j in range(i*i, n+1, i):
        li[j] = 0
# n 루트 3/2
start = 0
end = 0
count = 0
sum = 0

primeNums = set()


for i in li:
    if i != 0 and i != 1:
        primeNums.add(i)
# n

primeNumsLen = len(primeNums)

primeNums = list(primeNums)
# n
primeNums.sort()

for start in range(primeNumsLen): # 시작 포인터 고정
    while sum < n and end < primeNumsLen: # 끝 포인터 이동
        sum += primeNums[end]
        end += 1
    if sum == n:
        count += 1
    sum -= primeNums[start]

# n

print(count)





