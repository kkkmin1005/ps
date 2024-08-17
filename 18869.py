a,b = map(int, input().split())
space = []
space_sort = []
answer = []
fanswer = []

for i in range(a):
    space.append(list(map(int, input().split())))

for i in range(len(space)):
    space_sort.append(sorted(space[i]))

def binary_search(list,find):
    start = 0
    end = len(list)-1

    while start <= end:
        mid = (start + end)//2 

        if list[mid] < find: 
            start = mid + 1
        elif list[mid] > find:
            end = mid - 1
        else:
            return mid

n = 0
for k in space:
    n += 1
    for i in k:
        answer.append(binary_search(space_sort[n-1],i))
    fanswer.append(list(answer))
    answer = []

c = 0

for i in range(len(fanswer)):
    for k in range(i+1, len(fanswer)):
        if fanswer[i] == fanswer[k]:
            c += 1

print(c)

