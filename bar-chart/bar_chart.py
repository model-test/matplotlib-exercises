import matplotlib.pyplot as plt
import numpy as np

departments = ["Engineering", "Marketing", "Sales", "HR", "Support"]
headcount = np.array([18, 12, 15, 6, 9])

plt.barh(departments, headcount, color="#33b1ff")

plt.title("Company Headcount by Department", size=18)
plt.xlabel("Number of Employees", size=15)
plt.ylabel("Department", size=15)

plt.grid(axis="x", color="lightgray", alpha=0.5)

plt.subplots_adjust(bottom=0.17, left=0.17)

plt.savefig("sample_output.png")

plt.show()
