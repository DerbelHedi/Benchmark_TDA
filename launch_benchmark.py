
# Fit the model to the diagrams and test the accuracy
def launch_benchmark(model,train_dgms,test_dgms,train_labs,test_labs):
    model = model.fit(train_dgms, train_labs)
    best_par=model.best_params_
    test_accuracy=model.score(test_dgms,  test_labs)
    
    return test_accuracy,best_par