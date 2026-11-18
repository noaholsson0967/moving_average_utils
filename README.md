# moving_average_utils

Simple and exponential moving averages with warm-up handling.

```python
from moving_average_utils import SimpleMovingAverage, ExponentialMovingAverage

sma = SimpleMovingAverage(3)
print(sma.compute([1, 2, 3, 4]))  # [None, None, 2.0, 3.0]

ema = ExponentialMovingAverage(3)
print(ema.compute([1, 2, 3, 4]))  # [None, None, 2.25, 3.125]
```

## Why this exists

Streaming averages often need to signal when the result is not yet meaningful.
Rather than emitting a partial average or raising an error, these classes return
`None` until a full window of data has been observed. This makes it explicit
that the average is not yet available, which is safer than silently using an
incomplete window.

## Edge case

The first `window - 1` outputs are `None`. For a window of 1, the first output
is the first value itself, and no warm-up is needed.
