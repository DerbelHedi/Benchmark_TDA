import gudhi as gd
'''from memory_profiler import profile
@profile'''
def complex_rips(points, max_edge_length=None, sparse=None, max_dimension=None):
    
        RC = gd.RipsComplex(points=points, max_edge_length=max_edge_length, sparse=sparse).create_simplex_tree(max_dimension=max_dimension)
        return RC
     
