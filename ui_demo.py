import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://hmshop-test.itheima.net/")
driver.maximize_window()
time.sleep(1)

# 1. 路径+属性：定位 test1 输入框
driver.find_element(by=By.PARTIAL_LINK_TEXT, value="注册").click()
time.sleep(1)

# # 2. 相对路径+序号：定位第 2 个输入框所在段落里的 input
# driver.find_element(By.XPATH, "//p[@id='p2']/input").send_keys("层级加属性")
# time.sleep(1)
#
# # 3. 路径+文本：点击"访问 百度 网站"链接
# driver.find_element(By.XPATH, "//*[text()='访问 百度 网站']").click()
# time.sleep(2)

driver.quit()