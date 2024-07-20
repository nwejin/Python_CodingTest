import sys
input = sys.stdin.readline

N = int(input())

# 전체 인원을 담을 딕셔너리
log_dict = {}

# 남아있는 인원만 담을 리스트
enter_list = []

for i in range(N):
    # 이름과 현재 상태를 입력 받기
    name, status = input().split()
    # print(name, status)
    # 딕셔너리 안에 이름: 상태 형식으로 저장
    log_dict[name] = status


for key in log_dict.keys():
    value = log_dict[key]
    # 상태가 enter인 사람만 다시 리스트 생성
    if value == 'enter':
       enter_list.append(key)

# 리스트를 역순 정렬
enter_list = sorted(enter_list, reverse= True)

# 리스트 출력
for i in enter_list:
    print(i)
