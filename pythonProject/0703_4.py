# arrayA의 모든 수를 나눌수 있고, arrayB의 수는 나눌 수 없는 정수
# 각 array의 최대공약수 찾기


from math import gcd

def solution(arrayA, arrayB):
    answer = 0

    # numA = math.gcd(*arrayA) #A의 최대공약수
    # numB = math.gcd(*arrayB) #B의 최대공약수
    # numC = math.gcd()
    # print(numA)
    # print(numB)
    # max_num = max(numA, numB)

    for i in range(len(arrayA)):
        numA = gcd(answer, arrayA[i])
    print(numA)


    # for i in range(0, len(arrayA)):
    #    if arrayA[i] % max_num == 0:
    #         answer = max_num
    #
    # # A의 최대공약수로 B에서 나눌 수 있는지 확인
    # for i in range(0, len(arrayB)):
    #     if arrayB[i] % max_num == 0:
    #         answer = max_num
    #
    #
    # print(answer)
    return answer

solution([14, 35, 119],[18, 30, 102])


