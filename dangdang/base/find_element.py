#coding=utf-8
import os
path_ab = os.getcwd()
import sys
sys.path.append(path_ab)
from util.read_ini import ReadIni
from selenium import webdriver
import time
from base.base_driver import BaseDriver

class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
 
    def get_element(self,key):
        read_i = ReadIni()
        data = read_i.get_value(key)
        # print(data)
        element_by = data.split('>')[0]
        element_value = data.split('>')[1]

        try:
            if element_by == "id":
                return self.driver.find_element_by_id(element_value)
            elif element_by == "classname":
                return self.driver.find_element_by_class_name(element_value)
            elif element_by == "name":
                return self.driver.find_element_by_name(element_value)
            elif element_by == "xpath":
                return self.driver.find_element_by_xpath(element_value)
        except Exception as msg:
            print(msg)
            return None

if __name__ == "__main__":
    find_e = FindElement(BaseDriver().driver_dangdang())
    find_e.get_element("phone").send_keys("13066998855")
    find_e.get_element("password").send_keys("13066998855")
    find_e.get_element("code_text").send_keys("code")
    time.sleep(3)    