import matplotlib.pyplot as plt
import numpy as np

hours_studied = np.array([1, 2, 3, 4, 5, 6])
test_scores   = np.array([50, 55, 65, 70, 78, 85])
attendance    = np.array([90, 88, 92, 95, 94, 96])
study_groups  = ["Low", "Medium", "High"]
group_sizes   = [15, 25, 10]

figure, axes = plt.subplots(2, 2)

# Subplot 1 (Line Plot)
axes[0, 0].plot(hours_studied, test_scores,
                marker="o")
axes[0, 0].set_xlabel("Hours")
axes[0, 0].set_ylabel("Score")
axes[0, 0].set_title("Test Score vs Study Time")

# Subplot 2 (Scatter Plot)
axes[0, 1].scatter(hours_studied, attendance,
                   color="red")
axes[0, 1].set_xlabel("Hours")
axes[0, 1].set_ylabel("Attendance")
axes[0, 1].set_title("Attendance vs Study Time")

# Subplot 3 (Histogram)
axes[1, 0].hist(test_scores,
                bins=4,
                color="purple",
                edgecolor="black")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Students")
axes[1, 0].set_title("Score Distribution")

# Subplot 4 (Bar Chart)
axes[1, 1].bar(study_groups, group_sizes,
               color="green")
axes[1, 1].set_xlabel("Study Groups")
axes[1, 1].set_ylabel("Members")
axes[1, 1].set_title("Study Group Sizes")

plt.tight_layout()
plt.savefig("sample_output.png")
plt.show()
