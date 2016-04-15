import subprocess
import os
import unittest
from time import sleep

from appium import webdriver

PLATFORM_VERSION = '6.0'
DEVICE_NAME = 'Nexus_5'
PACKAGE_TO_TEST = 'com.google.example'


def grant_permissions(package):
    print 'Start grant permissions to devices'

    command = [
        'bash',
        os.path.join(os.path.dirname(__file__), 'scripts', 'permissions.sh'),
        package
    ]

    try:
        subprocess.call(command,
                        stderr=subprocess.STDOUT,
                        shell=False)
    except OSError:
        print 'ERROR executing shell to grant permissions.'


class AndroidNativeTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': DEVICE_NAME,
            'app': os.path.abspath(os.path.join(os.path.dirname(__file__), 'sample.apk')),
            'appPackage': PACKAGE_TO_TEST,
            'appActivity': '.activity'
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)
        grant_permissions(PACKAGE_TO_TEST)

    def testApk(self):
        # pause a moment, so xml generation can occur
        sleep(5)

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("SOME")').click()

        self.driver.find_element_by_id('com.package:id/something').click()
        self.driver.find_elements_by_class_name('android.widget.ImageButton')[0].click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("text1")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("text2")').click()

        # Switching to webview
        native_context = self.driver.current_context
        sleep(5)

        for context in self.driver.contexts:
            print context

        web_context = "WEBVIEW_package"
        self.driver.switch_to.context(web_context)

        # do web testing
        user_id = self.driver.find_element_by_id('something')

        # switch back to native
        self.driver.switch_to.context(native_context)

        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidNativeTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
