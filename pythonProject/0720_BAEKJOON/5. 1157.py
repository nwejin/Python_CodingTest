import sys
input = sys.stdin.readline

alphabet = input().strip()
a_dict= {}

for i in alphabet:
    # 알파벳과 빈도를 key: value로 저장
    i = i.upper() #대문자 변경
    if i not in a_dict:
        a_dict[i] = 1
    else:
        # 존재하면 +1
        a_dict[i] += 1

# print(a_dict)
# 가장 큰 값 찾기
max_count = max(a_dict.values())
# print(max_count)

# 중복값이 담길 리스트 만들기
a_list = []
# 딕셔너리에서 key, value값으로 중복 알파벳 찾기
for a, count in a_dict.items():
    # print(count)
    if count == max_count:
        a_list.append(a)

# print(a_list)

# 리스트에 2개 이상 있는 경우
if len(a_list) > 1:
    print('?')
else:
    print(a_list[0])


