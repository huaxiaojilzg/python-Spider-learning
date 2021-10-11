"""
https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx
"""

import requests
from lxml import etree
import os
#封装识别验证码识别函数
import chaojiying


if __name__ == "__main__":

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

    page_text = requests.get(url=url,headers=headers).text
    
    tree = etree.HTML(page_text)
    # img_src = tree.xpath('./body/form/div[4]/div[4]/img/@src')[0]
    img_src = tree.xpath('//*[@id="imgCode"]/@src')[0] #右键复制来的xpth
    img_src = 'https://so.gushiwen.cn' + img_src
    img_name = 'yanzhen.jpg'

    if not os.path.exists('./yanzhen'):
        os.mkdir('./yanzhen')

    img_data = requests.get(url=img_src,headers=headers).content
    img_path = './yanzhen/' + img_name
    print('正在获取....')
    with open(img_path,'wb') as f:
        f.write(img_data)
        print('验证码获取成功！')
    
    print('正在识别...')
    #调用chaojingying.py平台
    chaojiying = chaojiying.Chaojiying_Client('18955336286', '199712090054lzg', '915709')
    im = open('./yanzhen/yanzhen.jpg', 'rb').read()
    code = chaojiying.PostPic(im, 1902)
    code_text = code['pic_str']
    print('识别验证码为==>',code_text)
    
