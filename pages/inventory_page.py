from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART = (By.ID, "shopping_cart_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # Logout locators
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    def get_products_title(self):
        return self.get_text(self.PRODUCTS_TITLE)

    def add_backpack(self):
        self.click(self.BACKPACK)

    def add_bike_light(self):
        self.click(self.BIKE_LIGHT)

    def open_cart(self):
        self.click(self.CART)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)