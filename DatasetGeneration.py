import numpy as np
import pandas as pd
import random 
from quantile_filtration import quantile

random.seed(62445)  # we fix the seed in order to eliminate randomness
np.random.seed(62445)


def generate_data_clouds(points_for_cloud,num_diag_per_class,r_values):  # generating a list of data clouds (var points), with it's corresponding list of 10 percentiles
    
    labels = []
    points=[]
    
    for r in r_values:
        for _ in range(num_diag_per_class):
            
            X = np.empty([points_for_cloud, 2])
            x, y = np.random.uniform(), np.random.uniform()
            
            for i in range(points_for_cloud):
                
                X[i, :] = [x, y]
                x = (X[i, 0] + r * X[i, 1] * (1 - X[i, 1])) % 1
                y = (X[i, 1] + r * x * (1 - x)) % 1
                
            points.append(X)
            labels.append([str(r)])
    
    thresh = [quantile(element) for element in points]
    thresh_array = np.array(thresh)
    quantiles= np.mean(thresh_array, axis=0)        

            
    return (points,labels,quantiles)        
            


        
