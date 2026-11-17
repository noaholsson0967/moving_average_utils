import unittest

from moving_average_utils import ExponentialMovingAverage, SimpleMovingAverage


class TestSimpleMovingAverage(unittest.TestCase):
    def test_warmup_returns_none(self):
        sma = SimpleMovingAverage(3)
        self.assertEqual(sma.compute([1, 2]), [None, None])

    def test_full_window(self):
        sma = SimpleMovingAverage(3)
        self.assertEqual(sma.compute([1, 2, 3]), [None, None, 2.0])

    def test_rolling(self):
        sma = SimpleMovingAverage(3)
        self.assertEqual(sma.compute([1, 2, 3, 4, 5]), [None, None, 2.0, 3.0, 4.0])

    def test_invalid_window(self):
        with self.assertRaises(ValueError):
            SimpleMovingAverage(0)


class TestExponentialMovingAverage(unittest.TestCase):
    def test_warmup_returns_none(self):
        ema = ExponentialMovingAverage(3)
        self.assertEqual(ema.compute([1, 2]), [None, None])

    def test_full_window(self):
        ema = ExponentialMovingAverage(3)
        result = ema.compute([1, 2, 3])
        self.assertIsNone(result[0])
        self.assertIsNone(result[1])
        self.assertAlmostEqual(result[2], 2.25)

    def test_rolling(self):
        ema = ExponentialMovingAverage(3)
        result = ema.compute([1, 2, 3, 4])
        self.assertAlmostEqual(result[2], 2.25)
        self.assertAlmostEqual(result[3], 3.125)

    def test_invalid_window(self):
        with self.assertRaises(ValueError):
            ExponentialMovingAverage(0)


if __name__ == "__main__":
    unittest.main()
