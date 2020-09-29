import numpy as np
import pylab as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
sax = plt.axes([0.25, 0.1, 0.65, 0.03])

x = np.linspace(0, 2.*np.pi, 100)
f = np.sin(x)
l, = ax.plot(x, f)

slider1 = Slider(sax, 'amplitude', -0.8, 0.8, valinit=0.8)

tpos = int(0.25*x.shape[0])
t1 = ax.text(x[tpos], f[tpos],  str(slider1.val))

tpos = int(0.75*x.shape[0])
t2 = ax.text(x[tpos], f[tpos],  str(slider1.val))


def update(val):
    f = slider1.val*np.sin(x)
    l.set_ydata(f)

    # update the value of the Text object
    tpos = int(0.25*x.shape[0])
    t1.set_position((x[tpos], f[tpos]))
    t1.set_text(str(slider1.val))

    tpos = int(0.75*x.shape[0])
    t2.set_position((x[tpos], f[tpos]))
    t2.set_text(str(slider1.val))

    plt.draw()


slider1.on_changed(update)
plt.show()
