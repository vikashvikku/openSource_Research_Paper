import matplotlib.pyplot as plt
import numpy as np

# OSS vs Proprietary Software Comparison (Bar Chart) for Literature Review
categories = ["Cost Savings", "Flexibility", "Security", "Community Support", "Customization"]
oss_values = [90, 85, 70, 95, 88]  
proprietary_values = [40, 50, 85, 60, 45]  

x = np.arange(len(categories)) 
plt.figure(figsize=(8, 5))
plt.bar(x - 0.2, oss_values, width=0.4, label="Open-Source Software", color='green')
plt.bar(x + 0.2, proprietary_values, width=0.4, label="Proprietary Software", color='blue')

plt.xlabel("Factors")
plt.ylabel("Advantage (%)")
plt.title("Comparison of OSS vs Proprietary Software")
plt.xticks(ticks=x, labels=categories, rotation=20)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
