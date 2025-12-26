import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2021, 2022, 2023, 2024])
attendance = np.array([120, 135, 150, 145, 160])

plt.plot(years, attendance, marker="o")

plt.title("Student Attendance Over Time",
          fontsize=22,
          fontweight="bold")

plt.xlabel("Year", fontsize=16)
plt.ylabel("Students", fontsize=16)

plt.xticks(years)

plt.subplots_adjust(bottom=0.15, left=0.15)

plt.savefig("sample_output.png")

plt.show()
