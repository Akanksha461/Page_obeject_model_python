from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from base import Page
from locators import *
import users
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes
from setup import driver

class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocatars
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def check_error_message(self):
        return True if self.find_element(*self.locator.ERROR_MESSAGE) else False

    def enter_email(self, user):
        self.find_element(*self.locator.EMAIL).send_keys(users.get_Merchants(user)["email"])

    def enter_password(self, user):
        self.find_element(*self.locator.PASSWORD).send_keys(users.get_Merchants(user)["password"])

    def click_login_button(self):
        self.find_element(*self.locator.SUBMIT).click()

    def login(self, user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_login_button()
        self.page_refresh

    def login_with_valid_user(self, user):
        self.login(user)
        return loginPage(self.driver)

    def login_without_id_password(self):
        self.click_login_button()
        return self.find_element(*self.locator.ERROR_MESSAGE1).text

    def login_without_password(self, user):
        self.enter_email(user)
        self.click_login_button()
        return self.find_element(*self.locator.ERROR_MESSAGE1).text

    def login_without_id(self, user):
        self.enter_password(user)
        self.click_login_button()
        return self.find_element(*self.locator.ERROR_MESSAGE1).text


class loginPage(Page):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(loginPage, self).__init__(driver)  # Python2 version

    def login_page_loaded(self):
        return True if self.find_element(*self.locator.UNREGISTER) else False

    def click_unregister_button(self):
        self.find_element(*self.locator.UNREGISTER).click()

    def unregister_and_accept_alert(self):
        self.click_unregister_button()
        # self.wait_for_is_displayed(self.ACC, 10)
        time.sleep(4)
        self.find_element(*self.locator.ACCEPT).click()

    def unregister_and_cancel_alert(self):
        self.click_unregister_button()
        time.sleep(4)
        self.find_element(*self.locator.CANCLE).click()

    def enter_pin1(self,user):
        # self.find_element(*self.locator.PIN1).send_keys(users.get_employeelist(user)["pin1"])
        self.find_element(By.XPATH, "(//*[@class='pincode-input-text'])").send_keys(users.get_employeelist(user)["pin1"])


    def enter_pin(self,user):
        index = 1
        valid_pin = users.get_employeelist(user)['pin']
        for pin in valid_pin:
            xpath = (self.locator.PIN) % (index)
            self.driver.find_element(By.XPATH, xpath).send_keys(pin)
            time.sleep(1)    
            index += 1

    def enter_pin3(self,user):
        self.find_element(*self.locator.PIN3).send_keys(users.get_employeelist(user)["pin3"])

    def enter_pin4(self,user):
        self.find_element(*self.locator.PIN4).send_keys(users.get_employeelist(user)["pin4"])

    def employee_login1(self,user):
        employees = self.find_element(By.XPATH,  "(//*[@class='login-employee-item-label'])")
        employees = employees.find_elements(By.XPATH , self.locator.EMPLOYEE[1])
        check = "akan"
        #time.sleep(4)
        is_employee_found = False
        for employee in employees:

            name = employee.text
            print("employee login for \n" + str(name))
            if check.lower() in name.lower():
                is_employee_founds = True
                employee.click()
                self.enter_pin(user)
                element = self.find_element(By.CSS_SELECTOR, self.locator.CONFIRM[1])
                element.click()
                return HomePage(self.driver)
                break
                # self.find_element(*self.locator.CONFIRM).click()
        if not is_employee_found:
            print("No such employee found ")


    def employee_login(self,user):
        self.find_element(*self.locator.BHUP_DHORE).click()
        time.sleep(2)
        self.enter_pin1(user)
        time.sleep(2)
        self.enter_pin2(user)
        time.sleep(2)
        self.enter_pin3(user)
        time.sleep(2)
        self.enter_pin4(user)
        time.sleep(2)
        self.find_element(*self.locator.CONFIRM).click()

    def employee_invalid_login(self,user):
        self.employee_login1(user)
        time.sleep(2)
        return self.find_element(*self.locator.Error_message).text


class HomePage(Page):
    def __init__(self, driver):
        self.locator = homePageLocatars
        super(HomePage, self).__init__(driver)  # Python2 version


    def select_resturant(self):
        self.find_element(*self.locator.RESTURANT_LIST).click()
        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])  # type: WebDriverWait
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='dropdown-item'])[1]")))
        # try:
        #        elem = self.find_element(*self.locator.SELECT_RESTURANT)
        #        elem.click()
        # except nosuchelementexception:
        #        pass



