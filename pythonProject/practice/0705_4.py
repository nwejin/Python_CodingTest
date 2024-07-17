def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0 #배달 카운트
    pickup = 0 #수거 카운트

    for i in range(n-1, -1, -1): #맨 뒤에서 부터 배달, 수거 진행
        delivery += deliveries[i] # 배달 카운드에 현재 집의 배달 수 더하기
        # print(delivery) # 2 + 1 + 3 + 0 + 1
        pickup += pickups[i] #수거 카운트에 현재 집 수거 수거 수 더하기
        # print(pickup) # 0 + 4 + 0 + 3 + 0

        while delivery > 0 or pickup > 0: #배달, 수거 카운드가 0 이상 (현재 집에 배달할게 남아있다면)
            delivery -= cap
            pickup -= cap
            answer += (i + 1) * 2 #거리 계산
            print(answer)

    return answer


print(solution(4, 5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0] ))