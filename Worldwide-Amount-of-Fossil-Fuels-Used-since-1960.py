#Version 1.0, updated 20/3/2025

x = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
x1 = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
x2 = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
x3 = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
x4 = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
x5 = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
x6 = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
x7 = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
y = [78, 85, 82, 84, 84, 82, 80]
y1 = [97, 98, 94, 93, 89, 85, 75]
y2 = [80, 85, 70, 65, 60, 55, 50]
y3 = [80, 85, 90, 92, 93, 91, 85]
y4 = [85, 90, 92, 93, 95, 94, 90]
y5 = [85, 88, 85, 88, 90, 85, 90]
y6 = [95, 98, 98, 98, 98, 98, 97]
y7 = [95, 97, 98, 96, 95, 91, 90]
f = plt.figure()
f.set_figwidth(10)
f.set_figheight(5)
plt.plot(x, y, marker='o', linestyle='-', color="red", label="America")
plt.plot(x1, y1, marker='o', linestyle='-', color="red", markerfacecolor="blue", label="UK")
plt.plot(x2, y2, marker='o', linestyle='-', color="blue", markerfacecolor='r', label="France")
plt.plot(x3, y3, marker='o', linestyle='-', color="pink", label="China")
plt.plot(x4, y4, marker='o', linestyle='-', color="orange", label="India")
plt.plot(x5, y5, marker='o', linestyle='-', color="red", markerfacecolor='w', label="Japan")
plt.plot(x6, y6, marker='o', linestyle='-', color="green", markerfacecolor='w', label="Nigeria")
plt.plot(x7, y7, marker='o', linestyle='-', color="green", markerfacecolor='r', label="South Africa")
plt.title("Amount of Fossil Fuels used since 1960")
plt.xlabel("Years")
plt.ylabel("Tons of Fossil Fuel Used (In Percent)")
plt.legend()
plt.grid(True)
plt.show()
