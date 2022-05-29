from peewee import *
from db.model.BaseModel import BaseModel

class bilibili_videoimage(BaseModel):
    videoId = CharField()
    loadStatus = BooleanField()
    path = CharField()