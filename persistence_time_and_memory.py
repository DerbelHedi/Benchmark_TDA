
from build_complex import build_complex
from compute_persistence import compute_persistence
from measure_time_memory import measure_time_memory
import gudhi
from time_usage import measure_time
import numpy as np

# In addition to the construction of simplex trees out of a point cloud, it returns the diagram and add the time  and memory consumed  

def run_the_process(X,i,complex_alpha_parameters,whole_time,whole_memory,persistence_intervals_dimension):
    
    alpha_result,build_complex_timing,build_complex_memory=measure_time_memory(build_complex,X,**complex_alpha_parameters)
    print("ST {} computation time: {:.2f} seconds".format(i+1, build_complex_timing))
    print("ST {} Memory used: {:.2f} MB".format(i+1,build_complex_memory))
    print("ST number of simplices ", alpha_result.num_simplices())
    complex_type = complex_alpha_parameters['complex_type']
    
   
    if complex_type=='rips':
        dgm,compute_persistence_timing=measure_time(compute_persistence,alpha_result,persistence_intervals_dimension)
        compute_persistence_memory=np.inf
    else:
         dgm,compute_persistence_timing,compute_persistence_memory=measure_time_memory(compute_persistence,alpha_result,persistence_intervals_dimension) 
         
    print("persistence computation time: :{:.2f} seconds".format(compute_persistence_timing))
    print(" \n\n")
    whole_time.append(compute_persistence_timing+build_complex_timing)
    whole_memory.append(build_complex_memory+ compute_persistence_memory)
    return dgm


''' if complex_type=='rips':
        dgm,compute_persistence_timing=measure_time_memory(compute_persistence,alpha_result,persistence_intervals_dimension)
        compute_persistence_memory=None
    else:
         dgm,compute_persistence_timing,compute_persistence_memory=measure_time_memory(compute_persistence,alpha_result,persistence_intervals_dimension) '''