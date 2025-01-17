from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage

class MainMenu(BasePage):


    LANDING_PAGE = (By.XPATH, '/html/body/div[7]/div[1]/a[1]')
    SECONDARY_MENU = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/a[4]/div/div[2]')
    # add right page verification
    SECONDARY_PAGE = (By.XPATH, '/html/body/div[2]/div[1]/div/a[3]')
    # verify want to buy filter applied
    WANT_TO_BUY_TAG = (By.XPATH, "//select[@div= 'saleTagMLS']")

    # def click(self, *locator):
    #     self.driver.find_element(*locator).click()

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = None

    def verify_login(self):
        self.click(*self.LANDING_PAGE)
        self.wait = WebDriverWait(driver, 15)

    def click_secondary_menu(self):
        # self.wait_and_click(self, *self.SECONDARY_MENU)
        self.open('https://soft.reelly.io/secondary-listings')

    def verify_right_page_opens(self):
        self.click(*self.SECONDARY_PAGE )





