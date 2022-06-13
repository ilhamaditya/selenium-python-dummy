from cgi import test
import imp
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# from cucumbers.basket import CucumberBasket

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.set_page_load_timeout("10")
# driver.delete_all_cookies()

driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
# driver.get("https://www.stealmylogin.com/demo.html")
# time.sleep(3)
# driver.quit()

@given('user is on login page')
def user_is_on_login_page(context):
    driver.get("https://gateway-mp-test02.dana.id/app")

@when('user enters username and password')
def user_enters_username_and_password(context):
    driver.find_element_by_id("loginEmailInput").send_keys("bembeng@mailinator.com")
    driver.find_element_by_css_selector(".input-password > .ant-input").send_keys("!Password01")

@when('clicks on login button')
def clicks_on_login_button(context):
    driver.find_element_by_css_selector(".ant-btn-primary").click()

@then('user navigated to the home page')
def user_navigated_to_the_home_page(context):
    time.sleep(4)
    driver.quit()
