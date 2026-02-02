import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.81  # gravity (m/s^2)

# Rocket parameters
mass = 50.0        # kg
thrust = 1200.0    # N
burn_time = 5.0    # seconds

# Simulation parameters
dt = 0.01
time = np.arange(0, 15, dt)

# Initial conditions
velocity = 0.0
height = 0.0

heights = []
velocities = []

for t in time:
    if t <= burn_time:
        force = thrust - mass * g
    else:
        force = - mass * g

    acceleration = force / mass
    velocity += acceleration * dt
    height += velocity * dt

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
plt.title("Rocket Vertical Trajectory Simulation")
plt.grid()
plt.show()
