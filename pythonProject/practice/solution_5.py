def solution(s):
    answer = ''

    for i in s:
        if s.count(i) == 1:
            answer += answer.join(i)

    answer = ''.join(sorted(answer))

    return answer

print(solution("hello"))