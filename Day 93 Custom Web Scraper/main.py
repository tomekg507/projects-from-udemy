from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pandas as pd

#-----------CREATING CSV -----------_
# df = pd.DataFrame(columns=['name', 'portion size', 'calories', 'fat', 'carbo', 'protein'])
# df.to_csv('./nutrition_data.csv', index=False)

#-------------- WEB SCRAPPING ------------
URL = 'https://www.nutritionvalue.org/'
product = input('Name of the product: ')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', False)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

search_button = driver.find_elements(By.TAG_NAME, value='a')[1]
search_button.click()

search_entry = driver.find_element(By.ID, value='search-box')
search_entry.click()
search_entry.send_keys(product, Keys.ENTER)

most_common_product = driver.find_element(By.CLASS_NAME, value='table_item_name')
driver.get(most_common_product.get_attribute('href'))

# Had to scroll down to read all objects...
driver.execute_script("window.scrollTo(0, 300);")

table = driver.find_element(By.ID, value="nutrition-label").text.split('\n')
print(table)
portion_size = [item for item in table if item.startswith('Portion')][0].split(' ')[2]
calories = [item for item in table if item.startswith('Amount')][0].split(' ')[3]
total_fat = [item for item in table if item.startswith('Total Fat')][0].split(' ')[2]
total_carbo = [item for item in table if item.startswith('Total Carbo')][0].split(' ')[2]
total_protein = [item for item in table if item.startswith('Protein')][0].split(' ')[1]

# writing to csv
df = pd.DataFrame({'name': [product], 'portion size': [f'{portion_size}g'],
                   'calories': [f'{calories}kcal'], 'fat': [total_fat], 'carbo': [total_carbo], 'protein': [total_protein]})
# with open('nutrition_data.csv', mode='a', newline='') as nutrition_data:
df.reindex().to_csv('nutrition_data.csv', mode='a', header=False, index=False)
