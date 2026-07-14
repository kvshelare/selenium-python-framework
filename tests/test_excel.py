import pytest

from pages.login_page import LoginPage
from utilities.excel_utils import ExcelUtils

data = ExcelUtils.read_login_data(
    "test_data/login_data.xlsx",
    "LoginData"
)


@pytest.mark.parametrize(
    "username,password,expected",
    data
)
def test_excel(driver, username, password, expected):

    login = LoginPage(driver)

    login.login(username, password)

    if expected == "PASS":
        assert "inventory" in driver.current_url
        print(f"{username} -> Login Passed")

    else:
        assert login.get_error_message() != ""
        print(f"{username} -> Invalid Login Passed")