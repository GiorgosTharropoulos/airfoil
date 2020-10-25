from airfoil_points.points import TxtReader
import matplotlib.pyplot as plt

file = "airfoil_points/naca0008.txt"

txt = TxtReader(file)
foil_points = txt.read_x_y()
fig, ax = plt.subplots()
ax.set_aspect("equal", "box")
ax.plot(foil_points[0], foil_points[1])
plt.show()
