grades_1 = input("give me the first grade:")
grades_2 = input("give me the second grade:")
grades_3 = input("give me the third grade:")

average =  (float(grades_1) + float(grades_2) + float(grades_3) ) / 3
print(round(average,2))
lowest = (float(grades_1),float(grades_2),float(grades_3))
print(min(lowest))
print(max(lowest))
print(max(lowest) - min(lowest))