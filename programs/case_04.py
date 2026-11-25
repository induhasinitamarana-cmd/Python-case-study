# Case Study 4: Attendance Recovery
classes_conducted = 40
classes_attended = 26
required_percentage = 75.0

if classes_conducted <= 0 or classes_attended < 0 or classes_attended > classes_conducted:
    print("Invalid attendance data.")
else:
    current_percentage = classes_attended / classes_conducted * 100
    print("Current attendance:", round(current_percentage, 2), "%")
    extra_classes = 0
    total_conducted = classes_conducted
    total_attended = classes_attended

    while total_attended / total_conducted * 100 < required_percentage:
        total_conducted += 1
        total_attended += 1
        extra_classes += 1

    print("Additional consecutive classes to attend:", extra_classes)
    print("Attendance after recovery:",
          round(total_attended / total_conducted * 100, 2), "%")
