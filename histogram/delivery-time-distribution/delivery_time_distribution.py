import matplotlib.pyplot as plt
import numpy as np

delivery_times = np.array([
    12, 13, 14, 15, 16, 17, 18, 18, 19, 20,
    21, 22, 23, 25, 27, 30, 35, 40, 50
])
delivery_times = np.clip(delivery_times, np.min(delivery_times), np.max(delivery_times))

plt.hist(delivery_times,
         bins=6,
         color="#87CEEB",
         edgecolor="black")

plt.title("Delivery Times")
plt.xlabel("Minutes")
plt.ylabel("# of Deliveries")

plt.savefig("delivery_time_distribution.png")

plt.show()
