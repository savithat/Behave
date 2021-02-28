from behave import *
from selenium import webdriver
import time

@given('launch the chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when('open hrm home page')
def hrm_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(5)

@then('check the logo present on the home page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then('close the browser')
def close_browser(context):
    context.driver.close()
