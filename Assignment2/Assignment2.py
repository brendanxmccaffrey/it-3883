# Program Name:         Assignment2.py
# Course:               IT3883/Section W01
# Student Name:         Brendan McCaffrey
# Assignment Number:    Lab2
# Due Date:             10/2/2026
# Purpose:              Read student scores from a file, calculate each student's average,
#                       sort the students from highest to lowest average, and display the results.
# Resources used:       Module 2-1 Methods slides and Module 2-2 Files-Objects slides.

def main():
    # Create an empty list to store each student's name and average
    students = []

    # Open the input file for reading
    input_file = open("Assignment2input.txt", "r")

    # Read and process each line in the file
    for line in input_file:

        # Split the line into separate fields
        row = line.split()

        # The first field contains the student's name
        name = row[0]

        # Add the six score fields together
        total = 0

        for index in range(1, 7):
            total += int(row[index])

        # Calculate the student's average
        average = total / 6

        # Store the student's name and average
        students.append([name, average])

    # Close the input file
    input_file.close()

    # Sort students from highest to lowest average
    for current in range(len(students) - 1):

        highest = current

        for index in range(current + 1, len(students)):

            # Compare the average stored in position 1
            if students[index][1] > students[highest][1]:
                highest = index

        # Swap the current student with the highest remaining student
        temp = students[current]
        students[current] = students[highest]
        students[highest] = temp

    # Display each student's name and final average
    for student in students:
        print(student[0], format(student[1], ".2f"))

# Start the program
main()