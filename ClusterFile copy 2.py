from DatasetGeneration import generate_data_clouds
from ML_pipeline_third_test import ML_pipeline
import itertools
import time
from measure_time_memory import measure_time_memory
import numpy as np
from launch_benchmark import launch_benchmark
from alpha_job_to_run import run_the_process
import pandas as pd 
import matplotlib.pyplot as plt

"""points_for_cloud=800
num_diag_per_class=15
#r_values=[3, 3.5, 4]
r_values=[3, 3.5, 4, 4.1, 4.3, 4.5,5]"""



def script_final(points,labels,complex_alpha_params):
    results_list = []
    best_accuracy=0
    best_complex_parameters = {}
    best_grid_search_parameters = {}
    whole_time,whole_memory=[], []
    for complex_alpha_values in itertools.product(*complex_alpha_params.values()):
        timing,memory=[], [] # for the process of one set of parameters
        complex_alpha_parameters = dict(zip(complex_alpha_params.keys(), complex_alpha_values))
        print("TEST STARTED FOR :complex_alpha_parameters: ",complex_alpha_parameters)
        
        #step 1, compute the simplex tree and their corresponding diagram
        dgms = [run_the_process(X,i,complex_alpha_parameters,timing,memory,1) for i,X in enumerate(points)]
        dgm_time,dgm_memory=np.sum(timing), np.sum(memory)
        print("Time used for diagrams computation and persistence: ", np.sum(timing),"seconds")    
        print("Memory used for diagrams computation and persistence: {:.2f} MB".format(np.sum(memory)))
        
        #Step 2, define the pipeline 
        results_pipeline,pipeline_time,pipeline_memory=measure_time_memory(ML_pipeline,dgms,labels )
        model,train_dgms,test_dgms,train_labs,test_labs=results_pipeline
        print("Time used for pipeline creation: ",pipeline_time ,"seconds")    
        print("Memory used for diagrams computation and persistence: {:.2f} MB".format(pipeline_memory))
        print("The GridSearch model ",model)
        
        #Step 3, fit the pipeline and get the results
        results,launch_benchmark_time,launch_benchmark_memory=measure_time_memory(launch_benchmark,model,train_dgms,test_dgms,train_labs,test_labs)
        print("model best parameters",model.best_params_)
        print("Train accuracy = " + str(model.score(train_dgms, train_labs)))
        print("Test accuracy  = " + str(model.score(test_dgms,  test_labs)))
        test_accuracy,best_par=results
        print("Launch_benchmark computation time: :{:.2f} seconds".format(launch_benchmark_time))
        print(" \n\n")
        
        
        elapsed_memory=dgm_memory+ launch_benchmark_memory+pipeline_memory
        elapsed_time=dgm_time +pipeline_time+launch_benchmark_time
        
        print("Test for the parameters: {} took {:.2f} seconds and consumed {:.2f} MB in memory".format(complex_alpha_parameters, elapsed_time, elapsed_memory))
        
        print("============================================================================================================================================")
        print("============================================================================================================================================")
        print("============================================================================================================================================")
        whole_time.append(elapsed_time)
        whole_memory.append(elapsed_memory)
        result_dict = {
            'complex_parameters': complex_alpha_parameters,
            'elapsed_time': round(elapsed_time,3),
            'time for diagram computation' : round(dgm_time,3),
            'time for pipeline creation': round(pipeline_time,3),
            'time for pipeline fitting and testing': round(launch_benchmark_time),
            'elapsed_memory': round(elapsed_memory,3),
            'memory for diagram computation' : round(dgm_memory,3),
            'memory for pipeline creation': round(pipeline_memory,3),
            'memory for pipeline fitting and testing': round(launch_benchmark_memory),
            'test_accuracy': test_accuracy,
            'best parameters for the complex': best_par ,
        }

        results_list.append(result_dict)
        if test_accuracy >best_accuracy :
                best_accuracy=test_accuracy
                best_grid_parameters=best_par.copy()
                best_complex_parameters=complex_alpha_parameters.copy()
   
    
    print("Time consumed after the whole test {} seconds ".format(round(np.sum(whole_time),3) )   ) 
    print("Memory consumed for the whole test {} MB ".format(round(np.sum(whole_memory),3)) )
    print("Best Complex  Parameters:", best_complex_parameters)
    print("Best Grid Search Parameters:", best_grid_parameters)
    print("Best Test Accuracy:", best_accuracy) 
    df_results = pd.DataFrame(results_list)

    plt.figure(figsize=(10, 6))
    plt.axis('off')
    plt.table(cellText=df_results.values, colLabels=df_results.columns, cellLoc = 'center', loc='center')
    plt.savefig('results.png', bbox_inches='tight')
    df_results.to_csv('results.csv', index=False)


    
    
    
    return df_results
    
    
    
    
    
    
        

    
    


