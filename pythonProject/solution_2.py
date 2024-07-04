def solution(before, after):
    answer = 0

    a_sort = sorted(after)

    b_sort = sorted(before)

    if a_sort == b_sort:
        answer += 1
    else:
        answer = 0


    return answer


print(solution("olleh", "hello"))