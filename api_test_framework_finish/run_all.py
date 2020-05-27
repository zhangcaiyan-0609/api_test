# coding=utf-8
import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.send_email import send_email

logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover(test_path)

with open(report_file, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="zhangcaiyan").run(suite)
if send_email_after_run:
    send_email(report_file)  # 从配文件中读取
logging.info("================================== 测试结束 ==================================")
