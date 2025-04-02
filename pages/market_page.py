from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class MarketPage(BasePage):

    # OFF_PLAN_NEW_BTN = (By.XPATH,"//div[@class='bg-lime-400 rounded text-black text-xs px-1.5 py-1 h-6 ml-auto' and text()='New']")
    MARKET_BTN = (By.XPATH, "//div[@class ='g-menu-text' and text()='Market']")
    VERIFY_MARKET_PAGE = (By.XPATH, "//div[@class = 'page-title agency' and text() = 'Market']")
    ADD_COMPANY_BTN = (By.XPATH, "//a[@class = 'add-company-button w-inline-block']")
    PUBLISH_MY_COMPANY = (By.XPATH,"//a[@class = 'publish-button _1 w-button']")
    VIEW_PAGE_TEMPLATE = (By.XPATH, "//a[@class = 'publish-button color w-button' and text()='View page template']")
    SEND_MY_CV = (By.XPATH, "//a[@class = 'button-agency w-button']")


    def wait_for_element_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(*locator),
            message=f'Element by {locator} not visible'
        )

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = None

    # def click_off_plan_new_btn(self):
    #     sleep(1)
    #     self.click(*self.OFF_PLAN_NEW_BTN)

    def click_market_btn(self):
        self.click(*self.MARKET_BTN)

    def verify_market_page_opens(self):
        self.click(*self.VERIFY_MARKET_PAGE)
        self.wait = WebDriverWait(driver, 15)

    def click_add_company(self):
        self.click(*self.ADD_COMPANY_BTN)

    # def click_publish_my_company(self):
    #     self.click(*self.PUBLISH_MY_COMPANY)

        # page Scroll
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # current_page = self.click(*self.VIEW_PAGE_TEMPLATE)

    def click_view_page_template(self):
        self.click(*self.VIEW_PAGE_TEMPLATE)

    def click_send_my_cv(self):
        self.wait = WebDriverWait(driver, 15)
        self.click(*self.SEND_MY_CV)


