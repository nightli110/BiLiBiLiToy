from peewee import *
from db.model.BaseModel import BaseModel

class bilibili_videolog(BaseModel):
    id = CharField()
    title = CharField()
    date = DateTimeField()
    videoid = CharField()
    visit = CharField()
    barrage = CharField()
    rank = CharField()
    daydate = CharField()

