# Opening Facebook and loggin in

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from group_navigation import GroupPosting
import time
from logger import *

url = "https://www.facebook.com"
username = "YOUR USERNAME"
password = "YOUR PASSWORD!"

class Facebook_Init:

    def __init__(self):
        initialize_logger()
        self.navigation = GroupPosting

    def open_facebook(self):

        option = Options()
        # option.add_argument("--headless")
        option.add_argument('--disable-notifications')
        option.add_argument("--unhandledPromptBehavior=dismiss")
        option.add_argument("--disable-popup-blocking")
        
        
        self.driver = webdriver.Chrome(options=option)
        self.driver.get(url=url)
        try:
            self.email = self.driver.find_element(By.ID, "email")
            self.email.send_keys(username)
            self.password = self.driver.find_element(By.ID, "pass")
            self.password.send_keys(password)
            self.driver.find_element(By.NAME, "login").click()
            lg.info("Loggend In")
        except Exception as e:
            lg.info("Can't log in")
        time.sleep(2)
        self.navigation.posting(self)
                

navigate = Facebook_Init()
navigate.open_facebook()