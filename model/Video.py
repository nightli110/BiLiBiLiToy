from db.server import dboperator


class Video:
    def __init__(self, rank, title, visit, barrage, upName, url, space, upId, videoId):
        self.rank = rank
        self.title = title
        self.visit = visit
        self.barrage = barrage
        self.upName = upName
        self.url = url
        self.space = space
        self.upId = upId
        # BV号
        self.videoId = videoId

    def insertVideoInfo(self):
        dboperator.insertVideoInfo(self.title, self.visit, self.barrage, self.upName, self.url, self.space, self.upId,
                                   self.rank, self.videoId)

    #初始化图片的相关信息
    def parperVideoImage(self):
        dboperator.insertVideoImage(self.videoId)

    @staticmethod
    def csv_title():
        return ['排名', '标题', '播放量', '弹幕量', 'Up_ID', 'URL', '作者空间']
