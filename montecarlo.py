import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

theta = np.linspace(0, 2*np.pi, 100)

r = np.sqrt(1.0)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)
fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)
graph, = plt.plot([], [], 'o')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.grid(linestyle='--')
plt.show()
