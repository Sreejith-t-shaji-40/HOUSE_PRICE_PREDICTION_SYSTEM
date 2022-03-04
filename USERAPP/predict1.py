import sklearn
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import xgboost
import lightgbm
import re
import pickle
import numpy as np
import pandas as pd

import sklearn


import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
PATH = 'Dataset/'
PATH_TO_train_data = PATH + 'train.csv'
PATH_TO_test_data = PATH + 'test.csv'
PATH_TO_sample_submission = PATH + 'sample_submission.xlsx'
def preprocess_total_sqft(my_list):
    if len(my_list) == 1:
        
        try:
            return float(my_list[0])
        except:
            strings = ['Sq. Meter', 'Sq. Yards', 'Perch', 'Acres', 'Cents', 'Guntha', 'Grounds']
            split_list = re.split('(\d*.*\d)', my_list[0])[1:]
            area = float(split_list[0])
            type_of_area = split_list[1]
            
            if type_of_area == 'Sq. Meter':
                area_in_sqft = area * 10.7639
            elif type_of_area == 'Sq. Yards':
                area_in_sqft = area * 9.0
            elif type_of_area == 'Perch':
                area_in_sqft = area * 272.25
            elif type_of_area == 'Acres':
                area_in_sqft = area * 43560.0
            elif type_of_area == 'Cents':
                area_in_sqft = area * 435.61545
            elif type_of_area == 'Guntha':
                area_in_sqft = area * 1089.0
            elif type_of_area == 'Grounds':
                area_in_sqft = area * 2400.0
            return float(area_in_sqft)
        
    else:
        return (float(my_list[0]) + float(my_list[1]))/2.0
train_data = pd.read_csv(PATH_TO_train_data)
test_data = pd.read_csv(PATH_TO_test_data)
train_data.shape
train_data.head()
train_data.area_type.value_counts()
replace_area_type = {'Super built-up  Area': 0, 'Built-up  Area': 1, 'Plot  Area': 2, 'Carpet  Area': 3}
train_data['area_type'] = train_data.area_type.map(replace_area_type)


train_data.head()


def replace_availabilty(my_string):
    if my_string == 'Ready To Move':
        return 0
    elif my_string == 'Immediate Possession':
        return 1
    else:
        return 2
train_data['availability'] = train_data.availability.apply(replace_availabilty)
train_data.head()


train_data[~train_data.location.notnull()]


train_data['location'] = train_data['location'].fillna('Location not provided')

size_encoder = LabelEncoder()
size_encoder.fit(train_data['size'].astype('str').append(test_data['size'].astype('str')))
train_data['size'] = size_encoder.transform(train_data['size'].astype('str'))

# array(['1 BHK', '1 Bedroom', '1 RK', '10 BHK', '10 Bedroom', '11 BHK',
#        '11 Bedroom', '12 Bedroom', '13 BHK', '14 BHK', '16 BHK',
#        '16 Bedroom', '18 Bedroom', '19 BHK', '2 BHK', '2 Bedroom',
#        '27 BHK', '3 BHK', '3 Bedroom', '4 BHK', '4 Bedroom', '43 Bedroom',
#        '5 BHK', '5 Bedroom', '6 BHK', '6 Bedroom', '7 BHK', '7 Bedroom',
#        '8 BHK', '8 Bedroom', '9 BHK', '9 Bedroom', 'nan'], dtype=object)
train_data.head()
# train_data = train_data.drop(columns='society', axis=1)
train_data['society'] = train_data['society'].fillna('Other')
society_encoder = LabelEncoder()
society_encoder.fit(train_data['society'].append(test_data['society'].fillna('Other')))
train_data['society'] = society_encoder.transform(train_data['society'])
train_data.head()

train_data['total_sqft'] = train_data.total_sqft.str.split('-').apply(preprocess_total_sqft)
train_data['bath'].isna().sum()
column_bath = train_data.groupby('location')['bath'].transform(lambda x: x.fillna(x.mean()))
column_bath[~column_bath.notnull()]
column_bath = column_bath.fillna(column_bath.mean())
column_bath.isna().sum()
train_data['bath'] = column_bath
train_data.balcony.isna().sum()
train_data.balcony.value_counts()
column_balcony = train_data.groupby('location')['balcony'].transform(lambda x: x.fillna(x.mean()))
column_balcony = column_balcony.fillna(column_balcony.mean())
column_balcony.isna().sum()
train_data['balcony'] = column_balcony
train_data.head()
location_encoder = LabelEncoder()
location_encoder.fit(train_data['location'].append(test_data['location']))
train_data['location'] = location_encoder.transform(train_data['location'])
location_encoder.classes_


train_data.head()

columns = train_data.columns
X_train = train_data[columns[:-1]]
y_train = train_data[columns[-1]]
test_data = pd.read_csv(PATH_TO_test_data)
test_data.isna().sum()
test_data.head()
test_data['area_type'] = test_data.area_type.map(replace_area_type)

test_data['availability'] = test_data.availability.apply(replace_availabilty)

test_data['location'] = location_encoder.transform(test_data['location'].astype('str'))

test_data['size'] = size_encoder.transform(test_data['size'].astype('str'))

test_data['society'] = society_encoder.transform(test_data['society'].astype('str').fillna('Other'))

test_data['total_sqft'] = test_data.total_sqft.str.split('-').apply(preprocess_total_sqft)

test_data['bath'] = test_data['bath'].fillna(train_data.bath.mean())

test_data['balcony'] = test_data['balcony'].fillna(train_data.balcony.mean())

test_data = test_data.drop(columns='price')

X_test = test_data
X_test.head()




from sklearn.grid_search import GridSearchCV

params = {'min_child_weight':[4,5,6], 'gamma':[i/10.0 for i in range(3,6)],  'subsample':[i/10.0 for i in range(6,11)],
'colsample_bytree':[i/10.0 for i in range(6,11)], 'max_depth': [2,3,4], 'n_estimators':[1000, 1500, 2000], 
          'learning_rate':[0.01, 0.05, 0.1]}

xgb = xgboost.XGBRegressor(nthread=-1) 

grid = GridSearchCV(xgb, params)

grid.fit(X_train, y_train)
grid.best_estimator_
y_pred = grid.best_estimator_.predict(X_test)
# y_pred = model.predict(X_test)
y_pred
out_df = pd.DataFrame({'price': y_pred})
out_df.to_excel('predictions_grid_search.xlsx', index=False)
import pickle
pkl_filename = "xgboost_grid_search.pkl"  
with open(pkl_filename, 'wb') as file:
    pickle.dump(grid, file)


