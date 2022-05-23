from db.model.bilibili_videoinfo import *
from db.model.bilibili_videolog import *
import uuid
import datetime


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
