from peewee import *
from db.model.BaseModel import BaseModel

class bilibili_videoinfo(BaseModel):
    title = CharField()
    visit = CharField()
    barrage = CharField()
    up_id = CharField()
    url = CharField()
    space = CharField()



