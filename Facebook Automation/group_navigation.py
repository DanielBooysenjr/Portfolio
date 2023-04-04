# Navigating to groups and posting, posts

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from gvars import groups
import time
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
import random
from logger import *
from report import Report


images = ["ADD IMAGES IE: 1,2,3,4,5 OR A,B,C,D"]
random_image = random.choice(images)
FILE_PATH = "IMAGE PATH"

class GroupPosting:

    def __init__(self):
        initialize_logger()

    def posting(self):
        for i in range(len(groups)):
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
            except Exception as e:
                pass
            try:
                self.driver.get(url=groups[i])
            except Exception as e:
                lg.info(f"Can't go to url {i} \n{e}")
                continue
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
                print("Popup message closed")
            except Exception as e:
                print("No popup to close")
                pass
            try:
                photo = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Photo/video')]"))
                )
                photo.click()
            except Exception as e:
                lg.info(f"Can't initiate post {i} \n{e}")
                continue
            try:
                add_photo = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Add Photos/Videos')]"))
                )
                add_photo.click()
            except Exception as e:
                lg.info(f"Can't load image naviation window {i} \n{e}")
                continue
            try:
                time.sleep(3)
                pyautogui.hotkey("alt", "d")
                pyautogui.typewrite(FILE_PATH)
                pyautogui.press("enter")
                time.sleep(0.5)
                pyautogui.click(x=611, y=428, clicks=1, button='left')
                pyautogui.press(random_image)
                time.sleep(1)
                pyautogui.press("enter")
                # time.sleep(3)
            except Exception as e:
                lg.info(f"Can't navigate to photo and select photo {i} \n{e}")
                continue
            try:
                write = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div'))
                )
                write.click()
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'v')
            except Exception as e:
                lg.info(f"Can't navigate to paste in text {i} \n{e}")
                continue
            try:
                post_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='Post']//ancestor::div[@role='button']"))
                )
                post_button.click()
                lg.info(f"{i+1} Posted on group: {groups[i]}")
            except Exception as e:
                lg.info(f"Can't click on post button {i} \n{e}")
                continue
            time.sleep(15)
            try:
                alert = self.driver.switch_to.alert
                if alert.dismiss():
                    time.sleep(5)
            except:
                pass
        # Execute report method
        try:
            self.send_report = Report()
            self.send_report.send_email()
            print("Report sent")
        except Exception as e:
            print(f"Can't send email {e}")
        self.driver.quit()


