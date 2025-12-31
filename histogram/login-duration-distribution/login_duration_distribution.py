import matplotlib.pyplot as plt
import numpy as np

login_minutes = np.array([
    3, 4, 5, 5, 6, 6, 7, 8, 9, 10,
    12, 14, 16, 20, 25, 30, 45
])
login_minutes = np.clip(login_minutes, np.min(login_minutes), np.max(login_minutes))

plt.hist(login_minutes,
         bins=5,
         color="#BB3F3F",
         edgecolor="black")

plt.title("Login Duration")
plt.xlabel("Minutes")
plt.ylabel("# of Users")

plt.savefig("login_duration_distribution.png")

plt.show()
