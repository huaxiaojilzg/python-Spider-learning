from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options # 无头浏览器导入包
from time import sleep

# 无头浏览器参数配置
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

# 无图浏览器配置设置
web = Chrome(options=opt)
web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

# 定位到下拉列表
sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# 进行元素包装，包装成下拉菜单
sel = Select(sel_el)
# 让浏览器调整选项
for i in range(len(sel.options)):
    sel.select_by_index(i)
    sleep(3)
    table = web.find_element_by_xpath('//*[@id="TableList"]/table')
    print(table.text)
    print('===========================================')


print('运行结束')


# web.close()

# 拿到页面代码，经过数据加载js执行之后的数据内容
page_text = web.page_source
print(page_text)
 


