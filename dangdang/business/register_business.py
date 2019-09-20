#coding = utf-8
import os
path_ab = os.getcwd()
import sys
sys.path.append(path_ab)
from selenium import webdriver
from handle.register_handle import RegisterHandle
from base.base_driver import BaseDriver
import time
import unittest

class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)

    def login_input_data(self,phone,password,password_review,codetext):
        self.register_h.send_user_phone(phone)
        self.register_h.send_user_password(password)
        self.register_h.send_user_password_review(password_review)
        self.register_h.send_user_codetext(codetext)

    def login_click_button(self):
        # self.register_h.click_accept_box()
        self.register_h.click_submit_button()

    def login_judgment(self,phone,password,password_review,codetext,assertCode,assertText):
        self.login_input_data(phone,password,password_review,codetext)
        self.login_click_button()        
        get_text = self.register_h.get_element_text(assertCode)
        get_text = get_text.strip(' ')
        assertText = assertText.strip(' ')        
        return get_text,assertText   

if __name__ == "__main__":
    register_b = RegisterBusiness(BaseDriver().driver_dangdang())
    test = register_b.login_judgment("13011112222","qinaige123","qinaige123","code123","code_text_error",u"图形验证码输入错误，请重新输入")
    time.sleep(3)
    print(test)