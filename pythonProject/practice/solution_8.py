def solution(my_str, n):
    answer = []

    print(my_str[:n])
    print(my_str[n:n*2])
    print(my_str[n*2:n*3])

    for i in range(0, len(my_str), n):
        print(i)
        answer.append(my_str[i:n+i])



    return answer


print(solution("abc1Addfggg4556b", 6))