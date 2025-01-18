from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage

class Filters(BasePage):


    # Click on filter button
    FILTER_BTN = (By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/form/div[2]/div')
    # check want to buy tag
    WANT_TO_BUY_FILTER = (By.XPATH, "//div[@class='tag-text-filters' and text()='Want to buy']")
    # Click on apply filter button
    APPLY_FILTER_BTN = (By.XPATH, "//a[@wized='applyFilterButtonMLS' and @href='#' and @class='button-filter w-button' and text()='Apply filter']"
)

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 50)

    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def click_filters(self):
        sleep(2)
        self.click(*self.FILTER_BTN)
        # self.wait = WebDriverWait(driver, 25)

    def filter_by(self):
        sleep(2)
        self.click(*self.WANT_TO_BUY_FILTER)
        # self.wait = WebDriverWait(driver, 25)

    def click_apply_filter(self):
        sleep(2)
        self.click(*self.APPLY_FILTER_BTN)
        # self.wait = WebDriverWait(driver, 70)
