import pandas as pd
import numpy as np
import math
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from greyatomlib.time_series_day_02_project.q05_feature_engineering_part4.build import q05_feature_engineering_part4
from greyatomlib.time_series_day_02_project.q02_data_splitter.build import q02_data_splitter

fe =  ["WorkDay", "Peakhours", "Peakmonths"]

def q08_gradientboosting_regressor():
    
