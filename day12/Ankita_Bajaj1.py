import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 20.0, 10000)
#print(incomes)

plt.hist(incomes,50)

print(incomes.std())
print(incomes.var())

incomes=np.append(incomes,1100900)
print("after adding delimiters : ")
print(incomes.std())
print(incomes.var())
