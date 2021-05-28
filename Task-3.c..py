"""For the third code task you should create UI tests for https://www.metric-conversions.org/ .
You have to create the following tests:
- Test for converting Celsius to Fahrenheit temperature;
- Test for converting meters to feet;
- Test for converting ounces to grams;"""

import unittest
from time import sleep
from selenium import webdriver

class MetricTest(unittest.TestCase):
    testing_numbers = [3.435e-6, -10000, -7.64, 0, 0.000001, 4.51, 1000, 3e+5]

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def converting_celsius_to_fahrenheit(self, temp):
        self.temp = temp
        return self.temp * 1.80 + 32

    def converting_meters_to_feet(self, dist):
        self.dist = dist
        return self.dist * 3.280839895

    def converting_ounces_to_grams(self, weight):
        self.weight = weight
        return self.weight / 0.03527396195

    def select_format_of_conversion(self):
        return self.driver.find_element_by_id("format").find_elements_by_tag_name('option')

    def select_accuracy_of_conversion(self):
        return self.driver.find_element_by_id("sigfig").find_elements_by_tag_name('option')

    def going_accuracy_for_decimal(self, option, splitter, func):

        driver = self.driver
        self.option = option
        self.splitter = splitter
        self.func = func

        for i in MetricTest.testing_numbers:
            driver.find_element_by_name("argumentConv").send_keys(f"{i}")
            format = self.select_format_of_conversion()[self.option].click()
            accuracy = self.select_accuracy_of_conversion()
            for _ in range(1, len(accuracy)):
                accuracy[_].click()
                name = driver.find_element_by_id("answer").text.split(' ')
                num = name[1].split(self.splitter)[0]
                param = self.func(i)
                self.assertEqual(float(f'%.{_ - 1}e' % param), float(num))
            driver.find_element_by_name("argumentConv").clear()

    def going_accuracy_for_fractions(self, option, splitter, func):

        driver = self.driver
        self.option = option
        self.splitter = splitter
        self.func = func

        for i in MetricTest.testing_numbers:
            driver.find_element_by_name("argumentConv").send_keys(f"{i}")
            format = self.select_format_of_conversion()[self.option].click()
            accuracy = self.select_accuracy_of_conversion()
            for _ in range(1, len(accuracy)):
                accuracy[_].click()
                name = driver.find_element_by_id("answer").text.split(' ')
                try:
                    sup = driver.find_element_by_xpath('//*[@id="answer"]/sup').text
                except:
                    sup = ''
                try:
                    sub = driver.find_element_by_xpath('//*[@id="answer"]/sub').text
                except:
                    sub = ''
                if sup == sub:
                    num = name[1].split(self.splitter)[0]
                else:
                    num = name[1].split(self.splitter)[0].split(sup + '⁄')[0]
                param = self.func(i)
                first_part = str(round(param, 3)).split('.')[0]
                self.assertAlmostEqual(int(first_part), int(num), delta=1)
                if sup != '':
                    self.assertAlmostEqual((round(int(sup) / int(sub), 3)), round(param - float(first_part), 3),
                                           delta=0.9)
            driver.find_element_by_name("argumentConv").clear()

    def test_celsius_to_fahrenheit_with_decimal(self):
        driver = self.driver
        driver.get("https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm")
        sleep(3)
        self.going_accuracy_for_decimal(0, '°', self.converting_celsius_to_fahrenheit)

    def test_meters_to_feet_with_decimal(self):
        driver = self.driver
        driver.get("https://www.metric-conversions.org/length/meters-to-feet.htm")
        sleep(3)
        self.going_accuracy_for_decimal(1, 'f', self.converting_meters_to_feet)

    def test_ounces_to_grams_with_decimal(self):
        driver = self.driver
        driver.get("https://www.metric-conversions.org/weight/ounces-to-grams.htm")
        sleep(3)
        self.going_accuracy_for_decimal(0, 'g', self.converting_ounces_to_grams)

    def test_celsius_to_fahrenheit_with_fractions(self):
        driver = self.driver
        driver.get("https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm")
        sleep(3)
        self.going_accuracy_for_fractions(1, '°', self.converting_celsius_to_fahrenheit)

    def test_meters_to_feet_with_fractions(self):
        driver = self.driver
        driver.get("https://www.metric-conversions.org/length/meters-to-feet.htm")
        sleep(3)
        self.going_accuracy_for_fractions(-1, 'f', self.converting_meters_to_feet)

    def test_ounces_to_grams_with_fractions(self):
        driver = self.driver
        driver.get("https://www.metric-conversions.org/weight/ounces-to-grams.htm")
        sleep(3)
        self.going_accuracy_for_fractions(-1, 'g', self.converting_ounces_to_grams)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


# There is mistake in convert ounces to grams https://www.metric-conversions.org/weight/ounces-to-grams.htm
# numbers less than 1e-8.