import unittest
import time
from selenium import webdriver

from PUBLIC_FUNCTION import FUNC_LIBRARY, variables

from TESTSUITE.AccountInformation import account_information

class Account_Information_Test(unittest.TestCase):
    "Account Information Testcase"
    browser         = FUNC_LIBRARY.function.driver
    var             = variables.Variables
    account         = account_information.Account_Information

    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = Account_Information_Test.browser
        driver = self.driver
        #go to url
        #driver.get("https://www.google.com/")

    def _01(self):
        "Go to Account Information URL"
        self.startTime = time.time()
        self.driver.get(Account_Information_Test.var.SERVER)
        Account_Information_Test.account.AccountInformation(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def _02(self):
        "Fill account using empty name"
        self.driver.get(Account_Information_Test.var.SERVER)
        self.startTime = time.time()
        Account_Information_Test.account.FillAccount(self, self.driver, "", "mail@mailinator.com", "62", "8955632434")
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.ErrorEmail(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def _03(self):
        "Fill account using invalid name"
        self.driver.get(Account_Information_Test.var.SERVER)
        self.startTime = time.time()
        Account_Information_Test.account.FillAccount(self, self.driver, "ab", "mail@mailinator.com", "62", "8955632434")
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.ErrorName(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def _04(self):
        "Fill account using empty email"
        self.driver.get(Account_Information_Test.var.SERVER)
        self.startTime = time.time()
        Account_Information_Test.account.FillAccount(self, self.driver, "Raissa Asih Melinda", "", "62", "8955632434")
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.ErrorEmail(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def _05(self):
        "Fill account using invalid email"
        self.driver.get(Account_Information_Test.var.SERVER)
        self.startTime = time.time()
        Account_Information_Test.account.FillAccount(self, self.driver, "Raissa Asih Melinda", "mail.mail", "62", "8955632434")
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.ErrorEmail(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def _06(self):
        "Fill account using empty phone"
        self.driver.get(Account_Information_Test.var.SERVER)
        self.startTime = time.time()
        Account_Information_Test.account.FillAccount(self, self.driver, "Raissa Asih Melinda", "Raissa@mailinator.com", "62", "")
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.ErrorPhone(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def _07(self):
        "Fill account using invalid phone"
        self.driver.get(Account_Information_Test.var.SERVER)
        self.startTime = time.time()
        Account_Information_Test.account.FillAccount(self, self.driver, "Raissa Asih Melinda", "Raissa@mailinator.com", "62", "89")
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.Next(self, self.driver)
        Account_Information_Test.account.ErrorPhone(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def test_08(self):
        "Fill account using valid data"
        self.driver.get(Account_Information_Test.var.SERVER)
        self.startTime = time.time()
        Account_Information_Test.account.FillAccount(self, self.driver, Account_Information_Test.var.NAME, Account_Information_Test.var.EMAIL, Account_Information_Test.var.COUNTRY, Account_Information_Test.var.PHONE)
        Account_Information_Test.account.Next(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

if __name__ == '__main__':
    unittest.main()
