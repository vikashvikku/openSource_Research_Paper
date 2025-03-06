import matplotlib.pyplot as plt
import numpy as np

# 5. Skill Development through OSS Participation (Stacked Bar Chart)
skills = ["Coding", "Problem-Solving", "Collaboration", "Project Management", "Security Awareness"]
oss_contribution = [85, 75, 80, 70, 65]  # Percentage of users gaining these skills through OSS
traditional_learning = [60, 50, 55, 65, 50]  # Percentage of users gaining these skills through traditional methods

x = np.arange(len(skills))

plt.figure(figsize=(5, 3))
plt.bar(x, traditional_learning, width=0.4, label="Traditional Learning", color='gray')
plt.bar(x, oss_contribution, width=0.4, bottom=traditional_learning, label="OSS Contribution", color='green')
plt.xlabel("Skills Developed")
plt.ylabel("Percentage of Users (%)")
plt.title("Skill Development through OSS Participation")
plt.xticks(ticks=x, labels=skills, rotation=20)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()
