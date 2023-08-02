"""Add the new Employee details in the orange HRM portal"""
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By    # To use the Python Selenium Selector you have to use the By class
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep


class Prathyusha:
    '''To Add the new Employee details in the orange HRM portal'''
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    username = 'Admin'
    password = 'admin123'
    # username_locator is a TagName
    username_locator = 'username'
    # password_locator is a TagName
    password_locator = 'password'
    # Submit button Locator as XPATH
    submitBox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    admin_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    user_management = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'
    users = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li'
    user_role = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i'
    status_role = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i'

    # Startup method for the CRM application
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)    

    # Method for login into the CRM application
    def admin_users(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitBox_locator).click()
        # admin > user Management > users
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.admin_locator).click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.user_management).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.users).click()
        sleep(5)
        # dropdown validation # User Role # Status Role
        self.driver.find_element(by=By.XPATH, value=self.user_role).click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.status_role).click()


   
        while(True):    # only for chrome and Edge browsers #
            pass


Prathyusha().Browsing()
Prathyusha().admin_users()
