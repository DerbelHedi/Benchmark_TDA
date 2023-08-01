from ClusterFile import script_final
from DatasetGeneration import generate_data_clouds

points_for_cloud=800
num_diag_per_class=15
#r_values=[3, 3.5, 4]
r_values=[3, 3.5, 4, 4.1, 4.3, 4.5,5]
points,labels,quantile=generate_data_clouds(points_for_cloud,num_diag_per_class,r_values)
print(quantile)
complex_params = {
    'complex_type': ['edge'],
    'max_dimension': [2],
    'sparse': [None],
    'max_edge_length': quantile,
    'nb_iterations': [2,3]
} 
complex_params3 = {
    'complex_type': ['rips'],
    'max_dimension': [2],
    'sparse': [None],
    'max_edge_length': quantile
}


complex_params2 = {
    'complex_type': ['alpha'],
    'precision': ["fast","safe","exact"],
}
df=script_final(points,labels,complex_params)
#df=script_final(points,labels,complex_params2)
#df=script_final(points,labels,complex_params3)

print(quantile)
df['points_for_cloud']=points_for_cloud
df['num_diag_per_class']=num_diag_per_class
df['number_of_clouds']=num_diag_per_class*len(r_values)
print(df)