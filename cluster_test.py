from ClusterFile import script_final
from DatasetGeneration import generate_data_clouds

points_for_cloud=800
num_diag_per_class=15
#r_values=[3, 3.5, 4]
r_values=[3, 3.5, 4, 4.1, 4.3, 4.5,5]
points,labels,quantile=generate_data_clouds(points_for_cloud,num_diag_per_class,r_values)
complex_params = {
    'complex_type': ['edge'],
    'max_dimension': [2],
    'sparse': [None],
    'max_edge_length': [quantile[4],quantile[6],quantile[8]],
    'nb_iterations': [2]
}

df=script_final(points,labels,complex_params)
print(df)
 