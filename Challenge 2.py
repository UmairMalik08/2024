from numpy import linspace
from math import sin, cos, tan, sqrt, radians
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title(" Q2. Projectile Trajectory")
ax.set_xlabel("x/m"), ax.set_ylabel("y/m")
plt.grid(color="black", linestyle="--", linewidth=0.3)
plt.gca().set_aspect("equal", adjustable="box")
plt.axis("auto")

launch_angle_degrees = float(input("Enter launch angle: "))
launch_speed = float(input("Enter launch speed: "))
launch_height = float(input("Enter launch height: "))
gravity = float(input("Enter the strength of gravity: "))
launch_angle_radians = radians(launch_angle_degrees)
l_a_r = launch_angle_radians

launch_range = (
  (launch_speed**2 / gravity) * (sin(l_a_r) * cos(l_a_r) + cos(l_a_r) * sqrt(sin(l_a_r)**2 + (2 * gravity * launch_height) / launch_speed**2)))

apogee = [
  (launch_speed**2 / gravity)  * sin(l_a_r) * cos(l_a_r),
  (launch_height + ( (launch_speed**2 / (2* gravity) * (sin(l_a_r)**2))))]

time_taken = launch_range / (launch_speed * cos(l_a_r))

x_coords = linspace(0, launch_range, 51)
y_coords = []

for x in x_coords:
  y_coords.append (launch_height + x * (tan(l_a_r)) - (gravity / (2 * launch_speed**2) * (1 + tan(l_a_r)**2) * x**2 ))

line = ax.plot(x_coords, y_coords, label = "y vs x")
apogee_draw = ax.plot(apogee[0], apogee[1], color='green', marker='x', label = "apogee")

ax.legend(["y vs x", "Apogee"])
plt.show()