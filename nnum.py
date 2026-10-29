
import numpy as np

# Step 1: Create a 1D array
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

# Step 2: Display the array
print("Week 1 Temperatures:")
print(temperatures_w1)

# Step 3: Inspect array properties
print("Shape:", temperatures_w1.shape)
print("Data type:", temperatures_w1.dtype)
print("Number of elements:", temperatures_w1.size)

# Convert Celsius to Fahrenheit
fahrenheit = (temperatures_w1 * 9/5) + 32

print("Temperatures in Fahrenheit:")
print(fahrenheit)

# Find maximum, minimum and mean
print("Maximum temperature:", temperatures_w1.max())
print("Minimum temperature:", temperatures_w1.min())
print("Mean temperature:", temperatures_w1.mean())

# First three days
print("First three days:", temperatures_w1[:3])

# Weekend: last two days
print("Weekend temperatures:", temperatures_w1[-2:])

# Middle three days
print("Middle three days:", temperatures_w1[2:5])

temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]
])

print("Both weeks:")
print(temperatures)

print("Shape:", temperatures.shape)
print("Data type:", temperatures.dtype)
print("Total elements:", temperatures.size)

# Extract each week
print("Week 1:", temperatures[0])
print("Week 2:", temperatures[1])

# Weekend temperatures for both weeks
print("Weekends:")
print(temperatures[:, -2:])
