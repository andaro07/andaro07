import matplotlib.pyplot as plt
import numpy as np

#create an empty figure
fig = plt.figure(dpi=120)
ax = plt.axes()
x = np.linspace(0,10,1000)
ax.plot(x, np.sin(x));
plt.plot(x, np.sin(x), c='r', marker='o', mfc='r', linestyle='solid')
plt.plot(x, np.cos(x), c='b', marker='o', mfc='b', linestyle='solid')
plt.xlim(0,11)
plt.ylim(-2,2)
plt.axis('tight')
ax.set_facecolor('k')
plt.title('Graph of\nSin(x) against Cos(x)')
plt.legend(['Cos(x)',  'Sin(x)'], loc='lower left')
plt.grid(True, color='cyan')
plt.show()
#save the plot figure
#plt.savefig('first_figure.png')