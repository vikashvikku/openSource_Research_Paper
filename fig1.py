import matplotlib.pyplot as plt
import numpy as np

# A line graph showing the rise in OSS adoption over the years 
# will support your claim about the growing impact of OSS on innovation.
years = np.arange(2005, 2025, 2)  
adoption_rates = [5, 12, 25, 45, 65, 78, 90, 95, 98, 99]  

plt.figure(figsize=(8, 5))
plt.plot(years, adoption_rates, marker='o', linestyle='-', color='b', label="OSS Adoption Rate")
plt.xlabel("Year")
plt.ylabel("OSS Adoption Rate (%)")
plt.title("OSS Adoption Trends Over Time")
plt.grid(True)
plt.legend()
plt.show()
