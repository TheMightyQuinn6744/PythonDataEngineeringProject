#!mamba install pandas==1.3.3 -y
#!mamba install requests==2.26.0 -y
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y

#import additional libraries
from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

#Save the contents of the webpage in text format using the requests library and assign it to the variable html_data
url = "https://en.wikipedia.org/wiki/List_of_largest_banks?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01"
html_data = requests.get(url).text
# print(html_data)

#Parse the contents of the webpage
soup= BeautifulSoup(html_data,"html.parser")
# print(soup.prettify())

#Load the data into a pandas dataframe
DataFrame = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])
# print(data)

for row in soup.find_all('tbody')[3].find_all('tr'):
    col = row.find_all('td')
    
    if (col != []):
        name = col[1].text.strip()
        market_cap = col[2].text.strip()
        DataFrame = DataFrame.append({"Name": name, "Market Cap (US$ Billion)": market_cap}, ignore_index=True)
print(DataFrame)

#Display the first five rows
DataFrame.head()
