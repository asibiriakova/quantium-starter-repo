import pandas as pd
import numpy


def df_normalise(df_raw):
    df_norm = df_raw.query('product == "pink morsel"')
    df_norm['price'] = df_norm['price'].replace(r'[\$,]', '', regex=True).astype(float)

    df_norm['Sales'] = df_norm['price'] * df_norm['quantity']
    df_norm = df_norm.rename(columns={"date": "Date", "region": "Region"})
    df_norm['Year'] = pd.DatetimeIndex(df_norm['Date']).year
    df_norm['Date'] = pd.to_datetime(df_norm['Date'])
    df_norm['Month'] = (df_norm['Date'].dt.floor('d') + pd.offsets.MonthEnd(0) - pd.offsets.MonthBegin(1))

    return df_norm[['Sales', 'Date', 'Region', 'Year', 'Month']]


df_0 = pd.read_csv('data/daily_sales_data_0.csv')
df_1 = pd.read_csv('data/daily_sales_data_1.csv')
df_2 = pd.read_csv('data/daily_sales_data_2.csv')

df_0_norm = df_normalise(df_0)
df_1_norm = df_normalise(df_1)
df_2_norm = df_normalise(df_2)

frames = [df_0_norm, df_1_norm, df_2_norm]

result = pd.concat(frames)

result.to_csv('data/daily_sales.csv', index=False)
