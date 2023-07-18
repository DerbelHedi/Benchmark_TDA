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


# In addition to the construction of simplex trees out of a point cloud, it returns the diagram and add the time  and memory consumed  

def run_the_process(X,i,complex_alpha_parameters,whole_time,whole_memory):
    
    alpha_result,build_complex_timing,build_complex_memory=measure_time_memory(build_complex,X,**complex_alpha_parameters)
    print("ST {} computation time: {:.2f} seconds".format(i+1, build_complex_timing))
    print("ST {} Memory used: {:.2f} MB".format(i+1,build_complex_memory))
    
    dgm,compute_persistence_timing,compute_persistence_memory=measure_time_memory(compute_persistence,alpha_result)
    
    print("persistence computation time: :{:.2f} seconds".format(compute_persistence_timing))
    print(" \n\n")
    whole_time.append(compute_persistence_timing+build_complex_timing)
    whole_memory.append(build_complex_memory+ compute_persistence_memory)
    return dgm


