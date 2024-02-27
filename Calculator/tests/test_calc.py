import pytest
from app.calc import Calculator


class TestCalc:

    def setup_class(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 4, 5) == 9

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 4) == 12

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 8, 6) == 2

    def test_division_success(self):
        assert self.calc.division(self, 9, 3) == 3

    def teardown_class(self):
        print('Выполнение метода Teardown')



