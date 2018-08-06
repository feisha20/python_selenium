import allure
import sys
import pytest
import helper


@allure.severity("minor")
@allure.feature("smoke test")
@allure.story("test a dog")
@allure.issue('http://www.bug.com/bug001')
@allure.testcase("how to test a dog")
def test_dog():
    allure.environment(host="127.0.0.1", report='Allure report', browser='Chrome')
    print("this is a gold dog")
    pass


@allure.severity("minor")
@allure.feature("smoke test")
@allure.story("test a cat")
@allure.issue('http://www.bug.com/bug002')
@allure.testcase("how to test a cat2")
def test_cat():
    pass


@allure.severity("minor")
@allure.feature("smoke test")
@allure.story("test a monkey")
@allure.issue('http://www.bug.com/bug003')
@allure.testcase("how to test a monkey")
def test_monkey():
    pass


@allure.severity("minor")
@allure.feature("smoke test")
@allure.story("test a fish")
@allure.issue('http://www.bug.com/bug004')
@allure.testcase("how to test a fish")
def test_fish():
    pass


if __name__ == '__main__':
    pytest.main(helper.get_pytest_param(sys.argv[0]))
