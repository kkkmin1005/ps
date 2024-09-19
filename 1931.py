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
# 머지소트 사용

def merge_sort0(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        L = arr[:mid].copy()
        R = arr[mid:].copy() 

        merge_sort0(L)    
        merge_sort0(R)      

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# 2차원 리스트의 두번째 원소가 작는 녀석 순으로 정렬
# 머지소트 사용

def merge_sort1(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        L = arr[:mid].copy()
        R = arr[mid:].copy() 

        merge_sort1(L)    
        merge_sort1(R)      

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1] or (L[i][1] == R[j][1] and L[i][0] <= R[j][0]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

merge_sort0(li)
merge_sort1(li)

sum = 1
an.append(li[0])

for i in range(1,len(li)):
    if li[i][0] >= an[-1][1]:
        an.append(li[i])
        sum += 1
    else:
        continue

print(sum)

    
    