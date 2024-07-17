def solution(spell, dic):
    answer = 0
    s_spell = sorted(spell)
    s_dic = sorted(dic)
    # print(s_spell)
    # print(s_dic[2])
    result = []

    for i in range(0, len(s_dic)):
        print(list(sorted(s_dic[i])))
        print(s_spell)
        if list(sorted(s_dic[i])) == s_spell:
            result.append(1)
        else:
            result.append(2)

    if result.count(1):
        answer = 1
    else:
        answer = 2

    return answer


print(solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"]))