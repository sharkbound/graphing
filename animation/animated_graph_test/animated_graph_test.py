from matplotlib import pyplot as plt, animation
from random import randint

fig: plt.Figure = plt.figure()
axis: plt.Axes = fig.add_subplot()

data = [randint(1, 10) for _ in range(100)]


def animate(i):
    global data
    data = [it + randint(-5, 0) for it in data]
    axis.clear()
    for i, v in enumerate(data):
        axis.bar([i], [v])


anim = animation.FuncAnimation(fig, animate, interval=300)
plt.show()
