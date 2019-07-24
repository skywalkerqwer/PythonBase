def sum_sec(day=0, min=0, hour=0):
    total_sec = day * 3600 * 24 + min * 60 + hour * 3600
    return total_sec


print(sum_sec(hour=2))
