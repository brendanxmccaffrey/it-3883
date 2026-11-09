# Program Name:         Assignment5.py
# Course:               IT3883/Section W01
# Student Name:         Brendan McCaffrey
# Assignment Number:    Lab5
# Due Date:             11/20/2026
# Purpose:              Read temperature data from a text file, save the
#                       readings in a SQLite database, and calculate average
#                       temperatures for Sunday and Thursday.
# Resources:            Course Module 4-1 (Database), sqlite_sample_code.py,
#                       sqlite_exercise.py.

import sqlite3

# Create / open a SQLite database and get a cursor.
connection = sqlite3.connect("temperatures.db")
cursor = connection.cursor()

# Drop the old table so running the program again does not duplicate input data.
cursor.execute("DROP TABLE IF EXISTS temperatures")

# Create the temperatures table.
cursor.execute("""
    CREATE TABLE temperatures (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT NOT NULL,
        Temperature_Value REAL NOT NULL
    )
""")

# Open the input file and loop through rows in the file.
with open("Assignment5input.txt", "r") as input_file:
    for line in input_file:
        day, temperature = line.split()

        cursor.execute("""
            INSERT INTO temperatures (Day_Of_Week, Temperature_Value)
            VALUES (?, ?)
        """, (day, float(temperature)))

# Save all inserted rows to the database.
connection.commit()

# Calculate Sunday's average temperature.
cursor.execute("""
    SELECT ROUND(AVG(Temperature_Value), 2)
    FROM temperatures
    WHERE Day_Of_Week = 'Sunday'
""")

# Save result and display output
sunday_average = cursor.fetchone()[0]
print("Sunday average temperature:", sunday_average)

# Calculate Thursday's average temperature.
cursor.execute("""
    SELECT ROUND(AVG(Temperature_Value), 2)
    FROM temperatures
    WHERE Day_Of_Week = 'Thursday'
""")

# Save result and display output
thursday_average = cursor.fetchone()[0]
print("Thursday average temperature:", thursday_average)

# Close the database connection.
connection.close()
