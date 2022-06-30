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


# Function này generate ra tọa độ x, y, z của các điểm cần vẽ
# cho mỗi timestep (mỗi num)
def Gen_Wave(num):
    x = np.arange(-max_X, max_X, 0.1)
    y = np.arange(-max_X, max_X, 0.1)
    xgrid, ygrid = np.meshgrid(x, y)
    distance = np.sqrt(xgrid ** 2 + ygrid ** 2)
    zgrid = A*np.cos(-w*distance+num*wt+Fi)
    zgrid[zgrid < 0] = 0
    # print(zgrid)
    return {
        'x': xgrid,
        'y': ygrid,
        'z': zgrid
    }


# Function này sẽ update từng frame
# Vỡi mỗi step (ứng với num), đồ thị sẽ clear những cái đã vẽ trước
# và vẽ các điểm trong gen_wave
def update_lines(num):
    ax.cla()
    ax.set_xlabel('X')

    ax.set_ylabel('Y')

    ax.set_zlim3d([-1, 1])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')
    coordinate = Gen_Wave(num=num)
    ax.plot_surface(coordinate['x'],
                    coordinate['y'],
                    coordinate['z'],
                    cmap='gray')


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, frames=50,
                                   interval=10, blit=False)

plt.show()
