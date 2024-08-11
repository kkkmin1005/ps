import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

node_num , n = map(int, input().split())
graph = [[] for _ in range(node_num+1)]
count = 0
visited = [False] * (node_num+1)

def dfs(graph, start_node):
    
    visited[start_node] = True

    for i in graph[start_node]:
        if not visited[i]:
            dfs(graph,i)


for _ in range(n):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for k in range(1,node_num+1):
    if not visited[k]:
        dfs(graph,k)
        count+=1


print(count)