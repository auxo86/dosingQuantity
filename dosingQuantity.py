import math

expire_hrs = 12
dosing_course = 24
dosing_times = 4
dosing_interval_hrs = 6
med_contain = 1500
each_time_dosage = 1600
dosing_duration_days = 5
need_amps = 0
# 每支藥品可以投予幾次
valid_dosing_times_per_amp = math.floor(med_contain / each_time_dosage)
each_time_amps = math.floor(each_time_dosage / med_contain * 10) / 10
'''
[可累計次數] = 有效時數 / 給藥間隔時數
如果有餘數無條件捨去
如果沒有餘數就減一(因為就算除起來可以用兩次，到了第二次的時間也是過期了)
'''
if expire_hrs % dosing_interval_hrs == 0:
    valid_extent_times = expire_hrs / dosing_interval_hrs - 1
else:
    valid_extent_times = math.floor(expire_hrs / dosing_interval_hrs)

if valid_extent_times >= 1:  # 表示可以累計
    if (valid_dosing_times_per_amp - 1) >= valid_extent_times:
        # 可以延一次就是可以用兩次，可以延兩次就是可以用三次
        effectiive_amp_content = each_time_dosage * (valid_extent_times + 1)
        need_amps = 24 * dosing_duration_days / dosing_course * dosing_times * each_time_dosage / effectiive_amp_content
    else:
        need_amps = 24 * dosing_duration_days / dosing_course * dosing_times * each_time_dosage / med_contain
else:
    need_amps = 24 * dosing_duration_days / dosing_course * dosing_times * math.ceil(each_time_dosage / med_contain)

need_amps = math.ceil(need_amps)
print(f'共需要 {need_amps} 支')
