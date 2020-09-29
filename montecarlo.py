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
fig, ax = plt.subplots(1)

for i in range(num):
    x = np.random.uniform(-1.0, 1.0)
    y = np.random.uniform(-1.0, 1.0)
    dis = x*x + y*y - R*R
    type_point = 0
    if(dis <= 0):
        n_circle += 1
        type_point = 1
    else:
        n_square += 1
    pi = (4 * n_circle) / ((n_circle + n_square) * R*R)
    pi_list.append(pi)
    test.append([x, y, type_point])

r = np.sqrt(1.0)
t = ax.text(0.3, 1.05,  "0")


def animate(i):
    # ax.set_visible(True)
    if(test[i][2]):
        ax.scatter(test[i][0], test[i][1], 10, color='red')
    else:
        ax.scatter(test[i][0], test[i][1], 10, color='blue')
    # if(i == 0):
    #     text = plt.text(0.3, 1.05, "Some text")
    # else:
    t.set_text(str(pi_list[i]))

    plt.draw()
    # ax.set_visible(False)
    # fig.text.remove()
    # graph.set_data(test[i][0], test[i][1])
    # return graph


x1 = r*np.cos(theta)
x2 = r*np.sin(theta)


ax.plot(x1, x2)
ax.set_aspect(1)
graph, = plt.plot([], [], 'o')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.grid(linestyle='--')
ani = FuncAnimation(fig, animate, frames=num, interval=1)
plt.show()
