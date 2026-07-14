from pages.login_page import LoginPage
from utilities.logger import LogGen
from utilities.read_config import ReadConfig

def test_login(driver):

    logger = LogGen.loggen()

    logger.info("************ Login Test Started ************")

    login = LoginPage(driver)

    login.login(
    ReadConfig.get_username(),
    ReadConfig.get_password()
)

    logger.info("Entered Username and Password")

    assert driver.title == "Swag Labs"

    logger.info("Title Verified")

    assert "inventory" in driver.current_url

    logger.info("Inventory Page Loaded")

    assert login.get_products_title() == "Products"

    logger.info("Products Page Verified")

    logger.info("************ Login Test Passed ************")

    print("Valid Login Test Passed")