from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class OffPlanPage(BasePage):
    OFFPLAN_BTN = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/ul/li[2]/a")
    OFFPLAN_PAGE = (By.XPATH, "//button[@class ='pb-5 text-sm transition-all border-b-2 whitespace-nowrap font-bold border-foreground']")
    SALE_STATUS = (By. XPATH,"//button[@type ='button' and text()='Sale Status']")
    ANNOUNCED_FLTR_BTN = (By.XPATH,"//div[@class ='rounded-full flex items-center justify-center border-white w-4 h-4 border-[3px] bg-[#F572C8]' and text()='Announced']")
    CHECK_ANNOUNCED_FLTR = (By.XPATH,"//span[@class ='bg-white text-xs font-semibold px-2 py-1 rounded-lg shadow' and text()='Announced']")


    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 75)

    def click_offplan(self):
        sleep(1)
        self.click(*self.OFFPLAN_BTN)

    def verify_offplan_page_opens(self):
        self.click(*self.OFFPLAN_PAGE)

    def click_sale_status(self):
        self.click(*self.SALE_STATUS)
        sleep(1)

    def click_on_announced_filter(self):
        self.click(*self.ANNOUNCED_FLTR_BTN)

    def verify_announced_filter(self):
        self.click(*self.CHECK_ANNOUNCED_FLTR)
        sleep(1)