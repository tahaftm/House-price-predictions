from src.exception import CustomException
from src.logger import logging
import os
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from src.utils import save_object
import sys

@dataclass
class DataTransformationConfig:
    preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.preprocessor_path = DataTransformationConfig()

    def get_preprocessor(self):
        try:
            num_pipe = Pipeline([
                ("num_impute", SimpleImputer(strategy="mean")),
                ("scaler", StandardScaler())
            ])
            cat_pipe = Pipeline([
                ("cat_impute", SimpleImputer(strategy="most_frequent")),
                ("onehot",OneHotEncoder(handle_unknown='ignore'))
            ])

            cat_col = ['MSZoning', 'Street', 'LotShape', 'LandContour', 'Utilities',
        'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2',
        'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
        'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation',
        'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
        'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual',
        'Functional', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual',
        'GarageCond', 'PavedDrive', 'Fence', 'SaleType', 'SaleCondition']
            
            num_col = ['MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual',
        'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1',
        'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF',
        'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
        'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd',
        'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF',
        'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea',
        'MiscVal', 'YrSold',]
            
            preprocessor = ColumnTransformer([
                ("num_pipe", num_pipe, num_col),
                ('cat_col', cat_pipe, cat_col)
            ])

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train,test):
        try:
            preprocessor = self.get_preprocessor()
            train = preprocessor.fit_transform(train)
            test = preprocessor.transform(test)
            save_object(self.preprocessor_path.preprocessor_path,preprocessor)
            return train,test,self.preprocessor_path.preprocessor_path
        except Exception as e:
            raise CustomException(e,sys)
    