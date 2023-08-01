import gudhi as gd


def complex_rips(points, max_edge_length=None, sparse=None, max_dimension=None):
    
        return gd.RipsComplex(points=points, max_edge_length=max_edge_length, sparse=sparse).create_simplex_tree(max_dimension=max_dimension)
         
     
