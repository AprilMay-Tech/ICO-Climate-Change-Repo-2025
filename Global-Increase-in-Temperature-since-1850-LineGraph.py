#Version 1.0, updated 20/3/2025
import matplotlib.pyplot as plt
x = [1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
y = [-0.17, -0.16, -0.29, -0.39, -0.35, 0.03, -0.40, -0.20, -0.23, 0.12, -0.21, 0.15, 0.21, 0.46, 0.40, 0.54, 0.83, 1.21]
f = plt.figure()
f.set_figwidth(10)
f.set_figheight(5)
plt.plot(x, y, marker='o', markerfacecolor="black", linestyle='-', color="black", label="Average Temperature")
plt.title("Increase of Global Temperature in Celcius")
plt.xlabel("Years")
plt.ylabel("Rate of Temperature Increase (in Celcius)")
plt.legend()
plt.grid(True)
plt.show()
