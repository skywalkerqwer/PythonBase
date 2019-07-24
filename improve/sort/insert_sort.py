"""
    插入排序
"""
import time
def insert_sort(list_target):
    for i in range(len(list_target)):
        for j in range(i):
            if list_target[i]<list_target[j]:
                list_target.insert(j,list_target.pop(i))

list01 = [2, 8, 6, 1, 3, 9]
time1 = time.time()
insert_sort(list01)
time2 = time.time()
print(list01,time2-time1)