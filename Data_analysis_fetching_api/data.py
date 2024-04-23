import requests
api_key='IR8GM0NH1LG98L9U'
import pandas as pd


def get_data(api_key):
    url=f'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey={api_key}'
    response=requests.get(url)
    if response.status_code!=200:
        print("We can't fetch data")
    else:
        data=response.json()['Time Series FX (Monthly)']
        date=[date for date in data]
        open=[data[date]['1. open']for date in data]
        high=[data[date]['2. high']for date in data]
        low=[data[date]['3. low']for date in data]
        close=[data[date]['4. close']for date in data]
        return date,open,high,low,close

def dataframe_csv(data):
    date,open,high,low,close=data
    exchange_data={'date':date,
                'open':open,
                'high':high,
                'low':low,
                'close':close}
    df=pd.DataFrame(exchange_data)
    csv=df.to_csv('exhange.csv',index=False)

data=get_data(api_key)
dataframe_csv(data)
