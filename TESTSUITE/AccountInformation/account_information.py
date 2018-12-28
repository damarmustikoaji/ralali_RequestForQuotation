import time
from selenium import webdriver

from TESTSUITE.AccountInformation import object_repository
from PUBLIC_FUNCTION import FUNC_LIBRARY

class Account_Information(object):
    """docstring for Account_Information."""
    obj     = object_repository.object_repository
    func    = FUNC_LIBRARY.function

    def AccountInformation(self, driver):
        driver  = driver
        Account_Information.func.wait_XPATH(self, driver, Account_Information.obj.form)
        Account_Information.func.get_text_XPATH(self, driver, Account_Information.obj.subheader)

    def FillAccount(self, driver, NAME, EMAIL, COUNTRYCODE, PHONENUMBER):
        driver  = driver
        Account_Information.func.fill_XPATH(self, driver, Account_Information.obj.name, NAME)
        Account_Information.func.fill_XPATH(self, driver, Account_Information.obj.email, EMAIL)
        Account_Information.func.fill_XPATH(self, driver, Account_Information.obj.phone, PHONENUMBER)

    def Next(self, driver):
        driver  = driver
        Account_Information.func.click_XPATH(self, driver, Account_Information.obj.nextbtn)
        time.sleep(1)

    def ErrorName(self, driver):
        driver  = driver
        if driver.find_element_by_xpath(Account_Information.obj.name_required).is_displayed():
            Account_Information.func.get_text_XPATH(self, driver, Account_Information.obj.name_required)
        elif driver.find_element_by_xpath(Account_Information.obj.name_minlength).is_displayed():
            Account_Information.func.get_text_XPATH(self, driver, Account_Information.obj.name_minlength)

    def ErrorEmail(self, driver):
        driver  = driver
        if driver.find_element_by_xpath(Account_Information.obj.email_required).is_displayed():
            Account_Information.func.get_text_XPATH(self, driver, Account_Information.obj.email_required)
        elif driver.find_element_by_xpath(Account_Information.obj.email_format).is_displayed():
            Account_Information.func.get_text_XPATH(self, driver, Account_Information.obj.email_format)

    def ErrorPhone(self, driver):
        driver  = driver
        if driver.find_element_by_xpath(Account_Information.obj.phone_validity).is_displayed():
            Account_Information.func.get_text_XPATH(self, driver, Account_Information.obj.phone_validity)
        elif driver.find_element_by_xpath(Account_Information.obj.phone_required).is_displayed():
            Account_Information.func.get_text_XPATH(self, driver, Account_Information.obj.phone_required)
        elif driver.find_element_by_xpath(Account_Information.obj.phone_minlength).is_displayed():
            Account_Information.func.get_text_XPATH(self, driver, Account_Information.obj.phone_minlength)
