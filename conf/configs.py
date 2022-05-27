
import os
import yaml

class config:
    db = ""
    host = ""
    port = ""
    user = ""
    password = ""

    def __init__(self):
        # 如果项目外有配置文件则加载项目外的文件，方便测试
        if (os.path.exists("../../conf.yml")):
            file = os.path.join("../../conf.yml")
        else:
            file = "../conf.yml"
        configs = yaml.load(file, Loader=yaml.FullLoader)
        self.db = configs['DataBase']['db']
        self.host = configs['DataBase']['host']
        self.port = configs['DataBase']['port']
        self.user = configs['DataBase']['user']
        self.password = configs['DataBase']['password']
