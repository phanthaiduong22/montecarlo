import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

f, axes = plt.subplots()
figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
draw_circle = plt.Circle((0.5, 0.5), 0.3)

axes.set_aspect(1)
axes.plot([0.5], [0.5], 'o')
axes.add_artist(draw_circle)
plt.title('Circle')
plt.show()
