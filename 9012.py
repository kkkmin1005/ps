n = int(input())

for _ in range(n):
    data = [i for i in str(input())]
    
    stack = []

    no = False

    for elem in data:
        if elem == "(":
            stack.append(elem)
        if elem == ")":
            if len(stack) == 0:
                no = True
                break
            else:
                stack.pop(-1)

    if no:
        print("NO")
    elif len(stack) >= 1:
        print("NO")
    else:
        print("YES")
       