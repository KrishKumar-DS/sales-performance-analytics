import pandas as pd

file_path = "data/sales_data.csv"
# df = DataFrame
# reada_csv reads the csv file and loads its data into a pandas DataFrame(Like a table)
df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
# To get some specific data by column
# print("df['colmun_name']")


#  .shape tells the number of rows and columns
# print("\nShape: ")
# print(df.shape)


#  .columns returns the columns labels, and the .tolist() convert those columns into a normal Python list.
# print("\nColumns:")
# print(df.columns.tolist())


#  .dtypes tells the data type of each column, so we can decide which operations should we use in which column
# print("Data Types:")
# print(df.dtypes)


#  .isnull() & .isna() are used to check whether values are missing, it produces a Boolean table, false->Value exist | true->value is missing
#  .sum() is used to count every missing values for every column
# print("\nMissing Values:")
# print(df.isnull().sum())
# print(df['Order_Date'].isnull().sum())


#  .head() displays the first 5 rows by default, but we can also specify how many df.head(10)
# print("\nFirst 5 Rows:")
# print(df.head(10))


#  .tail() display the last 5 rows by default, but we can also specify how many df.tail(10)
# print("\nLast 5 Rows:")
# print(df.tail(10))


#  .nunique() means number of unique values
# print("\nUnique values:")
# print(df.nunique())


#  .duplicated() checks each entire row against previous rows
# print("Duplicate Rows")
# print(df.duplicated().sum())

#  To check whether all oder_id is unique
# print("Duplicate Order ID")
# print(df['Order_ID'].duplicated().sum())


dates = pd.to_datetime(
    df['Order_Date'],
    format="%d-%m-%Y",
    errors="coerce"
)

# print("Invalid Dates:", dates.isna().sum())

# Validate numeric columns

# numeric_colmuns = [
#     "Quantity",
#     "Unit_Price",
#     "Discount_Percent",
#     "Revenue",
#     "Cost",
#     "Profit"
# ]

# print(df[numeric_colmuns].dtypes)

# print(df.columns.tolist())
# print(df.dtypes)


# To check whether any value is negative or more than it should be
# print(f"Min Qty: {df['Quantity'].min()}")
# print(f"Max Qty: {df['Quantity'].max()}")
# print(f"Min Unit Price: {df['Unit_Price'].min()}")
# print(f"Max Unit Price: {df['Unit_Price'].max()}")
# print(f"Min Discount: {df['Discount_Percent'].min()}")
# print(f"Max Discount: {df['Discount_Percent'].max()}")
# print(f"Min Revenue: {df['Revenue'].min()}")
# print(f"Max Revenue: {df['Revenue'].max()}")
# print(f"Min Cost: {df['Cost'].min()}")
# print(f"Max Cost: {df['Cost'].max()}")
# print(f"Min Profit: {df['Profit'].min()}")
# print(f"Max Profit: {df['Profit'].max()}")


# Continue from this
# invalid_quantity = df[df['Quantity'] <= 0]
# print(f"Invalid Quantity:{len(invalid_quantity)}")
# print(invalid_quantity)

# invalid_price = df[df['Unit_Price'] <= 0]
# print(f"Invalid Price: {len(invalid_price)}")
# print(invalid_price)

# In Pandas we use '|' instead of 'or' and '&' instead of 'AND'
# invalid_discount = df[(df['Discount_Percent'] < 0) |
#                       (df['Discount_Percent'] >= 100)
#                       ]
# print(f"Invalid Discount: {len(invalid_discount)}")
# print(invalid_discount)

# invalid_dates = dates.isna().sum()
# print(invalid_dates)


# expected_revenue = (df['Quantity']*df['Unit_Price'] * (1-df['Discount_Percent']/100))
# revenue_difference = df['Revenue'] - expected_revenue

# print("\nRevenue")
# print(revenue_difference)

# invalid_revenue = df[abs(revenue_difference) > 0.01]
# print(f"Invalid Revenue: {len(invalid_revenue)}")

# print(invalid_revenue)


# profit_difference = df['Profit'] - (df['Revenue'] - df['Cost'])
# print("---PROFIT DIFFERENCE---")
# print(profit_difference)

# print("\nINVALID PROFIT\n")

# invalid_profit = df[abs(profit_difference) > 0.01]
# print(invalid_profit)


invalid_cost = df[df['Cost'] <= 0]
print("Invalid Cost:", len(invalid_cost))
print(invalid_cost)
