import seaborn as sn
import matplotlib.pyplot as plt
import random

numbers_a = range(12)
numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)
plt.show()
