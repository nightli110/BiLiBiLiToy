import datetime
import os.path

import requests
from bs4 import BeautifulSoup
from schedule import every, repeat

import conf.configs
from model.Video import Video
from db.server.dboperator import *
from conf.configs import config
from core.imageProcess import *

#获取排行榜视频的基本信息
@repeat(every(10).seconds)
def getRankVideo():
    # 发起网络请求
    url = 'https://www.bilibili.com/v/popular/rank/all'
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    # 提取列表
    items = soup.findAll('li', {'class': 'rank-item'})

    # 保存提取出来的Video列表
    videos = []

    for itm in items:
        title = itm.find('a', {'class': 'title'}).text.replace(' ', '').replace('\n', '').replace('\r', '')  # 视频标题
        rank = itm.find('i', {'class': 'num'}).text.replace(' ', '').replace('\n', '').replace('\r', '')  # 排名
        visit = itm.find_all('span')[3].text.replace(' ', '').replace('\n', '').replace('\r', '')  # 播放量
        barrage = itm.find_all('span')[4].text.replace(' ', '').replace('\n', '').replace('\r', '')  # 弹幕量
        upName = itm.find('span', {'class': 'data-box up-name'}).text.replace(' ', '').replace('\n', '').replace('\r',
                                                                                                                 '')  # 作者名字
        url = itm.find_all('a')[1].get('href').replace(' ', '').replace('\n', '').replace('\r', '')  # 获取视频网址
        space = itm.find_all('a')[2].get('href').replace(' ', '').replace('\n', '').replace('\r', '')  # 获取作者空间网址
        upId = space.split('/')[-1]
        videoId = url.split('/')[-1]
        v = Video(rank, title, visit, barrage, upName, url, space, upId, videoId)
        videos.append(v)

    for v in videos:
        v.insertVideoInfo()
        v.parperVideoImage()
    print(datetime.datetime.now())
    print("download finish")



# 下载图片
@repeat(every(10).seconds)
def getVideoImage():
    config = conf.configs.config()
    while(True):
        res = selectNotLoadImages()
        if(res.count()==0):
            print("download image finish")
            break
        for imageRecord in res:
            try:
                bvId = imageRecord.videoId
                imagePath = os.path.join(config.saveImagePath, bvId+".png")
                image = getImage(getAid(bvId))
                download(image, imagePath)
                updateImageStatus(bvId, imagePath)
            except Exception as e:
                print(e)
                print("download image finish")