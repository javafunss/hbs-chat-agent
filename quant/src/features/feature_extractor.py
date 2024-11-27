import pandas as pd
import talib
from sklearn.preprocessing import MinMaxScaler


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    # 缺失值处理
    df.fillna(method='ffill', inplace=True)

    # 异常值检测
    z_scores = (df - df.mean()) / df.std()
    df = df[(z_scores < 3).all(axis=1)]

    # 数据标准化
    scaler = MinMaxScaler()
    df[['open', 'high', 'low', 'close', 'volume']] = scaler.fit_transform(df[['open', 'high', 'low', 'close', 'volume']])

    # 添加技术指标
    df['macd'], df['macd_signal'], df['macd_hist'] = talib.MACD(df['close'])
    df['rsi'] = talib.RSI(df['close'])
    df['upper_band'], df['middle_band'], df['lower_band'] = talib.BBANDS(df['close'])

    # 添加时间特征
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['month'] = df.index.month

    # 删除NA值
    df.dropna(inplace=True)
    return df
