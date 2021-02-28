import pdb

from behave import *
from selenium import webdriver
import time


@given('I launch the chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open the orangehrm page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('enter user name "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('must login to orangehrm dashboard page')
def step_impl(context):
    time.sleep(2)
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test passed"


