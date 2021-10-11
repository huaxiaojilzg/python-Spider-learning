from selenium.webdriver import Chrome
from time import sleep
import re
from lxml import etree
import requests
from selenium.webdriver.chrome.options import Options


url = 'http://ziziyy1.com/acg/3749/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
# bro = webdriver.Chrome(executable_path='./chromedriver')
options = Options()
options.add_argument('--headless')
options.add_argument('--disalbe-gpu')
bro = Chrome(options=options)

bro.get(url=url)
page_text = bro.page_source
tree = etree.HTML(page_text)
sleep(2)
# detail_url_list = tree.xpath('//*[@id="stab_1_71"]/ul/li')
# # print(detail_url_list)
# for detail_urls in detail_url_list:
#     detail_url = 'http://ziziyy1.com' + detail_urls.xpath('./a/@href')[0]
#     print(detail_url)
detail_url = 'http://ziziyy1.com/acg/3749/1.html'
bro.get(url=detail_url)
# detail_page_text = bro.page_source
# print(detail_page_text)
bro.switch_to_frame('playiframe') # frame的id值
bro.switch_to_frame('playiframe') # frame的id值
bro.switch_to_frame('PLAYERS') # frame的id值
div = bro.find_element_by_id('video')
sleep(8)
div.click()

page_text_video = bro.page_source

# print(page_text_video)

ex = '<video class="dplayer-video dplayer-video-current" webkit-playsinline="" x-webkit-airplay="allow" playsinline="" poster="https://p.pstatp.com/origin/pgc-image/903d28ab0e2f4bb59bdf8f7c6fd22fe4" preload="auto" src="(.*?)">'
video_url = re.findall(ex,page_text_video,re.S)[0]
print('正在获取下载链接....')
# print(video_url)

print('正在下载...')
video_data = requests.get(video_url,headers).content

i = 3
with open(f'{i}.mp4','wb') as f:
    f.write(video_data)
    print('下载完成！')













sleep(8)



