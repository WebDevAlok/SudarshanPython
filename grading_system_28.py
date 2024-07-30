def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

try:
    # Get user input for marks in five subjects
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter the marks for subject {i}: "))
        marks.append(mark)
    
    # Calculate the average marks
    average = sum(marks) / 5

    # Determine the grade
    grade = calculate_grade(average)

    # Print the average marks and the grade
    print(f"Average Marks: {average}")
    print(f"Grade: {grade}")

except ValueError:
    print("Invalid input. Please enter valid numbers for the marks.")
