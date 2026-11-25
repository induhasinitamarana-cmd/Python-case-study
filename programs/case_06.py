# Case Study 6: Student Performance Trend Analysis
subjects = ["Mathematics", "Physics", "Programming", "English"]
previous_marks = [65, 72, 58, 80]
latest_marks = [78, 68, 74, 35]

if len(subjects) != len(previous_marks) or len(subjects) != len(latest_marks):
    print("Invalid data: list lengths must match.")
elif len(subjects) == 0:
    print("No subject data available.")
else:
    weak_subjects = []
    print("SUBJECT-WISE PERFORMANCE TREND")
    for i in range(len(subjects)):
        change = latest_marks[i] - previous_marks[i]
        if change > 0:
            trend = "Improved by " + str(change)
        elif change < 0:
            trend = "Declined by " + str(abs(change))
        else:
            trend = "No change"
        print(subjects[i], "| Previous:", previous_marks[i],
              "| Latest:", latest_marks[i], "|", trend)
        if latest_marks[i] < 40:
            weak_subjects.append(subjects[i])

    average = sum(latest_marks) / len(latest_marks)
    if average >= 75:
        classification = "Excellent"
    elif average >= 60:
        classification = "Good"
    else:
        classification = "Needs Improvement"

    print("Latest average:", round(average, 2))
    print("Weak subjects:", weak_subjects if weak_subjects else "None")
    print("Classification:", classification)
