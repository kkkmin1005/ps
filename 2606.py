import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
m = int(input())
count = -1

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

def dfs(graph, start_node):

    visited[start_node] = True

    for i in graph[start_node]:
        if not visited[i]:
            dfs(graph,i)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph,1)

for i in range(1,n+1):
    if visited[i]:
        count += 1

print(count)