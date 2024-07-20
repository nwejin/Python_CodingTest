#n의 숫자에 따라 별 출력
# 1 - 1, 2 - 5, 3 - 9, 4 - 13
N = int(input())

# 면
# M = (N * 4) - 3
star = '*'
star_left = '* '
star_right = ' *'
blank = ' '

if N == 1:
    print(star)

else:
    # 별을 3개로 나눠서 그리기
    for i in range(N - 1):
        print(i)
        print(star_left * i + star * (1 + 4 * (N - i - 1)) + star_right * i)
        print((1 + 4 * (N - i - 1)))
        print(star_left * (i + 1) + blank * (1 + 4 * (N - i - 2)) + star_right * (i + 1))
        print((1 + 4 * (N - i - 2)))

    # 가운데
    print(star_left * (2 * N - 1))

    # 아래
    for i in range(N - 1):
        print(star_left * (N - i - 1) + blank * (1 + 4 * i) + star_right * (N - i - 1))
        print(star_left * (N - i - 2) + star * (1 + 4 * (i + 1)) + star_right * (N - i - 2))