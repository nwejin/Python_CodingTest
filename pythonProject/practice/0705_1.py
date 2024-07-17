from itertools import product #중복순열

def solution(users, emoticons):
    register_user_count = 0
    max_price = 0

    discounts = product([10,20,30,40],repeat=len(emoticons))

    # 할인율 중복
    for discount in discounts:
        #각 조합마다 산 유저수 / 최대 판매금
        user_count = 0
        sum_price = 0

        # 각 유저마다
        for user in users:
            paid = 0

            # 이모티콘마다 구매비용 계산
            for i in range(len(emoticons)):
                print('discount',discount[i])
                print('user', user[0])
                if(discount[i] >= user[0]):
                    #구매비용에 더하기
                    rate = (100 - discount[i])
                    print('rate',rate)
                    price100 = emoticons[i] * rate
                    # print(price100)
                    paid += price100 //100
                    print(paid)

            if(paid >= user[1]):
                user_count += 1
            else:
                sum_price += paid


        if(register_user_count < user_count):
            register_user_count = user_count
            max_price = sum_price
        elif (register_user_count == user_count):
            if(max_price < sum_price):
                max_price = sum_price

    return [register_user_count,max_price]


print(solution([[40, 10000], [25, 10000]],[7000, 9000]))