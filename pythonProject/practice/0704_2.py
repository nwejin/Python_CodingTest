def solution(picks, minerals):
    answer = 0

    #곡괭이 종류
    dia_pick, iron_pick, stone_pick = picks

    #피로도
    dia_stack = {'dia': 1, 'iron': 1, 'stone': 1}
    iron_stack = {'dia': 5, 'iron': 1, 'stone': 1}
    stone_stack = {'dia': 25, 'iron': 5, 'stone': 1}

    # print(iron_stack['dia'])

    # 사용 가능 곡괭이
    for i in range(len(picks)):
        if picks[i] > 0:
            print(picks[i])

    # 캐야할 광물
    for i in minerals:
        print(i)

    return answer


print(solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))