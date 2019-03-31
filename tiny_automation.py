from selenium import webdriver
import page
from time import sleep

driver = webdriver.Firefox()
driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

# Load the login page for MyStore
login_page = page.LoginPage(driver)

# Go to the full form like a user would
login_page.email_create_text_element = "malle.maasikas@gmail.com"
login_page.click_create_account()
errors = login_page.get_errors()
assert len(errors) == 0

# INVALID
full_page = page.RegistrationPage(driver)
full_page.email_text_element = ""
# full_page.alias = ""
full_page.click_register()
errors = full_page.get_errors()
for possible_error in ["firstname is required.", "lastname is required.", "passwd is required.", "email is required.", "address1 is required.", "city is required.", "This country requires you to choose a State.", "The Zip/Postal code you've entered is invalid. It must follow this format: 00000", "You must register at least one phone number.", "alias is required."]:
    assert possible_error in errors, "'" + possible_error + "' - should be displayed, but isn't when submitting an empty form."

driver.close()
