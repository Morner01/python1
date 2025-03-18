import time

def sum(a, b):
    return a + b

def reverseArr(arr):
    result = arr.reverse()
    return arr

def time_scan(func, *args1, **args2):
    start_time = time.time()
    result = func(*args1, **args2)
    end_time = time.time()
    result_time = (end_time - start_time) * 1000
    return f'{result}, {result_time:.3f}'

print(time_scan(sum, 5, 10))
print(time_scan(reverseArr, [5, 6, 9]))