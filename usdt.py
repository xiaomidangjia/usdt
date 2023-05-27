import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime
i = 0
while True:
    if i%300 == 0:
        # 随机选取的user-agents
        headers = {

            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"

        }#设置头部信息,伪装浏览器

        response = requests.get( "https://usd.btc126.com/" , headers=headers )  #get方法访问,传入headers参数，
        soup = response.text
        usd = str(str(soup).split('var usdt =')[1][0:10]).strip().split(';')[0]
        usdt = str(str(soup).split('var usd =')[1][0:10]).strip().split(';')[0]
        # 包含当前日期和时间的datetime对象
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        
        #读取数据
        data = pd.read_csv('usdt.csv')
        df = pd.DataFrame({'date':dt_string,'usd':usd,'usdt':usdt},index=[0])
        data = pd.concat([data,df])
        data.to_csv('usdt.csv')
        i += 1
    else:
        i += 1
        continue

