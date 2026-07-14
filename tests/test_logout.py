from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_logout(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # Login
    login.login(
        "standard_user",
        "secret_sauce"
    )

    # Logout
    inventory.logout()

    # Verify redirected to login page
    assert "saucedemo.com" in driver.current_url
    assert login.get_login_button().is_displayed()

    print("Logout Test Passed")