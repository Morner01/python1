import time

def sum(a, b):
    start_time = time.time() 
    result = a + b
    end_time = time.time()
    result_time = end_time - start_time
    return f'Ответ: {result}, {result_time * 1000:.6f} милисекунд затрачено на решение'

print(sum(5, 10))