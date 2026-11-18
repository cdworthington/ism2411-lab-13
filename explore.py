#1. A boolean filter is a way to select certain data by rows depending on whether they meet a certain condition.

#2. df["revenue"] returns a Series, which is a single column of data. df[["revenue"]] returns a DataFrame, which is a table containing that column. The difference is important when certain data needs to be contained in a DataFrame.

#3. Pandas is much more efficient than Excel for large datasets such as this. It allows me to filter out data that I do not need and gives me the data that is important for me to calculate.


import pandas as pd

print("___Exercise 1___")

df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("___Exercise 2___")

south = df[df['region'] == 'South']

print(len(south))
print(south.head())

print("___Exercise 3___")

top5 = df.sort_values('revenue', ascending=False).head(5)

print(top5)

print("___Exercise 4___")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())

print("___Exercise 5___")

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())

print("___Exercise 6___")
print(df['region'].unique())
print(df['region'].value_counts())

print("___Exercise 7___")

selected = df[['region', 'product', 'revenue']]

print(selected.shape)

print("___Exercise 8___")

df.to_csv('data/explored.csv', index=False)
