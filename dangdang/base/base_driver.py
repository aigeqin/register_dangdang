from selenium import webdriver

class BaseDriver(object):
    def __init__(self):
        pass
    def driver_dangdang(self):
        driver = webdriver.Chrome()
        driver.get("https://login.dangdang.com/register.php?returnurl=http://myhome.dangdang.com/myOrder")
        return driver

