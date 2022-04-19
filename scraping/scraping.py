# bs approach
from bs4 import BeautifulSoup
import requests
import pandas as pd

for j in range(20, 28):
    r = requests.get(
        f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{j}-ianuarie-ora-13-00/")
    link = BeautifulSoup(r.text, "html.parser")
    div = link.find_all('div', attrs={'class': 'entry-content'})

    table_data = []
    for i in div:
        for table in i.find_all('table'):
            for tbody in table.find_all('tbody'):
                for tr_index in tbody.find_all('tr'):
                    for td_index in tr_index.find_all('td'):
                        table_data.append(td_index.get_text())
    print(table_data)

    result = pd.DataFrame({"CoronaData": table_data})
    result.to_csv(f"cazuri{j}.csv")

# pandas approach
# import pandas as pd

# url = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/'
# #for count in range(20, 27):
#     #print(f"{url}/={count}={count+1}")
# df_list = pd.read_html(url)[0]
# df_list=df_list[[0,1,2]]
# x=len(df_list)
# print(x)
# print(df_list)
# rezult=pd.DataFrame({"CoronaData": [df_list]})
# rezult.to_csv('cazuri.csv')
