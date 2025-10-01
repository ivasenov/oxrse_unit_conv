import unittest
from oxrse_unit_conv.units import lb, kg, stones


class TestPound(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(stones.si_unit.matches(kg))

    def test_basic_conversion(self):
        self.assertEqual(stones.to_si(1), 6.35)


if __name__ == '__main__':
    unittest.main()
