from build_alpha import complex_alpha
from build_rips import complex_rips
# from build_ripser import complex_ripser
from build_edge import complex_edge
'''from memory_profiler import profile
@profile'''

def build_complex( points,complex_type, **kwargs):
    if complex_type == "alpha":
        return complex_alpha(points, **kwargs)
    elif complex_type == "rips":
        return complex_rips(points, **kwargs)
    elif complex_type == "edge":
        return complex_edge(points, **kwargs)
    else:
        raise ValueError("Invalid complex type. Supported types are: alpha, rips, edge")
        