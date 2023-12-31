import gudhi as gd


def complex_alpha(points, precision, weights=None, max_alpha_square=None, default_filtration_value=None):
    
        return gd.AlphaComplex(points=points, precision=precision, weights=weights).create_simplex_tree(  default_filtration_value=default_filtration_value,max_alpha_square=max_alpha_square)
       
         
