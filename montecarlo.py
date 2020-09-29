from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib notebook

test = []
pi_list = []
n_circle = 0
n_square = 0
num = 100000
R = 1
theta = np.linspace(0, 2*np.pi, 100)


for i in range(num):
    x = np.random.uniform(-1.0, 1.0)
    y = np.random.uniform(-1.0, 1.0)
    dis = x*x + y*y - R*R
    if(dis <= 0):
        n_circle += 1
    else:
        n_square += 1
    pi = (4 * n_circle) / ((n_circle + n_square) * R*R)
    pi_list.append(pi)
    test.append([x, y])

r = np.sqrt(1.0)


def animate(i):
    ax.scatter(test[i][0], test[i][1], 10, color='red')
    plt.text(0.3, 1.05, "pi = {}".format(pi_list[i]),
             transform=plt.gca().transAxes)
    # graph.set_data(test[i][0], test[i][1])
    # return graph


x1 = r*np.cos(theta)
x2 = r*np.sin(theta)
fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)
graph, = plt.plot([], [], 'o')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.grid(linestyle='--')
ani = FuncAnimation(fig, animate, frames=1000, interval=200)
plt.show()
