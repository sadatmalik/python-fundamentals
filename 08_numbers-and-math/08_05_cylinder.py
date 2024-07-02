# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.
import math


radius = 3.14
height = 5

# π r² h
volume = math.pi * radius**2 * height
print(volume)

# 2π r h + 2π r²
surface_area = (2 * math.pi * radius * height) + (2 * math.pi * radius**2)
print(surface_area)
