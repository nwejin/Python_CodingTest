# N입력 받기
N = int(input())

# 1부터 N까지 담을 배열 생성
arr = []

# 1~N까지 arr에 넣기
for i in range(1, N+1):
    arr.append(str(i))

# 배열을 문자열로 합치기
answer = "".join(arr)

# 길이 출력
print(len(answer))