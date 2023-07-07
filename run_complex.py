from build_complex import build_complex
from compute_persistence import compute_persistence


def run_complex(complex_type, points, **kwargs):
    
    complex = build_complex(complex_type, points, **kwargs)
    dgm_interval=compute_persistence(complex)
    return  dgm_interval

