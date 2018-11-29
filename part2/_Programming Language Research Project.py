
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

# In[53]:


# import statements
import csv
import json as json
import threading
from io import StringIO
from tabulate import tabulate

import pandas as pd


# ## To Show all rows and coloumn in Output without truncating used this from (https://stackoverflow.com/a/37347783/8101986)
# 

# In[36]:


# To Show all rows and coloumn in Output without truncating used this from (https://stackoverflow.com/a/37347783/8101986)

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', -1)  # or 199

# Input File Read

df = pd.read_csv("32100054.csv", sep = ",") 

# df.rename(columns={'REF_DATE':'DATE', 'Food categories':'Food_categories'}, inplace=True) # rename one or more columns


#  # Examine the df data

# In[37]:


def DataExamination(): # examine the df data
    
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

# In[57]:


def showAllbyPd(): # Displaying data in pandas dataframe
    
    print("\n Author is Jay Italia \n ")  
    
    print(pd.DataFrame(df).head())



class DataReader(): # Created a class to read csv file and place into list
    

    def __init__(self, fname):  # DatabaseReader constructor
        self.fname = fname;

    def rowList(self):
        with open(self.fname, newline='') as csvfile: # CSV File reading
            reader = csv.reader(csvfile)
            dlist = list(reader)
        return dlist

def showData(dlist): # function to show all the rows from dataset
    
    print("\n Author is Jay Italia \n ") 
    
    for row in dlist: #Looping Structures
        print(row) # prints all the rows in console

def showNumRows(dlist): # function to count the total number of rows.
        
        print("\n Author is Jay Italia \n ") 
        
        return len(dlist) - 1

def showRow(dlist, row): # function to show specfic row that user wants.
    
    print("\n Author is Jay Italia \n ") 
    
    print(dlist[row])

def showCommodiytOnUOM():
    print("\n Author is Jay Italia \n ") 
    print(df[df["UOM_ID"] == 205])


# # To select rows whose column value equals a scalar, some_value, use ==:

# In[39]:


def showOnCommodityName():# To select rows whose column value equals a scalar, some_value, use ==:
    
    print("\n Author is Jay Italia \n ") 
    
    commodity_name = input("Enter Commodity Name for which you want to search same commodity values :\n")# Variable assignment

    print(df.loc[df['Commodity'] == commodity_name])# print all rows in which this specific commodity exist

    print("Total Count of data having ", commodity_name, "Commodity name is : ")
    print(df.loc[df.Commodity == commodity_name, 'Commodity'].count())  # find total count


#  # To select rows whose column value equals a scalar, some_value

# In[40]:


def show_on_UOM(): # To select rows whose column value equals a scalar, some_value, use ==:
    
    print("\n Author is Jay Italia \n ") 
    
    uom_name = input("\n Enter UOM Name which you want to search\n ") # Variable assignment

    print((df.loc[df['UOM'] == uom_name]))# print all rows in which this specific UOM exist

    print("\n Total Count of data having ",uom_name,"UOM is : \n ")

    # print(df.loc[df.UOM == uom_name, 'UOM'].count())  # find total count


# In[41]:


def total_ref_date():

    print("\n Author is Jay Italia \n ") 
    
    ref_date = input("Enter Ref date for which you want to search \n")  # Variable assignment
    print("Total Count of  Ref Year ", ref_date, " is : ")

    # print(df.loc[df.DATE == ref_date, 'DATE'].count())  # find total count


# # Function to convert a pandas data frame into a JSON object

# In[42]:


def df_to_json(df, filename=''): # Function to convert a pandas data frame into a JSON object
    
    print("\n Author is Jay Italia \n ") 
    
    x = df.to_json(orient="values")  # json = df1.to_json(orient="values") # Writing out Data in JSON Formating

    if filename:  # Decision Structures
        with open(filename, 'w+') as f: f.write(json.dumps(x)) # File Writing as Filename = ' ' given from input
    return x


