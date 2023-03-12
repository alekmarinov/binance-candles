# Binance Candles

Provides python generator for crypto currency candles via Binance Socket API

## CandlesGenerator example

```
from binance_candles import candles_generator

# 1 min candles generator for symbol BTCUSDT
for candles in candles_generator(symbols=["BTCUSDT"], interval=60):
    print(",".join(map(str, candles)))
```
