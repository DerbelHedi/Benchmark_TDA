import gudhi as gd
import gudhi.representations

def compute_vectorisation(dgm,representation) :

        if representation=="Landscape":
            vec=gd.representations.Landscape()
        elif representation=="PersistenceImage" :
            vec=gd.represensations.PersistenceImage()
        else:
            raise ValueError("Invalid representation type. Supported types are: Landscape, PersistenceImage")    
        vec=vec.fit_transform([dgm]) 
        return         vec

