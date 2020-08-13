from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://zrzy.jiangsu.gov.cn/nt/gtzx/gzdt/")
bt=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/a")
bt.click()
