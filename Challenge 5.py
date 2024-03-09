from numpy import sqrt, sin, cos, tan, arctan, roots, linspace, arcsin, reciprocal
import matplotlib.pyplot as plt

def low_ball(a, b, c, initial_velocity, height, target_x, gravity):
  low_ball_radians = arctan(min(roots([a,b,c])))
  l_b_rad = low_ball_radians
  launch_range = (
    (initial_velocity**2 / gravity) * (sin(l_b_rad) * cos(l_b_rad) + cos(l_b_rad) * sqrt(sin(l_b_rad)**2 + (2 * gravity * height) / initial_velocity**2)))
  x_coords = linspace(0, launch_range, 101)
  y_coords = []
  for x in x_coords:
    y_coords.append(height  + x*(tan(l_b_rad)) - ((gravity / (2*initial_velocity**2)) * ((1 + tan(l_b_rad)**2 ) * x**2)))
  
  return(x_coords, y_coords)

def high_ball(a, b, c, initial_velocity, height, target_x, gravity):
  high_ball_radians = arctan(max(roots([a,b,c])))
  h_b_rad = high_ball_radians
  launch_range = (
    (initial_velocity**2 / gravity) * (sin(h_b_rad) * cos(h_b_rad) + cos(h_b_rad) * sqrt(sin(h_b_rad)**2 + (2 * gravity * height) / initial_velocity**2)))
  x_coords = linspace(0, launch_range, 101)
  y_coords = []
  for x in x_coords:
    y_coords.append(height  + x*(tan(h_b_rad)) - ((gravity / (2*initial_velocity**2)) * ((1 + tan(h_b_rad)**2 ) * x**2)))
  
  return(x_coords, y_coords)

def min_ball(minimum_initial_velocity, height, target_x, target_y, gravity):
  minimum_speed_radians = arctan((target_y + sqrt(target_x**2 + target_y**2))/ target_x)
  m_b_rad = minimum_speed_radians

  launch_range = (
    (minimum_initial_velocity**2 / gravity) * (sin(m_b_rad) * cos(m_b_rad) + cos(m_b_rad) * sqrt(sin(m_b_rad)**2 + (2 * gravity * height) / minimum_initial_velocity**2)))
  x_coords = linspace(0, launch_range, 101)
  y_coords = []
  for x in x_coords:
    y_coords.append(height  + x*(tan(m_b_rad)) - ((gravity / (2*minimum_initial_velocity**2)) * ((1 + tan(m_b_rad)**2 ) * x**2)))
  
  return(x_coords, y_coords)

def max_range(initial_velocity, gravity, height):
  max_angle = arcsin(reciprocal(sqrt(2 + (2 * gravity * height / initial_velocity**2))))
  launch_range = (
    (initial_velocity**2 / gravity) * sqrt(1 + (2 * gravity * height / initial_velocity**2)))
  time_taken = launch_range / (initial_velocity * cos(max_angle))

  x_coords, y_coords = linspace(0, launch_range, 51), []

  for x in x_coords:
    y_coords.append(height + x * (tan(max_angle)) - (gravity / (2 * initial_velocity**2) * (1 + tan(max_angle)**2) * x**2 ))

  return(x_coords, y_coords, max_angle, time_taken, launch_range)

def bounding(initial_velocity, gravity, launch_range):
  
  x_coords = linspace(0, launch_range, 101)
  y_coords = []

  for x in x_coords:
    y_coords.append((initial_velocity**2 / (2 * gravity)) - (gravity / (2 * initial_velocity**2))* x**2)
  
  return(x_coords, y_coords)


fig, ax = plt.subplots()
ax.set_title("Q5. Bounding Parabola")
ax.set_xlabel("x/m"), ax.set_ylabel("y above launch height/m")
plt.grid(color="black", linestyle="--", linewidth=0.3)
plt.gca().set_aspect("equal", adjustable="box")
plt.axis("auto")

target_x = 1000#float(input("Enter target x: "))
target_y = 300#float(input("Enter target y: "))
gravity = 9.81#float(input("Enter gravity: "))
height = 0
initial_velocity = 1.3065*115
minimum_initial_velocity = sqrt(gravity) * sqrt(target_y + sqrt (target_x**2 + target_y**2))
while not initial_velocity >= minimum_initial_velocity:
  initial_velocity = float(input("Enter initial velocity: "))

a = (gravity/(2*  initial_velocity**2))   *  target_x**2
b = -target_x
c = target_y-height+(gravity*target_x**2)/(2*initial_velocity**2)

low_x, low_y = low_ball(a, b, c, initial_velocity, height, target_x, gravity)
high_x, high_y = high_ball(a, b, c, initial_velocity, height, target_x, gravity)
min_x, min_y = min_ball(minimum_initial_velocity, height, target_x, target_y, gravity)
max_x_coords, max_y_coords, max_angle, max_time, launch_range= max_range(initial_velocity, gravity, height)
bounding_x_coords, bounding_y_coords= bounding(initial_velocity, gravity, launch_range)


low_line = plt.plot(low_x, low_y, label = "Low Ball")
high_line = plt.plot(high_x, high_y, label = "High Ball")
min_line = plt.plot(min_x, min_y, label = "Minimum u")
maxed_line = plt.plot(max_x_coords, max_y_coords, label = "Maxed dist")
bounding_line = plt.plot(bounding_x_coords, bounding_y_coords, "--", label = "Bounding Parabola")

target = plt.plot(target_x, target_y, "rX", label = "Target Point")

ax.legend(["Low Ball", "High Ball", "Minimum u", "Target Point", "Maxed dist", "Bounding Parabola"])

plt.show()