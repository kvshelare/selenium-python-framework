from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_TITLE = (By.CLASS_NAME, "title")
    CHECKOUT = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_title(self):
        return self.get_text(self.CART_TITLE)

    def click_checkout(self):
        self.click(self.CHECKOUT)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)