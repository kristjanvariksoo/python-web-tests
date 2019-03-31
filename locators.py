from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here."""

    GO_BUTTON = (By.ID, 'submit')


class LoginPageLocators(object):
    """A class for login page locators."""

    EMAIL = (By.ID, 'email_create')
    CREATE_BUTTON = (By.ID, 'SubmitCreate')
    ACCOUNT_CREATE_ERROR = (By.ID, 'create_account_error')
    ACCOUNT_CREATION_FORM = (By.ID, 'account-creation_form')


class RegistrationPageLocators(object):
    """A class for registration page locators."""

    ERRORS = (By.CLASS_NAME, 'alert alert-danger')
    FIRST_NAME = (By.ID, 'customer_firstname')
    REGISTER_BUTTON = (By.ID, 'submitAccount')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here."""

    pass
