#coding = utf-8

import os
path_ab = os.getcwd()
import sys
sys.path.append(path_ab)
from selenium import webdriver
from base.find_element import FindElement
from base.base_driver import BaseDriver

class RegisterPage(object):
    def __init__(self,driver):
        self.find_e = FindElement(driver)
    #定位输入框，按钮    
    def get_phone_element(self):
        return self.find_e.get_element("phone")

    def get_password_element(self):
        return self.find_e.get_element("password")

    def get_password_review_element(self):
        return self.find_e.get_element("password_review")

    def get_code_text_element(self):
        return self.find_e.get_element("code_text")

    def get_accept_check_box_element(self):
        return self.find_e.get_element("accept_check_box")

    def get_submit_button_element(self):
        return self.find_e.get_element("submit_button")

    #错误元素定位
    def get_name_error_element(self):
        return self.find_e.get_element("name_error")
    def get_password_error_element(self):
        return self.find_e.get_element("password_error")
    def get_password_review_error_element(self):
        return self.find_e.get_element("password_review_error")
    def get_code_text_error_element(self):
        return self.find_e.get_element("code_text_error")
    def get_phone_error_element(self):
        return self.find_e.get_element("phone_error")

    #密码安全级别
    def get_password_complexity1_element(self):
        return self.find_e.get_element("password_complexity1")
    def get_password_complexity2_element(self):
        return self.find_e.get_element("password_complexity2")
    def get_password_complexity3_element(self):
        return self.find_e.get_element("password_complexity3")
            
if __name__ == "__main__":
    register_p = RegisterPage(BaseDriver().driver_dangdang())
    register_p.get_phone_element().send_keys("13066983670")
    register_p.get_code_text_element().send_keys("130665")
