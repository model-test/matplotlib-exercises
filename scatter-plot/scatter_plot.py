import matplotlib.pyplot as plt
import numpy as np

sleep_students = np.array([4, 5, 6, 7, 6, 8, 5, 7])
productivity_students = np.array([50, 55, 65, 70, 68, 75, 60, 72])

sleep_workers = np.array([5, 6, 7, 8, 6, 7, 9, 8])
productivity_workers = np.array([60, 65, 70, 78, 68, 72, 85, 80])

plt.scatter(sleep_students, productivity_students,
            color="#49759C",
            alpha=0.5,
            s=200,
            label="Students")

plt.scatter(sleep_workers, productivity_workers,
            color="#BB3F3F",
            alpha=0.5,
            s=200,
            label="Workers")

plt.title("Sleep vs. Productivity")
plt.xlabel("Hours of Sleep")
plt.ylabel("Productivity")

plt.legend()

plt.savefig("sample_output.png")

plt.show()
