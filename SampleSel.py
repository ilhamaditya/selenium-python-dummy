from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://www.stealmylogin.com/demo.html")
time.sleep(3)
driver.quit()

    
