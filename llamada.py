import requests
import pandas as pd
from datetime import datetime

def llamada(n):
    n=int(n/3)

    weatherJson= r = requests.get(url = "http://api.openweathermap.org/data/2.5/forecast?id=5391959&appid=76ea6b898b310c15efee929bfe21e602")
    data = weatherJson.json() 
    df = pd.io.json.json_normalize(data['list'])

    todays_date = datetime.now()
    index = pd.date_range(todays_date, periods=n, freq='3H')

    odf= pd.DataFrame(index=index, columns=['Temperatura','Humedad'])
    odf['Temperatura']=df['main.temp'].head(n).values
    odf['Humedad']=df['main.humidity'].head(n).values
    
    return odf