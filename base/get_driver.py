from appium import webdriver
import page


class GetDriver:
    driver = None
    caps = {}
    caps["platformName"] = "Android"
    caps["appium:deviceName"] = "9c1599f"
    caps["appium:appPackage"] = "com.asf.singa"
    caps["appium:appActivity"] = "com.asf.singa.buildnew.splash.SplashAct"
    caps["appium:noReset"] = "false"
    caps["appium:ensureWebviewsHavePages"] = True
    caps["appium:nativeWebScreenshot"] = True
    caps["appium:newCommandTimeout"] = 3600
    caps["appium:connectHardwareKeyboard"] = True

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cls.caps)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None