def solution(bin1, bin2):
    answer = ''
    print(bin1 + bin2)
    num1 = int(bin1, 2)
    print(num1)
    num2 = int(bin2, 2)
    print(num2)

    result = bin(num1+num2)

    answer = result[2:]

    return answer


print(solution("10","11"))