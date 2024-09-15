# 시간제한 1초, n <= 10^5, m<= 10^5, n log n이 마지노선

n, m = map(int, input().split())

li = list(map(int, input().split()))

sum_li = [0 for _ in range(n+1)]

for i in range(1,len(li)+1):
    sum_li[i] = li[i-1] + sum_li[i-1]


for i in range(m):
    s,e = map(int, input().split())
    print(sum_li[e] - sum_li[s-1])
