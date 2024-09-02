# Python API Automation Framework

# Tech Stack
python 3.12
requests-- http requests
Pytest--Testing Framework
Reporting-- Allure reports, PyTest HTML
Test Data-- CSV,Excel,JSON,Faker,API testing--jsonschema
Parallel Execution - x distribute (xdist)

# How to install packages
-- pip install requests pytest pytest-html faker allure pytest jsonschema

## how to run your Testcase parallely
--- pip install pytest-xdist
## how to add the .gitignore file?
--- copy the content from the website "https://www.toptal.com/developers/gitignore/api/pycharm+all"
to .gitignore file

## how to run the basic test with allure report
pytest tests/test/crud/test_create_booking.py --alluredir=allure_result -s

## for allure report we use command
allure serve allure_result

