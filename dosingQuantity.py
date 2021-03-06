import math

# 多久過期，以小時計
expire_hrs = 0.5
# 例如QID，每天給四次，每四小時給一次。每天即為dosing_course
dosing_course = 24
# 例如QID，每天給四次，每四小時給一次。四次即為dosing_times
dosing_times = 2
# 例如QID，每天給四次，每四小時給一次。每四小時即為dosing_interval_hrs
dosing_interval_hrs = 5
med_contain = 75
each_time_dosage = 37.5
dosing_duration_days = 5
# 最後需要幾銷售單位的參數
need_units = 0
# 每單位藥品可以投予幾次
valid_dosing_times_per_amp = math.floor(med_contain / each_time_dosage)
# 10.0是必要的，否則無條件進位可能出現奇怪的狀況
each_time_amps = math.floor(each_time_dosage / med_contain * 10) / 10.0
'''
[可累計次數] = 有效時數 / 給藥間隔時數
如果有餘數無條件捨去，0.x就是0次，1.x就是1次，2.x就是2次
如果沒有餘數就減一(因為就算除起來可以用兩次，到了第二次的時間也是過期了)
'''
if expire_hrs % dosing_interval_hrs == 0:
    valid_extent_times = expire_hrs / dosing_interval_hrs - 1
else:
    valid_extent_times = math.floor(expire_hrs / dosing_interval_hrs)

if valid_extent_times >= 1:  # 表示可以累計
    if (valid_dosing_times_per_amp - 1) >= valid_extent_times:
        # 可以延一次就是可以用兩次，可以延兩次就是可以用三次
        effective_amp_content = each_time_dosage * (valid_extent_times + 1)
        need_units = 24 * dosing_duration_days / dosing_course * dosing_times * each_time_dosage / effective_amp_content
    else:
        need_units = 24 * dosing_duration_days / dosing_course * dosing_times * each_time_dosage / med_contain
else:
    need_units = 24 * dosing_duration_days / dosing_course * dosing_times * math.ceil(each_time_dosage / med_contain)

need_units = math.ceil(need_units)
print(f'共需要 {need_units} 支')
