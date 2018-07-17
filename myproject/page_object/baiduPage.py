# -*- coding:UTF-8 -*-
import helper
import oper

tb_keyword = "x, //*[@id='kw']"
btn_submit = "x, //*[@id='su']"
lk_news = "x, //*[@id='u_sp']/a[1]"
lk_map = "x, //a[contains(text(),'地图')]"


def gotoBaiduHomePage(url=None):
    helper.open_url(url)

def search(keyword):
    oper.type(tb_keyword, keyword)
    oper.click(btn_submit)

def gotoNewsPage():
    oper.click(lk_news)