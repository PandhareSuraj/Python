import pandas as pd

df = pd.DataFrame(columns=['company','model','year'])

df.loc[0] = ['TATA', 'Nexon', 2017]
df.loc[1] = ['MG', 'Astor', 2021]
df.loc[2] = ['KIA', 'Seltos', 2019]
df.loc[3] = ['Hyundai', 'Creta', 2015]

print(df)