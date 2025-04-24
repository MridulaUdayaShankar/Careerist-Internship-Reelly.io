from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class OffPlanPage(BasePage):
    OFFPLAN_BTN = (By.XPATH, "//span[@class ='font-medium whitespace-nowrap' and text()='Off-plan']")




    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 75)

    def verify_want_to_buy_filter(self):
        sleep(1)
        self.click(*self.OFFPLAN_BTN)