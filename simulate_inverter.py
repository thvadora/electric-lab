import numpy as np
import matplotlib.pyplot as plt

# Grid voltage (assumed constant, 3-phase RMS)
V_grid = 33000  # volts

# Max solar availability
P_solar_max = 65e6  # watts

# Simulation time
time = np.linspace(0, 10, 1000)  # 10 seconds, 1000 steps

# Setpoint ramp from 0 to 50 MW
P_setpoint = np.clip(time * 5e6, 0, 50e6)  # linear ramp to 50 MW

# Assume the solar can always deliver setpoint (<= 65 MW)
P_actual = np.minimum(P_setpoint, P_solar_max)

# Compute required current: P = V * I => I = P / V (3-phase RMS)
I_injected = P_actual / V_grid  # Simplified model

# Simulate inverter response (low-pass filter to smooth changes)
tau = 0.2  # time constant (seconds)
dt = time[1] - time[0]
I_smoothed = np.zeros_like(I_injected)

for i in range(1, len(time)):
    dI = (I_injected[i] - I_smoothed[i-1]) * dt / tau
    I_smoothed[i] = I_smoothed[i-1] + dI

# Plot
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, P_setpoint / 1e6, label="Setpoint (MW)", linestyle='--')
plt.plot(time, P_actual / 1e6, label="Actual Output (MW)")
plt.ylabel("Power (MW)")
plt.title("Solar Plant Output vs Setpoint")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, I_smoothed, label="Inverter Current (A)", color='orange')
plt.ylabel("Current (A)")
plt.xlabel("Time (s)")
plt.title("Current Injected by Inverter")
plt.grid(True)

plt.tight_layout()
plt.show()
