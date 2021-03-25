import unittest

from rational_number.model.rational_number import RationalNumber


class TestRationalNumberClass(unittest.TestCase):
    def test_can_create_rational_number(self):
        number = RationalNumber(-1, 2)
        self.assertTrue(isinstance(number, RationalNumber))

    def test_can_not_create_divide_zero_rational_number(self):
        with self.assertRaises(ZeroDivisionError):
            RationalNumber(1, 0)

    def test_can_not_create_rational_number_from_bad_str(self):
        with self.assertRaises(TypeError):
            RationalNumber('a', 1)
        with self.assertRaises(TypeError):
            RationalNumber(1, 'b')

    def test_can_check_equality_rational_numbers1(self):
        number = RationalNumber(-1, 2)
        self.assertEquals(number, RationalNumber(-1, 2))

    def test_can_check_equality_rational_numbers2(self):
        number = RationalNumber(-1, 2)
        self.assertEquals(number, RationalNumber(1, -2))

    def test_reduce_zero_rational_number(self):
        number = RationalNumber(0, 3)
        self.assertEquals(number, RationalNumber(0, 1))

    def test_reduce_rational_number1(self):
        number = RationalNumber(-1, 2)
        self.assertEquals(number, RationalNumber(2, -4))

    def test_reduce_rational_number2(self):
        number = RationalNumber(-27, 144)
        self.assertEquals(number, RationalNumber(3, -16))

    def test_can_check_not_equality_rational_numbers1(self):
        number = RationalNumber(-1, 2)
        self.assertNotEquals(number, RationalNumber(1, 2))

    def test_can_check_not_equality_rational_numbers2(self):
        number = RationalNumber(-1, 2)
        self.assertNotEquals(number, RationalNumber(-1, 3))

    def test_str_rational_number1(self):
        number = RationalNumber(3, -4)
        self.assertEquals(str(number), '-3/4')

    def test_str_rational_number2(self):
        number = RationalNumber(-5, 5)
        self.assertEquals(str(number), '-1')

    def test_add_rational_numbers1(self):
        number1 = RationalNumber(-1, 2)
        number2 = RationalNumber(2, 3)
        self.assertEquals(number1 + number2, RationalNumber(1, 6))

    def test_add_rational_numbers2(self):
        number1 = RationalNumber(11, 10)
        number2 = RationalNumber(2, 5)
        self.assertEquals(number1 + number2, RationalNumber(3, 2))

    def test_unary_minus_rational_number1(self):
        number1 = RationalNumber(11, -10)
        number2 = RationalNumber(11, 10)
        self.assertEquals(number1, -number2)

    def test_unary_minus_rational_number2(self):
        number = RationalNumber(11, -10)
        self.assertEquals(number, -(-number))

    def test_subtract_rational_numbers(self):
        number1 = RationalNumber(-1, 2)
        number2 = RationalNumber(2, 3)
        self.assertEquals(number1 - number2, RationalNumber(-7, 6))

    def test_mult_rational_numbers(self):
        number1 = RationalNumber(-2, 5)
        number2 = RationalNumber(3, 4)
        self.assertEquals(number1 * number2, -RationalNumber(3, 10))

    def test_division_rational_numbers(self):
        number1 = RationalNumber(-2, 5)
        number2 = RationalNumber(4, 3)
        self.assertEquals(number1 / number2, -RationalNumber(3, 10))
