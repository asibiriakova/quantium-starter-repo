import pandas as pd

def df_normalise(df_raw):
    df_norm = df_raw.query('product == "pink morsel"')
    df_norm['price'] = df_norm['price'].replace(r'[\$,]', '', regex=True).astype(float)

    df_norm['Sales'] =  df_norm['price'] * df_norm['quantity']
    df_norm = df_norm.rename(columns={"date": "Date", "region": "Region"})

    return df_norm[['Sales','Date','Region']]

df_0 = pd.read_csv('data/daily_sales_data_0.csv')
df_1 = pd.read_csv('data/daily_sales_data_1.csv')
df_2 = pd.read_csv('data/daily_sales_data_2.csv')


df_0_norm = df_normalise(df_0)
df_1_norm = df_normalise(df_1)
df_2_norm = df_normalise(df_2)

frames = [df_0_norm, df_1_norm, df_2_norm]

result = pd.concat(frames)

result.to_csv('data/daily_sales.csv', index=False)
