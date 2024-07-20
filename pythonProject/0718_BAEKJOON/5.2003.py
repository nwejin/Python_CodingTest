import sys

N, M = map(int, sys.stdin.readline().split())

arr = sys.stdin.readline().split()

# N개로 된 수열, i부터 j번째 수까지 합이 M이 되는 경우의 수
# N은 수열 길이

for i in range(N):
    print(i)

print(N, M)
print(arr)