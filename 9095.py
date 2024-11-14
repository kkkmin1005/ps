n = int(input())

for i in range(n):
    memoization = [0] * 1000
    num = int(input())
    for j in range(1, num+1):
        if j == 1:
            memoization[j] = 1
        elif j == 2:
            memoization[j] = 2
        elif j == 3:
            memoization[j] = 4
        else:
            memoization[j] = memoization[j-1] + memoization[j-2] + memoization[j-3]
    print(memoization[num])       