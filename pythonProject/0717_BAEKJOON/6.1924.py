m, d = map(int, input().split())

# 각 월마다 일수
month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

total = 0 # 날짜 계산
for i in range(1, m):
    total += month[i] # (m-1)월까지 날짜 더하기
total += d - 1 #오늘 일수 더하기 (0일부터 시작)

# print(total)
# print(total % 7)

day = day[total % 7]

print(day)
