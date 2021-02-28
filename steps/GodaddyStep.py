from behave import *
from selenium import webdriver

print("print outside")

@given('Launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when('Open this URL - https://www.godaddy.com/')
def step_impl(context):
    cotext.driver.get("https://www.godaddy.com")


@when('maximize the window')
def step_impl(context):
    context.driver.maximize()
    print("heeeelllllllllo")


@when('get title of the page')
def step_impl(context):
    Daddy_title = context.driver.title
    print(Daddy_title)



@Then('close the browser')
def step_imp(context):
    context.driver.close()