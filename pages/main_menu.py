from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage

class MainMenu(BasePage):


    LANDING_PAGE = (By.XPATH, '/html/body/div[7]/div[1]/a[1]')
    SECONDARY_MENU = [By.XPATH, '//*[@id="w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b"]']
    # add right page verification
    SECONDARY_PAGE = (By.XPATH, '/html/body/div[2]/div[1]/div/a[3]')
    # verify want to buy filter applied
    WANT_TO_BUY_TAG = (By.XPATH, "//select[@div= 'saleTagMLS']")

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def __init__(self, driver):
        super().__init__(driver)
        # self.wait = None

    def verify_login(self):
        sleep(2)
        self.click(*self.LANDING_PAGE)


    def click_secondary_menu(self):
        # self.click(*self.SECONDARY_MENU)
        sleep(2)
        # self.open('https://soft.reelly.io/secondary-listings')
        self.click(*self.SECONDARY_MENU)


    def verify_right_page_opens(self):
        sleep(2)
        self.click(*self.SECONDARY_PAGE )






