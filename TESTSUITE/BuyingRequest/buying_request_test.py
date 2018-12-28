import unittest
import time
from selenium import webdriver

from PUBLIC_FUNCTION import FUNC_LIBRARY, variables

from TESTSUITE.BuyingRequest import buying_request

class Buying_Request_Test(unittest.TestCase):
    "Your Detail Request Testcase"
    browser         = FUNC_LIBRARY.function.driver
    var             = variables.Variables
    buy             = buying_request.Buying_Request

    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = Buying_Request_Test.browser
        driver = self.driver
        #go to url
        #driver.get("https://www.google.com/")

    def test_01(self):
        "Go to Buying Request URL"
        self.startTime = time.time()
        #self.driver.get(Buying_Request_Test.var.SERVER)
        Buying_Request_Test.buy.BuyingRequest(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def test_02(self):
        "Choose Will you pay to get your requested items/services faster?"
        self.startTime = time.time()
        #self.driver.get(Buying_Request_Test.var.SERVER)
        Buying_Request_Test.buy.WillYouPay(self, self.driver, "Not Really")
        Buying_Request_Test.buy.SubmitSurvey(self, self.driver)
        time.sleep(5)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

if __name__ == '__main__':
    unittest.main()
