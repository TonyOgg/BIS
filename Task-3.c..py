"""For the third code task you should create UI tests for https://www.metric-conversions.org/ .
You have to create the following tests:
- Test for converting Celsius to Fahrenheit temperature;
- Test for converting meters to feet;
- Test for converting ounces to grams;"""

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class MetricTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_celsius_to_fahrenheit(self):
        driver = self.driver
        driver.get("https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm")
        sleep(3)
        driver.find_element_by_name("argumentConv").send_keys("100")
        sel_format = driver.find_element_by_id("format").find_elements_by_tag_name('option')
        sel_accuracy = driver.find_element_by_id("sigfig").find_elements_by_tag_name('option')
        for i in range(len(sel_format)):
            sel_format[i].click()
            sleep(1)
            for j in range(1, len(sel_accuracy)):
                sel_accuracy[j].click()
                name = driver.find_element_by_id("answer").text.split(' ')
                num = name[1].split('°')[0]
                print(type(num))
                f = (100 * 1.8 + 32)
                print(f)
                sleep(100)
                assert num == str((100 * 1.8 + 32)), "something_wrong"
                print('Test ' + sel_format[i].text + sel_accuracy[j].text + ' is ok!')
                sleep(100)
        sleep(100)

    # def in_meters_to_feet(self):
    #     driver = self.driver
    #     driver.get("https://www.metric-conversions.org/length/meters-to-feet.htm")
    #     sleep(3)
    #
    # def in_ounces_to_grams(self):
    #     driver = self.driver
    #     driver.get("https://www.metric-conversions.org/weight/ounces-to-grams.htm")
    #     sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()









