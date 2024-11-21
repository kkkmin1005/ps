n = int(input())

li1 = []
visited1 = []
count1 = 0

li2 = []
visited2 = []
count2 = 0

for _ in range(n):
    for elem in (str(input())):
        li1.append(elem)

for elem in li1:
    if elem == 'G':
        li2.append('R')
    else:
        li2.append(elem)

# dfs로 탐색 진행
def dfs(li, start, n):
    visited = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop(0)

        if node not in visited:
            visited.append(node)
            for i in [node-1, node+1, node-n, node+n]:
                try:
                    if i == node -1 or i == node+1:
                        if li[node] == li[i] and i > 0 and node // n == i //n:
                            if i not in visited:
                                stack.append(i)
                    else:
                        if li[node] == li[i] and i > 0:
                            if i not in visited:
                                stack.append(i)

                except:
                    continue

    return visited

for k in range(len(li1)):
    if k not in visited1:
        visited1.extend(dfs(li1,k,n))
        count1 += 1

for k in range(len(li2)):
    if k not in visited2:
        visited2.extend(dfs(li2,k,n))
        count2 += 1

print(count1, count2)