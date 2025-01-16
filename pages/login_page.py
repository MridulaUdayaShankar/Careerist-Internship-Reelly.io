from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN = (By.CSS_SELECTOR, 'a.login-button.w-button')
    LOGIN_TXT = (By.XPATH, "//h1[text()='Sign in or create new account']")


    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def click_continue(self):
        self.click(*self.LOGIN)

    def verify_login(self):
        self.click(*self.LOGIN_TXT)



