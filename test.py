draw_circle = plt.Circle((0.5, 0.5), 0.3)

axes.set_aspect(1)
axes.plot([0.5], [0.5], 'o')
axes.add_artist(draw_circle)
plt.title('Circle')
plt.show()
