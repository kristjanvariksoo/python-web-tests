from element import BasePageElement
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator."""
    locator = 'q'


class EmailCreateTextElement(BasePageElement):
    locator = 'email_create'


class FirstNameTextElement(BasePageElement):
    locator = 'customer_firstname'


class LastNameTextElement(BasePageElement):
    locator = 'customer_lastname'


class EmailTextElement(BasePageElement):
    locator = 'email'


class PasswordTextElement(BasePageElement):
    locator = 'passwd'


class AddressFirstNameTextElement(BasePageElement):
    locator = 'firstname'


class AddressLastNameTextElement(BasePageElement):
    locator = 'lastname'


class AddressTextElement(BasePageElement):
    locator = 'address1'


class CityTextElement(BasePageElement):
    locator = 'address1'


class StateSelectElement(BasePageElement):
    locator = 'id_state'


class ZipTextElement(BasePageElement):
    locator = 'postcode'


class CountrySelectElement(BasePageElement):
    locator = 'id_country'


class MobileNrTextElement(BasePageElement):
    locator = 'phone_mobile'


class AliasTextElement(BasePageElement):
    locator = 'alias'



class BasePage(object):
    """Base class to initialize the base page that will be called from all pages."""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org."""

    # Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verify that the hardcoded text "Python" appears in page title."""
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search."""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultsPage(BasePage):
    """Search results page action methods come here."""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source


class RegistrationPage(BasePage):
    """The full registration page with all the fields."""
    email_text_element = EmailTextElement()
    firstname = FirstNameTextElement()
    lastname = LastNameTextElement()
    email = EmailTextElement()
    pwd = PasswordTextElement()
    address_firstname = AddressFirstNameTextElement()
    address_lastname = AddressLastNameTextElement()
    address = AddressTextElement()
    city = CityTextElement()
    state = StateSelectElement()
    zip = ZipTextElement()
    country = CountrySelectElement()
    mob_nr = MobileNrTextElement()
    alias = AliasTextElement()

    def get_errors(self):
        """Get list of errors with current form."""
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger'))
            )
        except TimeoutException:
            print ("No errors found.")
            return []
        else:
            li_elements = element.find_elements_by_tag_name("ol")[0].find_elements_by_tag_name("li")
            errors = [str(elem.text) for elem in li_elements]
            return errors

    def is_valid_mob_nr(self, errors):
        return 'phone_mobile is invalid.' not in errors

    def is_valid_email(self, errors):
        return 'email is invalid.' not in errors

    def is_valid_pwd(self, errors):
        return "passwd is invalid." not in errors

    def is_valid_zip(self, errors):
        return "The Zip/Postal code you've entered is invalid. It must follow this format: 00000" not in errors

    def click_register(self):
        element = self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        element.click()

class LoginPage(BasePage):
    """The login page with just the email field for registration."""

    email_create_text_element = EmailCreateTextElement()


    def get_errors(self):
        """Get list of errors with current form."""
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(LoginPageLocators.ACCOUNT_CREATE_ERROR)
            )
        except TimeoutException:
            # We can't see the error
            try:
                element = WebDriverWait(self.driver, 2).until(
                    EC.visibility_of_element_located(LoginPageLocators.ACCOUNT_CREATION_FORM)
                )
            except TimeoutException as e:
                raise Exception("We did not see error but also didn't get sent to full registration form.") from e
            else:
                # if we can see the full form, there were no errors
                return []


        else:
            # We can see the errors
            li_elements = element.find_elements_by_tag_name("ol")[0].find_elements_by_tag_name("li")
            errors = [str(elem.text) for elem in li_elements]
            return errors

    def is_valid_email(self, errors):
        return 'Invalid email address.' not in errors



    def click_create_account(self):
        """Goes from the page with 1 input to full form"""
        element = self.driver.find_element(*LoginPageLocators.CREATE_BUTTON)
        element.click()
