starting_hour = input("kindly provide with the starting hour:")
starting_minutes = input("kindly provide with the starting minutes:")
duration_in_minutes = input("kindly duration in minutes:")


starting_hour_int = int(starting_hour) * 60 + int(starting_minutes)
duration_in_minutes = int(duration_in_minutes) + starting_hour_int

days = duration_in_minutes // 1440
remaining_minutes = duration_in_minutes % 1440

hours = remaining_minutes //  60
minutes = remaining_minutes % 60

print(f"{hours} : { minutes}")
print (f"Days later : {days} ")
