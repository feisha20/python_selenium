import allure
import sys
import pytest
import helper


@allure.severity("minor")
@allure.feature("冒烟测试")
@allure.story("测试一只狗")
@allure.issue('http://www.bug.com/bug001')
@allure.testcase("如何测试一只狗")
@pytest.allure.step("摸一下狗头")
def test_dog():
    print("一只黄金猎犬")
    pass


@allure.severity("minor")
@allure.feature("冒烟测试")
@allure.story("测试一只猫")
@allure.issue('http://www.bug.com/bug002')
@allure.testcase("如何测试一只猫")
def test_cat():
    pass


@allure.severity("minor")
@allure.feature("冒烟测试")
@allure.story("测试一只猴子")
@allure.issue('http://www.bug.com/bug003')
@allure.testcase("如何测试一只猴子")
def test_monkey():
    pass


@allure.severity("minor")
@allure.feature("冒烟测试")
@allure.story("测试一条鱼")
@allure.issue('http://www.bug.com/bug004')
@allure.testcase("如何测试一条鱼")
def test_fish():
    pass


if __name__ == '__main__':
    pytest.main(helper.get_pytest_param(sys.argv[0]))
