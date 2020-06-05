# Script written by Patrick Crowe 
# <patcrowe@umich.edu>

import csv
import os

# Globals
filename = "201_grades.csv"
fields = []
rows = []

# Writer Helper
def writer_help(temp_fields, temp_rows):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(temp_fields)
        writer.writerows(temp_rows)

# Add/Edit Grade
def add_edit_grade():
    week = input("Enter Week Number: ")
    is_hw = input("(1) HW{}\n(2) ADV{}\n".format(week,week))
    grade = input("Input grade: ")
    week = int(week)
    is_hw = int(is_hw)
    rows[week][is_hw] = int(grade)
    writer_help(fields, rows)
    print("Grade Added\n")
# Add/Edit Grade End

# View Grades
def view_grades():
    HW_total = 0
    ADV_total = 0
    print("Week\tHW\tADV\n")
    for row in rows:
        print("{}\t{}\t{}\n".format(row[0], row[1], row[2]))
        HW_total += int(row[1])
        ADV_total += int(row[2])
    if HW_total > 60:
        extras = HW_total % 60
        HW_total = 60 + (extras / 2)
    if ADV_total > 40:
        extras = ADV_total % 40
        ADV_total = 40 + (extras / 2)
    total = HW_total + ADV_total
    trash = input("HWs: {}\tADVs: {}\tTotal: {}\n\
        Press Enter to return to menu\n".format(HW_total, ADV_total, total))
# View Grades End

# Init Grades
def init_grades():
    temp_fields = ['Week', 'HW', 'ADV']
    temp_rows = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0],
                [4, 0, 0], [5, 0, 0], [6, 0, 0], [7, 0, 0],
                [8, 0, 0], [9, 0, 0], [10, 0, 0], [11, 0, 0],
                [12, 0, 0]]
    writer_help(temp_fields, temp_rows)
    fields = temp_fields
    rows = temp_rows
    print("Gradebook Reset\n")
# Init Grades End

# Main
def main():

    try:
        if os.path.getsize(filename) == 0:
            init_grades()
    except:
        init_grades()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        fields = next(reader)
        for row in reader:
            rows.append(row)

    running = True
    while running:

        command = input("Welcome to EECS 201 grade tracker.\
                \nCommands:\
                \n\t(A)dd: Add in a homework or advanced grade,\
                \n\t(V)iew: View summed grades for ADV and HW,\
                \n\t(E)dit: Edit the score of an assignment,\
                \n\t(R)eset: Resets the gradebook\
                \n\t(Q)uit\n")

        if command.lower() == 'a' or command.lower() == 'add':
            add_edit_grade()
        elif command.lower() == 'v' or command.lower() == 'view':
            view_grades()
        elif command.lower() == 'e' or command.lower() == 'edit':
            add_edit_grade()
        elif command.lower() == 'r' or command.lower() == 'reset':
            init_grades()
        elif command.lower() == 'q' or command.lower() == 'quit':
            running = False
        else:
            print("Not a valid command, try again\n____________________________________________\n")

    print("Goodbye\n")


main()
