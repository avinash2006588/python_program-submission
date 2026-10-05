# 3.	WAP to draw Histograms and Box plots.
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.normal(0, 1, 1000)

# Histogram
plt.hist(data, bins=30)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Box plot
plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("Value")
plt.show()
