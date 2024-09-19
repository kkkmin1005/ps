# 제한시간 2초, 10^5 따라서 nlogn 까지 사용가능

n = int(input())
li = [[] for _ in range(n)]
an = []

# 2차원 리스트 제작
for i in range(n):
    a,b = map(int, input().split())
    li[i].append(a)
    li[i].append(b)

# 2차원 리스트의 첫번째 원소가 작는 녀석 순으로 정렬
# 힙정렬 사용

def heapify1(arr, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
 
    if l < n and arr[l][0] > arr[largest][0]:
        largest = l
 
    if r < n and arr[r][0] > arr[largest][0]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
 
        heapify1(arr, n, largest)
 
def heap_sort1(arr):
    n = len(arr)
 
    for i in range(n // 2 - 1, -1, -1):
        heapify1(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify1(arr, i, 0)

# 2차원 리스트의 두번째 원소가 작는 녀석 순으로 정렬
# 힙정렬 사용

def heapify2(arr, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
 
    if l < n and arr[l][1] > arr[largest][1]:
        largest = l
 
    if r < n and arr[r][1] > arr[largest][1]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
 
        heapify1(arr, n, largest)
 
def heap_sort2(arr):
    n = len(arr)
 
    for i in range(n // 2 - 1, -1, -1):
        heapify2(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify2(arr, i, 0)

heap_sort1(li)
heap_sort2(li)

print(li)

sum = 1
an.append(li[0])

for i in range(1,len(li)):
    if li[i][0] >= an[-1][1]:
        an.append(li[i])
        sum += 1
    else:
        continue

print(an)

print(sum)

    
    