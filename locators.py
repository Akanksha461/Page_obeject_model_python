from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name


class MainPageLocatars(object):
 LOGO = (By.CLASS_NAME, 'img-responsive')
 EMAIL = (By.ID, 'login-username')
 PASSWORD = (By.ID, 'login-password')
 SUBMIT = (By.ID, 'login-button')
 ERROR_MESSAGE = (By.CLASS_NAME, 's-alert-box')
 ERROR_MESSAGE1 = (By.XPATH, '//*[@class="alert alert-danger col-sm-10 col-xs-12"]')


class LoginPageLocators(object):
    UNREGISTER  = (By.CSS_SELECTOR, '#root > div > div:nth-child(1) > div.main-container > div.login-employee-container.container-fluid > div.login-employee-header.d-flex.justify-content-between.align-items-center > button')
    DIVEMPLOYEE    = (By.XPATH, "(//*[@class='row'])[2]")
    EMPLOYEE = (By.XPATH,  "(//*[@class='login-employee-item-label'])")
    BHUP_DHORE = (By.XPATH, "(//*[@class='login-employee-item-image'])[1]")
    PIN = "(//*[@class='pincode-input-text'])[%d]"
    PIN1 = (By.XPATH, "(//*[@class='pincode-input-text'])[1]")
    PIN2 = (By.XPATH, "(//*[@class='pincode-input-text'])[2]")
    PIN3 = (By.XPATH, "(//*[@class='pincode-input-text'])[3]")
    PIN4 = (By.XPATH, "(//*[@class='pincode-input-text'])[4]")
    CONFIRM = (By.CSS_SELECTOR, '#pinInputModal > div > div > div.modal-footer.addOnsModalFooterStyle > div:nth-child(2) > span:nth-child(2) > button')
    ACCEPT      = (By.CSS_SELECTOR, '#unregistself.driver.find_element(*locator)erAlert > div > div > div.modal-footer > div:nth-child(2) > span:nth-child(2) > button')
    CANCLE      = (By.CSS_SELECTOR,  '#unregisterAlert > div > div > div.modal-footer > div:nth-child(2) > span:nth-child(1) > button')
    Error_message = (By.XPATH,  '//*[@id="pinInputModal"]/div/div/div[2]/p')


class homePageLocatars(object):
    RESTURANT_LIST = (By.XPATH, "(//*[@class='customDropdown-label'])[0]")
    SELECT_RESTURANT = (By.XPATH,"(//*[@class='dropdown-item'])[1]")
    MENU        = (By.CLASS_NAME, "menuButton")
    # def top_category(self):
    FOOD        = (By.XPATH, "(//*[@class='icon-container'])[0]")
    DRINKS      = (By.XPATH, "(//*[@class='icon-container'])[1]")
    SPECIALS    = (By.XPATH, "(//*[@class='icon-container'])[2]")
    UNSENT      = (By.XPATH, "(//*[@class='icon-container'])[3]")
    SENT        = (By.XPATH, "(//*[@class='icon-container'])[4]")