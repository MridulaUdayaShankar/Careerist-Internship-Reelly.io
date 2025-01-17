from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class Filters(BasePage):

    # Click on filter button
    FILTER_BTN = (By.XPATH, '//*[@id="wf-form-Search-form"]/div[2]')
    # check want to buy tag
    WANT_TO_BUY_FILTER = (By.XPATH, '/html/body/div[4]/div[5]/div[2]/div[3]/div')
    # Click on apply filter button
    APPLY_FILTER_BTN = [By.XPATH, '/html/body/div[4]/a[1]']

    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def click_filters(self):
        self.click(*self.FILTER_BTN)


    def filter_by(self):
        self.click(*self.WANT_TO_BUY_FILTER)

    def click_apply_filter(self):
        self.click(*self.APPLY_FILTER_BTN)
