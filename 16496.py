import sys
input = sys.stdin.readline

N = int(input())
data = [*input().split()]

maxL = 0
for d in data:
  maxL = max(maxL,len(d))

maxL *= 2
nums = []

for d in data:
  newd = d*(maxL//len(d))
  for i in range(maxL%len(d)):
    newd += d[i]
  nums.append((newd,len(d)))

nums.sort(reverse = True)

result = ""
for n,l in nums:
  for i in range(l):
    result += n[i]

if result[0]=="0":
  print(0)
else:
  print(result)