a, b = map(int, input().split())

strings = []

for i in range(a):
    strings.append(int(input()))


def count(li,len):
    n = 0
    for i in li:
        n += i//len
    return n

def binary_search():
    start = 1
    end = max(strings)

    while start <= end:
        mid = (start + end) // 2    
        if count(strings,mid) < b:
            end = mid-1
        elif count(strings,mid) >= b:
            start = mid +1
    return end

print(binary_search())