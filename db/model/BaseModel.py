from peewee import *

db = MySQLDatabase(
    "bilibilitest", host="192.168.1.49", port=3306, user="root", passwd="xxxxx"
)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


