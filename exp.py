import pandas as pd

df=pd.read_csv('./dirty_cafe_sales.csv')
# print("Original shape:", df.shape)
# print(df)
# print(df.info())
# df['age']=df['age'].astype('int64') ------> Error

# df['age'] = pd.to_numeric(df['age'], errors='coerce')
# print(df)
# df['age']=df['age'].fillna(0)
# print(df)
# a={
#        'twenty five': 25,
#     'twenty six': 26,
#     'NaN': 0

# }
# df['age']=df['age'].replace(a,inplace=True)
# df['age']=df['age'].fillna(0,inplace=True)
# df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['age']=df['age'].fillna(df['age'].median())
df['age']=df['age'].astype('int64')







