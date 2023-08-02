"""Locating Elements on the Web page"""
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep


class Prathyusha:
    '''To Register the nopCommerce Portal'''
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    linktext = "OrangeHRM, Inc"

    # Link_text: continues login to other link
    def orghrm(self):   
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element(by=By.LINK_TEXT, value=self.linktext).click()
        sleep(5)

    driver.close()

Prathyusha().orghrm()