from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from pages.base_page import BasePage


class SettingsPage(BasePage):

    SETTINGS_BTN = (By.XPATH, "//a[@class='account_block-2 w-inline-block']")
    VERIFICATION_BTN = (By.XPATH,"//div[@class='setting-text' and text()='Verification']")
    VERIFY_PROFILE_IMAGE = (By.XPATH,"//img[@class = 'verify-profile-image']")
    VERIFY_UPLOAD_IMG = (By.XPATH,"//label[@class = 'upload-button-2']")
    CLOSE_POP_UP = (By.XPATH,"//button[@class='close-pop-up']")
    VERIFY_NXT_STEP = (By.XPATH,"//div[@class = 'next-step--']")

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def __init__(self, driver):
        super().__init__(driver)

    def click_settings(self):
        self.click(*self.SETTINGS_BTN)

    def click_verification_option(self):
        self.click(*self.VERIFICATION_BTN)

    def verify_upload_image_page_opens(self):
        self.click(*self.VERIFY_PROFILE_IMAGE)

    def verify_upload_image_button_is_available(self):
        sleep(1)
        self.click(*self.VERIFY_UPLOAD_IMG)

    def click_close_pop_up(self):
        self.click(*self.CLOSE_POP_UP)

    def verify_next_step_button_is_available(self):
        self.click(*self.VERIFY_NXT_STEP)