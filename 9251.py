#lcs

#제한시간  2초 - 2 * 10^8, 문자 길이 10^3

# step1 - 문자열 입력 받기, 예외처리를 위해 앞에 0 붙이기

s1 = '0'+str(input())
s2 = '0'+str(input())

# step2 - 수 저장할 2차원 배열 제작 - 10^6

li = [[0 for _ in range(len(s2))] for _ in range(len(s1))] 

# step3 - s1을 행, s2를 열로 잡고 비교하며 2차원 배열에 값 저장 - 10^6

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == '0' or s2[j] == '0':
            continue
        else:
            if s1[i] == s2[j]:
                li[i][j] = li[i-1][j-1] + 1
            else:
                li[i][j] = max(li[i-1][j], li[i][j-1])


# step4 - 최댓값 찾기 (최댓값은 무조건 마지막 행에 있으므로 마지막 행에 해당하는 배열만 조사) - 10^3

print(max(li[-1])) 

