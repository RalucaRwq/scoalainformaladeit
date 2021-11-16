from selenium import webdriver  # we need the webdriver for opening the page and parsing the info
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
# ne citim driver-ul si il instalam. inlocuieste downloadarea manuala a driver-elor
browser.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/')
# receive values from the link

table_20 = []
for i in browser.find_elements(By.XPATH, '//*[@id="post-25121"]/div/div/table[1]/tbody'):
    for td_value in browser.find_elements(By.CSS_SELECTOR, 'td'):
        table_20.append(td_value.text)

final_table = []
for i in table_20:
    if i != '43.':
        final_table.append(i)
    else:
        break

header = table_20[0:5]
dictionary = {i: [] for i in header}

for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(final_table), len(header)):
        dictionary[header[int(j)]].append(final_table[i])

print(dictionary)
df = pd.DataFrame(dictionary)
df.to_csv("MAI.xls")

time.sleep(20)
browser.close()