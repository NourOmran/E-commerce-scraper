from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


#//div[@data-comp='Search ']//div[@data-comp='Search ']
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.sephora.com/search?keyword=hair%20oil")
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(20)

try:
	outside_usa = driver.find_element(By.XPATH , """//button[@aria-label='Continue shopping']//*[name()='svg']""")
	outside_usa.click()
except:
	pass

while True:
	try:
		wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-bk5oor.eanm77i0"))).click()
		time.sleep(5)
	except:
		break

#page = driver.find_element(By.TAG_NAME , 'a')
elems = driver.find_elements(By.XPATH ,"//a[@href]" )


links = []
for elem in elems:

	if '/product/' in elem.get_attribute("href") :
		links.append(elem.get_attribute("href"))


for link in links:
	driver.get(link)

	try:
		outside_usa = driver.find_element(By.XPATH, """//button[@aria-label='Continue shopping']//*[name()='svg']""")
		outside_usa.click()
	except:
		pass
	webdriver.support.expected_conditions.visibility_of("""//button[@data-at='ingredients']""")
	try:

		click_agian = driver.find_element(By.XPATH,"""//button[@data-at='ingredients']""")
		click_agian.click()

		ingredients = driver.find_element(By.XPATH,"""//div[@id='ingredients']""")
		print(ingredients.text)
		#category = driver.find_element(By.XPATH, """//ul[@id='Breadcrumbs__List']""")
		brand_name = driver.find_element(By.XPATH, """//h1[@class='css-11zrkxf eanm77i0']""")
		print(brand_name.text)
		company = driver.find_element(By.XPATH, """//h1[@class='css-11zrkxf eanm77i0']""")


		err = True
	except:
		print(link)
		err = False

