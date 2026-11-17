"""Moving average utilities.

Exports :class:`SimpleMovingAverage` and :class:`ExponentialMovingAverage`.
"""

from .core import ExponentialMovingAverage, SimpleMovingAverage

__all__ = ["SimpleMovingAverage", "ExponentialMovingAverage"]
