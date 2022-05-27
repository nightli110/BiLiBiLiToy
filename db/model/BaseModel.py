from peewee import *
from conf.configs import config

config = config()
db = MySQLDatabase(
    config.db, host=config.host, port=config.port, user=config.user, passwd=config.password
)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db
