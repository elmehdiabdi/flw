
# coding: utf-8

# ##########################################################
# # CST8333 2018 Final Project         #
# #                                                         #
# # Created by Jay  Italia      #
# # November 22 ,2018                        #
# #                                                         #
# ##########################################################
# 

#  ## import statements
# 

# In[78]:


# import statements
import csv
import json as json
import threading
from io import StringIO
from tabulate import tabulate

import pandas as pd


# ## To Show all rows and coloumn in Output without truncating used this from (https://stackoverflow.com/a/37347783/8101986)
# 

# In[79]:


# To Show all rows and coloumn in Output without truncating used this from (https://stackoverflow.com/a/37347783/8101986)

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', -1)  # or 199
pd.set_option('max_colwidth', 800)

# Input File Read

df = pd.read_csv("32100054.csv", sep = ",") 

# df.rename(columns={'REF_DATE':'DATE', 'Food categories':'Food_categories'}, inplace=True) # rename one or more columns


#  # Examine the df data

# In[80]:


def DataExamination(): # Examining the dataframe(df ) data
    
    print("\n Author is Jay Italia \n ") 
    
    # print(df.head(5)) # Display data After Renaming

    # print(df)           # print the first 30 and last 30 rows
    print(type(df) )    # DataFrame
    print(df.tail())    # print the last 5 rows
    print(df.index)     # “the index” (aka “the labels”)
    print(df.columns)   # column names (which is “an index”)
    print(df.dtypes)    # data types of each column
    print(df.shape)     # number of rows and columns
    print(df.values)    # underlying numpy array — df are stored as numpy arrays for effeciencies.

    print("Shape(Row) Of Data Frame is ",df.shape[0]) # display only the number of rows of the ‘df’ DataFrame
    print("Shape(column) Of Data Frame is ",df.shape[1])# display only the number of column of the ‘df’ DataFrame


# # Displaying data in pandas dataframe

# In[81]:


def showAllbyPd(): # Displaying data in pandas dataframe
    
    print("\n Author is Jay Italia \n ")  
    
    print(pd.DataFrame(df).head())



class DataReader(): # Created a class to read csv file and place into list
    
# DatabaseReader constructor

    def __init__(self, fname): 
        self.fname = fname;

    def rowList(self):
        with open(self.fname, newline='') as csvfile: # CSV File reading
            reader = csv.reader(csvfile)
            dlist = list(reader)
        return dlist


# function to show all the rows from dataset

def showData(dlist): 
    
    print("\n Author is Jay Italia \n ") 
    
    #Looping Structures
    
    for row in dlist: 
        print(row) # prints all the rows in console

# function to count the total number of rows.
            
def showNumRows(dlist):
        
        print("\n Author is Jay Italia \n ") 
        
        return len(dlist) - 1

# function to show specfic row that user wants.

def showRow(dlist, row): 
    
    print("\n Author is Jay Italia \n ") 
    
    print(dlist[row])

def showCommodiytOnUOM():
    print("\n Author is Jay Italia \n ") 
    print(df[df["UOM_ID"] == 205])


# # To select rows whose column value equals a scalar, some_value, use ==:

# In[82]:


# To select rows whose column value equals a scalar, some_value, use ==:

def showOnCommodityName():
    
    print("\n Author is Jay Italia \n ") 
    
    commodity_input = input("Enter Commodity Name for which you want to search same commodity values :\n")# Variable assignment

    print(df.loc[df['Commodity'] == commodity_input])# print all rows in which this specific commodity exist

    print("Total Count of data having ", commodity_input, "Commodity name is : ")
    print(df.loc[df.Commodity == commodity_input, 'Commodity'].count())  # find total count


#  # To select rows whose column value equals a scalar, some_value

# In[83]:


def show_on_UOM(): # To select rows whose column value equals a scalar, some_value, use ==:
    
    print("\n Author is Jay Italia \n ") 
    
    # Variable assignment
    
    uom_input = input("\n Enter UOM Name which you want to search\n ")
    
    # print all rows in which this specific UOM exist
    
    print((df.loc[df['UOM'] == uom_input]))

    print("\n Total Count of data having ",uom_input,"UOM is : \n ")

    # print(df.loc[df.UOM == uom_input, 'UOM'].count())  # find total count


# In[84]:


def total_ref_date():

    print("\n Author is Jay Italia \n ") 
    
    # Variable assignment
        
    ref_date_input = input("Enter Ref date for which you want to search \n") 
    
    print("Total Count of  Ref Year ", ref_date_input, " is : ")

    # print(df.loc[df.DATE == ref_date_input, 'DATE'].count())  # find total count


# # Function to convert a pandas data frame into a JSON object

# In[85]:


# Function to convert a pandas data frame into a JSON object
def df_to_json(df, filename=''):
    
    print("\n Author is Jay Italia \n ") 
    
    # json = df1.to_json(orient="values") # Writing out Data in JSON Formating
    
    y = df.to_json(orient="values")  
    
    # Decision Structures
    
    if filename:  
        
        # File Writing as Filename = ' ' given from input
        
        with open(filename, 'w+') as f: f.write(json.dumps(y)) 
    return y


# # print all rows in which this specific Food categories exist

# In[86]:


