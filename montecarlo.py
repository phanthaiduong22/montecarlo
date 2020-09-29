%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
theta = np.linspace(0, 2*np.pi, 100)

for i in range(100): 
    test.append([np.random.uniform(-1.0, 1.0), np.random.uniform(-1.0, 1.0)])

r = np.sqrt(1.0)

def animate(i):
    ax.scatter(test[i][0], test[i][1], 10, color='red')
    #graph.set_data(test[i][0], test[i][1])
    #return graph
    
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)
fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)
graph, = plt.plot([], [], 'o')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.grid(linestyle='--')
ani = FuncAnimation(fig, animate, frames=1000, interval=200)
plt.show()
