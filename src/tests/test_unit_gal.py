import unittest
from oxrse_unit_conv.units import gallon, m3


class TestGallon(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(gallon.si_unit.matches(m3))

    def test_basic_conversion(self):
        self.assertEqual(gallon.to_si(1), 0.00378541)


if __name__ == '__main__':
    unittest.main()
