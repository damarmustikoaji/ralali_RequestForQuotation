import unittest
import time
from selenium import webdriver

from PUBLIC_FUNCTION import FUNC_LIBRARY, variables

from TESTSUITE.YourDetailRequest import detail_request

class Detail_Request_Test(unittest.TestCase):
    "Your Detail Request Testcase"
    browser         = FUNC_LIBRARY.function.driver
    var             = variables.Variables
    request         = detail_request.Detail_Request

    @classmethod
    def setUpClass(self):
        "Setup for the test"
        self.driver = Detail_Request_Test.browser
        driver = self.driver
        #go to url
        #driver.get("https://www.google.com/")

    def test_01(self):
        "Go to Your Detail Request URL"
        self.startTime = time.time()
        #self.driver.get(Detail_Request_Test.var.SERVER)
        Detail_Request_Test.request.DetailRequest(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def test_02(self):
        "Fill Your Detail Request with empty all field"
        self.startTime = time.time()
        #self.driver.get(Detail_Request_Test.var.SERVER)
        Detail_Request_Test.request.FindMe(self, self.driver)
        Detail_Request_Test.request.ErrorItemService(self, self.driver)
        Detail_Request_Test.request.ErrorDescription(self, self.driver)
        Detail_Request_Test.request.ErrorQuantity(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def test_03(self):
        "Fill Your Detail Request with invalid item service"
        self.startTime = time.time()
        #self.driver.get(Detail_Request_Test.var.SERVER)
        Detail_Request_Test.request.FillInvalidItem(self, self.driver, "sd")
        Detail_Request_Test.request.FindMe(self, self.driver)
        Detail_Request_Test.request.ErrorItemService(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def test_04(self):
        "Fill Your Detail Request with invalid description"
        self.startTime = time.time()
        #self.driver.get(Detail_Request_Test.var.SERVER)
        Detail_Request_Test.request.FillInvalidDesc(self, self.driver, "sd")
        Detail_Request_Test.request.FindMe(self, self.driver)
        Detail_Request_Test.request.ErrorDescription(self, self.driver)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def test_05(self):
        "Fill Your Detail Request without Item Service"
        self.startTime = time.time()
        #self.driver.get(Detail_Request_Test.var.SERVER)
        Detail_Request_Test.request.FillWithoutItemservice(self, self.driver, "Electronics", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "1", "Unit")
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def test_06(self):
        "Fill Your Detail Request using valid data"
        self.startTime = time.time()
        #self.driver.get(Detail_Request_Test.var.SERVER)
        Detail_Request_Test.request.FillDetail(self, self.driver, "Jasa", "Electronics", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "1", "Set")
        Detail_Request_Test.request.FindMe(self, self.driver)
        time.sleep(3)
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

if __name__ == '__main__':
    unittest.main()
