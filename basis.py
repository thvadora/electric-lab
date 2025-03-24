import numpy as np
import matplotlib.pyplot as plt

# Define resistance in ohms
R = 10  # Ohms

# Create a range of voltages
voltages = np.linspace(0, 100, 100)

# Calculate current using Ohm's Law: I = V / R
currents = voltages / R

# Calculate power: P = V * I
powers = voltages * currents

# Plotting
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(voltages, currents)
plt.title("Ohm's Law: Current vs Voltage")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(voltages, powers)
plt.title("Power vs Voltage")
plt.xlabel("Voltage (V)")
plt.ylabel("Power (W)")
plt.grid(True)

plt.tight_layout()
plt.show()
