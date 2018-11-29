##########################################################
# CST8333 2018 Final Project                             #
#                                                        #
# Created by Arish Kakadiya                              #
# Student number: 040894137                              #
# November 26 ,2018                                      #
#                                                        #
##########################################################

import csv # import statements


class Commodity:
    # constructor
    def __init__(self,REF_DATE,GEO,DGUID,Food_categories,Commodity,UOM,UOM_ID,SCALAR_FACTOR,SCALAR_ID,VECTOR,COORDINATE,VALUE,STATUS,SYMBOL,TERMINATED,a):
        self.REF_DATE = REF_DATE
        self.GEO = GEO
        self.DGUID= DGUID
        self.Food_categories = Food_categories
        self.Commodity = Commodity
        self.UOM = UOM
        self.UOM_ID = UOM_ID
        self.SCALER_FACTOR = SCALAR_FACTOR
        self.SCALER_ID = SCALAR_ID
        self.VECTOR = VECTOR
        self.COORDINATE = COORDINATE
        self.VALUE = VALUE
        self.STATUS = STATUS
        self.SYMBOL = SYMBOL
        self.TERMINATED = TERMINATED
        self.a = a

    def count_commodity(self,Commodity):
        count = 0
        for ele in Commodity:
            if (ele == "Rice"):
                count = count + 1
        print(count)
        return count




class DataReader(): # Created a class to read csv file and place into list

    def __init__(self, fname): # DatabaseReader constructor
        self.fname = fname;

    def rowList(self):
        with open(self.fname, newline='') as csvfile:
            reader = csv.reader(csvfile)
            dlist = list(reader)
        return dlist

def showData(dlist): # function to show all the rows from dataset
    for row in dlist:
        print(row[2]) # prints all the rows in console


def __str__(self):
        return self.REF_DATE + "\t\t" +self.GEO +" " +self.DGUID +"\t\t" +self.Food_categories +"-" +self.Commodity +"-" +self.UOM +"\t" +self.UOM_ID

def main():
    data = DataReader('32100054.csv')
    dList = data.rowList()
    showData(dList)

if __name__ == "__main__":
    # executes if run as main program.
    main()
