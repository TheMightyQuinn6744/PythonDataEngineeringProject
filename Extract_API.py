#!mamba install pandas==1.3.3 -y
#!mamba install requests==2.26.0 -y

import requests
import pandas as pd

#Using the requests library call the endpoint and save the text
url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=WdMZXvS0nZBqlDR6nEYttIe67OMwuYmS"
exchange_rate = requests.get(url)

print(exchange_rate)
# type(html_data)

# Turn the data into a dataframe
curr_exchange_json = exchange_rate.json()

df = pd.DataFrame.from_dict(curr_exchange_json)
df.index.name = 'Currency'
# print(df)

# Drop unnescessary columns
df = df.drop(['success','timestamp','base','date'], axis=1)
print(df)

# Save the Dataframe
df.to_csv('exchange_rates_1.csv', index = True)
