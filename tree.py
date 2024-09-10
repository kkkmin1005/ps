# 전위 순회 탐색

def preorder(n): # 입력 받는 n은 루트 노드
    if n <= N:
        print(tree[n], end = ' ')
        preorder(n*2)
        preorder(n*2 + 1)
    
# 중위 순회 탐색

def midorder(n):
    if n <= N:
        midorder(n*2)
        print(tree[n], end = ' ')
        midorder(n*2 + 1)

# 후위 순회 탐색

def postorder(n):
    if n <= N:
        postorder(n*2)
        postorder(n*2 + 1)
        print(tree[n], end = ' ')


N = 9 # 노드의 수
tree = [0,'a', 'b', 'c', 'd', 'e','f','g','h','i'] # 트리

preorder(1)
print('\n')
midorder(1)
print('\n')
postorder(1)