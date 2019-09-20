#coding = utf-8

import os
path_ab = os.getcwd()
import sys
sys.path.append(path_ab)
import unittest
import ddt
import os
import HTMLTestRunner
from business.register_business import RegisterBusiness
from base.base_driver import BaseDriver
import time
from util.read_excel import ReadExcel

case_data_excel = ReadExcel()
case_data = case_data_excel.get_part_data()
# print(data)
@ddt.ddt
class DangdangCase(unittest.TestCase):

    def setUp(self):
        self.driver = BaseDriver().driver_dangdang()
        self.register_b = RegisterBusiness(self.driver)
    
    def tearDown(self):
        self.driver.close()
   
    @ddt.data(*case_data)
    def test_register_login(self,data):
        phone,password,password_review,codetext,assertCode,assertText = data
        just_result = self.register_b.login_judgment(phone,password,password_review,codetext,assertCode,assertText)
        self.assertEqual(just_result[0],just_result[1],"case执行出错，未检测到相应的error信息")
        # time.sleep(2)

if __name__ == "__main__":
    path_file = path_ab+r"\report\dangdang_case.html"
    f = open(path_file,"wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(DangdangCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="当当网测试报告",description="这是当当网注册页面的测试报告",verbosity=2)
    runner.run(suite)
    time.sleep(2)
    
