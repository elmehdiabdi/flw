import csv

# Program made by Arish Kakadiya
# Student number: 040894137
class DataReader(): # Created a class to read csv file and place into list

    def __init__(self, fname): # DatabaseReader constructor
        self.fname = fname;

    def rowList(self):
        with open(self.fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            dlist = list(reader)
        return dlist


def showMenu(): # function that shows all the menu option to be select by user.
    print("Author is Arish Kakadiya")
    print("1 - Show all data")
    print("2 - Show Total number of rows")
    print("3 - Show a specific row")
    print("Q - Quit")


def showData(dlist): # function to show all the rows from dataset
    for row in dlist:
        print(row) # prints all the rows in console


def showNumRows(dlist): # function to count the total number of rows.
    return len(dlist) - 1


def showRow(dlist, row): # function to show specfic row that user wants.
    print(dlist[row])


def main():
    data = DataReader('32100054.csv') # reads the .csv file
    dList = data.rowList()
    showOption = "a"
    while showOption != "Q" and showOption != "q":
        showMenu()
        showOption = input()
        if showOption == "1":
            print("Author is Arish Kakadiya")
            showData(dList) # call this function if user pressed 1.
        elif showOption == "2":

            print(showNumRows(dList)) #call this function if user pressed 2
        elif showOption == "3":
            print("Author is Arish Kakadiya")
            row = int(input("Enter the of row to show:"))
            while (row <= 0):
                row = input("Invalid. Enter the of row to show:")
            print(showRow(dList, row)) #call this function if user pressed 3.
        elif showOption == "Q" or showOption == "q":
            print("Author is Arish Kakadiya")
        else:
            print("Invalid")


if __name__ == "__main__": # executes if run as main program.
    main()