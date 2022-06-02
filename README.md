# BiLiBiLiToy
搞事情搞事情  
1. 修改conf.yaml 根据本地环境修改db名字，mysql host地址，user，密码  
运行sql文件导入数据库会生成三张表  
bilibili_videoinfo：视频信息  
bilibili_videolog:视频播放数量等log历史信息    
bilibili_videoimage：封面信息  

3. 爬取bilibili的排行榜视频 
```python
python main.py
```
![效果](/img/爬取效果.PNG)
saveimage文件中为视频封面


  

安装小记:  
pyyaml升级 :
```python
pip install --ignore-installed PyYAML
```

代码：  
process.py  获取上热门基本信息  
imageProcess.py 下载封面  

action:  
报表

参考：  
1. 获取视频封面：https://cloud.tencent.com/developer/article/1865839  

欢迎访问我的小站https://www.styxhelix.life/  
欢迎一起来搞事情  
![公众号](/img/gaoshiqing.jpg)
 
