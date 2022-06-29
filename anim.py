from time import time
import wave
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from pyparsing import line


# Function này đưa ra tọa độ các điểm cần vẽ
def Gen_Wave(length, dims=2):
    wave_coordinate = []
    for i in range(length):
        time_coordinate = {}
        x = np.empty(length)
        y = np.empty(length)
        z = np.empty(length)
        time_coordinate['x'] = x
        time_coordinate['y'] = y
        time_coordinate['z'] = z
    return wave_coordinate


# Function này sẽ update từng frame
# Vỡi mỗi step (ứng với num), đồ thị sẽ clear những cái đã vẽ trước
# và tất cả các điểm trong coordinate[num]
def update_lines(num, coordinate):
    ax.cla()
    ax.set_xlim3d([-100, 100.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-100, 100.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-100, 100])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')
    curr_coordinate = coordinate[num]
    ax.scatter3D(curr_coordinate['x'],
                 curr_coordinate['y'],
                 curr_coordinate['z'],
                 cmap='gray')


wave_coordinate = Gen_Wave(length=1000, dims=3)

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, frames=50,
                                   fargs=wave_coordinate,
                                   interval=100, blit=False)

plt.show()
