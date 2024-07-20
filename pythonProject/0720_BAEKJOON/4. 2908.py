import sys

input = sys.stdin.readline

# 두 수 받기
num_A, num_B = map(str, input().split())

# 두 수를 뒤집고, 최대값 출력
print(max(int(num_A[::-1]),int(num_B[::-1])))