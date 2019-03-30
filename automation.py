from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://automationpractice.com/index.php?controller=authentication") #Let's go to the full registration form to reduce time spent loading the front page and navigating there while sacrificing robustness incase the website should change the url of the registration page.

correct_email = "malle.maasikas@gmail.com"
incorrect_email = "malle.maasikas.malle.malle"

assert "Login" in driver.title

elem = driver.find_element_by_id("email_create")
elem.clear()
elem.send_keys(incorrect_email)

driver.find_element_by_css_selector('#SubmitCreate').click()

elem = driver.find_element_by_id("customer_firstname")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
driver.close()
