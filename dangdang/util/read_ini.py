#coding = utf-8
import os
path_ab = os.getcwd()
import sys
sys.path.append(path_ab)
import configparser

class ReadIni(object):
    def __init__(self,filename=None,section=None):
        if(filename == None):
            filename = path_ab+r"\config\RegisterElement.ini"
        if(section == None):
            self.section = "RegisterElement"
        else:
            self.section = section
        self.conf = self.load_ini(filename)
    
    #加载文件
    def load_ini(self,filename):
        conf = configparser.ConfigParser()
        conf.read(filename)
        return conf

    #读取文件
    def get_value(self,key):
        value = self.conf.get(self.section,key)
        return value

if __name__ == "__main__":
    read_i = ReadIni()
    text = read_i.get_value("phone")
    print(text)