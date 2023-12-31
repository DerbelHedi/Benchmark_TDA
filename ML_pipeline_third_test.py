
import numpy as np
from memory_profiler import profile
from sklearn.preprocessing   import MinMaxScaler
from sklearn.pipeline        import Pipeline
from sklearn.svm             import SVC
from sklearn.ensemble        import RandomForestClassifier
from sklearn.neighbors       import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from gudhi.representations import PersistenceImage
from gudhi.representations import BottleneckDistance
from gudhi.representations import Landscape
import gudhi as gd



def ML_pipeline(dgms,labels):
    
    
    test_size            = 0.2
    perm                 = np.random.permutation(len(labels))
    limit                = int(test_size * len(labels))
    test_sub, train_sub  = perm[:limit], perm[limit:]
    train_labs           = np.array(np.array(labels)[train_sub]).ravel()
    test_labs            = np.array(np.array(labels)[test_sub]).ravel()
    train_dgms           = [dgms[i] for i in train_sub]
    test_dgms            = [dgms[i] for i in test_sub]
        
    pipe = Pipeline([("Separator", gd.representations.DiagramSelector(limit=np.inf, point_type="finite")),
                    ("Scaler",    gd.representations.DiagramScaler(scalers=[([0,1], MinMaxScaler())])),
                    ("TDA",       gd.representations.PersistenceImage()),
                    ("Estimator", RandomForestClassifier())])

    # Parameters of pipeline. This is the place where you specify the methods you want to use to handle diagrams
    param =    [
                                
                {"Scaler__use":         [True],
                "TDA":                 [gd.representations.Landscape()], 
                "TDA__resolution":     [100],
                "Estimator":           [RandomForestClassifier()]},
            
                {"Scaler__use":         [True],
                "TDA":                 [gd.representations.PersistenceImage()], 
                "TDA__resolution":     [ [5,5], [6,6] ],
                "TDA__bandwidth":      [0.01, 0.1, 1.0, 10.0],
                "Estimator":           [RandomForestClassifier()]},
                {"Scaler__use":         [False],
                "TDA":                 [gd.representations.BottleneckDistance()], 
                "TDA__epsilon":        [0.1], 
                "Estimator":           [RandomForestClassifier()]}
            ]

    model = GridSearchCV(pipe, param, cv=4, error_score='raise')    
    
    return model,train_dgms,test_dgms,train_labs,test_labs