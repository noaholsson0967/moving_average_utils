"""Moving average implementations with warm-up handling.

Both classes accept an iterable of numbers and produce a list of averages.
Warm-up is handled by emitting ``None`` until enough data is available.
"""

from collections import deque
from typing import Iterable, List, Optional


class SimpleMovingAverage:
    """Simple moving average (SMA).

    The SMA of window ``n`` is the arithmetic mean of the last ``n`` values.
    Before ``n`` values have been seen, the output is ``None`` because there
    is no complete window to average.
    """

    def __init__(self, window: int) -> None:
        if window < 1:
            raise ValueError("window must be >= 1")
        self.window = window
        self._buf: deque = deque(maxlen=window)
        self._sum = 0.0

    def update(self, value: float) -> Optional[float]:
        """Add *value* and return the current SMA, or ``None`` during warm-up."""
        if len(self._buf) == self.window:
            self._sum -= self._buf[0]
        self._buf.append(value)
        self._sum += value
        if len(self._buf) < self.window:
            return None
        return self._sum / self.window

    def compute(self, values: Iterable[float]) -> List[Optional[float]]:
        """Return the SMA for each value in *values*."""
        return [self.update(v) for v in values]


class ExponentialMovingAverage:
    """Exponential moving average (EMA).

    Uses the standard smoothing factor ``alpha = 2 / (window + 1)``.
    The first value initialises the EMA; subsequent values are blended with
    the previous EMA. The first ``window - 1`` outputs are ``None`` because
    the EMA has not yet seen a full window of data.
    """

    def __init__(self, window: int) -> None:
        if window < 1:
            raise ValueError("window must be >= 1")
        self.window = window
        self.alpha = 2.0 / (window + 1.0)
        self._ema: Optional[float] = None
        self._count = 0

    def update(self, value: float) -> Optional[float]:
        """Add *value* and return the current EMA, or ``None`` during warm-up."""
        if self._ema is None:
            self._ema = value
        else:
            self._ema = self.alpha * value + (1.0 - self.alpha) * self._ema
        self._count += 1
        if self._count < self.window:
            return None
        return self._ema

    def compute(self, values: Iterable[float]) -> List[Optional[float]]:
        """Return the EMA for each value in *values*."""
        return [self.update(v) for v in values]
