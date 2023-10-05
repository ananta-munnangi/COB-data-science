import requests
import pandas as pd
url="https://api.binance.com/api/v3/ticker/24hr"
response=request.get(url)
if response.status_code==200:
  data=response.json()
else:
  print("FAILED TO FETCH DATA")
df=pd.Dataframe(data)  
df.tocsv('binance_data.csv',index=False)
  
  
