from cs50 import SQL
import sys
db = SQL("sqlite:///students.db")

if not len(sys.argv) == 2:
    print("Usage: python roster.py [Gryffindor, Ravenclaw, Hufflepuff, Slytherin]")
    exit(1)

if sys.argv[1] == 'Gryffindor':
    FullRow = db.execute('SELECT * FROM students WHERE students.house = "Gryffindor" ORDER BY last, first')
    for ElementInRow in FullRow:
        print(ElementInRow["first"], end=' ')
        if ElementInRow["middle"] is not None:
            print(ElementInRow["middle"], end=' ')
        print(ElementInRow["last"], end='')
        print(f', born {ElementInRow["birth"]}')
elif sys.argv[1] == 'Ravenclaw':
    FullRow = db.execute('SELECT * FROM students WHERE students.house = "Ravenclaw" ORDER BY last, first')
    for ElementInRow in FullRow:
        print(ElementInRow["first"], end=' ')
        if ElementInRow["middle"] is not None:
            print(ElementInRow["middle"], end=' ')
        print(ElementInRow["last"], end='')
        print(f', born {ElementInRow["birth"]}')
elif sys.argv[1] == 'Hufflepuff':
    FullRow = db.execute('SELECT * FROM students WHERE students.house = "Hufflepuff" ORDER BY last, first')
    for ElementInRow in FullRow:
        print(ElementInRow["first"], end=' ')
        if ElementInRow["middle"] is not None:
            print(ElementInRow["middle"], end=' ')
        print(ElementInRow["last"], end='')
        print(f', born {ElementInRow["birth"]}')
else:
    FullRow = db.execute('SELECT * FROM students WHERE students.house = "Slytherin" ORDER BY last, first')
    for ElementInRow in FullRow:
        print(ElementInRow["first"], end=' ')
        if ElementInRow["middle"] is not None:
            print(ElementInRow["middle"], end=' ')
        print(ElementInRow["last"], end='')
        print(f', born {ElementInRow["birth"]}')