# # print all rows in which this specific Food categories exist

# In[43]:


def show_on_Food_categories():

    print("\n Author is Jay Italia \n ") 
    
    food_categories = input("\n Enter Food categories Name which you want to search\n ")
    print((df.loc[df['Food categories'] == food_categories]))  # print all rows in which this specific Food categories exist


# # Sorting 

# In[44]:


def sorting_OnValue():
    
    print("\n Author is Jay Italia \n ") 
    
    val = df.sort_values(['VALUE'], ascending=False) # sorting algorithms is used to sort rows in ascending on VALUE 's values # Variables: declaration
    df1 = val[['Food categories','Commodity','VALUE']]
    maxvalues = df1[df1['VALUE'] == df1['VALUE'].max()] # pandas df max function used to get max value in VALUE coloumn
    minvalues = df1[df1['VALUE'] == df1['VALUE'].min()]# pandas df min function used to get min value in VALUE coloumn

    print(df1.head())
    print("\n Max values row is : \n", maxvalues)
    print("\n Min values row is : \n", minvalues)
    print("\n Memory usage information in accurate number :\n")
    print(df1.info(memory_usage='deep'))  # we'll set the memory_usage parameter to 'deep' to get an accurate number.
    df_to_json(df1,'JSON_output.txt')  # Pandas to JSON converting Function Call

    print("\n Output in JSON format \n")
    print(json)



# In[45]:


def sortingOn_UOM_ID():
    
    print("\n Author is Jay Italia \n ") 
    
    newval = df.sort_values(['UOM_ID'],ascending=True)  # sorting algorithms is used to sort rows in ascending on VALUE 's values # Variables: declaration
    df2 = newval[['Food categories', 'Commodity','UOM_ID']]  # new dataframe declaration
    print(df2.head(10))
    print("\n Memory usage information in accurate number :\n")
    print(df2.info(memory_usage='deep')) # we'll set the memory_usage parameter to 'deep' to get an accurate number.

pd.set_option('max_colwidth', 800)


# In[60]:


def StatOperetions():
    
    print("\n Author is Jay Italia \n ") 
    
    print(df.groupby('VALUE').mean())
    print(df.groupby('VECTOR').describe())
    print(" And Operations")
    print(df[(df.VALUE >60) & (df.REF_DATE==1960)])# ampersand for AND condition # boolean filtering with multiple conditions; indexes are in square brackets, conditions are in parens


# # List Comprehensions

# In[61]:


def List_iterator(): # List Comprehensions

    print("\n Author is Jay Italia \n ") 
    
    squares = []
    # print(df.loc[:,"VALUE"])
    for x in (df.loc[:,"VALUE"]>0):
         print(squares.append(x**2))
         print(squares)


# In[62]:


def main():
        
    # data = DataReader('32100054.csv') # reads the .csv file
    #
    # dList = data.rowList()    # Function for Showing the data
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

# In[64]:


# Multithreading to execute two given process

   t1 = threading.Thread(target=sorting_OnValue)
   t2 = threading.Thread(target=sortingOn_UOM_ID)

   t1.start()# starting thread 1

   t2.start() # starting thread 2

   t1.join()# wait u ntil thread 1 is completely executed

   t2.join() # wait until thread 


#  # function for sorting Values in ascending or descending order
# 

# In[65]:


sortingOn_UOM_ID()


#  # function for sorting Values in ascending or descending order

# In[66]:


sorting_OnValue()


# In[68]:


show_on_UOM()


# In[69]:


show_on_Food_categories() #function for showing all rows having specific food category


# In[70]:


data = DataReader('32100054.csv') # reads the .csv file
    
dList = data.rowList()    # Function for Showing the data
showData(dList)
  


# In[71]:


total_ref_date()


# In[72]:


showOnCommodityName()


# In[73]:


showAllbyPd()


# In[74]:


showCommodiytOnUOM()

