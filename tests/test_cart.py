from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utilities.logger import LogGen
from utilities.read_config import ReadConfig


def test_cart(driver):

    logger = LogGen.loggen()

    logger.info("************ Cart Test Started ************")

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.login(
    ReadConfig.get_username(),
    ReadConfig.get_password()
    )

    logger.info("Login Successful")

    inventory.add_backpack()

    logger.info("Backpack Added")

    inventory.open_cart()

    logger.info("Cart Opened")

    assert cart.get_cart_title() == "Your Cart"

    logger.info("Cart Title Verified")

    assert len(cart.get_cart_items()) == 1

    logger.info("One Item Present In Cart")

    logger.info("************ Cart Test Passed ************")

    print("Cart Test Passed")