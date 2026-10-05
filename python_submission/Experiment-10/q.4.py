# 4.	WAP to draw Pie Charts and Contour plots.
import matplotlib.pyplot as plt
import numpy as np

# ---------------- Pie Chart ----------------

labels = ["Python", "Java", "C", "HTML"]
sizes = [40, 25, 20, 15]

plt.figure()
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Programming Language Usage")
plt.show()


# ---------------- Contour Plot ----------------

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

plt.figure()
plt.contour(X, Y, Z)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Contour Plot")
plt.colorbar()
plt.show()
