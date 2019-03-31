import unittest
from selenium import webdriver
import page
from time import sleep


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works."""

    def setUp(self):
        """Set up the webdriver for work."""
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """
        Tests python.org search feature.

        Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """
        # Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        # Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        # Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        """Stop the webdriver."""
        self.driver.close()


class MyStore(unittest.TestCase):
    """Test class for MyStore using page objects."""

    def setUp(self):
        """Set up the webdriver for work."""
        self.driver = webdriver.Firefox()

    def get_full_form(self):
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

        # Go to the full form like a user would
        login_page = page.LoginPage(self.driver)
        login_page.email_create_text_element = "malle.maasikas@gmail.com"
        login_page.click_create_account()
        errors = login_page.get_errors()
        assert len(errors) == 0

    def test_login_email_validity_check(self):
        """Tests mystore email validity check on login page. Checks if a email address that does not match syntax of *@*.* is allowed to pass."""

        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

        # Load the login page for MyStore
        login_page = page.LoginPage(self.driver)

        # INVALID
        login_page.email_create_text_element = "test"
        login_page.click_create_account()
        errors = login_page.get_errors()
        assert not login_page.is_valid_email(errors)

        # VALID
        login_page.email_create_text_element = "malle.maasikas@gmail.com"
        login_page.click_create_account()
        errors = login_page.get_errors()
        assert login_page.is_valid_email(errors)

    def test_email_validity_check(self):
        """Tests the email validity check on the full form. Checks if it matches *@*.* ."""
        self.get_full_form()

        full_page = page.RegistrationPage(self.driver)

        # INVALID
        full_page.email_text_element = "test"
        full_page.click_register()
        errors = full_page.get_errors()
        assert not full_page.is_valid_email(errors)

        # VALID
        full_page.email_text_element = "malle.maasikas@gmail.com"
        full_page.click_register()
        errors = full_page.get_errors()
        assert full_page.is_valid_email(errors)

    def test_phone_number_validity_check(self):
        """Tests mystore phone number validity check. Checks if a phone number contains something other than numbers and (, ) and +."""
        self.get_full_form()

        full_page = page.RegistrationPage(self.driver)

        # INVALID MOB NR
        full_page.mob_nr = "jkjkjkjk"
        full_page.click_register()
        errors = full_page.get_errors()
        assert not full_page.is_valid_mob_nr(errors)

        # VALID MOB NR
        full_page.mob_nr = "+(29)9128821"
        full_page.click_register()
        errors = full_page.get_errors()
        assert full_page.is_valid_mob_nr(errors)

    def test_pwd_length_check(self):
        """Tests mystore pwd length check. Checks if the pwd is atleast 5 charachters long."""
        self.get_full_form()
        full_page = page.RegistrationPage(self.driver)

        # INVALID
        full_page.pwd = "1234"
        full_page.click_register()
        errors = full_page.get_errors()
        assert not full_page.is_valid_pwd(errors)

        # VALID
        full_page.pwd = "12345"
        full_page.click_register()
        errors = full_page.get_errors()
        assert full_page.is_valid_pwd(errors)


    def test_zip_length_check(self):
        """Tests mystore zip code length check. Checks if the zip code is 5 numbers long."""
        self.get_full_form()
        full_page = page.RegistrationPage(self.driver)

        # INVALID
        full_page.zip = "1234"
        full_page.click_register()
        errors = full_page.get_errors()
        assert not full_page.is_valid_zip(errors)

        # VALID
        full_page.zip = "12345"
        full_page.click_register()
        errors = full_page.get_errors()
        assert full_page.is_valid_zip(errors)


    def test_mandatory_fields_check(self):
        """Tests mystore mandatory field check. Checks if mandatory fields show error, when form is submited with them empty."""
        self.get_full_form()

        full_page = page.RegistrationPage(self.driver)
        full_page.email_text_element = ""
        full_page.alias = ""
        full_page.click_register()
        errors = full_page.get_errors()
        for possible_error in ["firstname is required.", "lastname is required.", "passwd is required.", "email is required.", "address1 is required.", "city is required.", "This country requires you to choose a State.", "The Zip/Postal code you've entered is invalid. It must follow this format: 00000", "You must register at least one phone number.", "alias is required."]:
            assert possible_error in errors, "'" + possible_error + "' - should be displayed, but isn't when submitting an empty form."

    def test_field_prefill(self):
        """Tests mystore field prefilledness. Checks if alias and email fields are prefilled for the user."""
        self.get_full_form()

        full_page = page.RegistrationPage(self.driver)
        assert full_page.email_text_element != "", "The email field was not prefilled, but should have been."
        assert full_page.alias != "", "The alias field was not prefilled, but should have been."

    def tearDown(self):
        """Stop the webdriver."""
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
