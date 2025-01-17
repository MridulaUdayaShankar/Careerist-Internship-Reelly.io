from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class LoginPage(BasePage):


    # LOGIN_TXT = (By.XPATH, "//h1[text()='Sign in or create new account']")
    ENTER_EMAIL = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/form/div/input[1]')
    ENTER_PASSWORD = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/form/div/input[2]')
    CONTINUE_BTN = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/form/a')


    def enter_email(self):
        self.click(*self.ENTER_EMAIL)
        self.input_text('mridulaudayashankar01@gmail.com', *self.ENTER_EMAIL)

    def enter_password(self):
        self.click(*self.ENTER_PASSWORD)
        self.input_text('Apple@2025', *self.ENTER_PASSWORD)

    def click_continue(self):
        self.click(*self.CONTINUE_BTN)
        self.wait = WebDriverWait(driver, 25)






