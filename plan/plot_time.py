import matplotlib.pyplot as plt

# Read timing data from file
timing_file = "timing.txt"
timing_data = []
s = 0.0
# Read the first 30 data points
with open(timing_file, 'r') as file:
    for i, line in enumerate(file):
        time = float(line.strip('s\n'))
        timing_data.append(time)

        if i <= 30:
            s = s+time
        # Remove 's' from each line and convert to float
        
# Plot the timing data
plt.plot(timing_data, marker='o')
plt.title('Execution Time per Iteration (First 30 Data Points)')
plt.xlabel('Iteration')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()
print("last time")
print(time)
print("pred")
print(s)
