from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage

class MainMenu(BasePage):


    LANDING_PAGE = (By.XPATH, '/html/body/div[7]/div[1]/a[1]')
    SECONDARY_MENU = [By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/a[4]/div/div[2]']
    # add right page verification
    SECONDARY_PAGE = (By.XPATH, '/html/body/div[2]/div[1]/div/a[3]')
    # SECONDARY_PAGE_FF = (By.XPATH,'//*[@id="w-node-bf44e609-bef9-12ba-bb17-9e5d5d1e09d4-7f66df43"]')
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
        self.open('https://soft.reelly.io/secondary-listings')
        # self.wait_for_element_clickable(*self.SECONDARY_MENU)


    def verify_right_page_opens(self):
        sleep(2)
        self.click(*self.SECONDARY_PAGE )

    # def verify_right_page_opens(self):
    #     self.click(*self.SECONDARY_PAGE_FF )







