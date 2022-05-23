import requests
from bs4 import BeautifulSoup
from db.server import dboperator
from schedule import every, repeat, run_pending
import time

# 创建Video对象
class Video:
    def __init__(self, rank, title, visit, barrage, up_id, url, space):
        self.rank = rank
        self.title = title
        self.visit = visit
        self.barrage = barrage
        self.up_id = up_id
        self.url = url
        self.space = space

    def insertVideoInfo(self):
        dboperator.insertVideoInfo(self.title, self.visit, self.barrage, self.up_id, self.url, self.space, self.rank)

    def to_csv(self):
        return [self.rank, self.title, self.visit, self.barrage, self.up_id, self.url, self.space]

    @staticmethod
    def csv_title():
        return ['排名', '标题', '播放量', '弹幕量', 'Up_ID', 'URL', '作者空间']

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
        up_id = itm.find('span', {'class': 'data-box up-name'}).text.replace(' ', '').replace('\n', '').replace('\r', '')  # 作者id
        url = itm.find_all('a')[1].get('href').replace(' ', '').replace('\n', '').replace('\r', '')  # 获取视频网址
        space = itm.find_all('a')[2].get('href').replace(' ', '').replace('\n', '').replace('\r', '')  # 获取作者空间网址
        v = Video(rank, title, visit, barrage, up_id, url, space)
        videos.append(v)

    for v in videos:
        v.insertVideoInfo()
        print(v.to_csv())

if __name__ == "__main__":
    while True:
        run_pending()
        time.sleep(1)