import pandas as pd




# 加载1分钟数据
# 读取原始 CSV 文件
input_file = '/Users/admin/.qlib/csv_data/mt5_data/vnpy.bar_data.csv'  # 替换为你的文件路径
df = pd.read_csv(input_file)

# 预处理数据


# 转换为5分钟数据
df_5min = df.resample('5T').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum',
    'macd': 'last',
    'macd_signal': 'last',
    'macd_hist': 'last',
    'rsi': 'last',
    'upper_band': 'last',
    'middle_band': 'last',
    'lower_band': 'last',
    'hour': 'last',
    'dayofweek': 'last',
    'month': 'last'
}).dropna()

# 保存5分钟数据
df_5min.to_csv('/Users/admin/.qlib/csv_data/forex_5min')

# # 转换为15分钟数据
# df_15min = df_1min_processed.resample('15T').agg({
#     'open': 'first',
#     'high': 'max',
#     'low': 'min',
#     'close': 'last',
#     'volume': 'sum',
#     'macd': 'last',
#     'macd_signal': 'last',
#     'macd_hist': 'last',
#     'rsi': 'last',
#     'upper_band': 'last',
#     'middle_band': 'last',
#     'lower_band': 'last',
#     'hour': 'last',
#     'dayofweek': 'last',
#     'month': 'last'
# }).dropna()

# # 保存15分钟数据
# df_15min.to_csv('data/processed/forex_15min.csv')

# # 转换为1小时数据
# df_1hour = df_1min_processed.resample('1H').agg({
#     'open': 'first',
#     'high': 'max',
#     'low': 'min',
#     'close': 'last',
#     'volume': 'sum',
#     'macd': 'last',
#     'macd_signal': 'last',
#     'macd_hist': 'last',
#     'rsi': 'last',
#     'upper_band': 'last',
#     'middle_band': 'last',
#     'lower_band': 'last',
#     'hour': 'last',
#     'dayofweek': 'last',
#     'month': 'last'
# }).dropna()

# # 保存1小时数据
# df_1hour.to_csv('data/processed/forex_1hour.csv')
