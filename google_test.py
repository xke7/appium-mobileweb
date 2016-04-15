import unittest

from appium import webdriver

ANDROID_DEVICE_POOL = {
    'nexus5': {
        'platformVersion': '6.0',
        'deviceName': 'Nexus_5',
        'browserName': 'Chrome'
    },
    'emulator': {
        'platformVersion': '6.0',
        'deviceName': 'Android Emulator',
        'browserName': 'Chrome'
    }
}

TEST_DEVICE = ANDROID_DEVICE_POOL['nexus5']


class AndroidWebViewTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': TEST_DEVICE['platformVersion'],
            'deviceName': TEST_DEVICE['deviceName'],
            'browserName': TEST_DEVICE['browserName']
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)

    def test_mobileweb(self):
        self.driver.get('http://www.google.com')
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
