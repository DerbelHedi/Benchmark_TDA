import gudhi as gd
'''from memory_profiler import profile
@profile'''

def complex_edge(points,max_edge_length=None,sparse=None,max_dimension=None,nb_iterations=None):  
        RC=gd.RipsComplex(points=points,max_edge_length=max_edge_length, sparse=sparse).create_simplex_tree(max_dimension=max_dimension)
        RC.collapse_edges(nb_iterations=nb_iterations)
        
        return RC        



     
