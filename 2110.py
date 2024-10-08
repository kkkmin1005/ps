home,wifi = map(int,input().split())
home_li = []

for i in range(home):
    home_li.append(int(input()))

home_li.sort()

start = 1
end = home_li[-1] - home_li[0]
answer = 0

while start <= end:
    count = 1
    mid = (start + end)//2
    select = home_li[0]

    for i in range(1,home):
        if home_li[i] >= select + mid:
            count += 1
            select = home_li[i]
        
    if count >= wifi:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
    
print(answer)
        