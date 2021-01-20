# Import Decimal below:
import decimal

# Fix the floating point math below:
getcontext().prec = 2
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)
# 0.8899999999999999


getcontext().prec = 4
four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)
# 0.34450000000000003
