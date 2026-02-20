import unittest
from datasystems import process, MIN_INT32, MAX_INT32

class TestDataSystem(unittest.TestCase):

    # Positive value
    def test_positive(self):
        result, overflow, sat = process("123", "DEC")
        self.assertEqual(result, "123")
        self.assertEqual(overflow, 0)
        self.assertEqual(sat, 0)

    # Zero
    def test_zero(self):
        result, overflow, sat = process("0", "BIN")
        self.assertEqual(result, "00000000000000000000000000000000")
        self.assertEqual(overflow, 0)

    # Negative
    def test_negative(self):
        result, overflow, sat = process("-123", "HEX")
        self.assertEqual(result, "0xFFFFFF85")

    # Max boundary
    def test_max(self):
        result, overflow, sat = process(str(MAX_INT32), "DEC")
        self.assertEqual(result, str(MAX_INT32))
        self.assertEqual(overflow, 0)

    # Min boundary
    def test_min(self):
        result, overflow, sat = process(str(MIN_INT32), "DEC")
        self.assertEqual(result, str(MIN_INT32))
        self.assertEqual(overflow, 0)

    # Overflow high
    def test_overflow_high(self):
        result, overflow, sat = process(str(MAX_INT32 + 1), "DEC")
        self.assertEqual(result, str(MAX_INT32))
        self.assertEqual(overflow, 1)
        self.assertEqual(sat, 1)

    # Overflow low
    def test_overflow_low(self):
        result, overflow, sat = process(str(MIN_INT32 - 1), "DEC")
        self.assertEqual(result, str(MIN_INT32))
        self.assertEqual(overflow, 1)
        self.assertEqual(sat, 1)


if __name__ == "__main__":
    unittest.main()