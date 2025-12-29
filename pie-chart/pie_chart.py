import matplotlib.pyplot as plt
import numpy as np

categories = ["Rent", "Food", "Transportation", "Savings", "Entertainment"]
expenses = np.array([1200, 450, 200, 350, 150])

colors = ["#a4dfcc", "#90ceba", "#7db6a3", "#6ba998", "#54927d"]

plt.pie(expenses,
        labels=categories,
        autopct="%1.1f%%",
        explode=[0.05, 0, 0, 0, 0],
        colors=colors)

plt.title("Monthly Expense Breakdown")

plt.savefig("sample_output.png")

plt.show()
