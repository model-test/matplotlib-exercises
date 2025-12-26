import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2021, 2022, 2023, 2024])

product_a = np.array([50, 60, 75, 70, 90])
product_b = np.array([40, 55, 65, 80, 85])

custom_style = dict(
    marker="o",
    markersize=10,
    linestyle="dotted",
    linewidth=2
)

plt.plot(years, product_a, color="#0037ff", **custom_style)
plt.plot(years, product_b, color="#ff3700", **custom_style)

plt.title("Product Sales Over Time")
plt.xlabel("Year")
plt.ylabel("Units Sold (by thousands)")

plt.savefig("sample_output.png")

plt.show()
