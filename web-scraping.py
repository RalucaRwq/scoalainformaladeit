from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://frsah.ro/index.php/2021/11/16/presedintele-federatiei-romane-de-sah-vlad-ardeleanu-a-participat-la-board-ul-uniunii-europene-de-sah-ecu-de-la-terme-catez-slovenia/')
table = browser.find_element(By.XPATH, '//*[@id="post-11870"]')

table_text = table.text
print(table_text)

my_list = table_text.split('\n')
my_list.append("Am adaugat si alt text.")

with open("web_scraping.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(my_list))
