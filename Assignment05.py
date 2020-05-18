# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# N. Tolliver,5.11.2020,Created started script
# N. Tolliver, 5.12.2020, Added code to remove a task
# N. Tolliver, 5.15.2020, Restructured code to remove a task
# N. Tolliver, 5.16.2020, Took the "remove row" out of the for loop for option 3
# N. Tolliver, 5.17.2020, Modified section reading the file from memory to strip newline character
# N. Tolliver, 5.17.2020, Modified section for writing to file to add newline character back in
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
strFlag = 0

strName = ""
strPriority = ""

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

txtFile = open(objFile, "r")
for row in txtFile:
    strTask, strPriority = row.split(",")
    dicRow = {"strName": strTask, "strPriority": strPriority.strip()}
    lstTable.append(dicRow)
txtFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row["strName"] + ',' + row["strPriority"].strip())
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strName = input("Enter task name: ")
        strPriority = input("Enter task priority: ")
        dicRow = {"strName": strName, "strPriority": strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strFlag = "false"
        strItem = (input("Which item would you like to remove? "))
        for row in lstTable:
            if row["strName"].lower() == strItem.lower():
                lstTable.remove(row)
                print(strItem, "task was removed.")
                strFlag = "true"
        if (strFlag != "true"):
            print("Row not found, please choose option 3 and try re-entering the task to be removed")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        txtFile = open(objFile, "w")
        for row in lstTable:
            txtFile.write(row["strName"] + ',' + row["strPriority"] + "\n")
        txtFile.close()
        print("Data saved to file")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Goodbye")
        break  # and Exit the program

    else:
        print("Please enter only 1, 2, 3, 4, or 5.")

input("Press enter to exit the program")
