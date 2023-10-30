import time

# Get the current time
current_time = time.localtime()
current_hour = current_time.tm_hour

# Determine the appropriate greeting based on the given time
if 5 <= current_hour < 12:
    greeting = "Good Morning"
elif 12 <= current_hour < 17:
    greeting = "Good Afternoon Sir"
else:
    greeting = "Good Evening"

# Print the greeting
print(f"{greeting}, how are you today?")
