import pandas as pd
from sqlalchemy import create_engine

orders = pd.read_csv('data/orders.csv')
order_product = pd.read_csv('data/order_product.csv')
shoppers = pd.read_csv('data/shoppers.csv')
storebranch = pd.read_csv('data/storebranch.csv')

engine = create_engine('postgresql://nicolas:000@localhost:5432/cornershop')

orders.to_sql("orders", engine)
order_product.to_sql("order_product", engine)
shoppers.to_sql("shoppers", engine)
storebranch.to_sql("storebranch", engine)