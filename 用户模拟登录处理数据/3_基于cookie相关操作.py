"""
http://www.renren.com/SysHome.do
1 验证码识别，获取验证码数据
2 对POST请求
3 响应数据的持久化存储

bug未修复,未直接进入登陆后页面 2021/4/22
"""
import requests
from lxml import etree
import os
#调用验证码识别函数
import chaojiying


if __name__ == "__main__":

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }
    # url = 'http://passport2.chaoxing.com/login?fid=466&refer=http://ahnu.gj.chaoxing.com'
    # url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    url = 'http://www.renren.com/SysHome.do'

    page_text = requests.get(url=url,headers=headers).text
    
    tree = etree.HTML(page_text)
    img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0] #右键复制来的xpth
    print(img_src)

    img_name = 'code.jpg'
    

    if not os.path.exists('./yanzhen'):
        os.mkdir('./yanzhen')

    img_data = requests.get(url=img_src,headers=headers).content
    img_path = './yanzhen/' + img_name
    print('正在获取....')
    with open(img_path,'wb') as f:
        f.write(img_data)
        print('验证码获取成功！')
    
    print('正在识别...')
    # 调用chaojingying.py平台
    chaojiying = chaojiying.Chaojiying_Client('18955336286', '199712090054lzg', '915709')
    im = open(img_path, 'rb').read()
    code = chaojiying.PostPic(im, 1902)
    code_text = code['pic_str']
    
    print('识别验证码为 === ',code_text)

    #模拟登录
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021341437897'

    datas = {
        'email': '18955336286',
        'icode': code_text,
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': '98f246751a21dde497fe24f2202d7d2d94de6295528eac8525d93843343e9f42',
        'rkey': 'c7ed9a1e2c5b1a7dd7bc76bfc2ca7c5d',
        'f': "http%3A%2F%2Fwww.renren.com%2F976671112",
    }

    session = requests.session()

    response = session.post(url=login_url,headers=headers,data=datas)
    
    print('响应状态码：',response.status_code)

    login_text = response.text
    # login_text.encoding = login_text.apparent_encoding
    # login_text = login_text.content
    # login_text_list = str(list(dict.values(login_text)))
    print(login_text)

    success_text_url = 'http://www.renren.com/home'
    print(success_text_url)

    success_text = session.get(url=success_text_url,headers=headers).text

    with open('login_success.html','w',encoding='utf-8') as f:
        f.write(success_text)
        # print(success_text)
        print('获取成功！！')

    # main_url = 'http://www.renren.com/976671112/newsfeed/photo'

    # main_text = session.get(url=main_url,headers=headers).text

    # with open('main.html','w',encoding='utf-8') as f:
    #     f.write(main_text)

    





    
