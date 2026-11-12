from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
input("按回车关闭浏览器")
driver.quit()