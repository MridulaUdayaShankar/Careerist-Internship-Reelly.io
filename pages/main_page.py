from pages.base_page import BasePage


class MainPage(BasePage):

    def open_main_page(self):
        self.open('https://soft.reelly.io/sign-in')