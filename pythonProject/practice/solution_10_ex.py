def solution(spell, dic):

    for i in dic:
        if sorted(i) == sorted(spell):
            return 1

    return 2


print(solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"]))