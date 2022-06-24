from parser import _is_float, parse_user_spending
from unittest import TestCase, main
from calculator import (
    RoundingBoundary, _calculate_rounding,
    calculate_all_roundings,
)
from printer import prepare_roundings_results


class UserDataParsingTestCase(TestCase):

    def test_is_float(self):
        self.assertTrue(_is_float('123'))
        self.assertTrue(_is_float('-123'))
        self.assertTrue(_is_float('12.4'))
        self.assertTrue(_is_float('-12.4'))

        self.assertFalse(_is_float('12,4'))
        self.assertFalse(_is_float('f124'))
        self.assertFalse(_is_float('f12.4'))

    def test_parse_user_spending(self):
        self.assertEqual(
            parse_user_spending('asdg 12 13,4 2sdg4 14.2'),
            [12.0, 13.4, 14.2]
        )
        self.assertEqual(
            parse_user_spending('asdg'),
            []
        )


class CalculationTestCase(TestCase):

    def test_calculate_rounding(self):
        self.assertEqual(
            _calculate_rounding(
                100,
                RoundingBoundary(start=100, end=500, ceiling=50)
            ),
            50
        )
        self.assertEqual(
            _calculate_rounding(
                210,
                RoundingBoundary(start=100, end=500, ceiling=50)
            ),
            40
        )

    def test_calculate_all_roundings(self):
        spending = [1, 1251, 353, 23, 12.54]
        self.assertEqual(
            calculate_all_roundings(spending),
            [9, 49, 47, 7, 7.46]
        )


class RoundingResultTestCase(TestCase):

    def test_form_rounding_result(self):
        spending = [1, 1251, 353, 23, 12.54]
        rnds = [9, 49, 47, 7, 7.46]

        result = prepare_roundings_results(spending, rnds)
        expected = '1: spending        1 ₽ - rounding 9 ₽\n'\
                   '2: spending     1251 ₽ - rounding 49 ₽\n'\
                   '3: spending      353 ₽ - rounding 47 ₽\n'\
                   '4: spending       23 ₽ - rounding 7 ₽\n'\
                   '5: spending    12.54 ₽ - rounding 7.46 ₽\n'\
                   'Total: 119.46 ₽'
        self.assertEqual(result, expected)

    def test_form_rounding_result_no_spending(self):
        spending = []
        rnds = []

        result = prepare_roundings_results(spending, rnds)
        expected = 'Total: 0 ₽'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
