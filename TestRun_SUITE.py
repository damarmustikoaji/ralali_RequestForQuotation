#!/usr/bin/python
# -*- coding: utf-8 -*-
# author damarmustikoaji / damar.mustikoaji@gmail.com
import unittest
import os

from PUBLIC_FUNCTION import FUNC_LIBRARY
from PUBLIC_FUNCTION.ExtentHTMLTestRunner import HTMLTestRunner

from TESTSUITE.AccountInformation import account_information_test
from TESTSUITE.YourDetailRequest import detail_request_test
from TESTSUITE.BuyingRequest import buying_request_test
from TESTSUITE.ThankYou import thank_you_test

direct = os.getcwd()

class RalaliTest(unittest.TestCase):
    driver = FUNC_LIBRARY.function.driver

    def test_main(self):

        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(account_information_test.Account_Information_Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(detail_request_test.Detail_Request_Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(buying_request_test.Buying_Request_Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(thank_you_test.Thank_You_Test),
            ])

        outfile = open(direct + "/REPORT/Report.html", "wb")

        runner1 = HTMLTestRunner(
            stream=outfile,
            title='Test Report - Ralali Website',
            description='Functionality Tests'
        )

        runner1.run(smoke_test)

    def tearDown(self):
        RalaliTest.driver.quit()

if __name__ == '__main__':
    unittest.main()
