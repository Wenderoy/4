from bs4 import BeautifulSoup
import requests


def cbr_data():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    res = requests.get(
        f'https://miningmoon.ru/kursy-kriptovalyut',
        headers=headers
    )
    
    soup = BeautifulSoup(res.text, 'html.parser')
    
    table = soup.find('table')
    table_rows = table.find_all('tr')


    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        print(row)

    
    # tb = soup.findAll('table', attrs={'class':'value td-w-4 _bold _end mono-num'})

    # for table in soup.find_all ('table'):
    #     uan = table[0]
    # print(uan)

    # py_table = soup.find ('table', {'class':'value td-w-4 _bold _end mono-num'})
    # py_rows = py_table.find_all ('tr')
    # print(py_rows)



def cbr_check():
    data = cbr_data()