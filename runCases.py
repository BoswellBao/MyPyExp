import os
import unittest
import datetime
import MyHTMLTestRunner
from cases.getTVChannal import GetTVChannal
from cases.checkQQOnline import CheckQQOnline


if __name__ == "__main__":
    # 此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(GetTVChannal)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(CheckQQOnline)
    suite = unittest.TestSuite([suite1, suite2])

    report_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S ")
    report_path = os.path.join(os.path.curdir, "result\\" + report_time + "report.html")
    fp = open(report_path, "wb")
    runner = MyHTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=4, title="自动化测试报告", description="框架搭建")
    runner.run(suite)
    fp.close()