def show_on_Food_categories():

    print("\n Author is Jay Italia \n ") 
    
    food_categories = input("\n Enter Food categories Name which you want to search\n ")
     
    # print all rows in which this specific Food categories exist
        
    print((df.loc[df['Food categories'] == food_categories])) 


# # Sorting 

# In[102]:


def sorting_OnValue():
    
    print("\n Author is Jay Italia \n ") 
    
    # sorting algorithms is used to sort rows in ascending on VALUE 's values # Variables: declaration
    
    
    val = df.sort_values(['VALUE'], ascending=True) 
    
    df1 = val[['Food categories','Commodity','VALUE']]
    
    # pandas df max function used to get max value in VALUE coloumn
    
    max_values = df1[df1['VALUE'] == df1['VALUE'].max()] 
    
    # pandas df min function used to get min value in VALUE coloumn
    
    min_values = df1[df1['VALUE'] == df1['VALUE'].min()]

    print(df1.head(10))
    
    print("\n Max values row is : \n", max_values)
    
    print("\n Min values row is : \n", min_values)
    
    print("\n Memory usage information in accurate number :\n")
    
    # we'll set the memory_usage parameter to 'deep' to get an accurate number.
    
    print(df1.info(memory_usage='deep'))  
    
    # Pandas to JSON converting Function Call
    
    df_to_json(df1,'Ouput_In_Json_format.txt')  

    print("\n Output in JSON format \n")
    
#     print(json)



# In[88]:


def sortingOn_UOM_ID():
    
    print("\n Author is Jay Italia \n ") 
    
    var = df.sort_values(['UOM_ID'],ascending=True)  # sorting algorithms is used to sort rows in ascending on VALUE 's values # Variables: declaration
    
    df2 = var[['Food categories', 'Commodity','UOM_ID']]  # new dataframe declaration
    
    print(df2.head(10))
    
    print("\n Memory usage information in accurate number :\n")
    print(df2.info(memory_usage='deep')) # we'll set the memory_usage parameter to 'deep' to get an accurate number.


# In[89]:


def StatOperetions():
    
    print("\n Author is Jay Italia \n ") 
    
    print(df.groupby('VALUE').mean()) # Mean 
    
    print(df.groupby('VECTOR').describe()) # Summary Statistics in python pandas by describe
    
    print(" And Operations")
    
    print(df[(df.VALUE >60) & (df.REF_DATE==1960)])# ampersand for AND condition # boolean filtering with multiple conditions; indexes are in square brackets, conditions are in parens


# # List Comprehensions

# In[90]:


# List Comprehensions

def List_iterator(): 
    print("\n Author is Jay Italia \n ") 
    
    squared_values = []
    # print(df.loc[:,"VALUE"])
    for x in (df.loc[:,"VALUE"]>0):
         print(squared_values.append(x**2))
         print(squared_values)


# In[91]:


def main():
        
    # input_data = DataReader('32100054.csv') # reads the .csv file
    #
    # dList = input_data.rowList()    # Function for Showing the data
    # showData(dList)
    # showCommodiytOnUOM()   # Function for Showing all rows Commodity based on UOM
    # showAllbyPd()
    # showOnCommodityName()  #Function for Showing all rows having specific commodity name
    # total_ref_date()
    # show_on_Food_categories() #function for showing all rows having specific food category
    #
    # show_on_UOM()
    # sorting_OnValue() # function for sorting Values in ascending or descending order
    #
    # sortingOn_UOM_ID()# function for sorting Values in ascending or descending order
    #
    # Multithreading to execute two given process

#     t1 = threading.Thread(target=sorting_OnValue)
#     t2 = threading.Thread(target=sortingOn_UOM_ID)

#     t1.start()# starting thread 1

#     t2.start() # starting thread 2

#     t1.join()# wait u ntil thread 1 is completely executed

#     t2.join() # wait until thread 2 is completely executed
    #
    StatOperetions()
    # List_iterator() # Iterator Function for List

    # DataExamination() # Function for input data explorations
# this block of code allows running this program from the command line,
# taken from Python's official PyUnit documentation.
# Python Software Foundation. (2015). 26.4.1. Basic example. [Webpage].
# Retrieved from https://docs.python.org/3/library/unittest.html#basic-example.

if __name__ == "__main__":
    # executes if run as main program.
    main()


#  # Multithreading to execute two given process
# 

# In[92]:


# Multithreading to execute two given process

   t1 = threading.Thread(target=sorting_OnValue)
   t2 = threading.Thread(target=sortingOn_UOM_ID)

   t1.start()# starting thread 1

   t2.start() # starting thread 2

   t1.join()# wait u ntil thread 1 is completely executed

   t2.join() # wait until thread 


#  # function for sorting Values in ascending or descending order
# 

# In[93]:


sortingOn_UOM_ID()


#  # function for sorting Values in ascending or descending order

# In[103]:


sorting_OnValue()


# In[95]:


show_on_UOM()


# In[96]:


show_on_Food_categories() #function for showing all rows having specific food category


# In[97]:


input_data = DataReader('32100054.csv') # reads the .csv file
    
dList = input_data.rowList()    # Function for Showing the data
showData(dList)
  


# In[98]:


total_ref_date()


# In[99]:


showOnCommodityName()


# In[100]:


showAllbyPd()


# In[101]:


showCommodiytOnUOM()


# In[104]:


DataExamination()

