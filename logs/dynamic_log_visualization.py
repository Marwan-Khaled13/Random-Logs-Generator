import matplotlib.pyplot as plt
import time
import random

plt.ion()  
fig, ax = plt.subplots()
x_data = []
y_data = []

def dynamic_log_simulation(interval):
    start_time = time.time()
    while time.time() - start_time < 10:  
        x_data.append(time.time() - start_time)
        y_data.append(random.randint(1, 10))  

        ax.clear()
        ax.plot(x_data, y_data, marker='o')
        ax.set_title("Dynamic Log Level Over Time")
        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("Log Level")

        plt.draw()
        plt.pause(interval)  


dynamic_log_simulation(2)
