from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.common.exceptions import StaleElementReferenceException
driver = webdriver.Chrome(executable_path="C:\\Users\\pawan_sharma\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

class Registration():
    def locate_registration(self):
        driver.get("https://www.maizebazar.com/")
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@class='header-top']//li[2]//a[1]").click()
        time.sleep(4)
        driver.find_element(By.XPATH ,"//a[@href='User_Reg_Buyer.aspx']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//label[normalize-space()='Manufacturer']").click()
        time.sleep(2)
        el=driver.find_element(By.XPATH,"//input[@id='txtlandlinno']")
        el.click()
        driver.refresh()
        try:
            el.send_keys("234561")
        except StaleElementReferenceException:
            el=driver.find_element(By.XPATH,"//input[@id='txtlandlinno']")
            el.send_keys("234561")
        driver.find_element(By.XPATH,"//input[@id='txtmobile']").send_keys('9414261370')
        driver.find_element(By.XPATH,"//input[@id='Txtemail']").send_keys('ram@gmail.com')
        driver.find_element(By.XPATH,"//input[@id='txtproduct']").send_keys('wheat')
        driver.find_element(By.XPATH,"//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH,"//input[@id='txtcnfrmpsd']").send_keys('123456')
        driver.find_element(By.XPATH,"//input[@id='txtwebsite']").send_keys('rameshbuyer.in')
        driver.find_element(By.XPATH,"//input[@id='txtGst']").send_keys('1234qwerty5670')
        driver.find_element(By.XPATH,"//textarea[@id='txtaddress']").send_keys('Shanti Vihar, Haryana')
        driver.find_element(By.XPATH,"//*[@id='txtName']").send_keys('Ramesh')
        driver.find_element(By.XPATH,"//*[@id='txtCompany']").send_keys('demo1')
        Select(driver.find_element(By.XPATH,"//select[@id='Ddlstate']")).select_by_value('6')
        time.sleep(4)
        driver.find_element(By.XPATH," //a[normalize-space()='Login']").click()
        time.sleep(2)
      
      
        
       
class FindLogin():
    def locate_login(self):
        driver.find_element(By.XPATH,"//input[@id='txtuserid']").send_keys('3198')
        driver.find_element(By.XPATH,"//input[@id='txtpsd']").send_keys('123456')
        driver.find_element(By.XPATH,"//input[@id='btnlogin']").click()
        time.sleep(40)
        
Registration=Registration()
Registration.locate_registration()
loginId= FindLogin()
loginId.locate_login()