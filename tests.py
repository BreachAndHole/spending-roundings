from unittest import TestCase, main
import roundings


class SpendingRoundingsTestCase(TestCase):

    def test_is_float(self):
        self.assertTrue(roundings.is_float('123'))
        self.assertTrue(roundings.is_float('-123'))
        self.assertTrue(roundings.is_float('12.4'))
        self.assertTrue(roundings.is_float('-12.4'))

        self.assertFalse(roundings.is_float('12,4'))
        self.assertFalse(roundings.is_float('f124'))
        self.assertFalse(roundings.is_float('f12.4'))

    def test_parse_user_spending(self):
        self.assertEqual(
            roundings.parse_user_spending('asdg 12 13,4 2sdg4 14.2'),
            [12.0, 13.4, 14.2]
        )
        self.assertEqual(
            roundings.parse_user_spending('asdg'),
            []
        )


if __name__ == '__main__':
    main()
