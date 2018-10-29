import pytest
from selenium.webdriver import Chrome,Firefox,Ie
def get_driver_instance():
    browser=pytest.config.option.browser.lower()
    url=pytest.config.option.server.lower()
    if browser=='firefox':
        driver=Firefox("./browser-servers/geckodriver.exe")
    elif browser=='chrome':
        driver=Chrome("./browser-servers/chromedriver.exe")
    elif browser=='ie':
        driver=Ie("./browser-servers/internetexplorerdriver.exe")
    else:
        print("------invalid browser------")
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)
    if url=='prod':
        driver.get("https://demo.actitime.com")
    else:
        driver.get("https://demo.actitime.com")
    return driver

