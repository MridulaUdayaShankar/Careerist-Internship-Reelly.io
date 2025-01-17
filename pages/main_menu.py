from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class MainMenu(BasePage):


    SECONDARY_MENU = (By.XPATH, "//select[@div= 'menu-button-text']")
    # add right page verification
    SECONDARY_PAGE = (By.XPATH, '//*[@id="w-node-bf44e609-bef9-12ba-bb17-9e5d5d1e09d4-7f66df43"]')

    # verify want to buy filter applied
    WANT_TO_BUY_TAG = (By.XPATH, "//select[@div= 'saleTagMLS']")

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def click_secondary_menu(self):
        self.click(*self.SECONDARY_MENU)

    def verify_right_page_opens(self):
        self.click(*self.SECONDARY_PAGE )





