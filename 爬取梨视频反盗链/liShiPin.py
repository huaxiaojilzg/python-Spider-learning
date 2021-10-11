# url = 'https://www.pearvideo.com/'

import requests
import os
from lxml import etree

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
# url = 'https://www.pearvideo.com/category_6'
url = 'https://www.pearvideo.com/category_6'



if not os.path.exists('./video'):
    os.mkdir('./video')

    # # for start_num in range(6):
    # datas = {
    #     'reqType': '6',
    #     'categoryId': '12',
    #     # 'start': int(start_num*6)
    #     'start': '60'
    # }

page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
video_detail_url_list = tree.xpath('//*[@id="categoryList"]/li')

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
    

