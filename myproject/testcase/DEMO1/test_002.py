import allure
import sys
import pytest
import helper

@allure.severity("minor")
@allure.feature("冒烟测试")
@allure.story("测试一辆小车")
@allure.issue('http://www.bug.com/bug004')
@allure.testcase("如何测试一辆小车")
def test_car():
    pass

@allure.severity("critical")
@allure.feature("冒烟测试")
@allure.story("测试一辆自行车")
@allure.issue('http://www.bug.com/bug005')
@allure.testcase("如何测试一辆自行车")
def test_bike():
    pass

@allure.severity("blocker")
@allure.feature("冒烟测试")
@allure.story("测试一架飞机")
@allure.issue('http://www.bug.com/bug006')
@allure.testcase("如何测试一架飞机")
def test_fly():
    pass


if __name__ == '__main__':
    pytest.main(helper.get_pytest_param(sys.argv[0]))