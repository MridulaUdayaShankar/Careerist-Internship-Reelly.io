from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class LoginPage(BasePage):
    LANDING_PAGE = (By.XPATH, '/html/body/div[7]/div[1]/a[1]')
    ENTER_EMAIL = (By.XPATH, "//input[@wized= 'emailInput' and @id='email-2']")
    ENTER_PASSWORD = (By.XPATH, "//input[@wized= 'passwordInput' and @id='field']")
    CONTINUE_BTN = (By.XPATH, "//a[@wized= 'loginButton' and @class='login-button w-button']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = None

    def enter_email(self):
        sleep(1)
        self.click(*self.ENTER_EMAIL)
        self.input_text('mridulaudayashankar01@gmail.com', *self.ENTER_EMAIL)

    def enter_password(self):
        sleep(1)
        self.click(*self.ENTER_PASSWORD)
        self.input_text('Apple@2025', *self.ENTER_PASSWORD)

    def click_continue(self):
        sleep(1)
        self.click(*self.CONTINUE_BTN)
        self.wait = WebDriverWait(driver, 25)

    def verify_login(self):
        sleep(1)
        self.click(*self.LANDING_PAGE)






