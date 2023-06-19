
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True )
#options.add_argument("headless")
driver = webdriver.Chrome(options=options)

def ulta():
	options = webdriver.ChromeOptions()
	options.add_experimental_option("detach", True)
	options.add_argument("headless")
	driver = webdriver.Chrome(options=options)
	driver.get("https://www.ulta.com/search?search=mango+butter+")
	wait = WebDriverWait(driver, 10)
	driver.implicitly_wait(20)
	while True:
		try:
			wait.until(EC.element_to_be_clickable((By.XPATH, """//button[normalize-space()='Show More Products']    """))).click()
			time.sleep(5)
		except:
			break
	fetch = driver.find_element(By.XPATH, """/html/body/div[5]/div/div/div/div/main/div[5]/div/div/div/div/div[3]/ul""")
	links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',fetch.get_attribute("innerHTML"))
	product_links = []
	for link in links :
		if '/p/' in link:
			product_links.append(link)
	products =[]
	for link in product_links:

		driver.implicitly_wait(10)
		driver.get(link)


		webdriver.support.expected_conditions.visibility_of( """//summary[@id='Ingredients']//h3[@class='Accordion_Huge__summary__header']""")
		try:


			click_agian = driver.find_element(By.XPATH , """//summary[@id='Ingredients']//h3[@class='Accordion_Huge__summary__header']""")
			click_agian.click()

			ingredients = driver.find_element(By.XPATH,"""//details[@aria-controls='Ingredients']//div[@class='Accordion_Huge__content']//div[@class='Markdown Markdown--body-2']""")
			#print(ingredients.text)
			category = driver.find_element(By.XPATH , """//ul[@id='Breadcrumbs__List']""")
			brand_name = driver.find_element(By.XPATH , """//span[@class='Text-ds Text-ds--title-5 Text-ds--left']""")
			company = driver.find_element(By.XPATH , """//*[@id="92384e5c-2234-4e8f-bef7-e80391889cfc"]/h1/span[1]/a""")

			err = True
		except :
			print(link)
			err = False

		if err:
			product = [company.text,brand_name.text,category.text ,ingredients.text,link]
			products.append(product)
	fields = ['company', 'product name ', 'category' ,'ingredients', 'link']
	with open('ulta.csv', 'w') as f:

		csv_writer = csv.writer(f)
		csv_writer.writerow(fields)
		csv_writer.writerows(products)


def sephora():
	driver.get("https://www.sephora.com/search?keyword=mango%20butter")
	wait = WebDriverWait(driver, 10)
	driver.implicitly_wait(20)

	products = []
	try:
		outside_usa = driver.find_element(By.XPATH, """//button[@aria-label='Continue shopping']//*[name()='svg']""")
		outside_usa.click()
	except:
		pass

	while True:
		try:
			wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-bk5oor.eanm77i0"))).click()
			time.sleep(5)
		except:
			break

	# page = driver.find_element(By.TAG_NAME , 'a')
	elems = driver.find_elements(By.XPATH, "//a[@href]")

	links = []
	for elem in elems:

		if '/product/' in elem.get_attribute("href"):
			links.append(elem.get_attribute("href"))

	for link in links:
		driver.get(link)

		try:
			outside_usa = driver.find_element(By.XPATH,"""//button[@aria-label='Continue shopping']//*[name()='svg']""")
			outside_usa.click()
		except:
			pass
		webdriver.support.expected_conditions.visibility_of("""//button[@data-at='ingredients']""")
		try:

			click_agian = driver.find_element(By.XPATH, """//button[@data-at='ingredients']""")
			click_agian.click()

			ingredients = driver.find_element(By.XPATH, """//div[@id='ingredients']""")

			category = driver.find_element(By.XPATH, """//ol[@class='css-9w1s77 eanm77i0']""")

			brand_name = driver.find_element(By.XPATH, """//h1[@class='css-11zrkxf eanm77i0']""")

			company = driver.find_element(By.XPATH, """//h1[@class='css-11zrkxf eanm77i0']""")

			err = True
		except:
			print(link)
			err = False

		if err :
			product = [ company.text , brand_name.text ,category.text ,ingredients.text , link]
			products.append(product)

	fields = ['company', 'product name ', 'category' ,'ingredients', 'link']
	with open('sephora.csv', 'w') as f:

		# Create a CSV writer object that will write to the file 'f'
		csv_writer = csv.writer(f)

		# Write the field names (column headers) to the first row of the CSV file
		csv_writer.writerow(fields)

		# Write all of the rows of data to the CSV file
		csv_writer.writerows(products)


#ulta()

sephora()