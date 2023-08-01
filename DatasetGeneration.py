import numpy as np
import pandas as pd
import random 
from quantile_filtration import quantile




def generate_data_clouds(points_for_cloud,num_diag_per_class,r_values):  # generating a list of data clouds (var points), with it's corresponding list of 10 percentiles
    
    labels = []
    points=[]
    '''  random.seed(62445)  # we fix for first test
    np.random.seed(62445)'''
    
    '''random.seed(6245)  # we fix the seed in order to eliminate randomness
    np.random.seed(6245)'''
    '''random.seed(625)  # we fix the seed in order to eliminate randomness
    np.random.seed(625)'''
    '''random.seed(62588)  # we fix for first test
    np.random.seed(62588)'''
    '''random.seed(6255558)  # we fix for first test
    np.random.seed(6255558)'''
    '''random.seed(621238)  # we fix for first test
    np.random.seed(621238)'''
    '''random.seed(56238)  # we fix for first test
    np.random.seed(56238)'''
    '''random.seed(336238)  # we fix for first test
    np.random.seed(336238)'''
    """random.seed(7644338)  # we fix for first test
    np.random.seed(76438)"""
    """random.seed(9986)  # we fix for first test
    np.random.seed(9986)"""
    """random.seed(99846)  # we fix for first test
    np.random.seed(99846)"""
    """random.seed(89846)  # we fix for first test
    np.random.seed(89846)"""
    """random.seed(1234)  # we fix for first test
    np.random.seed(1234)"""
    """random.seed(12345)  # we fix for first test
    np.random.seed(12345)"""
    
    """random.seed(123456)  # we fix for first test
    np.random.seed(123456)"""
    """random.seed(3456)  # we fix for first test
    np.random.seed(3456)"""
    """random.seed(31456)  # we fix for first test
    np.random.seed(31456)"""
    """random.seed(345633)  # we fix for first test
    np.random.seed(345633)"""
    """random.seed(65633)  # we fix for first test
    np.random.seed(65633)"""
    """ random.seed(6544633)  # we fix for first test
    np.random.seed(6544633)"""
    """random.seed(91384)  # we fix for first test
    np.random.seed(91384)"""
    """random.seed(891384)  # we fix for first test
    np.random.seed(891384)"""
    random.seed(384)  # we fix for first test
    np.random.seed(384)
    
    
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
            


        
