n = int(input())
li = ['n' for _ in range(n+1)]

li[0] = 0
li[1] = 1

for i in range(n+1):
    if li[i] != 'n':
        continue
    else:
        li[i] = li[i-1] + li[i-2]

print(li[n])
    
    
