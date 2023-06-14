
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True )
driver = webdriver.Chrome(options=options)

def ulta():
	driver.get("https://www.ulta.com/search?search=mango+butter+")
	wait = WebDriverWait(driver, 10)
	driver.implicitly_wait(20)
	while True:
		try:
			wait.until(EC.element_to_be_clickable((By.XPATH, """//button[normalize-space()='Load More']"""))).click()
			time.sleep(5)
		except:
			break
	fetch = driver.find_element(By.XPATH, """/html/body/div[5]/div/div/div/div/main/div[5]/div/div/div/div/div[3]/ul""")
	links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',fetch.get_attribute("innerHTML"))
	product_links = []
	for link in links :
		if '/p/' in link:
			product_links.append(link)

	for link in product_links:
		print(link)
		driver.implicitly_wait(10)
		driver.get(link)


		webdriver.support.expected_conditions.visibility_of( """//summary[@id='Ingredients']//h3[@class='Accordion_Huge__summary__header']""")
		try:
			ingredients = driver.find_element(By.XPATH,"""/html[1]/body[1]/div[5]/div[1]/div[1]/div[1]/div[1]/main[1]/div[3]/div[1]/div[9]/div[1]/div[1]/details[3]/div[1]/div[1]/p[1]""")
			category = driver.find_element(By.XPATH , """//ul[@id='Breadcrumbs__List']""")
			brand_name = driver.find_element(By.XPATH , """//span[@class='Text-ds Text-ds--title-5 Text-ds--left']""")
		except :
			print("error")

		print("--" * 30 )
		print(ingredients.text)
		#print(category.text)
		#print(brand_name.text)

def target():
	pass

		#content = driver.page_source
		#print(content)
#driver.get("https://www.sephora.com/search?keyword=mango%20butter")
#pop= driver.find_element(By.XPATH, """//*[@id="modal0Dialog"]/button""")
#pop.click()

#driver.get("https://www.target.com/s?searchTerm=mango+butter+")
#search = driver.find_element(By.XPATH, """//*[@id="site_search_input"]""")

#search.send_keys("mango")


ulta()