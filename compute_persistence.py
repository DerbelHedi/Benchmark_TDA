import gudhi
'''from memory_profiler import profile
@profile'''

def compute_persistence(ST):
    
        persistence=ST.persistence(persistence_dim_max=True)
        persistence_intervals=ST.persistence_intervals_in_dimension(1)  # return only the first dimension persistence
        
        return persistence_intervals #persistence   ,
        
     