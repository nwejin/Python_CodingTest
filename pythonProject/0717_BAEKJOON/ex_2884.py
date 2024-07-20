H, M = map(int,input().split())

early = 45*60 #45분
sec = (H*3600) + (M*60) # 입력 시간 초로 변환

total_time = (sec-early)

if total_time//3600 < 0:
    H = 24+total_time//3600
else:
    H = total_time//3600

M = (total_time%3600)//60

print(H, M)


