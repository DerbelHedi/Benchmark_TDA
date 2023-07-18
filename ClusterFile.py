from DatasetGeneration import generate_data_clouds
from ML_pipeline_third_test import ML_pipeline
from quantile_filtration import quantile
import itertools
import gudhi as gd
from build_complex import build_complex
from run_complex import run_complex
from compute_persistence import compute_persistence
from measure_time_memory import measure_time_memory
import matplotlib.pyplot as plt
import numpy as np
from compute_vectorisation import compute_vectorisation
from memory_profiler import profile
from sklearn.preprocessing   import MinMaxScaler
from sklearn.pipeline        import Pipeline
from sklearn.svm             import SVC
from sklearn.ensemble        import RandomForestClassifier
from sklearn.neighbors       import KNeighborsClassifier
from launch_benchmark import launch_benchmark
import random
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from alpha_job_to_run import run_the_process
import pandas as pd 

'''points_for_cloud=800
num_diag_per_class=15
#r_values=[3, 3.5, 4]
r_values=[3, 3.5, 4, 4.1, 4.3, 4.5,5]'''

points_for_cloud=80
num_diag_per_class=6
#r_values=[3, 3.5, 4]
r_values=[3, 3.5, 4, 4.1,4.5]

def script_final(complex_alpha_params):
    results_list = []
    points,labels,quantile=generate_data_clouds(points_for_cloud,num_diag_per_class,r_values) # generation of multiple data clouds in the variable points with their corresponding label. the quantile is a list of the 10 percentile of the pairwise distance of points
    best_accuracy=0
    best_complex_parameters = {}
    best_grid_search_parameters = {}
    whole_time,whole_memory=[], []
    for complex_alpha_values in itertools.product(*complex_alpha_params.values()):
        start_time = time.time() 
        timing,memory=[], [] # for the process of one set of parameters
        complex_alpha_parameters = dict(zip(complex_alpha_params.keys(), complex_alpha_values))
        print("TEST STARTED FOR :complex_alpha_parameters: ",complex_alpha_parameters)
        
        #step 1, compute the simplex tree and their corresponding diagram
        dgms = [run_the_process(X,i,complex_alpha_parameters,timing,memory) for i,X in enumerate(points)]
        print("Time used for diagrams computation and persistence: ", np.sum(timing),"seconds")    
        print("Memory used for diagrams computation and persistence: {:.2f} MB".format(np.sum(memory)))
        
        #Step 2, define the pipeline 
        results_pipeline,pipeline_time,pipeline_memory=measure_time_memory(ML_pipeline,dgms,labels )
        model,train_dgms,test_dgms,train_labs,test_labs=results_pipeline
        print("Time used for pipeline creation: ",pipeline_time ,"seconds")    
        print("Memory used for diagrams computation and persistence: {:.2f} MB".format(pipeline_memory))
        print(model)
        
        #Step 3, fit the pipeline and get the results
        results,launch_benchmark_time,launch_benchmark_memory=measure_time_memory(launch_benchmark,model,train_dgms,test_dgms,train_labs,test_labs)
        test_accuracy,best_par=results
        print("Launch_benchmark computation time: :{:.2f} seconds".format(launch_benchmark_time))
        print(" \n\n")
        
        print("TEST RESULT FOR PARAMETERS : ", complex_alpha_parameters)
        end_time = time.time()
        elapsed_time=end_time-start_time
        elapsed_memory=np.sum(memory)+ launch_benchmark_memory+pipeline_memory
        print("Test for the parameters: {} took {:.2f} seconds ".format(complex_alpha_parameters,end_time-start_time))
        print("============================================================================================================================================")
        print("============================================================================================================================================")
        print("============================================================================================================================================")
        whole_time.append(elapsed_time)
        whole_memory.append(elapsed_memory)
        result_dict = {
            'complex_alpha_parameters': complex_alpha_parameters,
            'elapsed_time': round(elapsed_time,3),
            'elapsed_memory': round(elapsed_memory,3),
            'test_accuracy': test_accuracy,
            'best_par': best_par
        }

        results_list.append(result_dict)

    # Create a dataframe from the results list
    df_results = pd.DataFrame(results_list)
        
    
    if test_accuracy >best_accuracy :
        best_accuracy=test_accuracy
        best_grid_parameters=best_par.copy()
        best_complex_parameters=complex_alpha_parameters.copy()
    print("Time consumed after the whole script {} seconds ".format(round(np.sum(whole_time),3) )   ) 
    print("Memory consumed for the whole script {} MB ".format(round(np.sum(whole_memory),3)) )
    print("Best Complex  Parameters:", best_complex_parameters)
    print("Best Grid Search Parameters:", best_grid_parameters)
    print("Best Test Accuracy:", best_accuracy) 
    
    return df_results
    
    
    
    
    
    
        

    
    


