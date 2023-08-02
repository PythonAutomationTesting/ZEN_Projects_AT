"""Task1_Login to https://forum.guvi.in/"""
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep

# To use the Python Selenium Selector you have to use the By class
from selenium.webdriver.common.by import By


class Prathyusha:
    '''To login the orange HRM portal'''
    url = "https://forum.guvi.in/"
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    username = 'prathyusha.vr@gmail.com'
    password = 'kanha@369'

    # Login button to login Page
    login1_locator = 'login'
    # username_locator is a TagName
    username_locator = 'login_email'
    # password_locator is a TagName
    password_locator = 'login_password'
    # Login button Locator as XPATH
    login2_locator_id = 'login_button'

    # Startup method for the CRM application
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)      


    # Method for login into the CRM application
    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.login1_locator).click()
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        sleep(5)
        self.driver.find_element(by=By.ID, value=self.login2_locator_id).click()

        while(True):    # only for chrome and Edge browsers #
            pass 


Prathyusha().Browsing()
Prathyusha().login()
