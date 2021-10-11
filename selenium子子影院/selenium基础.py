from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
web = Chrome()

web.get('http://www.lagou.com')

web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a').click()
sleep(3)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)

# li_lists = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
# for li in li_lists:
#     # job_name = li.find_element_by_xpath('./div[1]/div[1]/div[1]/a/h3').text
#     job_name = li.find_element_by_tag_name('h3').text
#     job_inf = li.find_element_by_class_name('li_b_l').text
#     company_name = li.find_element_by_class_name('company_name').text

#     print(job_name,job_inf,company_name)
# 获取数据
job_detail = web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
web.switch_to_window(web.window_handles[-1]) #变更窗口
job_detail_inf = web.find_element_by_xpath('//*[@id="job_detail"]').text

print(job_detail_inf)
web.close()
web.switch_to_window(web.window_handles[0])


