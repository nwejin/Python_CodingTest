# 입력 받은 숫자를 list로 저장
num_list = list(map(int, input().split()))

#입력 받은 수를 더할 변수
answer = 0

# 검증수
result = 0

# 각각 num_list 제곱하여 더하기
for i in num_list:
    answer += i**2

result = answer%10

print(result)