
import unittest
from order_calculator import calculate_order

class TestOrderCalculator(unittest.TestCase):
    def test_tk01_standard_no_discount(self):
        self.assertEqual(calculate_order(1000, 2, 0, 'standard'), 2300.0)

    def test_tk02_standard_with_discount(self):
        self.assertEqual(calculate_order(1000, 5, 10, 'standard'), 4800.0)

    def test_tk03_express_no_discount(self):
        self.assertEqual(calculate_order(500, 3, 0, 'express'), 2100.0)

    def test_tk04_free_delivery_over_10000(self):
        self.assertEqual(calculate_order(6000, 2, 0, 'express'), 12000.0)

    def test_tk05_zero_price(self):
        self.assertEqual(calculate_order(0, 10, 0, 'standard'), 300.0)

    def test_tk06_zero_quantity(self):
        self.assertEqual(calculate_order(1000, 0, 0, 'standard'), 300.0)

    def test_tk07_full_discount(self):
        self.assertEqual(calculate_order(500, 1, 100, 'standard'), 300.0)

    def test_tk08_boundary_10000_paid_delivery(self):
        self.assertEqual(calculate_order(1000, 10, 0, 'standard'), 10300.0)

    def test_tk09_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order(-100, 5, 10, 'standard')

    def test_tk10_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order(1000, -1, 0, 'standard')

    def test_tk11_discount_too_high(self):
        with self.assertRaises(ValueError):
            calculate_order(1000, 1, 150, 'standard')

    def test_tk12_discount_negative(self):
        with self.assertRaises(ValueError):
            calculate_order(1000, 1, -10, 'standard')

    def test_tk13_invalid_delivery_type(self):
        with self.assertRaises(ValueError):
            calculate_order(1000, 1, 0, 'fast')

    def test_tk14_express_discount_free_delivery(self):
        self.assertEqual(calculate_order(2000, 6, 10, 'express'), 10800.0)

    def test_tk15_minimal_order(self):
        self.assertEqual(calculate_order(1, 1, 0, 'standard'), 301.0)

if __name__ == '__main__':
    unittest.main()
