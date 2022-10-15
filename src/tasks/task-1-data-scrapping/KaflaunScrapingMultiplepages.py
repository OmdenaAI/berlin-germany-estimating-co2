from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import warnings
import pprint
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
import urllib.request
import json
from PIL import Image
# from IPython.display import Image
#from transformers import MarianMTModel, MarianTokenizer

basic_link = 'https://www.kaufland.de/lebensmittel/'

warnings.simplefilter('ignore')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get(basic_link)

cat = driver.find_elements(By.CLASS_NAME,"rd-category-tree__list-item")

links = []
clickable_element = driver.find_element(By.CLASS_NAME,"rd-category-tree__toggle-more-btn")
driver.execute_script("arguments[0].click()", clickable_element)
for i in cat:

    try:
        links.append((i.text, i.find_element(By.TAG_NAME,'a').get_attribute("href")))
    except:
        pass

print(links)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

new_links = []

for link in links:
    super_cat = link[0]
    l = link[1]
    driver.get(l)

    # click on "mehr anzeigen"
    try:
        tree_element = driver.find_element(By.CLASS_NAME,"rd-category-tree__toggle-more-btn")
        driver.execute_script("arguments[0].click()", tree_element)
    except:
        pass

    # scrapp all the elements on the left hand side
    cat = driver.find_elements(By.CLASS_NAME,"rd-category-tree__list-item")

    for i in cat:
        try:
            new_links.append((super_cat, i.text, i.find_element(By.TAG_NAME,'a').get_attribute("href")))
        except:
            pass

print(new_links)

product_list = []
image_list = []
for new_link in new_links:
    product_category = new_link[0]
    product_subcategory = new_link[1]
    product_link = new_link[2]
    driver.get(product_link)
    pages_int = 0
    try:
        pages = driver.find_element(By.XPATH,'//button[contains(@aria-label, "Weiter")]/preceding-sibling::button[1]')
        pages_int = int(pages.get_attribute("innerText"))
        print(pages_int)
    except:
        pass
    try:
        for j in range(pages_int):
            print("We are in Page", j)
            product_description = driver.find_elements(By.TAG_NAME, 'article')
            for product in product_description:
                image = product.find_element(By.TAG_NAME,'img').get_attribute("src")
                title = product.find_element(By.CLASS_NAME,"product__title")
                product_list.append( title.get_attribute("innerText"))
                image_list.append(image)
            buttons = driver.find_element(By.XPATH, '//button[@aria-label="Weiter"]')
            if buttons:
                driver.execute_script("arguments[0].click()", buttons)
    except:
        pass

for i in range(len(image_list)):
    try:
        urllib.request.urlretrieve(str(image_list[i]),"F:\ScrapedImagesNew\product_image{}.jpg".format(i))
    except:
        pass
    # image_reader = Image.open("product_image{}.jpg".format(i))
    # image_reader.show()
driver.close()
df = pd.DataFrame(product_list, columns=["product_title"])
print(df)
df.to_csv("ScrappingList.csv")
# #model_name = 'Helsinki-NLP/opus-mt-de-en'
#model = MarianMTModel.from_pretrained(model_name)
#translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
#[tokenizer.decode(t, skip_special_tokens=True) for t in translated]