import math

from mortgage_calculator.model.term_types import TermType


"""
The module is designed to calculate mortgage parameters during planning a realty purchase.

Mortgage() constructor:
    amount -- the cost of property
    initial_payment - initial payment
    rate -- mortgage loan interest rate

    One of the next optional parameters should be specified:
        1)  term -- desired mortgage term
            term_type -- term type (TermType.YEARLY / TermType.MONTHLY)

        2) monthly_payment - desired monthly payment amount


calculate_monthly_payment - can be used for mortgage monthly payment calculation.
    Note: can be used only if Mortgage object was created with 'term' specified.

calculate_expected_term - can be used for expected mortgage term calculation.
    Note: can be used only if Mortgage object was created with 'monthly_payment' specified.

calculate_overpaid_amount - can be used to calculate mortgage overpaid amount.

"""


class Mortgage:

    def __init__(self, amount, initial_payment, rate,
                 term=None, term_type=TermType.YEARLY, monthly_payment=None):
        if amount <= 0:
            raise ValueError('Incorrect amount. Should be positive value')

        if amount < initial_payment:
            raise ValueError('Error. Amount cannot be less than initial payment value')

        if term is None and monthly_payment is None:
            raise ValueError('One of "term" / "monthly_payment" parameters should be specified')

        self.amount = amount
        self.initial_payment = initial_payment
        self.mortgage_amount = amount - initial_payment
        self.rate = rate
        self.term = term
        self.period_type = term_type
        self.monthly_payment = monthly_payment

        if term is not None:
            self.months_period = term if term_type == TermType.MONTHLY else term * 12

    def calculate_monthly_payment(self):
        if self.term is None:
            return self.monthly_payment

        monthly_rate = self._get_monthly_rate(self.rate)
        common_rate = math.pow((1 + monthly_rate), self.months_period)
        monthly_payment = self.mortgage_amount * monthly_rate * common_rate / (common_rate - 1)
        return round(monthly_payment, 2)

    def calculate_expected_term(self):
        if self.monthly_payment is None:
            raise Exception('To calculate mortgage term need to specify expected monthly payment.')
        monthly_rate = self._get_monthly_rate(self.rate)
        common_rate = self.monthly_payment / (self.monthly_payment - self.mortgage_amount * monthly_rate)
        monthly_term = math.log(common_rate, (1 + monthly_rate))
        return round(monthly_term)

    def calculate_overpaid_amount(self):
        if self.term is None:
            expected_term = self.calculate_expected_term()
            amount = self.monthly_payment * expected_term - self.mortgage_amount
        else:
            monthly_payment = self.calculate_monthly_payment()
            amount = monthly_payment * self.months_period - self.mortgage_amount
        return round(amount, 2)

    def _get_monthly_rate(self, rate):
        return self.rate / 12 / 100
