"""For the third code task you should create UI tests for https://www.metric-conversions.org/ .
You have to create the following tests:
- Test for converting Celsius to Fahrenheit temperature;
- Test for converting meters to feet;
- Test for converting ounces to grams;"""

import unittest
from time import sleep
from selenium import webdriver


class MetricTest(unittest.TestCase):
    testing_numbers = [3.435e-6, -100000, -7.64, 0, 0.000001, 4.55, 1000, 3e+5]

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

    def test_celsius_to_fahrenheit_with_decimal(self):
        driver = self.driver
        driver.get("https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm")
        sleep(3)
        self.going_accuracy_for_decimal(0, '°', self.converting_celsius_to_fahrenheit())

    #     for i in MetricTest.testing_numbers:
    #         driver.find_element_by_name("argumentConv").send_keys(f"{i}")
    #         format = self.select_format_of_conversion()[0].click()
    #         accuracy = self.select_accuracy_of_conversion()
    #         for _ in range(1, len(accuracy)):
    #             accuracy[_].click()
    #             name = driver.find_element_by_id("answer").text.split(' ')
    #             num = name[1].split('°')[0]
    #             param = self.converting_celsius_to_fahrenheit(i)
    #             self.assertEqual(float(f'%.{_ - 1}e' % param), float(num))
    #         driver.find_element_by_name("argumentConv").clear()
    # #
    # def test_celsius_to_fahrenheit_with_fractions(self):
    #     driver = self.driver
    #     driver.get("https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm")
    #     sleep(3)
    #     for i in MetricTest.testing_numbers:
    #         driver.find_element_by_name("argumentConv").send_keys(f"{i}")
    #         format = self.select_format_of_conversion()[1].click()
    #         accuracy = self.select_accuracy_of_conversion()
    #         for _ in range(1, len(accuracy)):
    #             accuracy[_].click()
    #             name = driver.find_element_by_id("answer").text.split(' ')
    #             try:
    #                 sup = driver.find_element_by_xpath('//*[@id="answer"]/sup').text
    #             except:
    #                 sup = ''
    #             try:
    #                 sub = driver.find_element_by_xpath('//*[@id="answer"]/sub').text
    #             except:
    #                 sub = ''
    #             if sup == sub:
    #                 num = name[1].split('°')[0]
    #             else:
    #                 num = name[1].split('°')[0].split(sup + '⁄')[0]
    #             fahrenheit = self.converting_celsius_to_fahrenheit(i)
    #             first_part = str(round(fahrenheit, 1)).split('.')[0]
    #             self.assertEqual(first_part, num)
    #             if sup != '':
    #                 self.assertEqual(round(int(sup) / int(sub), 1), round(fahrenheit - float(first_part), 1))
    #         driver.find_element_by_name("argumentConv").clear()
    #
    #
    # def test_meters_to_feet_with_decimal(self):
    #     driver = self.driver
    #     driver.get("https://www.metric-conversions.org/length/meters-to-feet.htm")
    #     sleep(3)
    #     for i in MetricTest.testing_numbers:
    #         driver.find_element_by_name("argumentConv").send_keys(f"{i}")
    #         format = self.select_format_of_conversion()[1].click()
    #         accuracy = self.select_accuracy_of_conversion()
    #         for _ in range(1, len(accuracy)):
    #             accuracy[_].click()
    #             name = driver.find_element_by_id("answer").text.split(' ')
    #             num = name[1].split('f')[0]
    #             feet = self.converting_meters_to_feet(i)
    #             self.assertEqual(float(f'%.{_ - 1}e' % feet), float(num))
    #         driver.find_element_by_name("argumentConv").clear()
    #
    # def test_meters_to_feet_with_fractions(self):
    #     driver = self.driver
    #     driver.get("https://www.metric-conversions.org/length/meters-to-feet.htm")
    #     sleep(3)
    #     for i in MetricTest.testing_numbers:
    #         driver.find_element_by_name("argumentConv").send_keys(f"{i}")
    #         format = self.select_format_of_conversion()[-1].click()
    #         accuracy = self.select_accuracy_of_conversion()
    #         for _ in range(1, len(accuracy)):
    #             accuracy[_].click()
    #             name = driver.find_element_by_id("answer").text.split(' ')
    #             try:
    #                 sup = driver.find_element_by_xpath('//*[@id="answer"]/sup').text
    #             except:
    #                 sup = ''
    #             try:
    #                 sub = driver.find_element_by_xpath('//*[@id="answer"]/sub').text
    #             except:
    #                 sub = ''
    #             if sup == sub:
    #                 num = name[1].split('f')[0]
    #             else:
    #                 num = name[1].split('f')[0].split(sup + '⁄')[0]
    #             meters = self.converting_meters_to_feet(i)
    #             first_part = str(round(meters, 1)).split('.')[0]
    #             self.assertEqual(first_part, num)
    #             if sup != '':
    #                 self.assertEqual(round(int(sup)/int(sub), 1), round(meters - float(first_part), 1))
    #         driver.find_element_by_name("argumentConv").clear()
    #
    # def test_ounces_to_grams_with_decimal(self):
    #     driver = self.driver
    #     driver.get("https://www.metric-conversions.org/weight/ounces-to-grams.htm")
    #     sleep(3)
    #     for i in MetricTest.testing_numbers:
    #         driver.find_element_by_name("argumentConv").send_keys(f"{i}")
    #         format = self.select_format_of_conversion()[0].click()
    #         accuracy = self.select_accuracy_of_conversion()
    #         for _ in range(1, len(accuracy)):
    #             accuracy[_].click()
    #             name = driver.find_element_by_id("answer").text.split(' ')
    #             num = name[1].split('g')[0]
    #             gram = self.converting_ounces_to_grams(i)
    #             self.assertEqual(float(f'%.{_ - 1}e' % gram), float(num))
    #         driver.find_element_by_name("argumentConv").clear()

    # def test_ounces_to_grams_with_fractions(self):
    #     driver = self.driver
    #     driver.get("https://www.metric-conversions.org/weight/ounces-to-grams.htm")
    #     sleep(3)
    #     for i in MetricTest.testing_numbers:
    #         driver.find_element_by_name("argumentConv").send_keys(f"{i}")
    #         format = self.select_format_of_conversion()[-1].click()
    #         accuracy = self.select_accuracy_of_conversion()
    #         for _ in range(1, len(accuracy)):
    #             accuracy[_].click()
    #             name = driver.find_element_by_id("answer").text.split(' ')
    #             try:
    #                 sup = driver.find_element_by_xpath('//*[@id="answer"]/sup').text
    #             except:
    #                 sup = ''
    #             try:
    #                 sub = driver.find_element_by_xpath('//*[@id="answer"]/sub').text
    #             except:
    #                 sub = ''
    #             if sup == sub:
    #                 num = name[1].split('g')[0]
    #             else:
    #                 num = name[1].split('g')[0].split(sup + '⁄')[0]
    #             grams = self.converting_ounces_to_grams(i)
    #             first_part = str(round(grams, 2)).split('.')[0]
    #             self.assertEqual(first_part, num)
    #             if sup != '':
    #                 self.assertEqual(round(int(sup)/int(sub), 1), round(grams - float(first_part), 1))
    #         driver.find_element_by_name("argumentConv").clear()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
