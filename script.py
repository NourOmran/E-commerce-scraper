from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import csv


def ulta1(url, page):
	options = webdriver.ChromeOptions()
	options.add_experimental_option("detach", True)
	options.add_argument("headless")

	driver = webdriver.Chrome(options=options)
	driver.get(url)
	wait = WebDriverWait(driver, 10)
	driver.implicitly_wait(20)
	fetch = driver.find_element(By.XPATH, """/html/body/div[5]/div/div/div/div/main/div[5]/div/div/div/div/div[3]/ul""")
	links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
	                   fetch.get_attribute("innerHTML"))
	product_links = []
	for link in links:
		if '/p/' in link:
			product_links.append(link)
	products = []
	print("Fetching the products may take time , please wait .")
	for link in product_links:

		driver.implicitly_wait(10)
		driver.get(link)
		webdriver.support.expected_conditions.visibility_of(
			"""//summary[@id='Ingredients']//h3[@class='Accordion_Huge__summary__header']""")
		try:
			click_agian = driver.find_element(By.XPATH,
			                                  """//summary[@id='Ingredients']//h3[@class='Accordion_Huge__summary__header']""")
			click_agian.click()
			ingredients = driver.find_element(By.XPATH,
			                                  """//details[@aria-controls='Ingredients']//div[@class='Accordion_Huge__content']//div[@class='Markdown Markdown--body-2']""")
			category = driver.find_element(By.XPATH, """//ul[@id='Breadcrumbs__List']""")

			brand_name = driver.find_element(By.XPATH, """//span[@class='Text-ds Text-ds--title-5 Text-ds--left']""")
			reviews = driver.find_element(By.CSS_SELECTOR,
			                              "div[class='ReviewStars__Content'] span[class='Text-ds Text-ds--body-3 Text-ds--left']")

			company = driver.find_element(By.XPATH, """//*[@id="92384e5c-2234-4e8f-bef7-e80391889cfc"]/h1/span[1]/a""")

			try:

				numbers_of_reviews = driver.find_element(By.CSS_SELECTOR, ".pr-rd-review-total.pr-h1")
				num, _ = numbers_of_reviews.text.split()
			except:
				num = '0'

			err = True
		except:
			print(f"This product does not have ingredients {link}")
			err = False

		if err:
			product = [company.text, brand_name.text, category.text, ingredients.text, link, num, reviews.text]
			products.append(product)
	fields = ['company', 'product name ', 'category', 'ingredients', 'link', 'total number of reviews', 'product rate ']
	with open(f'beeswax_{page}.csv', 'w') as f:

		csv_writer = csv.writer(f)
		csv_writer.writerow(fields)
		csv_writer.writerows(products)



if __name__ == "__main__":

	for page in range(1,60):
		ulta1(f'https://www.ulta.com/search?search=beeswax&page={page}',page)

