from db.model.bilibili_videoinfo import *
from db.model.bilibili_videolog import *
from db.model.bilibili_videoimage import *
import uuid
import datetime


def insertVideoInfo(title, visit, barrage, upname,url, space, upid,rank, videoid):
    if (exitVideoInfo(url)):
        bilibili_videoinfo.update(title=title, visit=visit, barrage=barrage).where(
            bilibili_videoinfo.url == url).execute()
    else:
        bilibili_videoinfo.create(title=title, visit=visit, barrage=barrage, upname = upname, upid=upid, url=url, space=space, videoid = videoid)
    insertVideoLog(title, visit, barrage, rank, url)


def exitVideoInfo(url):
    res = bilibili_videoinfo.select().where(bilibili_videoinfo.url == url)
    num = res.count()
    if (num > 0):
        return True
    else:
        return False


def insertVideoLog(title, visit, barrage, rank, url):
    id = uuid.uuid1()
    daydate = datetime.date.today()
    time = datetime.datetime.now()
    videoId = bilibili_videoinfo.select().where(bilibili_videoinfo.url == url)[0].id

    bilibili_videolog.create(id=id, title=title, date=time, videoid=videoId, visit=visit, barrage=barrage, rank=rank,
                             daydate=daydate)


## 初始化图片状态
def insertVideoImage(videoId):
    status = False
    res= bilibili_videoimage.select().where(bilibili_videoimage.videoId == videoId)
    if(res.count()<1):
        bilibili_videoimage.create(videoId=videoId, loadStatus=status)


def selectVideoImageStatus(videoId):
    res = bilibili_videoimage.select().where(bilibili_videoimage.videoId == videoId)
    if (len(res) > 0):
        return res[0]
    else:
        return None


# 选择未下载的图片
def selectNotLoadImages():
    status = False
    res = bilibili_videoimage.select().limit(10).where(bilibili_videoimage.loadStatus == status)
    return res


# 更新图片状态
def updateImageStatus(videoId, path):
    status = True
    bilibili_videoimage.update(loadStatus=status, path=path).where(bilibili_videoimage.videoId == videoId).execute()

# 分页查询 修复之前为下载的封面图片使用
def fixAllImage():
    infoNum = bilibili_videoinfo.select().count()
    pagesize = 10
    pages = int(infoNum/pagesize)+1
    for i in range(1, pages):
        print(i)
        for videoInfo in bilibili_videoinfo.select().order_by(bilibili_videoinfo.videoId).paginate(i, pagesize):
            bvNum = videoInfo.url.split('/')[-1]
            insertVideoImage(bvNum)


if __name__ == "__main__":
    fixAllImage()
