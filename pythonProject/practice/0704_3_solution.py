from heapq import heappop, heappush


def solution(n, k, enemy):
    answer = 0
    i = 0
    heap = []

    # 1. 적들의 데미지 루프
    for e in enemy:
        heappush(heap, -e)
        i += e

        if i > n:
            if k == 0:
                break
            i += heappop(heap)
            k -= 1

        answer += 1

    return answer


print(solution(7,3,[4,2,4,5,3,3,1]))