from cs50 import SQL 
import csv
import sys

IndexStudentsTable = 0
db = SQL("sqlite:///students.db")
db.execute("DELETE FROM students")

if not len(sys.argv) == 2:
    print("Usage: python import.py characters.csv")
    exit(1)

with open(sys.argv[1], newline='') as StudentsDataBase: 
    Reader = csv.reader(StudentsDataBase, delimiter=',')
    FirstRow = next(Reader)
    for ElementsInRow in Reader:
        IndexStudentsTable += 1
        NewString = ElementsInRow[0].split(' ')
        FirstName = NewString[0]
        House = ElementsInRow[1]
        Birth = ElementsInRow[2]
        if len(NewString) == 2:
            MiddleName = None
            LastName = NewString[1]
        else:
            MiddleName = NewString[1]
            LastName = NewString[2]
        db.execute("INSERT INTO students(id, first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?, ?)",
                   (IndexStudentsTable, FirstName, MiddleName, LastName, House, Birth))