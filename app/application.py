from pages.base_page import BasePage
from pages.secondary_listings_page import SecondaryListingsPage
from pages.filters import Filters
from pages.login_page import LoginPage
from pages.main_menu import MainMenu
from pages.main_page import MainPage
from pages.settings_page import SettingsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.filters = Filters(driver)
        self.main_menu = MainMenu(driver)
        self.login_page = LoginPage(driver)
        self.secondary_listings_page = SecondaryListingsPage(driver)
        self.settings_page = SettingsPage(driver)


