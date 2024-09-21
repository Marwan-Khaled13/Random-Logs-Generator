import matplotlib.pyplot as plot
import time as t
import re as re
import numpy as np

plot.ion()  
figure, ax = plot.subplots()

x_data = np.array([])
y_data = np.array([])

file_path = r"C:\Users\snake\Desktop\Courses\Big data training\Task 2\Random-Logs-Generator-main\logs\generated_logs.log"

def latest_log():
    with open(file_path, "r") as file:
        lines = file.readlines() 
        if lines:  
            last_generated_line = lines[-1]
            search = re.search(r"(INFO|DEBUG|WARNING|ERROR|CRITICAL)", last_generated_line)
            if search:
                return search.group(0)
    return None 

def log_to_numeric(level):
    level_details = {
        "DEBUG": 3,
        "INFO": 1,
        "WARNING": 4,
        "ERROR": 2,
        "CRITICAL": 5
    }
    return level_details.get(level, 0)

def dynamic_log_simulation(a):
    global x_data, y_data  
    start = t.time()
    while t.time() - start < 60:  
        end_time = t.time() - start
        x_data = np.append(x_data, end_time)
        log_level = latest_log()  
        y_data = np.append(y_data, log_to_numeric(log_level))

        ax.clear()
        ax.plot(x_data, y_data, marker='o')      
        ax.set_xlabel("Time (in seconds)") 
        ax.set_ylabel("Log Level") 
        ax.set_title("Real-Time Levels") 
        plot.draw() 
        plot.pause(a)  

dynamic_log_simulation(2)
