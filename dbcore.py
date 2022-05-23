import datetime
from peewee import *
import uuid

db = MySQLDatabase(
    "bilibilidata_test", host="192.168.1.49", port=3306, user="root", passwd="xxxxxx"
)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class bilibili_videoinfo(BaseModel):
    title = CharField()
    visit = CharField()
    barrage = CharField()
    up_id = CharField()
    url = CharField()
    space = CharField()


class bilibili_videolog(BaseModel):
    id = CharField()
    title = CharField()
    date = DateTimeField()
    videoid = CharField()
    visit = CharField()
    barrage = CharField()
    rank = CharField()
    daydate = CharField()


def insertVideoInfo(title, visit, barrage, up_id, url, space, rank):
    if (exitVideoInfo(url)):
        bilibili_videoinfo.update(title=title, visit=visit, barrage=barrage, up_id=up_id, url=url, space=space).where(
            bilibili_videoinfo.url == url)
    else:
        bilibili_videoinfo.create(title=title, visit=visit, barrage=barrage, up_id=up_id, url=url, space=space)
    insertVideoLog(title, visit, barrage, rank, url)


def exitVideoInfo(url):
    res = bilibili_videoinfo.select().where(bilibili_videoinfo.url == url)
    num = res.count()
    #print(dist)
    if (num>0):
        return True
    else:
        return False

def insertVideoLog(title, visit, barrage, rank, url):
    id = uuid.uuid1()
    daydate = datetime.date.today()
    time = datetime.datetime.now()
    videoId = bilibili_videoinfo.select().where(bilibili_videoinfo.url == url)[0].id

    bilibili_videolog.create(id = id, title = title, date = time, videoid = videoId, visit = visit, barrage = barrage, rank = rank,daydate = daydate)



if __name__ == "__main__":
    # 创建
    bilibili_videoinfo.create(title='2', visit='2', barrage='2', up_id='2', url='2', space='2')

    bilibili_videoinfo.create(title='3', visit='2', barrage='2', up_id='2', url='2', space='2')

    bilibili_videoinfo.create(title='4', visit='2', barrage='2', up_id='2', url='2', space='2')

    bilibili_videoinfo.create(title='6', visit='2', barrage='2', up_id='2', url='2', space='2')

    # 查询
    res = bilibili_videoinfo.select().where(bilibili_videoinfo.title == '2')
    insertVideoLog(2,2,2,2,2)
    print(res[0])
    print(res[0].url)
