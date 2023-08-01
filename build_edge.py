import gudhi as gd


def complex_edge(points,max_edge_length=None,sparse=None,max_dimension=None,nb_iterations=None,expansion_dim=2):  
        RC=gd.RipsComplex(points=points,max_edge_length=max_edge_length, sparse=sparse).create_simplex_tree(max_dimension=1)
        RC.collapse_edges(nb_iterations=nb_iterations)
        RC.expansion(expansion_dim)
        
        return RC



     
