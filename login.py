# Trying to open a chrome web browser through python. open a chrome web browser through python.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\pawan_sharma\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://wheatbazar.com//Login.aspx/")

# Login Check
driver.find_element_id('txtuserid').send_keys('pawansharmacsu197@gmail.com')
driver.find_element_id("txtpsd").send_keys("pawan@123")
driver.find_element_id("btnlogin").click()

# driver.find_element_by_link_text()
