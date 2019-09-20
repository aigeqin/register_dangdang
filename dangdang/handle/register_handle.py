#coding = utf-8

import os
path_ab = os.getcwd()
import sys
sys.path.append(path_ab)
from selenium import webdriver
from page.register_page import RegisterPage
from base.base_driver import BaseDriver
import time

class RegisterHandle(object):
    def __init__(self,driver):
        self.register_p = RegisterPage(driver)

    def send_user_phone(self,phone):
        self.register_p.get_phone_element().send_keys(phone)

    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)

    def send_user_password_review(self,password_review):
        self.register_p.get_password_review_element().send_keys(password_review)
    
    def send_user_codetext(self,codetext):
        self.register_p.get_code_text_element().send_keys(codetext)

    def click_accept_box(self):
        self.register_p.get_accept_check_box_element().click()
    
    def click_submit_button(self):
        self.register_p.get_submit_button_element().click()

    def get_element_text(self,info):
        try:
            if info == "name_error":
                text_error = self.register_p.get_name_error_element().text
            elif info == "password_error":
                text_error = self.register_p.get_password_error_element().text
            elif info == "password_review_error":
                text_error = self.register_p.get_password_review_error_element().text
            elif info == "code_text_error":
                text_error = self.register_p.get_code_text_error_element().text
            elif info == "phone_error":
                text_error = self.register_p.get_phone_error_element().text
            elif info == "password_complexity1":
                text_error = self.register_p.get_password_complexity1_element().text
            elif info == "password_complexity2":
                text_error = self.register_p.get_password_complexity2_element().text
            elif info == "password_complexity3":
                text_error = self.register_p.get_password_complexity3_element().text
            else:
                text_error = "找不到该定位元素"
        except Exception as msg:
            print(msg)
            text_error = "输入框鉴定出错"
        return text_error

    def get_element_submit_text(self,text = None):
        text_submit = self.register_p.get_submit_button_element().text
        return text_submit

if __name__ == "__main__":
    register_h = RegisterHandle(BaseDriver().driver_dangdang())
    register_h.send_user_phone("13655448899")
    time.sleep(1)
    register_h.send_user_codetext("send")
    text = register_h.get_element_text("code_text_error")
    print(text)
    time.sleep(3)
    register_h.click_accept_box()
    register_h.click_submit_button()
    time.sleep(2)
    
    

