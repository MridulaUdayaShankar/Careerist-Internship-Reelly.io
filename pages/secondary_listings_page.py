from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class SecondaryListingsPage(BasePage):


    VERIFY_WANT_TO_BUY_FILTER = (
    By.XPATH, "//div[@wized='saleTagMLS' and @style='color: rgb(255, 61, 0);' and @w-el-text='For sale' and @w-el-style-color='rgb(120, 162, 0)' and text()='Want to buy']"
)
    TOTAL_PAGES = (By.XPATH, "//div[text()= '5']")
    FIRST_PAGE= (By.XPATH, "//div[@wized= 'currentPageProperties' and @class='page-count']")
    LAST_PAGE= (By.XPATH, "//div[@wized= 'totalPageProperties' and @class='page-count']")
    FIRST_ARROW_BUTTON = (By.XPATH, "//div[@wized= 'previousPageMLS' and @class='pagination__button']")
    LAST_ARROW_BUTTON = (By.XPATH, "//div[@wized= 'nextPageMLS' and @class='pagination__button']")


    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 75)

    def verify_want_to_buy_filter(self):
        sleep(1)
        self.click(*self.VERIFY_WANT_TO_BUY_FILTER)


    def forward_pagination(self, *locator):
        sleep(2)
        total_pages = int(self.driver.find_element(*self.TOTAL_PAGES).text)
        print(f"Total pages: {total_pages}")


        # page Scroll
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        current_page = self.click(*self.TOTAL_PAGES)
        print("Successfully reached last page")

    def backward_pagination(self, *locator):
        sleep(2)
        total_pages = int(self.driver.find_element(*self.TOTAL_PAGES).text)
        print(f"Total pages: {total_pages}")


        # page Scroll
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for page in range(1, total_pages):
            wait = WebDriverWait(self.driver, 15)
            first_page_arrow_button = wait.until(EC.visibility_of_element_located(self.FIRST_ARROW_BUTTON))
            first_page_arrow_button.click()
            print(f"Successfully loaded page {page}")
        sleep(2)

        first_page_number = int(self.driver.find_element(*self.FIRST_PAGE).text)
        print(first_page_number)
        sleep(2)
        print("Successfully returned to first page.")