

Requirements:

- Documentation exists (also includes information about how to execute)
- Test scenarios choice is good (also covers acceptance criteria)
- Code is clean, readable
- Test assets are well structured (low maintenance cost, easy to extend)
  - Page object pattern for Selenium tests for example
- Results make debugging easy

**User story 1 (register e-shop user)**

_Testable web page:_[http://automationpractice.com/index.php](http://automationpractice.com/index.php)

As new e-shop customer, I would like to register myself as user. In registration process I would also like to know what fields are required and get feedback if I don&#39;t fill those correctly.

Acceptance criteria (choose min 4 to cover):

1. Do I see appropriate error message if I enter e-mail or phone number in incorrect format?
2. Do I see appropriate error message if I enter password or ZIP code that doesn&#39;t meet length requirements?
3. Do I see appropriate error message if mandatory fields (first name, last name, password, e-mail, address, city, state, ZIP code, country, atleast one phone number, address alias) are not filled?
4. Are e-mail and address alias field pre-filled for me?
5. Can I fill in all possible fields, including non-mandatory?
6. If registration succeeds, am I automatically logged in?
7. If registration succeeds, can I then log out and log back in with my user?

_User story should be covered with automated tests using Selenium in any programming language._

**User story 2 (Star Wars people query)**

_Testable REST API documentation:_[https://swapi.co/documentation](https://swapi.co/documentation) (resource: GET /people)

As Star Wars fan, I would like to have web service from which I could query Star Wars people data, so that I could show the data in my web application.

Acceptance criteria (choose min 4 to cover):

1. Can I query individual Star Wars character information?
2. Do I get appropriate error as response when trying to update character information? (PUT)
3. Do I get appropriate error as response when trying to insert new character information? (POST)
4. Can I query multiple Star Wars characters (by page)?
5. Are there no duplicate entries returned?
6. Do I see count of characters and links to next and previous page when querying by page?
7. Do I get appropriate error as response when trying to query by page which doesn&#39;t exist?

_User story should be covered with automated tests in any programming language._
