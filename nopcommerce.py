"""Locating Elements on the Web page"""
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep


class Prathyusha:
    '''To Register the nopCommerce Portal'''
    url = "https://demo.nopcommerce.com/register"
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    searchbox = "//*[@id='small-searchterms']"
    male = "//*[@id='gender-male']"
    female = "//*[@id='gender-female']"

    # is_displayed             #is_senabled
    
    def test(self):   
        self.driver.maximize_window()
        self.driver.get(self.url)
        search = self.driver.find_element(by=By.XPATH, value=self.searchbox)
        print("display_status: ",search.is_displayed()) # True
        print("enable_status: ",search.is_enabled()) # True
        # is_selected
        select_male = self.driver.find_element(by=By.XPATH, value=self.male)
        select_female = self.driver.find_element(by=By.XPATH, value=self.female)
        print("default radio button status: ")
        print("male_status: ",select_male.is_selected()) # False
        print("female_status: ",select_female.is_selected()) # False
        sleep(5)
        # select male radio button
        select_male.click()
        print("male radio button status: ")
        print("male_status: ",select_male.is_selected()) # True
        print("female_status: ",select_female.is_selected()) # False
        # select female radio button
        sleep(5)
        select_female.click()
        print("female radio button status: ")
        print("male_status: ",select_male.is_selected()) # False
        print("female_status: ",select_female.is_selected()) # True

   
Prathyusha().test() 