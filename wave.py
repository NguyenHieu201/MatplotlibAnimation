# This file is used for test 3d wave

from time import time
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from pyparsing import line

L = 10
w = 2 * np.pi / L
S = 1
Fi = np.pi / 2
wt = S * 2 * np.pi / L
A = 0.5

max_X = 40

# Function này đưa ra tọa độ các điểm cần vẽ


def Gen_Wave(num):
    x = np.arange(-max_X, max_X, 0.1)
    y = np.arange(-max_X, max_X, 0.1)
    xgrid, ygrid = np.meshgrid(x, y)
    distance = np.sqrt(xgrid ** 2 + ygrid ** 2)
    zgrid = A*np.cos(-w*distance+num*wt+Fi)
    # print(zgrid)
    return {
        'x': xgrid,
        'y': ygrid,
        'z': zgrid
    }


coordinate = Gen_Wave(0)
xgrid = coordinate['x']
ygrid = coordinate['y']
zgrid = coordinate['z']

zgrid[zgrid < 0] = 0

fig = plt.figure()
ax = p3.Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

ax.plot_surface(xgrid, ygrid, zgrid, cmap='gray')
ax.set_zlim(-2, 2)

plt.show()
