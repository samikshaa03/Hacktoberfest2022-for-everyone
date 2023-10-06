import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    # Calculate differences in x and y coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps required
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calculate incremental changes in x and y
    x_increment = dx / steps
    y_increment = dy / steps

    # Initialize current coordinates
    x, y = x1, y1

    # Create lists to store the x and y coordinates of the line
    x_points = [x]
    y_points = [y]

    # Loop through each step and plot the points along the line
    for _ in range(int(steps)):
        x += x_increment
        y += y_increment
        x_points.append(round(x))
        y_points.append(round(y))

    return x_points, y_points

# Define the coordinates of the endpoints
x1, y1 = 1, 1
x2, y2 = 8, 5

# Call the DDA line drawing function
x_points, y_points = dda_line(x1, y1, x2, y2)

# Plot the line
plt.plot(x_points, y_points, marker='o')
plt.title('DDA Line Drawing Algorithm')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
