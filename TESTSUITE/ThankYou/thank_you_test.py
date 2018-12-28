import unittest
import time
from selenium import webdriver

from PUBLIC_FUNCTION import FUNC_LIBRARY, variables

from TESTSUITE.ThankYou import thank_you

class Thank_You_Test(unittest.TestCase):
    "Your Detail Request Testcase"
    browser         = FUNC_LIBRARY.function.driver
    var             = variables.Variables
    thanks          = thank_you.Thank_You

    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = Thank_You_Test.browser
        driver = self.driver
        #go to url
        #driver.get("https://www.google.com/")

    def test_01(self):
        "Go to Thank You URL"
        self.startTime = time.time()
        #self.driver.get(Thank_You_Test.var.SERVER)
        Thank_You_Test.thanks.ThankYou(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def test_02(self):
        "Your request is sent - See request or continue shopping"
        self.startTime = time.time()
        #self.driver.get(Thank_You_Test.var.SERVER)
        Thank_You_Test.thanks.SeeYourRequests(self, self.driver)
        time.sleep(5)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

if __name__ == '__main__':
    unittest.main()
