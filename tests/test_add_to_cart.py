from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.logger import LogGen
from utilities.read_config import ReadConfig


def test_add_to_cart(driver):

    logger = LogGen.loggen()

    logger.info("************ Add To Cart Test Started ************")

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login(
    ReadConfig.get_username(),
    ReadConfig.get_password()
    )

    logger.info("Login Successful")

    inventory.add_backpack()

    logger.info("Backpack Added")

    assert inventory.get_cart_count() == "1"

    logger.info("Cart Badge Verified")

    logger.info("************ Add To Cart Test Passed ************")

    print("Add To Cart Test Passed")