import matplotlib.pyplot as plt
import numpy as np

# Survey Results on OSS Challenges and Benefits (Bar Chart)
factors = ["Cost Savings", "Innovation Potential", "Security Concerns", "Ease of Integration"]
positive_impact = [78, 82, 30, 45]  # % of users reporting benefits
challenges = [10, 8, 60, 50]  # % of users reporting challenges

x = np.arange(len(factors))

plt.figure(figsize=(8, 5))
plt.bar(x - 0.2, positive_impact, width=0.4, label="Positive Impact", color='blue')
plt.bar(x + 0.2, challenges, width=0.4, label="Challenges", color='red')
plt.xlabel("Factors")
plt.ylabel("Percentage of Users (%)")
plt.title("Survey Results: OSS Challenges vs Benefits")
plt.xticks(ticks=x, labels=factors, rotation=20)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
