# -*- coding:UTF-8 -*-
import baiduPage
import helper
import pytest
import sys
import allure

@pytest.fixture(scope="module")
@allure.step("打开百度首页")
def setup_module():
   helper.open_url("http://www.baidu.com")

@allure.story("测试百度搜索功能")
@allure.step("输入关键字搜索")
def test_search(setup_module):
    baiduPage.search("selenium")

if __name__ == '__main__':
    pytest.main(helper.get_pytest_param(sys.argv[0]))
