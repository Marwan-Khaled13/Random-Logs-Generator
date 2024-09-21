import matplotlib.pyplot as plot
import re as re
import numpy as np

file_path = r"C:\Users\snake\Desktop\Courses\Big data training\Task 2\Random-Logs-Generator-main\logs\generated_logs.log"

def count_levels(log_file):
    levels = ["INFO", "ERROR", "DEBUG", "WARNING", "CRITICAL"] 
    counts = np.zeros(len(levels))  

    with open(log_file, "r") as f:
        for line in f:  
            for i, check in enumerate(levels):
                if re.search(f"\\b{check}\\b", line):  
                    counts[i] += 1  
    return levels, counts 

def plot_distribution(levels, counts):
    plot.bar(levels, counts, color='red')    
    plot.title("Log Distribution")
    plot.xlabel("Log Levels")
    plot.ylabel("Frequency") 
    plot.show()

levels, counts = count_levels(file_path)
plot_distribution(levels, counts)
