#Version 1.0, updated 20/3/2025
import matplotlib.pyplot as plt
import numpy as np
sources = ["Nonrenewable Energy", "Renewable Energy", "Nuclear Energy"]
data = [80, 10, 10]
colors = ("yellow", "orange", (0.3, 1, 0))
wp = {'linewidth': 1, 'edgecolor': "black"}
def func(pct, allvalues):
  absolute = int(pct / 100.*np.sum(allvalues))
  return "{:.1f}%".format(pct, absolute)
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(data,
                autopct=lambda pct: func(pct, data),
                labels=sources,
                shadow=True,
                colors=colors,
                startangle=90,
                wedgeprops=wp,
                textprops=dict(color="black"))
ax.legend(wedges, sources, title="Key", loc="center right", bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=8, weight="bold")
plt.title("World Power Supply Source in 2020")
plt.show()
