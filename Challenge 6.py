from numpy import sqrt, sin, cos, tan, arcsin, linspace, radians, degrees, reciprocal, around
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
ax.set_title("Q4. Maximising Distance")
ax.set_xlabel("x/m"), ax.set_ylabel("y/m")
plt.grid(color="black", linestyle="--", linewidth=0.3)
plt.gca().set_aspect("equal", adjustable="box")
plt.axis("auto")

initial_velocity = float(input("Enter initial velocity: "))
height = float(input("Enter height: "))
gravity = float(input("Enter gravity: "))
launch_angle_degrees = float(input("Enter launch angle: "))
launch_angle_radians = radians(launch_angle_degrees)
l_a_r = launch_angle_radians


def original_line(initial_velocity, gravity, l_a_r, height):
  launch_range = (
    (initial_velocity**2 / gravity) * (sin(l_a_r) * cos(l_a_r) + cos(l_a_r) * sqrt(sin(l_a_r)**2 + (2 * gravity * height) / initial_velocity**2)))
  time_taken = launch_range / (initial_velocity * cos(l_a_r))
  x_coords, y_coords = linspace(0, launch_range, 51), []

  for x in x_coords:
    y_coords.append(height + x * (tan(l_a_r)) - (gravity / (2 * initial_velocity**2) * (1 + tan(l_a_r)**2) * x**2 ))
  
  return(x_coords, y_coords, time_taken)

def maximised_lin(initial_velocity, gravity, height):
  max_angle = arcsin(reciprocal(sqrt(2 + (2 * gravity * height / initial_velocity**2))))
  launch_range = (
    (initial_velocity**2 / gravity) * sqrt(1 + (2 * gravity * height / initial_velocity**2)))
  time_taken = launch_range / (initial_velocity * cos(max_angle))

  x_coords, y_coords = linspace(0, launch_range, 51), []

  for x in x_coords:
    y_coords.append(height + x * (tan(max_angle)) - (gravity / (2 * initial_velocity**2) * (1 + tan(max_angle)**2) * x**2 ))

  return(x_coords, y_coords, max_angle, time_taken)


orig_x_coords, orig_y_coords, orig_time = original_line(initial_velocity,gravity, l_a_r, height)
max_x_coords, max_y_coords, max_angle, max_time= maximised_lin(initial_velocity, gravity, height)

original_line = ax.plot(orig_x_coords, orig_y_coords, label = f"θ={around(degrees(l_a_r),2)} t={around(orig_time, 2)}s")
maxed_line = ax.plot(max_x_coords, max_y_coords, label = f"θ={around(degrees(max_angle),2)} t={around(max_time, 2)}s")
ax.legend([f"θ={around(degrees(l_a_r),2)} t={around(orig_time, 2)}s", f"θ={around(degrees(max_angle),2)} t={around(max_time, 2)}s"])

plt.show()