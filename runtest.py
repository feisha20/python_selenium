#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
import helper


# 设置启动的浏览器
def select_run_browser():
    """选择要启动的浏览器"""
    items = {"1", "2", "3"}
    select = input("<第一步：请选择要启动的浏览器(不输入默认chrome)：1:Chrome  2:Firefox  3.IE）>\n->请输入序号：")
    if select in items:
        select = int(select)
        if select == 1:
            print("您选择了启动Chrome浏览器")
            helper.set_run_browser()
        elif select == 2:
            print("您选择了启动Firefox浏览器")
            helper.set_run_browser("Firefox")
        elif select == 3:
            print("您选择了启动IE浏览器")
            helper.set_run_browser("IE")
        else:
            print("您输入的序号不在选择范围内，自动默认选择Chrome")
            helper.set_run_browser()
    else:
        print("自动默认选择Chrome")
        helper.set_run_browser()


# 获取指定路径的用例集合
def run_test(test_case_path ="\\testcase", file_front="test_"):
    """根据指定的路径和文件前缀收集测试用例"""
    test_case_path = input(
        "<第二步：选择要执行的用例的文件路径；输入路径：\\testcase"
        "\ ; 多个路径写法：\\testcase\DEMO1;\\testcase\DEMO2 >\n->输入用例路径：")
    file_front = input("<第三步：选择要执行的用例的文件名前缀；比如：test_  或者 test_aa_  >\n->输入要执行的用例的前缀：")
    folderPath = sys.path[0]
    suiteName = os.path.realpath(sys.argv[0]).replace(folderPath, "")[1:-3]
    batPath = folderPath + "\\" + suiteName + ".bat"
    outputFile = open(batPath, "w")
    outputFile.truncate()
    list = os.listdir(sys.path[0])
    outputFile.write("py.test ")
    path_input1 = test_case_path.split(";")
    path_num = len(path_input1)
    for i in range(0, path_num):
        test_case_path = folderPath + "\\myproject" + path_input1[i]
        g = os.walk(test_case_path)

        fileName = None
        folderName = None

        for path, d, filelist in g:
            for filePath in filelist:
                if filePath.endswith(".py") and filePath.startswith(file_front) and not filePath.__contains__(
                        "__init__") and not filePath.__contains__("Suite"):
                    outputFile.write(os.path.join(path, filePath).replace(os.getcwd(), ".").replace("\\", "/") + " ")
    # driver_path = helper.get_chromedriver_path().replace(folderPath, ".").replace("\\", "/")
    outputFile.write("--alluredir ./report")
    # outputFile.write("--driver Chrome --driver-path " + driver_path)
    outputFile.close()


# 收集测试用例集
select_run_browser()
run_test()
