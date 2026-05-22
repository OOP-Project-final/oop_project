import matplotlib.pyplot as plt

# import custom class
from my_extension import MyCustomAxis




# Create figure and axes
fig, ax = plt.subplots()

# Use existing xaxis from matplotlib
custom_x = ax.xaxis

# Change class to our custom class
custom_x.__class__ = MyCustomAxis


# Plot simple data
ax.plot([1, 2, 3], [4, 5, 6])


# Use custom methods
custom_x.set_custom_label("Custom X Axis", color="blue")

custom_x.highlight_ticks("red")


# Show graph
plt.show()