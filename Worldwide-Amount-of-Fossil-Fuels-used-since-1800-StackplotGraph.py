#Version 1.0, updated 20/3/2025
import matplotlib.pyplot as plt
import numpy as np
years = [1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]
coal = [7, 9, 12, 17, 28, 45, 82, 131, 207, 309, 480, 731, 712, 816, 898, 925, 1252, 1387, 1748, 2146, 2116]
natural_gas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 11, 19, 46, 67, 153, 374, 815, 1158, 1618, 2026]
oil = [0, 0, 0, 0, 0, 0, 0, 1, 3, 10, 25, 53, 91, 207, 292, 505, 1030, 2237, 3010, 3135, 3542]
biomass = [298, 323, 352, 375, 403, 438, 459, 476, 518, 555, 581, 599, 589, 576, 558, 545, 608, 643, 789, 938, 1096]
plt.plot([], [], color='blue', label="Coal")
plt.plot([], [], color='red', label="Natural Gas")
plt.plot([], [], color='green', label="Oil")
plt.stackplot(years, coal, natural_gas, oil, biomass, baseline='zero', colors=['blue', 'red', 'green'])
ax.stackplot(x, y)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
plt.legend()
plt.title("Amount of Fossil Fuels consumed since 1800")
plt.xlabel("Years")
plt.ylabel("Fossil Fuels used (in Mtoe)")
plt.show()
