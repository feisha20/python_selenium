import allure
import sys
import pytest
import helper

@allure.severity("minor")
@allure.feature("smoke test")
@allure.story("test a car")
@allure.issue('http://www.bug.com/bug004')
@allure.testcase("how to test a car")
def test_car():
    pass

@allure.severity("critical")
@allure.feature("smoke test")
@allure.story("test a bike")
@allure.issue('http://www.bug.com/bug005')
@allure.testcase("how to test a car")
def test_bike():
    pass

@allure.severity("blocker")
@allure.feature("smoke test")
@allure.story("test a fly")
@allure.issue('http://www.bug.com/bug006')
@allure.testcase("how to test a car")
def test_fly():
    pass


if __name__ == '__main__':
    pytest.main(helper.get_pytest_param(sys.argv[0]))