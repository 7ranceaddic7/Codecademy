## NOTES ##
# each_transaction = [name of the customer   ;,;amount spent   ;,;types of thread purchased   ;,;date of sale   ,]
# 

from ThreadShed_DailySales import daily_sales

# what we got, WWG
# print(daily_sales)

# massage out the ';,;' delimiter
daily_sales_replaced = daily_sales.replace(';,;', ':').replace('\n', '')
# print("daily_sales_replaced")
# print(daily_sales_replaced)
# print("\n")

# transactions as a list of lists
daily_transactions = daily_sales_replaced.split(',')
# WWG
# print("daily_transactions")
# print(daily_transactions)
# print(daily_transactions[0])
# print("\n")

# cleanup transaction data
daily_transactions_split = []
for each in daily_transactions:
  daily_transactions_split.append(each.split(":"))
# print("daily_transactions_split")
# print(daily_transactions_split)

transactions_clean = []
for transactions in daily_transactions_split:
  each_transaction = []
  for item in transactions:
    each_transaction.append(item.strip())
  transactions_clean.append(each_transaction)
print("transactions_clean")
print(transactions_clean)
print('\n')

# database creation: customers, sales, thread_sold
customers = []
sales = []
thread_sold = []
for each in transactions_clean:
  customers.append(each[0])
  sales.append(each[1])
  thread_sold.append(each[2])
print("ThreadShed Databases")
print(customers)
print(sales)
print(thread_sold)
print('\n')

# Day sales
total_daily_sales = 0
for sale in sales:
  # print(sale.strip('$'))
  total_daily_sales += float(sale.strip('$'))
print("total_daily_sales")
print('${:,.2f}'.format(total_daily_sales))
print('\n')

# Thread sales
color_sold = []
for sale in thread_sold:
  for color in sale.split('&'):
    color_sold.append(color)
print("color_sold")
print(color_sold)
print('\n')

def color_count(color):
  color_total = 0
  for thread_color in color_sold:
    if color == thread_color:
      color_total += 1
  return color_total

colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

for color in colors:
  print(
    "Thread Shed sold {count} spools of {color} thread today."
    .format(count=color_count(color), color=color)
    )
