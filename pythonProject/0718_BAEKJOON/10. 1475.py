N = list(input())

answer = 0
arr2=[0]*10

num = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(N)):
    if N[i] in num:
        print(N[i])
        break
