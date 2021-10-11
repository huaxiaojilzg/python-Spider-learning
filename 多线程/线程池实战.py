# http://xinfadi.com.cn/marketanalysis/0/list/14869.shtml
# 1 提取单页面数据
# 2 线程池多个页面同时抓取
# 3 
import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

f = open('data.csv',mode='w',encoding='utf-8',newline='')
csvwriter = csv.writer(f)

def download_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers).text
    tree = etree.HTML(response)
    table = tree.xpath('/html/body/div[2]/div[4]/div[1]/table')[0]
    # tr_list = table.xpath('./tr')[1:]
    tr_list = table.xpath('./tr[position()>1]')
    # print(len(tr_list))
    for tr in tr_list:
        txt = tr.xpath('./td/text()')
        # 数据简单处理 去掉 \\ 和 /
        txt = (item.replace('\\','').replace('/','').replace('|','') for item in txt)
        txt = list(txt)
        csvwriter.writerow(txt)
    print(url,'提取完毕')


if __name__ == '__main__':
    # 单线程下载
    # for i in range(1,14000):
    #     download_one_page(url=f'http://xinfadi.com.cn/marketanalysis/0/list/{i}.shtml')

    # 多线程下载
    with ThreadPoolExecutor(100) as t:
        for i in range(1,200):
            # 提交下载任务给线程池
            t.submit(download_one_page,url=f'http://xinfadi.com.cn/marketanalysis/0/list/{i}.shtml')
    print('全部下载完成')
