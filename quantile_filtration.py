from scipy.spatial import distance_matrix
import numpy as np


def quantile(points) :
    

            pairwise_distances = distance_matrix(points, points)
            upper_triangle = np.triu(pairwise_distances, k=1).flatten()
            dis=np.sort(upper_triangle[upper_triangle!=0])

            percentiles = np.arange(10, 100, 10)
            max_edge_lengths = np.percentile(dis, percentiles)

            # Print the calculated quantiles
            for p, q in zip(percentiles, max_edge_lengths):
                print(f"{p}th Percentile: {q}")
            return     max_edge_lengths
    
    
    