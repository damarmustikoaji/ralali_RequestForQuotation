import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from TESTSUITE.BuyingRequest import object_repository
from PUBLIC_FUNCTION import FUNC_LIBRARY

class Buying_Request(object):
    """docstring for Buying_Request."""
    obj     = object_repository.object_repository
    func    = FUNC_LIBRARY.function

    def BuyingRequest(self, driver):
        driver  = driver
        #Buying_Request.func.wait_XPATH(self, driver, Buying_Request.obj.question)
        Buying_Request.func.get_text_XPATH(self, driver, Buying_Request.obj.question)

    def WillYouPay(self, driver, CHOOSE):
        driver  = driver
        if CHOOSE == "Sure":
            print (CHOOSE)
            Buying_Request.func.click_XPATH(self, driver, Buying_Request.obj.sure)
        elif CHOOSE == "Not Really":
            print (CHOOSE)
            Buying_Request.func.click_XPATH(self, driver, Buying_Request.obj.notreally)

    def SubmitSurvey(self, driver):
        driver  = driver
        Buying_Request.func.click_XPATH(self, driver, Buying_Request.obj.submitbtn)
