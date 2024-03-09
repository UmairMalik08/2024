from numpy import roots, linspace
from math import sqrt, tan, atan
import matplotlib.pyplot as plt

def low_ball(a, b, c, initial_velocity, height, target_x, gravity):
  low_ball_radians = atan(min(roots([a,b,c])))
  l_b_rad = low_ball_radians
  x_coords = linspace(0, target_x, 101)
  y_coords = []
  for x in x_coords:
    y_coords.append(height  + x*(tan(l_b_rad)) - ((gravity / (2*initial_velocity**2)) * ((1 + tan(l_b_rad)**2 ) * x**2)))
  
  return(x_coords, y_coords)

def high_ball(a, b, c, initial_velocity, height, target_x, gravity):
  high_ball_radians = atan(max(roots([a,b,c])))
  h_b_rad = high_ball_radians
  x_coords = linspace(0, target_x, 101)
  y_coords = []
  for x in x_coords:
    y_coords.append(height  + x*(tan(h_b_rad)) - ((gravity / (2*initial_velocity**2)) * ((1 + tan(h_b_rad)**2 ) * x**2)))
  
  return(x_coords, y_coords)

def min_ball(minimum_initial_velocity, height, target_x, target_y, gravity):
  minimum_speed_radians = atan((target_y + sqrt(target_x**2 + target_y**2))/ target_x)
  m_b_rad = minimum_speed_radians
  x_coords = linspace(0, target_x, 101)
  y_coords = []
  for x in x_coords:
    y_coords.append(height  + x*(tan(m_b_rad)) - ((gravity / (2*minimum_initial_velocity**2)) * ((1 + tan(m_b_rad)**2 ) * x**2)))
  
  return(x_coords, y_coords)

fig, ax = plt.subplots()
ax.set_title("Q3. Projectile To Hit (x,y)")
ax.set_xlabel("x/m"), ax.set_ylabel("y above launch height/m")
plt.grid(color="black", linestyle="--", linewidth=0.3)
plt.gca().set_aspect("equal", adjustable="box")
plt.axis("auto")

target_x = float(input("Enter target x: "))
target_y = float(input("Enter target y: "))
gravity = float(input("Enter gravity: "))
height = 0
initial_velocity = 0
minimum_initial_velocity = sqrt(gravity) * sqrt(target_y + sqrt (target_x**2 + target_y**2))
while not initial_velocity >= minimum_initial_velocity:
  initial_velocity = float(input("Enter initial velocity: "))

a = (gravity/(2*  initial_velocity**2))   *  target_x**2
b = -target_x
c = target_y-height+(gravity*target_x**2)/(2*initial_velocity**2)

low_x, low_y = low_ball(a, b, c, initial_velocity, height, target_x, gravity)
high_x, high_y = high_ball(a, b, c, initial_velocity, height, target_x, gravity)
min_x, min_y = min_ball(minimum_initial_velocity, height, target_x, target_y, gravity)

low_line = plt.plot(low_x, low_y, label = "Low Ball")
high_line = plt.plot(high_x, high_y, label = "High Ball")
min_line = plt.plot(min_x, min_y, label = "Minimum u")

target = plt.plot(target_x, target_y, "rX", label = "Target Point")

ax.legend(["Low Ball", "High Ball", "Minimum u", "Target Point"])

plt.show()