import matplotlib.pyplot as plt
import numpy as np

# OSS Adoption Barriers and Solutions (Comparative Bar Chart)
barriers = ["Awareness", "Support & Maintenance", "Security Concerns", "Integration Issues", "Training Needs"]
percentage_barriers = [50, 55, 60, 50, 45]  # Percentage of users facing these barriers
percentage_solutions = [80, 75, 70, 65, 85]  # Effectiveness of solutions to overcome barriers

x = np.arange(len(barriers))

plt.figure(figsize=(8, 5))
plt.bar(x - 0.2, percentage_barriers, width=0.4, label="OSS Barriers", color='red')
plt.bar(x + 0.2, percentage_solutions, width=0.4, label="Proposed Solutions Effectiveness", color='green')
plt.xlabel("Barriers to OSS Adoption")
plt.ylabel("Percentage of Respondents (%)")
plt.title("OSS Adoption Barriers vs Solutions")
plt.xticks(ticks=x, labels=barriers, rotation=20)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
