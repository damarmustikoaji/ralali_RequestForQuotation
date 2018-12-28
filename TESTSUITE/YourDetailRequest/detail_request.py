import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from TESTSUITE.YourDetailRequest import object_repository
from PUBLIC_FUNCTION import FUNC_LIBRARY

class Detail_Request(object):
    """docstring for Detail_Request."""
    obj     = object_repository.object_repository
    func    = FUNC_LIBRARY.function

    def DetailRequest(self, driver):
        driver  = driver
        #Detail_Request.func.wait_XPATH(self, driver, Detail_Request.obj.form)
        Detail_Request.func.get_text_XPATH(self, driver, Detail_Request.obj.subheader)

    def FillDetail(self, driver, ITEMSERVICE, CATEGORY, DESC, QUANTITY, UNIT):
        driver  = driver
        Detail_Request.func.clear_XPATH(self, driver, Detail_Request.obj.item_service)
        Detail_Request.func.fill_XPATH(self, driver, Detail_Request.obj.item_service, ITEMSERVICE)
        Detail_Request.func.wait_XPATH(self, driver, Detail_Request.obj.suggestion)
        #Detail_Request.func.wait_XPATH(self, driver, '//*[contains(text(), "Jasa Kalibrasi Alat Ukur Laser Level")]')
        Detail_Request.func.fill_XPATH(self, driver, Detail_Request.obj.item_service, Keys.RETURN)
        #Detail_Request.CategorySelect(self, driver, CATEGORY)
        Detail_Request.func.clear_XPATH(self, driver, Detail_Request.obj.description)
        Detail_Request.func.fill_XPATH(self, driver, Detail_Request.obj.description, DESC)
        Detail_Request.func.clear_XPATH(self, driver, Detail_Request.obj.quantity)
        Detail_Request.func.fill_XPATH(self, driver, Detail_Request.obj.quantity, QUANTITY)
        #driver.find_element_by_xpath('//select[@name="unit"]/option[text()="'+UNIT+'"]').click()

    def FillInvalidItem(self, driver, ITEMSERVICE):
        driver  = driver
        Detail_Request.func.fill_XPATH(self, driver, Detail_Request.obj.item_service, ITEMSERVICE)

    def FillInvalidDesc(self, driver, DESC):
        driver  = driver
        Detail_Request.func.fill_XPATH(self, driver, Detail_Request.obj.description, DESC)

    def FillWithoutItemservice(self, driver, CATEGORY, DESC, QUANTITY, UNIT):
        driver  = driver
        Detail_Request.func.clear_XPATH(self, driver, Detail_Request.obj.item_service)
        Detail_Request.CategorySelect(self, driver, CATEGORY)
        Detail_Request.func.fill_XPATH(self, driver, Detail_Request.obj.description, DESC)
        Detail_Request.func.fill_XPATH(self, driver, Detail_Request.obj.quantity, QUANTITY)

    def CategorySelect(self, driver, CAT1):
        driver  = driver
        Detail_Request.func.click_XPATH(self, driver, Detail_Request.obj.category)
        Detail_Request.func.wait_XPATH(self, driver, Detail_Request.obj.categoryselector)
        Detail_Request.func.click_XPATH(self, driver, '//*[contains(text(), "'+CAT1+'")]')
        Detail_Request.func.click_XPATH(self, driver, Detail_Request.obj.categorybtn)

    def FindMe(self, driver):
        driver  = driver
        Detail_Request.func.click_XPATH(self, driver, Detail_Request.obj.findmebtn)
        time.sleep(1)

    def ErrorItemService(self, driver):
        driver  = driver
        if driver.find_element_by_xpath(Detail_Request.obj.item_required).is_displayed():
            Detail_Request.func.get_text_XPATH(self, driver, Detail_Request.obj.item_required)
        elif driver.find_element_by_xpath(Detail_Request.obj.item_minlength).is_displayed():
            Detail_Request.func.get_text_XPATH(self, driver, Detail_Request.obj.item_minlength)

    def ErrorDescription(self, driver):
        driver  = driver
        if driver.find_element_by_xpath(Detail_Request.obj.desc_required).is_displayed():
            Detail_Request.func.get_text_XPATH(self, driver, Detail_Request.obj.desc_required)
        elif driver.find_element_by_xpath(Detail_Request.obj.desc_minlength).is_displayed():
            Detail_Request.func.get_text_XPATH(self, driver, Detail_Request.obj.desc_minlength)

    def ErrorQuantity(self, driver):
        driver  = driver
        if driver.find_element_by_xpath(Detail_Request.obj.qt_error).is_displayed():
            Detail_Request.func.get_text_XPATH(self, driver, Detail_Request.obj.qt_error)
