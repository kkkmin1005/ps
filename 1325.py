from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)

def bfs(start_node):
    visited = [0] * (n+1)
    count = 1
    visited[start_node] = 1
    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        for k in graph[node]:
            if not visited[k]:
                queue.append(k)
                visited[k] = 1
                count += 1

    return count

an = []
maxresult = 0

for i in range(1,n+1):
    result = bfs(i)
    if result > maxresult:
        maxresult = result
        an.clear()
        an.append(i)
    elif result == maxresult:
        an.append(i)

print(*an)

