#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import sys
import os
import pytest
import selenium

project_folder = os.getcwd()[0:os.getcwd().find("pytest_selenium")]
sys.path.append(project_folder+"pytest_selenium")
sys.path.append(project_folder+"pytest_selenium\\se")
sys.path.append(project_folder+"pytest_selenium\\myproject\\page_object")
sys.path.append(project_folder+"pytest_selenium\\myproject")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    summary = []
    extra = getattr(report, 'extra', [])
    if report.when == 'call' and not report.passed:
        try:
            screenshot = selenium.webdriver.Chrome().get_screenshot_as_base64()
        except Exception as e:
            summary.append('WARNING: Failed to gather screenshot: {0}'.format(e))
            return
        if pytest_html is not None:
            # add screenshot to the html report
            extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))