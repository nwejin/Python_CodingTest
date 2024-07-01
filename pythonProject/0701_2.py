import math
from datetime import datetime

def time_operator(in_time, out_time):
    in_time = datetime.strftime(in_time, '%H:%M')
    out_time = datetime.strftime(out_time,'%H:%M')
    return int((out_time-in_time).seconds / 60)

def fee_operatior(total_parking_time, fees):
    base_time, base_fee, unit_time, unit_fee = fees
    if total_parking_time <= base_time:
        return base_fee
    return base_fee + math.ceil((total_parking_time - base_time) / unit_time) * unit_fee

def solution(fees, records):


