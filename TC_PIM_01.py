"""Search -(text box) Validation on Admin Page"""
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
    admin = 'admin'
    blank = ''
    pim = 'pim'
    # username_locator is a TagName
    username_locator = 'username'
    # password_locator is a TagName
    password_locator = 'password'
    # Submit button Locator as XPATH
    submitBox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    # pim_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    # add_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    # save_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    name_search = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    find_search = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/svg'
    # last_name = 'lname'

    # Startup method for the CRM application
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)    

    # Method for login into the CRM application
    def search_box(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitBox_locator).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.name_search).send_keys(self.admin)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.find_search).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.name_search).send_keys(self.blank)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.name_search).send_keys(self.pim)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.find_search).click()
   
        while(True):    # only for chrome and Edge browsers #
            pass


Prathyusha().Browsing()
Prathyusha().search_box()
