from ML_pipeline import ML_pipeline


def launch_benchmark(model,train_dgms,test_dgms,train_labs,test_labs):
    model = model.fit(train_dgms, train_labs)
    best_par=model.best_params_
    test_accuracy=model.score(test_dgms,  test_labs)
    print(model.best_params_)
    print("Train accuracy = " + str(model.score(train_dgms, train_labs)))
    print("Test accuracy  = " + str(model.score(test_dgms,  test_labs)))
    return test_accuracy,best_par