import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import platform

from PUBLIC_FUNCTION import variables

wait = 30

class function():
    print('Importing Function Lib')
    var     = variables.Variables
    options = Options()

    print (platform.system())
    try:
        if var.BROWSER == "Chrome":
            print ("Chrome")
            options = webdriver.ChromeOptions()
            #block permission webnotif
            prefs = {"profile.default_content_setting_values.notifications" : 2}
            options.add_experimental_option("prefs",prefs)
            if var.BROWSER_MODE == "headless":
                options.add_argument('headless')
            elif var.BROWSER_MODE == "mobile":
                mobile_emulation = {
                "deviceName": "iPhone 5"
                #"deviceName": "iPhone 6 Plus"
                }
                options.add_experimental_option("mobileEmulation", mobile_emulation)
            #options.add_argument('disable-gpu')
            #options.add_argument('no-sandbox')
            #options.add_argument('disable-popup-blocking')
            if platform.system() == "Darwin":
                options.add_argument("--kiosk")
                driver = webdriver.Chrome(chrome_options=options, executable_path='driver/mac/chromedriver')
            elif platform.system() == "Windows":
                options.add_argument("--start-maximized")
                driver = webdriver.Chrome(chrome_options=options, executable_path='driver/windows/chromedriver.exe')
            elif platform.system() == "Linux":
                options.add_argument("--kiosk")
                driver = webdriver.Chrome(chrome_options=options, executable_path='driver/linux/chromedriver')
        elif var.BROWSER == "Firefox":
            print ("Firefox")
            if var.BROWSER_MODE == "headless":
                options.set_headless(True) # newer webdriver versions #options.headless = True  # older webdriver versions
            elif var.BROWSER_MODE == "mobile":
                user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
                options.set_preference("general.useragent.override", user_agent)
            options.set_preference('dom.webnotifications.enabled', False)
            if platform.system() == "Darwin":
                driver = webdriver.Firefox(options=options, executable_path="driver/mac/geckodriver")
            elif platform.system() == "Windows":
                driver = webdriver.Firefox(options=options, executable_path="driver/windows/geckodriver.exe")
            elif platform.system() == "Linux":
                driver = webdriver.Firefox(options=options, executable_path="driver/linux/geckodriver")

            if var.BROWSER_MODE == "mobile":
                driver.set_window_size(360,640)
            else:
                driver.maximize_window()
        elif var.BROWSER == "IE":
            print ("Internet Explorer")
            if platform.system() == "Windows":
                driver = webdriver.Ie(options=options, executable_path="driver/windows/IEDriverServer.exe")
            driver.maximize_window()
        else:
            print (var.BROWSER, " driver not support")
    except Exception as e:
        raise

#=========================================================================================================

    def wait_ID(self, driver, obj):
        print (" >> Waiting element by ID ", obj)
        for i in range(wait):
            try:
                if driver.find_element_by_id(obj).is_displayed():break
            except: pass
            time.sleep(1)
        else: self.fail("No such element found ")
        return driver

    def wait_XPATH(self, driver, obj):
        print (" >> Waiting element by XPATH ", obj)
        for i in range(wait):
            try:
                if driver.find_element_by_xpath(obj).is_displayed():break
            except: pass
            time.sleep(1)
        else: self.fail("No such element found ")
        return driver

    def click_ID(self, driver, obj):
        print (" >> Clicking elemeny by ID ", obj)
        try:
            driver.find_element_by_id(obj).click()
        except:
            self.fail("Can't clicking element ", obj)
        return driver

    def click_XPATH(self, driver, obj):
        print (" >> Clicking elemeny by XPATH ", obj)
        try:
            driver.find_element_by_xpath(obj).click()
        except:
            self.fail("Can't clicking element ")
        return driver

    def fill_ID(self, driver, obj, input):
        print (" >> Fill in element by ID ", obj)
        try:
            driver.find_element_by_id(obj).send_keys(input)
        except:
            self.fail("Can't fill in element ")
        return driver

    def fill_XPATH(self, driver, obj, input):
        print (" >> Fill in element by XPATH ", obj)
        try:
            driver.find_element_by_xpath(obj).send_keys(input)
        except:
            self.fail("Can't fill in element ")
        return driver

    def clear_ID(self, driver, obj):
        print (" >> Clear element by ID ", obj)
        try:
            driver.find_element_by_id(obj).clear()
        except:
            self.fail("Can't fill in element ")
        return driver

    def clear_XPATH(self, driver, obj):
        print (" >> Clear element by XPATH ", obj)
        try:
            driver.find_element_by_xpath(obj).clear()
        except:
            self.fail("Can't fill in element ")
        return driver

    def get_text_ID(self, driver, obj):
        print (" >> Get text element by ID ", obj)
        try:
            print (driver.find_element_by_id(obj).text)
            time.sleep(1)
        except:
            self.self.fail("Can't get text element ")
        return driver

    def get_text_XPATH(self, driver, obj):
        print (" >> Get text element by XPATH ", obj)
        try:
            print (driver.find_element_by_xpath(obj).text)
            time.sleep(1)
        except:
            self.self.fail("Can't get text element")
        return driver

    def scroll_XPATH(self, driver, obj):
        print (" >> Scroll element to XPATH ", obj)
        for i in range(wait):
            try:
                if driver.find_element_by_xpath(obj).is_displayed():break
            except: pass
            driver.swipe(470, 1400, 470, 950, 330)
            time.sleep(1)
        else: self.fail("Element not found or not accessible. For more details please see stacktrace ")
        return driver

    def scroll_ID(self, driver, obj):
        print (" >> Scroll element to ID ", obj)
        for i in range(wait):
            try:
                if driver.find_element_by_id(obj).is_displayed():break
            except: pass
            driver.swipe(470, 1400, 470, 950, 330)
            time.sleep(1)
        else: self.fail("Element not found or not accessible. For more details please see stacktrace ")
        return driver

    def go_back(self, driver, obj):
        for i in range(wait):
            try:
                if driver.find_element_by_id(obj).is_displayed():break
            except: pass
            driver.back()
            time.sleep(1)
        else: self.fail("Element not found or not accessible. For more details please see stacktrace ")
        return driver
