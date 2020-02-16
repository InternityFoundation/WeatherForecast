# importing libraries 
import pandas as pd 
import numpy as np 
import sklearn as sk 
from sklearn.linear_model import LinearRegression as lm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
import json
import requests
from wwo_hist import retrieve_hist_data
#path for csv
import os
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def forecast(city_name):
    os.chdir(r"C:\Users\Administrator\Desktop")
    frequency = 3
    start_date = '1-JAN-2019'
    end_date = '1-JAN-2020'
    api_key = 'e60a5f5f96574a33947210842201502'
    #city_name = input('Enter city name: ')
    location_list = [city_name]
    hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)
    path="C:\\Users\\Administrator\\Desktop\\"

    data = pd.read_csv(path+city_name+".csv") 

    # drop or delete the unnecessary columns in the data. 
    data = data.drop(["date_time", 'maxtempC','DewPointC', 'mintempC','sunHour','moon_illumination','moonrise','moonset','sunrise','sunset','HeatIndexC','WindChillC','WindGustKmph', 
                    'totalSnow_cm'],axis=1,inplace=False) 

    data.to_csv(city_name+'.csv')

    params = {
    'access_key': '7f31a3c1baed8dddc5b06a0448f4b534',
    'query': city_name
    }

    api_result = requests.get('http://api.weatherstack.com/current', params)
    arr=[]
    api_response = api_result.json()
    print('\n')
    print(u'Given City Name: %s' % (api_response['location']['name']))
    #a=api_response['location']['name']
    #these variables a to k can be returned to get the current details 
    print(u'Current temperature is %d℃' % (api_response['current']['temperature']))
    a=api_response['current']['temperature']
    print(u'Current Humidity is %d' % (api_response['current']['humidity']))
    b=api_response['current']['humidity']
    print(u'Current Pressure is %d Pascal' % (api_response['current']['pressure']))
    c=api_response['current']['pressure']
    print(u'Current Cloud Cover is %d' % (api_response['current']['cloudcover']))
    d=api_response['current']['cloudcover']
    print(u'Current Precipitation is %d' % (api_response['current']['precip']))
    e=api_response['current']['precip']
    print(u'Current Visibility is %d' % (api_response['current']['visibility']))
    f=api_response['current']['visibility']
    print(u'Current Wind Speed is %d' % (api_response['current']['wind_speed']))
    g=api_response['current']['wind_speed']
    print(u'Current Feels Like is %d' % (api_response['current']['feelslike']))
    h=api_response['current']['feelslike']
    print(u'Current Wind Direction is %s' % (api_response['current']['wind_dir']))
    i=api_response['current']['wind_arr']
    print(u'Current UV Index is %d' % (api_response['current']['uv_index']))
    j=api_response['current']['uv_index']
    print(u'Current Wind Degree is %d' % (api_response['current']['wind_degree']))
    k=api_response['current']['wind_degree']


    # save the data in a csv file  
    path="C:\\Users\\Administrator\\Desktop\\"
    data = pd.read_csv(path+city_name+".csv") 
    #for pressure
    X = data.drop(['pressure'], axis = 1)  
    Y = data['pressure']  
    Y = Y.values.reshape(-1, 1) 

    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.01)
    model=lm().fit(x_train,y_train)
    pressure=model.predict(x_test)
    print(pressure, 'This is the pressure in pascal for the input') 

    #for temperature
    X = data.drop(['tempC'], axis = 1)  

    Y = data['tempC']  
    Y = Y.values.reshape(-1, 1) 

    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.01)
    model=lm().fit(x_train,y_train)
    temp=model.predict(x_test)
    print(temp, 'This is the temperature in degrees C for the input') 

    #for humidity
    X = data.drop(['humidity'], axis = 1)  

    Y = data['humidity']  
    Y = Y.values.reshape(-1, 1) 

    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.01)
    model=lm().fit(x_train,y_train)
    hum=model.predict(x_test)
    print(hum, 'This is the humidity for the input')
    pressure=str(pressure)
    temp=str(temp)
    hum=str(hum)
    return temp,pressure,hum