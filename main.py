import pandas as pd
import pandas_ta as ta
import numpy as np

# Tạo dữ liệu mẫu
data = {
    'open': [100, 102, 101, 105, 107, 110, 108, 109, 112, 111],
    'high': [103, 104, 106, 108, 110, 112, 111, 113, 114, 115],
    'low': [99, 100, 98, 102, 104, 108, 107, 108, 110, 109],
    'close': [101, 103, 100, 107, 109, 111, 109, 110, 113, 112],
    'volume': [1000, 1500, 1300, 1700, 1600, 1800, 1400, 1500, 1900, 2000]
}

df = pd.DataFrame(data)

# Tính RSI (Relative Strength Index)
df['RSI'] = ta.rsi(df['close'], length=5)

# Tính ATR (Average True Range)
df['ATR'] = ta.atr(high=df['high'], low=df['low'], close=df['close'], length=5)

# Tính CMF (Chaikin Money Flow)
df['CMF'] = ta.cmf(high=df['high'], low=df['low'], close=df['close'], volume=df['volume'], length=5)

# Hiển thị kết quả
print(df[['close', 'RSI', 'ATR', 'CMF']])
