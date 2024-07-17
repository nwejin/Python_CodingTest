# 두 수 입력받기 (정수로) , 공백으로 구분
A, B = map(int, input().split())

# 각각 비교 후 값 출력
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print("==")