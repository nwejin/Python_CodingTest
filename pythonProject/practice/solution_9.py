def solution(my_string):
    answer = 0

    my_string = my_string.split(' ')
    answer = int(my_string[0])

    for i in range(0, len(my_string)):
        if my_string[i] == '+':
            print(i)
            answer += int(my_string[i+1])
        elif my_string[i] == '-':
            answer -= int(my_string[i + 1])

    return answer

print(solution("3 + 4"))