import matplotlib.pyplot as plt
import numpy as np

screen_time = np.array([
    1.5, 2.0, 2.2, 2.5, 3.0, 3.1, 3.5, 4.0, 4.2, 4.5,
    5.0, 5.5, 6.0, 6.2, 6.5, 7.0, 7.5, 8.0, 9.0, 10.0
])
screen_time = np.clip(screen_time, np.min(screen_time), np.max(screen_time))

plt.hist(screen_time,
         bins=8,
         color="#D89090",
         edgecolor="black")

plt.title("Screen Time Distribution",
          size=20)
plt.xlabel("Hours",
           size=13)
plt.ylabel("# of Users",
           size=13)

plt.savefig("screen_time_distribution.png")

plt.show()
