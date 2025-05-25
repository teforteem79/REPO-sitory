import os

def sortingGrades():
    filename = ''
    filename = input("Select a group to sort: ")
    filePath = f"C:/Users/Admin/Desktop/groups/{filename}.txt"
    while not os.path.exists(filePath):
        filename = input("Enter the group name: ")
        if os.path.exists(filePath):
            break
    print(f"Now working with {filename}"+".txt")
    file = open(f"C:/Users/Admin/Desktop/groups/{filename}.txt", "r+", encoding="utf-8")
    fileList = file.readlines()
    fileList.sort(reverse=True)
    file.seek(0)
    file.truncate()
    for i in range(len(fileList)):
        file.write(fileList[i]+"\n")
    print(f"{filename}.txt sorted!")
    file.close()
    startOver()

def startOver():
    a = ''
    while a != 'Y' or a != 'N':
        a = input("Do you wish to make another change or sort grades? (Y/N/S) ")
        if a == 'Y':
            initiateWork()
            startOver()
            break
        if a == 'N':
            print("Finished!")
            break
        if a ==  'S':
            sortingGrades()

def initiateWork():
    filename = ''
    filename = input("Enter the group name: ")
    filePath = f"C:/Users/Admin/Desktop/groups/{filename}.txt"
    while not os.path.exists(filePath):
        filename = input("Enter the group name: ")
        if os.path.exists(filePath):
            break
    print(f"Now working with {filename}"+".txt")
    def findStudent():
        file = open(filePath, "r", encoding="utf-8")
        findinput = input("Enter the students name to find: ")
        lines = file.readlines()
        for line in lines:
            if line.find(findinput) != -1:
                print(f"{findinput} is found in line {lines.index(line)+1}")
                studentf = lines[lines.index(line)][2:] 
                gradef = lines[lines.index(line)][0:1]
                print(f"Student {studentf}has a grade {gradef}")
        WriteOrAppend()
        file.close()
    def WriteOrAppend():
        w_or_a = ''
        while w_or_a != "w" or w_or_a != "a" or w_or_a !="e":
            w_or_a = input("reWrite (w), Append (a), Find (f) Exit (e)? ")
            if w_or_a == "w":
                file = open(filePath, "w", encoding="utf-8")
                students = []
                grades = []
                inp = ''
                inp1 = ''
                print("Type -1 on both student and grade to finish writing")
                while inp != '-1' and inp1 != '-1':
                    inp = input("Enter a student: ")
                    inp1 = input("Enter their grade: ")
                    students.append(inp)
                    grades.append(inp1)
                students.remove('-1')
                grades.remove('-1')
                for i in range(len(students)):
                    file.write("\n" + f"{grades[i]} {students[i]}" + "\n")
                file.close()
                break
            if w_or_a == "a":
                file = open(filePath, "a", encoding="utf-8")
                students = []
                grades = []
                inp = ''
                inp1 = ''
                print("type -1 on both student and grade to finish writing")
                while inp != '-1' and inp1 != '-1':
                    inp = input("Enter a student: ")
                    inp1 = input("Enter their grade: ")
                    students.append(inp)
                    grades.append(inp1)
                students.remove('-1')
                grades.remove('-1')
                for i in range(len(students)):
                    file.write("\n" + f"{grades[i]} {students[i]}" + "\n")
                break
            if w_or_a == "e":
                print("Finished!")
                quit()
            if w_or_a == "f":
                findStudent()
    WriteOrAppend()

initiateWork()
startOver()