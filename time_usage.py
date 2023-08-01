from time import perf_counter_ns
def measure_time(func, *args, **kwargs):
    

    start_time = perf_counter_ns()/ (10**9) 
    result = func(*args, **kwargs)
    end_time = perf_counter_ns() / (10**9) 
    elapsed_time = end_time - start_time
    

    return result, elapsed_time
