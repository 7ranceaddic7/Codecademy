hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

sum_price = 0
total_revenue = 0

for price in prices:
  sum_price += price

avg_price = sum_price/len(prices)
print("Average Haircut Price: $" + str(avg_price))

new_prices = [price-5 for price in prices]
print("New Prices: " + str(new_prices))

for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
  
print("Total revenue: $" + str(total_revenue))
print("Average Daily Revenue: $" + str(total_revenue / len(last_week)))

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i]<30]
print(cuts_under_30)