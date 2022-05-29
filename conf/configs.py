
import os
import yaml

class config:
    db = ""
    host = ""
    port = ""
    user = ""
    password = ""
    saveImagePath = ""

    def __init__(self):
        # 如果项目外有配置文件则加载项目外的文件，方便测试
        if (os.path.exists("../conf.yaml")):
            file = open("../conf.yaml",'r')
        else:
            file =open("conf.yaml", 'r')
        configs = yaml.load(file, Loader=yaml.FullLoader)
        self.db = configs['DataBase']['db']
        self.host = configs['DataBase']['host']
        self.port = configs['DataBase']['port']
        self.user = configs['DataBase']['user']
        self.password = configs['DataBase']['password']
        self.saveImagePath = configs['Image']['path']


# if __name__ == "__main__":
#     config = config()