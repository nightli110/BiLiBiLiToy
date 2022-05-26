import requests
import chardet
import json
import os


# 对爬取的页面内容进行json格式处理
def getText(url):
    res = requests.get(url=url)
    res.encoding = chardet.detect(res.content)['encoding']  # 统一字符编码
    res = res.text
    data = json.loads(res)  # json格式化
    return data


# 根据bv号获取av号
def getAid(bv):
    url_1 = 'https://api.bilibili.com/x/player/pagelist?bvid={}'.format(bv)

    response = getText(url_1)
    cid = response['data'][0]['cid']  # 获取cid

    url_2 = 'https://api.bilibili.com/x/web-interface/view?cid={}&bvid={}'.format(cid, bv)
    response_2 = getText(url_2)

    aid = response_2['data']['aid']  # 获取aid
    return aid


# 根据av号获取封面图片
def getImage(aid):
    url_3 = 'https://api.bilibili.com/x/web-interface/view?aid={}'.format(aid)
    response_3 = getText(url_3)
    image_url = response_3['data']['pic']  # 获取图片的下载连接
    image = requests.get(url=image_url).content  # 获取图片
    return image

def getFileName(bv, saveDir):
    return os.path.join(saveDir, bv)

# 下载封面
def download(image, file_name):
    with open(file_name, 'wb') as f:
        f.write(image)
        f.close()


if __name__ == "__main__":
    image = getImage(getAid("BV1ev4y1A7cJ"))
    download(image,'test.png')