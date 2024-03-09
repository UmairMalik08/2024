from math import sin, cos, radians
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title("Q1. Projectile Motion Model")
ax.set_xlabel("x/m"), ax.set_ylabel("y/m")
plt.grid(color="black", linestyle="--", linewidth=0.3)
plt.gca().set_aspect("equal", adjustable="box")
plt.axis("auto")

launch_angle_degrees = float(input("Enter launch angle: "))
launch_speed = float(input("Enter launch speed: "))
launch_height = float(input("Enter launch height: "))
gravity = float(input("Enter the strength of gravity: "))

time_step = 0.02
launch_angle_radians = radians(launch_angle_degrees)

def calculate_parabola(int_hight, int_velocity, launch_angle, gravity):
  x,y, iteration_number= [], [], 0
  x_base = int_velocity * cos(launch_angle)
  positivity = True
  while positivity == True:
    time = time_step * iteration_number
    x.append(x_base * time)
    y.append(int_hight + (int_velocity * sin(launch_angle) * time) - (0.5 * gravity * time**2))
    iteration_number += 1
    if y[-1] < 0:
      positivity = False

  return(x, y)
  
x_coords, y_coords = calculate_parabola(launch_height, launch_speed, launch_angle_radians, gravity)

ax.plot(x_coords[:-1], y_coords[:-1])
ax.legend(["y vs x (no air)"])

plt.show()