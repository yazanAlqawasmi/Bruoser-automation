import time
from selenium import webdriver
from selenium.webdriver.common.by import By

mtime=time.localtime()
# yu = time.strftime("%H:%M:%S", mtime)
# while yu !="11:40:25":
#     mtime = time.localtime()
#     yu = time.strftime("%H:%M:%S", mtime)
#     print(yu)

PATH = r"C:\Users\HOME\Documents\chromrDriver\chromedriver_win32\chromedriver.exe" #path of driver

driver=webdriver.Chrome(PATH) #to open the google chrome driver
driver.get("http://eco.black-ch.com/wp-login.php?redirect_to=http%3A%2F%2Feco.black-ch.com%2Fwp-admin%2F&reauth=1") # the url that the app will work on it

print(driver.title) # get the title
driver.find_element(By.ID,'user_login').send_keys("enas") # search on element have ID user and put on it 1@1
driver.find_element(By.ID,'user_pass').send_keys("wael") # search on element have name password and put on it 1
driver.find_element(By.NAME,'wp-submit').click() #find elemant have name login and click on it
# See PyCharm help at https://www.jetbrains.com/help/pycharm/