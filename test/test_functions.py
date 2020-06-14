import unittest
from main import camper_age_input
from main.camper_age_input import convert_to_months


class MyTestCase(unittest.TestCase):
    def test_convert_to_months(self):
        self.assertEqual(convert_to_months(12),144)


if __name__ == '__main__':
    unittest.main()
    print (age_in_years, "years is", convert_to_months, "months")
