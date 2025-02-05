import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://bharatpurmun.gov.np/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')
data = []

if table:
    rows = table.find_all('tr')

    for row in rows:
        rowdata = []
        values = row.find_all('td')
        for value in values:
            rowdata.append(value.text.lstrip().rstrip())

        if rowdata:
            data.append(rowdata)

    dataset = pd.DataFrame(data)
    dataset.to_csv('contact_details.csv')
else:
    print("Table not found. XD!")