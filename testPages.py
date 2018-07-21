import unittest
from selenium import webdriver
from pages import *
from testCases import test_cases
from locators import *
from selenium.webdriver.common.by import By
import time
chrome_path = "/home/leanapps/Downloads/chromedriver"

# I am using python unittest for asserting cases.
# In this module, there should be test cases.s
# If you want to run it, you should type: python <module-name.py>


class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.implicitly_wait(10)
        #time.sleep(2)
        self.driver.get("http://test.web.infiniarestaurant.com/")
        #time.sleep(2)
        self.driver.maximize_window()

    # def test_page_load(self):
    #     print ("\n" + str(test_cases(0)))
    #     # print("\n" + str(test_cases(0)['Blocker'][0]))
    #     page = MainPage(self.driver)
    #     self.assertTrue(page.check_page_loaded())
    #
    # def test_login_in_button(self):
    #     print("\n" + str(test_cases(1)))
    #     page = MainPage(self.driver)
    #     mainpage = page.click_login_button()
    #
    def test_sign_in_with_valid_user(self):
        print("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        result = page.login_with_valid_user("valid_user")
        # # page = loginPage(self.driver)
        # self.assertTrue(result.login_page_loaded())
        # time.sleep(4)
    #
    # def test_sign_in_with_invalid_user(self):
    #     print("\n" + str(test_cases(3)))
    #     mainPage = MainPage(self.driver)
    #     result = mainPage.login_with_valid_user("invalid_user")
    #     time.sleep(5)

    # def test_sign_in_with_demo_user(self):
    #     print("\n" + str(test_cases(4)))
    #     mainPage = MainPage(self.driver)
    #     result = mainPage.login_with_valid_user("demo")
    #     time.sleep(5)
    #
    # def test_unregister_select_accept(self):
    #     print("\n" + str(test_cases(5)))
    #     self.test_sign_in_with_valid_user()
    #     page= loginPage(self.driver)
    #     result = page.unregister_and_accept_alert()
    #     time.sleep(5)
    #
    # def test_unregister_select_cancel(self):
    #     print("\n" + str(test_cases(6)))
    #     self.test_sign_in_with_valid_user()
    #     page = loginPage(self.driver)
    #     result = page.unregister_and_cancel_alert()
    #     time.sleep(5)

    def test_employee_login_with_valid_pin(self):
         print("\n" + str(test_cases(7)))
         self.test_sign_in_with_valid_user()
         time.sleep(4)
         page = loginPage(self.driver)
         result = page.employee_login1('akanksha')

    def test_employee_login_with_Invalid_pin(self):
         print("\n" + str(test_cases(8)))
         self.test_sign_in_with_valid_user()
         time.sleep(4)
         page = loginPage(self.driver)
         result = page.employee_invalid_login('Bhup_invalid')
         time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)

