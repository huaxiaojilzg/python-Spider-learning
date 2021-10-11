# url = 'https://wuhu.58.com/yijiang/hezu/pn1/'

import requests
from lxml import etree

def download_one_page(url):
    proxies = {
        # 'http' : 'http://42.237.102.177:9999',
        'http' : 'http://112.123.40.135:8080',
        'http' : 'http://114.96.218.220:8888',
        'http' : 'http://171.41.150.172:8080',
        'http' : 'http://113.194.136.201:9999',
        'http' : 'http://36.56.103.98:9999',
        'http' : 'http://60.174.191.116:9999',

    }
    # url = 'https://wuhu.58.com/yijiang/hezu/pn1/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    page_text = requests.get(url=url,proxies=proxies,headers=headers).text
    tree = etree.HTML(page_text)
    li_lists = tree.xpath('/html/body/div[6]/div[2]/ul/li')
    for li_list in li_lists:
        title = li_list.xpath('./div[2]/h2/a/text()')[0]
        inf = li_list.xpath('./div[2]/p[1]/text()')[0]
        place = li_list.xpath('./div[2]/p[2]//text()')[0]

        print(title,inf,place)




if __name__ == '__main__':

    i = 1
    url = f'https://wuhu.58.com/yijiang/hezu/pn{i}/'
    download_one_page(url)






