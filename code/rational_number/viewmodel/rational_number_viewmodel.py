import re
from rational_number.model.rational_number import RationalNumber

from rational_number.logger.reallogger import RealLogger


class RationalNumberViewModel:
    VALID_OPERATIONS = ['+', '-', '*', '/']
    RATIONAL_NUMBER_REGEX = r"([-]?\d+)\/([-]?\d+)"
    DENOMINATOR_ZERO_REGEX = r"([-]?\d+)\/([-]?0)"
    NUMERATOR_ZERO_REGEX = r"([-]?0)\/([-]?\d+)"

    def __init__(self, logger=RealLogger()):
        self.__first_number = ""
        self.__second_number = ""
        self.__operation = RationalNumberViewModel.VALID_OPERATIONS[0]
        self.__calculate_button_state = "disabled"
        self.__info_message = ""
        self.__result = ""
        self.logger = logger
        self.logger.log("Start view")

    @staticmethod
    def is_rational_number(value):
        return re.match(RationalNumberViewModel.RATIONAL_NUMBER_REGEX, value)

    @staticmethod
    def is_denominator_zero(value):
        return re.match(RationalNumberViewModel.DENOMINATOR_ZERO_REGEX, value)

    @staticmethod
    def is_numerator_zero(value):
        return re.match(RationalNumberViewModel.NUMERATOR_ZERO_REGEX, value)

    def validate_input(self):
        self.__info_message = self.validate_operation() + self.validate_input_numbers()

        if not self.__info_message:
            if self.__operation == "/" and self.is_numerator_zero(self.__second_number):
                self.__info_message = "Numerator of second number is zero. Division by zero is not allowed."
                self.logger.log("Division by zero")
                self.disable_calculate_button()
            else:
                self.logger.log("Operation and input numbers are correct")
                self.enable_calculate_button()
        else:
            self.disable_calculate_button()

    def validate_operation(self):
        operation_message = ""

        if self.__operation not in self.VALID_OPERATIONS:
            operation_message = "Operation is invalid."
            self.logger.log("Operation %s is invalid" % self.__operation)
        return operation_message

    def validate_input_numbers(self):
        first_info = ""
        second_info = ""

        if not self.__first_number:
            first_info = "First number is empty."
            self.logger.log("First number is empty")
        elif not self.is_rational_number(self.__first_number):
            first_info = "First number is invalid."
            self.logger.log("First number is invalid")
        elif self.is_denominator_zero(self.__first_number):
            first_info = "Denominator of first number is zero."
            self.logger.log("Denominator of first number is zero")

        if not self.__second_number:
            second_info = "Second number is empty."
            self.logger.log("Second number is empty")
        elif not self.is_rational_number(self.__second_number):
            second_info = "Second number is invalid."
            self.logger.log("Second number is invalid")
        elif self.is_denominator_zero(self.__second_number):
            second_info = "Denominator of second number is zero."
            self.logger.log("Denominator of second number is zero")

        return first_info + second_info

    def enable_calculate_button(self):
        self.__calculate_button_state = "normal"

    def disable_calculate_button(self):
        self.__calculate_button_state = "disabled"

    def get_calculate_button_state(self):
        return self.__calculate_button_state

    def set_first_number(self, value):
        self.reset_result()
        self.__first_number = value.strip()
        self.validate_input()

    def set_second_number(self, value):
        self.reset_result()
        self.__second_number = value.strip()
        self.validate_input()

    def set_operation(self, value):
        self.reset_result()
        self.__operation = value.strip()
        self.validate_input()

    def get_info_message(self):
        return self.__info_message

    @staticmethod
    def str_to_rational_number(str_number):
        search = re.search(RationalNumberViewModel.RATIONAL_NUMBER_REGEX, str_number)
        numerator = int(search.group(1))
        denominator = int(search.group(2))
        number = RationalNumber(numerator, denominator)
        return number

    def calculate(self):
        num1 = self.str_to_rational_number(self.__first_number)
        num2 = self.str_to_rational_number(self.__second_number)

        if self.__operation == "+":
            self.__result = str(num1 + num2)
        elif self.__operation == "-":
            self.__result = str(num1 - num2)
        elif self.__operation == "*":
            self.__result = str(num1 * num2)
        elif self.__operation == "/":
            self.__result = str(num1 / num2)

        result_str = "%s %s %s = %s" % (self.__first_number, self.__operation,
                                        self.__second_number, self.__result)
        self.logger.log("Calculating was finished successfully. Result: %s" % result_str)

    def reset_result(self):
        self.__result = ""

    def get_result(self):
        return self.__result
