answer_li = []

a = int(input())
li1 = list(map(int, input().split()))
b = int(input())
li2 = list(map(int, input().split()))

li1.sort()

def binarySearch(li, target):
    start = 0
    end = len(li) - 1

    while start <= end:
        mid = (start + end) // 2
        if li[mid] == target:
            return True
        elif li[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False

for i in li2:
    if binarySearch(li1, i):
        answer_li.append(1)
    else:
        answer_li.append(0)

print(*answer_li)
