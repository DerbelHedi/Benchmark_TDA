from ClusterFile import script_final
from DatasetGeneration import generate_data_clouds
from TestTest import test
import numpy as np
points_for_cloud=800
num_diag_per_class=15
#r_values=[3, 3.5, 4]
r_values=[2.5,3.5,4,4.1,4.3]
points,labels,quantile=generate_data_clouds(points_for_cloud,num_diag_per_class,r_values)

complex_time=test(points,labels,quantile)
#df=script_final(points,labels,complex_params2)
#df=script_final(points,labels,complex_params3)

for i,q in enumerate(complex_time):
    print(q)
    print(" avg mean time for computation for rips ",i, " ", np.mean(q) )