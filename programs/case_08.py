# Case Study 8: Student Marks Matrix Analysis
students = ["Asha", "Bharat", "Charan"]
subjects = ["Python", "Maths", "English"]
marks = [
    [88, 76, 81],
    [67, 72, 59],
    [45, 48, 52]
]

valid = len(marks) == len(students)
for row in marks:
    if len(row) != len(subjects):
        valid = False

if not valid or len(students) == 0 or len(subjects) == 0:
    print("Invalid marks matrix.")
else:
    totals = []
    print("STUDENT-WISE RESULTS")
    for i in range(len(students)):
        total = sum(marks[i])
        average = total / len(subjects)
        totals.append(total)
        print(students[i], "| Total:", total, "| Average:", round(average, 2))

    print("\nSUBJECT-WISE AVERAGES")
    for j in range(len(subjects)):
        column_total = 0
        for i in range(len(students)):
            column_total += marks[i][j]
        subject_average = column_total / len(students)
        print(subjects[j], ":", round(subject_average, 2))
        if subject_average < 50:
            print("  Warning: Low average in", subjects[j])

    top_index = totals.index(max(totals))
    print("\nTop student:", students[top_index], "with", totals[top_index], "marks")
