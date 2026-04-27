import dill
import os
from src.exception import CustomException
import sys
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
import numpy as np

def save_object(file_path, obj):
    try:
        dir_path  = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_model(X_train,y_train,X_test,y_test,models,param):
    try:
        report = {}
        for name,model in models.items():
            model_param = param.get(name, {})
            gs= GridSearchCV(model,cv=3, param_grid=model_param)
            gs.fit(X_train,y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            train_pred = model.predict(X_train)
            test_pred = model.predict(X_test)
            training_rmse = np.sqrt(mean_squared_error(y_train, train_pred))    
            testing_rmse = np.sqrt(mean_squared_error(y_test, test_pred))
            report[name] = testing_rmse
        return report  
    except Exception as e:
        raise CustomException(e,sys)
