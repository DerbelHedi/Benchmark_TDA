from DatasetGeneration import generate_data_clouds
from ML_pipeline_5_test import ML_pipeline
import itertools
import time
from measure_time_memory import measure_time_memory
import numpy as np
from fit_model import launch_benchmark
from persistence_time_and_memory import run_the_process
import pandas as pd 
from time_usage import measure_time

from ClusterFile import script_final
from DatasetGeneration import generate_data_clouds



def test(points,labels,quantile):
    

   
    for i, q in enumerate(quantile):
        print( "quantile ", i+1, " ", q)

    complex_params3 = {
        'complex_type': ['rips'],
        'max_dimension': [2],
        'sparse': [None],
        'max_edge_length': quantile
    }
    whole_time,whole_memory=[], []





    for complex_alpha_values in itertools.product(*complex_params3.values()):
        timing,memory=[], [] # for the process of one set of parameters
        complex_alpha_parameters = dict(zip(complex_params3.keys(), complex_alpha_values))
        print("TEST STARTED FOR :complex_alpha_parameters: ",complex_alpha_parameters)
        
        #step 1, compute the simplex tree and their corresponding diagram
        dgms = [run_the_process(X,i,complex_alpha_parameters,timing,memory,1) for i,X in enumerate(points)]
        dgm_time,dgm_memory=np.sum(timing), np.sum(memory)
        print("Time used for diagrams computation and persistence: ", np.sum(timing),"seconds")    
        print("Memory used for diagrams computation and persistence: {:.2f} MB".format(np.sum(memory)))
        
        whole_time.append(timing)
    
    return whole_time    

        
        