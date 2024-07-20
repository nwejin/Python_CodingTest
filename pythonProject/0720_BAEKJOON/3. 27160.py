import sys

input = sys.stdin.readline

N = int(input())

# 과일들의 수를 담을 딕셔너리
cards = {
    'STRAWBERRY': 0,
    'BANANA': 0,
    'LIME': 0,
    'PLUM':0,
}

# 결과 출력값
answer = 'NO'

for i in range(N):
    # 과일과 숫자 입력 받기
    S, X = map(str, input().split())
    # 각 카드별로 갯수를 추가
    cards[S] += int(X)

# print(cards)

# 숫자가 5이면 answer값 변경
for i in cards:
    if cards[i] == 5:
        answer = 'YES'

print(answer)