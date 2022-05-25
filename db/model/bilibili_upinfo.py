from peewee import *
from db.model.BaseModel import BaseModel

class bilibili_upinfo(BaseModel):
    upname = CharField()
    desc = CharField()
    poster = CharField()
    image = CharField()
    extinfo = CharField()