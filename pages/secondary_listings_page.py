from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecondaryListingsPage(BasePage):


    VERIFY_WANT_TO_BUY_FILTER = (
    By.XPATH, '//*[@id="w-node-d154af0f-0b87-f248-08ed-6776e36f551f-7f66df43"]/div[1]/div[2]/div[1]/div')

    def apply_filter(self):
        self.click(*self.VERIFY_WANT_TO_BUY_FILTER)

