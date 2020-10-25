from utils.arrays import is_symmetric
from airfoil_points.read_txt import TxtReader
import matplotlib.pyplot as plt

file = "airfoil_points/naca0008.txt"

txt = TxtReader(file)
foil_points = txt.read_x_y()
fig, ax = plt.subplots()
ax.set_aspect("equal", "box")
ax.plot(foil_points[0], foil_points[1])
# plt.show()
print(is_symmetric(foil_points[1]))
