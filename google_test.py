import os
import glob
import unittest
from time import sleep

from appium import webdriver

PLATFORM_VERSION = '6.0'
DEVICE_NAME = 'Nexus_5'

class AndroidWebViewTests(unittest.TestCase):

    def setUp(self):       
        desired_caps = {          
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': DEVICE_NAME,
            'browserName': 'Chrome'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)

    def test_mobileweb(self):
        self.driver.get('http://www.google.com');
        search_input = self.driver.find_element_by_name('q')
        search_input.clear()
        search_input.send_keys('international celebration')
        search_input.submit()

        source = self.driver.page_source
        self.assertNotEqual(-1, source.find('international celebration'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidWebViewTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
