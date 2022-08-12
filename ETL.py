# !mamba install pandas==1.3.3 -y
# !mamba install requests==2.26.0 -y

#Import libraries needed for the project
import glob
import pandas as pd
from datetime import datetime

#Download the exchnage rate data
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/bank_market_cap_1.json
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/bank_market_cap_2.json
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Final%20Assignment/exchange_rates.csv
  
 #Extract JSON files
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe
  
 #Define the extract function that finds JSON file and stores in a pandas dataframe
# columns=['Name','Market Cap (US$ Billion)']

def extract():
  extracted_data = pd.DataFrame(columns=['Name','Market Cap (US$ Billion)'])
  for jsonfile in glob.glob("*.json"):
    extracted_data=extract_from_json(jsonfile)
  return extracted_data

#Load the file exchange rates as a dataframe and find the exchnage rate for British pounds with the symbol GBP, store it in the variable exchange_rate
df=pd.read_csv("exchange_rates.csv")

#print(df)

df.rename( columns={'Unamed: 0':'Pounds'}, inplace=True )
df1=df.loc[df["Pounds"] == 'GBP']
print(df1)
exchange_rate=float(df1["Rates"].values)
print(exchange_rate)

#Using exchange _rate and the excahnge_rates.csv file find the exchange rate of USD to GBP
def transform(data):
    # Write your code here
    data['Market Cap (US$ Billion)']= round(data['Market Cap (US$ Billion)']*exchange_rate,3)
#     print(data['Market Cap (US$ Billion)'])
    data=data.rename(columns={"Market Cap (US$ Billion)":"Market Cap (GBP$ Billion)"},inplace=False)
    return data
  
  #Create a function that takes a dataframe and load it to a csv named bank_market_cap__gbp.csv
  targetfile="bank_matket_cap_gbp.csv"
def load(targetfile,datatoload):
    # Write your code here
    datatoload.to_csv(targetfile, index=False)
    
    #Write a logging function to log your data
    def log(message):
    # Write your code here
    timestamp_format='%Y-%h-%d-%H%M%S'
    now=datetime.now()
    timestamp=now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp+','+message+'\n')

log("ETL Job Started")

# Call the function here
log("Extract Phase Started")
extract_data=extract()
# Print the rows here
extract_data.head(5)

log("Extract Phase Ended")

log("Transform Phase Started")

# Call the function here
transformed_data=transform(extract_data)

# Print the first 5 rows here
transformed_data.head(5)

log("Transform Phase Ended")

log("load Phase Started")

#Load the function
load(targetfile,transformed_data)

log("load Phase Ended")
    
