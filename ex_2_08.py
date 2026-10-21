seconds_to_clock = input(" Enter duration in seconds:")
hours = int(seconds_to_clock) // 3600
# print(hours,"h")
minutes = (int(seconds_to_clock)  % 3600) // 60
# print(minutes,"m")
seconds = int(seconds_to_clock) % 60
# print(seconds,"s")
print(f"{hours}h {minutes}m {seconds}s")