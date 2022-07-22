# Trying to open a chrome web browser through python. open a chrome web browser through python.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\pawan_sharma\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()

class NiaAgroCommodity():
    def registration(self):
        driver.get("https://wheatbazar.com/User_Reg_Seller.aspx")
        driver.find_element(By.ID, 'txtName').send_keys('Ramesh')
        time.sleep(1)
        driver.find_element(By.ID, 'txtCompany').send_keys('demo1')
        time.sleep(1)
        driver.find_element(By.ID, 'Txtemail').send_keys('feefERR@gmail.com')
        time.sleep(2)
        driver.find_element(By.ID, 'txtmobile').send_keys('96344999912')
        time.sleep(1)
        driver.find_element(By.ID, 'txtaddress').send_keys('Ashok Vihar')
        time.sleep(1)
        driver.find_element(By.ID, 'txtlandlinno').send_keys('1001002034')
        time.sleep(1)
        driver.find_element(By.ID, 'txtGst').send_keys('123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//label[normalize-space()='Wholeseller']").click()
        time.sleep(1)

        Select(driver.find_element(By.NAME, 'Ddlstate')).select_by_value('6')
        time.sleep(1)

        Select(driver.find_element(By.NAME, 'Ddldistrict')).select_by_value('86')

        time.sleep(2)

        driver.find_element(By.ID, 'Password').send_keys('Ramesh123')
        time.sleep(2)
        driver.find_element(By.ID, 'txtcnfrmpsd').send_keys('Ramesh123')
        time.sleep(3)

        driver.find_element(By.ID, 'btnsubmit').click()

        time.sleep(1)


        Select(driver.find_element(By.NAME, 'ddlmonth1')).select_by_visible_text('June')
        time.sleep(1)

        Select(driver.find_element(By.NAME, 'Ddlstate')).select_by_value('6')
        time.sleep(1)

        Select(driver.find_element(By.NAME, 'Ddldistrict')).select_by_value('86')
        time.sleep(1)

        driver.find_element(By.ID, 'txtqty1').send_keys(100)

        driver.find_element(By.NAME, 'btnsbmt2').click();



dmouse = NiaAgroCommodity()
dmouse.registration()
dmouse.commodity_details()

















