import time
from memory_profiler import memory_usage

def measure_time_memory(func, *args, **kwargs):
    
    mem_usage = memory_usage((func, args, kwargs))
    peak_mem_usage = max(mem_usage) - min(mem_usage)

    # Call the function and obtain the result
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time

    return result, elapsed_time, peak_mem_usage


