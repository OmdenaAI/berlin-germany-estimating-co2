# from bs4 import BeautifulSoup
# import requests
# import csv

# source = requests.get('https://ig.ft.com/carbon-food-labelling/').text
# soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

#from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd

# service = ChromeService(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

url = 'https://ig.ft.com/carbon-food-labelling/'
service = Service(executable_path=r'C:/Users/fjf3rl/Downloads/chromedriver_win32/chromedriver.exe')
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=chrome_options)
#driver = webdriver.Chrome()
driver.get(url)


overlays = driver.find_element(By.XPATH , '//*[@id="root"]/main/article/div[2]/div[1]/div[2]/main/div[1]/div/div/div[2]/div[6]/div[1]')
buttons = overlays.find_elements(By.TAG_NAME , 'button')
dict_food_items = {'item':[],
                'CO2_per_kg':[],
                'CO2_level':[]}

for button in buttons:
    print(button.text)
    if button.text != "":
        dict_food_items['item'].append(button.text)
for button in buttons:
    driver.execute_script("arguments[0].click();", button)
    right_value = driver.find_element(By.XPATH, '//*[@id="root"]/main/article/div[2]/div[1]/div[2]/main/div[1]/div/div/div[1]/div[2]/div[1]/div[4]')
    co2_value = right_value.find_element(By.XPATH,'//*[@id="root"]/main/article/div[2]/div[1]/div[2]/main/div[1]/div/div/div[1]/div[2]/div[1]/div[4]/div[2]/div').text
    co2_level = right_value.find_element(By.XPATH,'//*[@id="root"]/main/article/div[2]/div[1]/div[2]/main/div[1]/div/div/div[1]/div[2]/div[1]/div[4]/div[1]').text
    dict_food_items['CO2_per_kg'].append(co2_value)
    dict_food_items['CO2_level'].append(co2_level)
    # print(button.text)
    # print(co2_value)
    # print(co2_level)

df = pd.DataFrame(dict_food_items)
df.to_csv('data.csv')