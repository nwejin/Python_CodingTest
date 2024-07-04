

# dictionary 활용
from math import ceil

def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee = fees

    parking = {}   #주차 시간
    using_time = {} #이용 시간

    for record in records:
        time, number, io = record.split()
        hour, minute =




