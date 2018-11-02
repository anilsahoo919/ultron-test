import unittest
import json

from lib.ui.login_page import LoginPage
from lib.utils import create_driver

class TestLoginS13265(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login=LoginPage(self.driver)
    def tearDown(self):
        self.driver.close()
    def test_login_invalid_tc134567(self):
        test_data=json.load(open('./test/regression/login/s13265.json'))

        #Go to login page
        self.login.wait_for_login_page_to_load()

        #Enter valid UserName
        self.login.get_username_textbox().send_keys(test_data['TC134567']['username'])

        #Enter Invalid Password
        self.login.get_password_textbox().send_keys(test_data['TC134567']['password'])

        #Click on login button
        self.login.get_login_button().click()

        #Get Error message
        actual_msg=self.login.get_login_error_msg().text
        expect_msg=test_data['TC134567']['error_msg']
        assert actual_msg==expect_msg







