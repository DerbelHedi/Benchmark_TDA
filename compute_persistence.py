import gudhi
import numpy as np

def compute_persistence(ST,persistence_intervals_dimension=1):
    
        ST.compute_persistence(2, 0, persistence_dim_max=True)
        persistence_intervals=ST.persistence_intervals_in_dimension(persistence_intervals_dimension)  # return only the first dimension persistence
        persistence_intervals_filtered = persistence_intervals[~np.isinf(persistence_intervals).any(axis=1)]
        gudhi.plot_persistence_barcode(persistence_intervals,alpha=0.8)


        return persistence_intervals_filtered 