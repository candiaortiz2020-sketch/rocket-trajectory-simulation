import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.81  # gravity (m/s^2)

# Rocket parameters
mass = 50.0        # kg
thrust = 1200.0    # N
burn_time = 5.0    # seconds

# Aerodynamic parameters
rho = 1.225        # air density (kg/m^3)
Cd = 0.75          # drag coefficient
radius = 0.15      # rocket radius (m)
A = np.pi * radius**2

# Simulation parameters
dt = 0.01
time = np.arange(0, 15, dt)

# Initial conditions
velocity = 0.0
height = 0.0

heights = []
velocities = []

for t in time:
    # Drag force
    drag = 0.5 * rho * Cd * A * velocity**2
    drag_force = -np.sign(velocity) * drag

    # Net force
    if t <= burn_time:
        force = thrust - mass * g + drag_force
    else:
        force = - mass * g + drag_force

    # Motion equations
    acceleration = force / mass
    velocity += acceleration * dt
    height += velocity * dt

    # Prevent going below ground
    if height < 0:
        height = 0
        velocity = 0

    heights.append(height)
    velocities.append(velocity)

# Plot results
plt.figure()
plt.plot(time, heights)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Rocket Vertical Trajectory with Air Resistance")
plt.grid()
plt.show()
