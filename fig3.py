import matplotlib.pyplot as plt
import numpy as np
# 3. Economic Impact of OSS (Pie Chart)
labels = ["Cost Savings", "Investment in R&D", "Job Creation", "Support Services", "Market Growth"]
values = [40, 20, 15, 15, 10]  # Hypothetical distribution of economic benefits

plt.figure(figsize=(5, 4))
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple', 'orange'], startangle=140)
plt.title("Economic Impact of OSS")
plt.show()
