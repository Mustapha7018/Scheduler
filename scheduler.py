import matplotlib.pyplot as plt
import numpy as np

# Schedule in 24-hour format
schedule = {
    'Morning Routine + Quran': (6, 7),
    'Focused Study (Python/Self-improvement)': (7, 9),
    'Short Break/Exercise': (9, 9.5),
    'A2SV Program': (9.5, 12),
    'Break + Leetcoding': (12, 14),
    'A2SV Program Continued': (14, 18),
    'Gym/Leisure': (18, 19),
    'Dinner and Relaxation': (19, 20),
    'Project Work/GIG/A2SV Internship': (20, 22),
    'Wind Down': (22, 23),
    'Flex Time/Rest': (0, 5)
}

plt.figure(figsize=(12, 8))

for task, (start, end) in schedule.items():
    plt.plot([start, end], [task, task], marker = 'o', markersize = 8, linewidth=2)

# Formatting the plot
plt.yticks(list(schedule.keys()), fontsize=12)
plt.xticks(np.arange(0, 25, 1), fontsize=10)
plt.grid(axis='x', linestyle='--')
plt.title('Vacation Schedule', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Tasks', fontsize=14)
plt.xlim(0, 24)
plt.tight_layout()

# Show plot
plt.show()
