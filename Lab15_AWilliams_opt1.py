""" 
Author: Ambrea Williams
Date: 04/24/2025
Project: Graphing Data
Unit 14: Lab 15, Opt 1
Description: This program will make a graph that plots a sine wave.
"""
import numpy as np
import matplotlib.pyplot as plt

# Create x values from 0 to 4π (about 12.56)
x = np.linspace(0, 4 * np.pi, 500)
y = np.sin(x)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, color='blue', linewidth=2)

# Customize
ax.set_title("Sine Wave", fontsize=20)
ax.set_xlabel("x values (radians)", fontsize=14)
ax.set_ylabel("sin(x)", fontsize=14)
ax.grid(True)

plt.show()
