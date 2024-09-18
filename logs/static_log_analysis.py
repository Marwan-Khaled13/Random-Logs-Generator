import matplotlib.pyplot as plt
import re

log_file = "logs/generated_logs.log"

def count_log_levels(log_file):
    levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]
    level_counts = {level: 0 for level in levels}

    with open(log_file, "r") as f:
        for line in f:
            for level in levels:
                if re.search(f"\\b{level}\\b", line):
                    level_counts[level] += 1

    return level_counts

def plot_log_level_distribution(level_counts):
    levels = list(level_counts.keys())
    counts = list(level_counts.values())

    plt.bar(levels, counts, color='blue')
    plt.xlabel("Log Levels")
    plt.ylabel("Frequency")
    plt.title("Log Level Distribution")
    plt.show()

# Example usage
log_level_counts = count_log_levels(log_file)
plot_log_level_distribution(log_level_counts)
