from selenium import webdriver
from src.pages.homePage import HomePage
import time


def test_products():
    driver=webdriver.Chrome()
    driver.get("https://bstackdemo.com/")
    driver.maximize_window()

    homepage=HomePage(driver)
    time.sleep(2)
    homepage.click_apple()
    time.sleep(5)
    homepage.check_samsung()