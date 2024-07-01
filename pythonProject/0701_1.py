
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = ''

    while n:
        # n을 k진법으로 변환
        word = str(n%k)+num
        n = n//k

    # num을 0으로 분리
    num = num.split('0')

    for i in num:
        if len(i) == 0:
            continue
        if num == '0':
            continue
        elif is_prime(int(i)):
            answer += 1



