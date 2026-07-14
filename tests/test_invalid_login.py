from pages.login_page import LoginPage
from utilities.logger import LogGen


def test_invalid_login(driver):

    logger = LogGen.loggen()

    logger.info("************ Invalid Login Test Started ************")

    login = LoginPage(driver)

    login.login(
        "standard_user",
        "wrong_password"
    )

    logger.info("Entered Invalid Password")

    assert login.get_error_message() != ""

    logger.info("Error Message Verified")

    logger.info("************ Invalid Login Test Passed ************")

    print("Invalid Login Test Passed")