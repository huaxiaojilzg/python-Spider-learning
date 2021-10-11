# url = 'https://www.pearvideo.com/'

import requests
import os
from lxml import etree
from time import sleep

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
# url = 'https://www.pearvideo.com/category_6'
url = 'https://www.pearvideo.com/category_loading.jsp?'
print('================梨视频下载器(美食视频)v1.0================\n\n')
n = int(input('输入下载页数:'))

if not os.path.exists('./video'):
    os.mkdir('./video')

n += 1
for start_num in range(1,n):
    sleep(1)
    params = {
        'reqType': '5',
        'categoryId': '6',
        'start': int(start_num*6),
        # 'start': '48',
        'filterIds': '1728277,1727914,1726962,1725616,1724919,1725573,1725463,1725379,1725313,1725288,1725263,1724407,1725089,1725068,1722539'
    }

    page_text = requests.get(url=url,params=params,headers=headers).text
    tree = etree.HTML(page_text)
    # video_detail_url_list = tree.xpath('//*[@id="categoryList"]/li')
    video_detail_url_list = tree.xpath('/html/body/li')

    for video_detail_urls in video_detail_url_list:
        video_detail_url = 'https://www.pearvideo.com/' + video_detail_urls.xpath('./div/a/@href')[0]
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Referer' : video_detail_url
        }
        
        # print(video_detail_url)
        video_coutId = video_detail_url.split('_')[1]
        params = {
            'contId': video_coutId
        }


        video_name = video_detail_urls.xpath('./div/a/div[2]/text()')[0]
        # video_path = 'video/' + video_name + '.mp4'
        video_detail = requests.get(video_detail_url)
        video_ajax_url = 'https://www.pearvideo.com/videoStatus.jsp'
        video_data = requests.get(url=video_ajax_url,params=params,headers=headers).json()
        # print(video_data)
        video_data_srcUrl = video_data['videoInfo']['videos']['srcUrl']
        video_data_systemTime = video_data['systemTime']
        # print(video_data_systemTime)
        video_coutId_url = 'cont' + '-' + video_coutId
        # video_really_url = video_data_srcUrl.replace(video_data_systemTime, f"cont-{video_coutId}")
        video_really_url = video_data_srcUrl.replace(video_data_systemTime, video_coutId_url)
        video_name = video_name.split('|')[0]
        video_path = 'video/' + video_name + '.mp4'
        print(video_name,'正在下载.....')
        video_data_down = requests.get(url=video_really_url,headers=headers).content
        with open(video_path,'wb') as f:
            f.write(video_data_down)
            print(video_name,'下载成功!')
    print(start_num,'页下载完成！')
print('全部下载结束！！正在退出')
sleep(8)
    

