# 4K 动漫 https://pic.netbian.com/4kdongman/
# 4K 美女 https://pic.netbian.com/4kmeinv/
# 4K 风景 https://pic.netbian.com/4kfengjing/
# 4K 游戏 https://pic.netbian.com/4kyouxi/
#

import requests
import os
from time import sleep
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}

img_dic = {
    '动漫' : 'https://pic.netbian.com/4kdongman/index_%d.html',
    '美女' : 'https://pic.netbian.com/4kmeinv/index_%d.html',
    '风景' : 'https://pic.netbian.com/4kfengjing/index_%d.html',
    '游戏' : 'https://pic.netbian.com/4kyouxi/index_%d.html',
}

img_type = input('输出你要下载的壁纸类型(动漫、美女、风景、游戏)：')
img_num = int(input('输出你要下载的壁纸页数：'))
if img_num > 172:
    print('不存在这么多页面哦！')
    exit(0)
    
# 测试
# img_type = '美女'
# img_num = 1

img_num = img_num + 2

if not os.path.exists('./img/' + img_type):
    os.makedirs('./img/' + img_type)
    
print('正在进行下载....')
for num in range(2,img_num):
    url = img_dic[img_type] % num

    page_text = requests.get(url=url,headers=headers)
    # sleep(1)
    page_text.encoding = page_text.apparent_encoding
    page_text = page_text.text

    img_tree = etree.HTML(page_text)

    li_list = img_tree.xpath('//*[@id="main"]/div[3]/ul/li')
    print('正在进行下载第%d页....' % int(num-1))
    for li in li_list:
        img_url = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = img_url.split('-')[-1]

        img_path = 'img/' + img_type + '/' + img_name
        img_data = requests.get(url=img_url,headers=headers).content
        # sleep(1)
        with open(img_path,'wb') as f:
            f.write(img_data)
            print(img_name,'下载成功!')
    print('第%d页下载成功' % int(num-1))
print('你选择的%d页图片下载已全部完成！！' % int(num-1))

    



