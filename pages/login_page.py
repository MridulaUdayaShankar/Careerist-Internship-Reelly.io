from selenium.webdriver.common.by import By

from pages.base_page import BasePage

import json

class LoginPage(BasePage):


    # LOGIN_TXT = (By.XPATH, "//h1[text()='Sign in or create new account']")
    ENTER_EMAIL = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/form/div/input[1]')
    ENTER_PASSWORD = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/form/div/input[2]')
    CONTINUE_BTN = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/form/a')
    LANDING_PAGE = (By.XPATH, '/html/body/div[7]/div[1]/a[1]')

    with open("/Users/mridulas_macair/PycharmProjects/Careerist-Internship-Reelly.io/config/cred.json", 'r') as f:
        LOGIN_CRED = json.load(f)

    LOGIN_USER= LOGIN_CRED['user']
    LOGIN_PASS= LOGIN_CRED['password']

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def enter_email(self):
        self.click(*self.ENTER_EMAIL)
        self.input_text('kjhgkjhg', *self.ENTER_EMAIL)

    def enter_password(self):
        self.click(*self.ENTER_PASSWORD)
        self.input_text('jhgfjhgj', *self.ENTER_PASSWORD)

    def click_continue(self):
        self.click(*self.CONTINUE_BTN)

    def verify_login(self):
        self.click(*self.LANDING_PAGE)




