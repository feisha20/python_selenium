# -*- coding:UTF-8 -*-
import baiduPage
import helper
import pytest
import sys
import allure


@pytest.fixture(scope="module")
@allure.step("open the baidu home page")
def setup_module():
    helper.open_url("http://www.baidu.com")


@allure.story("test baidu search")
@allure.step("input the key word")
def test_search(setup_module):
    baiduPage.search("selenium")


if __name__ == '__main__':
    pytest.main(helper.get_pytest_param(sys.argv[0]))
