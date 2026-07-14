import os
from datetime import datetime

import pytest
from pytest_html import extras

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.read_config import ReadConfig


@pytest.fixture()
def driver():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()
    driver.implicitly_wait(ReadConfig.get_implicit_wait())
    driver.get(ReadConfig.get_base_url())

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extras", [])

    if report.when == "call":

        if report.failed:

            driver = item.funcargs.get("driver")

            if driver:

                os.makedirs("screenshots", exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                file_name = f"{item.name}_{timestamp}.png"

                path = os.path.join(
                    "screenshots",
                    file_name
                )

                driver.save_screenshot(path)

                extra.append(extras.image(path))

        report.extras = extra