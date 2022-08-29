from bs4 import BeautifulSoup
import requests
import pandas as pd
from lxml import etree
def load_currencies_list():
    url = 'https://justforex.com/education/currencies'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.find('table',{'id':"js-table-currencies"})
    headers = []

    for i in table.find_all('th'):
        title = i.text.strip()
        headers.append(title)

    df = pd.DataFrame(columns=headers)

    for row in table.find_all('tr')[1:]:
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        length = len(df)
        df.loc[length] = row_data
    return df

