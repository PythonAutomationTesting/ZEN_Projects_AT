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
    first_name = 'fname'
    last_name = 'lname'
    username1 = 'Test_toggle'
    password1 = 'test123'
    confirm_password = 'test123'
    username_locator = 'username' # TagName
    password_locator = 'password' # TagName
    first_name_locator = 'firstName' # TagName
    last_name_locator = 'lastName' # Tag Name
    # username1_locator is a XPATH
    username1_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    # password1_locator is a XPATH
    password1_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    # password1_locator is a XPATH
    confirm_password_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    # Submit button Locator as XPATH
    submitBox_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    pim_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'    
    toggle_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    save_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    # Startup method for the CRM application
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)    

    # Method for login into the CRM application > Toggle button
    def add_pim(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitBox_locator).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.pim_locator).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.add_button).click()
        sleep(2)
        self.driver.find_element(by=By.NAME, value=self.first_name_locator).send_keys(self.first_name)
        self.driver.find_element(by=By.NAME, value=self.last_name_locator).send_keys(self.last_name)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.toggle_button).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.username1_locator).send_keys(self.username1)
        self.driver.find_element(by=By.XPATH, value=self.password1_locator).send_keys(self.password1)
        self.driver.find_element(by=By.XPATH, value=self.confirm_password_locator).send_keys(self.confirm_password)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.save_button).click()

   
        while(True):    # only for chrome and Edge browsers #
            pass


Prathyusha().Browsing()
Prathyusha().add_pim()
