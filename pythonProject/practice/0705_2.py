def solution(targets):
    targets.sort(key= lambda x : (x[0], x[1]))
    print(targets)

    start, end, count = 0,0,0
    start = targets[0][0]
    print(start)
    end = targets[0][1]
    print(end)

    for target in targets:
        if target[0] >= end:
            count += 1
            start, end = target[0], target[1]
        elif start < target[0] or end > target[1]:
            start = max(target[0], start)
            end = min(target[1], end)

    return count + 1
    #검사를 하다가 다음게 오버가 나와야지 실행이되는데 없어서 + 1




print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))