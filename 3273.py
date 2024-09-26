n = int(input())
li = list(map(int, input().split()))
target = int(input())

li.sort()

#투포인터 이용해서 찾기

start = 0
end = len(li)-1
count = 0

while start < end:
    if li[start] + li[end] == target:
        count += 1
        end -= 1
    else:
        if li[start] + li[end] < target:
            start += 1
        else:
            end -= 1
print(count)


