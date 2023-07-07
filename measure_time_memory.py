import time
from memory_profiler import memory_usage

def measure_time_memory(func, *args, **kwargs):
    start_time = time.time()
    mem_usage = memory_usage((func, args, kwargs))
    end_time = time.time()
    elapsed_time = end_time - start_time
    peak_mem_usage = max(mem_usage) - min(mem_usage)

    # Call the function and obtain the result
    result = func(*args, **kwargs)

    return result, elapsed_time, peak_mem_usage
