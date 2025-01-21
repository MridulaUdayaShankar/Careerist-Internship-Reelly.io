from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class SecondaryListingsPage(BasePage):


    VERIFY_WANT_TO_BUY_FILTER = (
    By.XPATH, "//div[@wized='saleTagMLS' and @style='color: rgb(255, 61, 0);' and @w-el-text='For sale' and @w-el-style-color='rgb(120, 162, 0)' and text()='Want to buy']"
)

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 75)

    def verify_want_to_buy_filter(self):
        sleep(1)
        self.click(*self.VERIFY_WANT_TO_BUY_FILTER)


