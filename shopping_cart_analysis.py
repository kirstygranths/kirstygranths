import csv
import statistics
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

customers = pd.read_csv("shop_db_customers.csv")
print(customers.head())
print(customers.shape)

orders = pd.read_csv("shop_db_orders.csv")
print(orders.head())
print(orders.shape)

products = pd.read_csv("shop_db_products.csv")
print(products.head())
print(products.shape)

sales = pd.read_csv("shop_db_sales.csv")
print(sales.head())
print(sales.shape)

#excluding poducts
csv_list = [customers, orders, sales]

customer_orders = pd.merge(customers, orders, left_index=True, right_index=True)
print(customer_orders.head())
print(customer_orders.shape)

df = pd.merge(customer_orders, products, left_index=True, right_index=True)
print(df.head())
print(df.shape)
print(df.info())

#review age range of customers
max_age = df['age'].max()
min_age = df['age'].min()
ave_age = round(statistics.mean(df['age']))
print(f'Maximum customer age is:{max_age}.\n'
      f'Minimum customer age is:{min_age}.\n'
      f'Average customer age is:{ave_age}.')


#split customers into age category bins
bins = [0, 18, 34, 64, np.inf]
names = ["0-18", "19-34", "35-64", "65+"]

df['age_group'] = pd.cut(df['age'], bins, labels=names)
print(df.head())

#cust_order_prod.to_excel(r'C:\Users\kirst\PycharmProjects\kirstys-projects\Customer Order Data.xlsx', index = False)


