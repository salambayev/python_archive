import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
import numpy as np

y = [1, 1, 0, 0, 0, 0, 0]
y1 = [0, 0, 1, 0, 0, 0, 0]
y2 = [0, 0, 0, 1, 0, 0, 0]
y3 = [0, 0, 0, 0, 1, 1, 1]

x = [0, 10, 30, 50, 70, 90, 110]


plt.xlabel("Temp {F*}")
plt.grid(True)
plt.xlim(0, 110)
plt.ylim(-1, 2)

plt.plot(x, y, color="blue", label="Freezing")
blue_patch = mpatches.Patch(color='blue', label="Freezing")
plt.plot(x, y1, color="cyan", label="Cool")
cyan_patch = mpatches.Patch(color='cyan', label="Cool")
plt.plot(x, y2, color="yellow", label="Warm")
yellow_patch = mpatches.Patch(color='yellow', label="Warm")
plt.plot(x, y3, color="red", label="Hot")
red_patch = mpatches.Patch(color='red', label="Hot")
plt.legend(handles=[blue_patch, cyan_patch, yellow_patch, red_patch])
plt.show()
