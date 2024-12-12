import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4)
y = (np.sin(10*x) * np.sin(3*x)) / x**2

plt.title('Графік', fontsize=15)
plt.plot(x, y, 'b', label="Графік функції f(x)")
plt.xlabel('X', fontsize=12, color='blue')
plt.ylabel('Y', fontsize=12, color='blue')

plt.legend()
plt.grid()
plt.show()
