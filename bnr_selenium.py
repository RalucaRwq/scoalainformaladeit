from selenium import webdriver  # we need the webdriver for opening the page and parsing the info
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm')
table = browser.find_element(By.XPATH, '//*[@id="Data_table"]')
table_text = table.text
lista = table_text.split('\n')
# print(lista)
header = browser.find_element(By.XPATH, '//*[@id="Data_table"]/table/thead/tr').text.split('\n')
# print(header.text.split('\n'))
dictionary = {i: [] for i in header}
print(dictionary) # cheia o sa fie randul pe care suntem
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionary[header[int(j)]].append(lista[i])
print(dictionary)
df = pd.DataFrame(dictionary)
df.to_csv("BNR_ALL_DATA.xls")


time.sleep(5)
browser.close()