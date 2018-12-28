import time
from selenium import webdriver

from TESTSUITE.ThankYou import object_repository
from PUBLIC_FUNCTION import FUNC_LIBRARY

class Thank_You(object):
    """docstring for Thank_You."""
    obj     = object_repository.object_repository
    func    = FUNC_LIBRARY.function

    def ThankYou(self, driver):
        driver  = driver
        Thank_You.func.wait_XPATH(self, driver, Thank_You.obj.sent)
        Thank_You.func.get_text_XPATH(self, driver, Thank_You.obj.info)

    def SeeYourRequests(self, driver):
        driver  = driver
        Thank_You.func.get_text_XPATH(self, driver, Thank_You.obj.seerequest)
        Thank_You.func.click_XPATH(self, driver, Thank_You.obj.seerequest)

    def ContinueShopping(self, driver):
        driver  = driver
        Thank_You.func.get_text_XPATH(self, driver, Thank_You.obj.continueshop)
        Thank_You.func.click_XPATH(self, driver, Thank_You.obj.continueshop)
