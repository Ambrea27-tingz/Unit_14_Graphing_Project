""" 
Author: Ambrea Williams
Date: 04/24/2025
Project: Graphing Data
Unit 14: Lab 15, Opt 1
Description: This program will make a graph that plots a sine wave.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

""" Makes our x and y values for the sine wave."""
x = np.linspace(0, 4 * np.pi, 500) #500 points of sin(x) between 0 and 4π
y = np.sin(x) #fomrula: y = sin(x)

"""Creates the figure and axis for the graph."""
fig, ax = plt.subplots(figsize=(10, 6))

"""Background colors for the inside and outside the graph"""
fig.patch.set_facecolor('teal')     # entire background color
ax.set_facecolor('teal')            # inside plot background color

"""Creates line segments from (x, y) points for color mapping.
   
   The points are reshaped to create segments between the points
   allowing for a smooth gradient effect.
   """
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

"""Graph line color using a colormap."""
cmap = plt.get_cmap('spring') 

"""Line collection is created using the segments and colormap."""
lc = LineCollection(segments, cmap=cmap, linewidth=2)
lc.set_array(y)  # Color by y-values
ax.add_collection(lc)

""" Our x and y limits are set to the min and max values of the x and y arrays."""
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min(), y.max())

"""Titles and labels for the graph."""
ax.set_title('Sine Wave', fontsize=24, color='white', pad=20)
ax.set_xlabel('x (radians)', fontsize=16, color='white')
ax.set_ylabel('sin(x)', fontsize=16, color='white')

"""tick label in the color white."""
ax.tick_params(axis='both', colors='white')

"""Line border color and width of the border"""
for spine in ax.spines.values():
    spine.set_edgecolor('white')
    spine.set_linewidth(1.4)

"""Grid lines added to the graph."""
ax.grid(True, linestyle='--', color='white', alpha=0.4)

plt.savefig('sine_wave_graph.png', bbox_inches='tight',pad_inches=0.5) #add 1st to save the graph as a png
plt.show() #shows the graph in an interactive window