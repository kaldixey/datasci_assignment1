'''
ARCL0160 Assessment 1 2018

@author: CTRL0
'''

'''
IMPORTS:

'''
import os
from table import Table

class Analysis(object):
    '''
    This class runs scaling and regression analysis on a list of tables from a folder, using 
    functions defined inside the Tables class.
    The class variables include folder (the location of the files - a string), the desired filetype
    as a list, and tables as an empty list to be populated.
    '''
    folder = ""
    file_type = [".csv"]
    tables =[]
    
    def __init__(self, folder, r):
        '''
        The constructor searches through files in the folder and  loads in each csv table 
        by checking the file extension is of csv type.
        It then appends each table in the data folder to the list self.tables.
        '''
        self.r = r
        self.folder = folder
        all_files = (os.listdir(self.folder))
        for tablename in all_files:
            if os.path.splitext(tablename)[1] in self.file_type:
                #print(tablename)
                self.tables.append(Table(self.folder,tablename,self.r))
            #print(self.tables)

    def do_analysis(self):
        '''
        This function loops through each table in self.tables and calls the do_scaling and do_regression
        function from the tables class on each one.
        '''
        for table in self.tables:
            table.do_scaling()
            #table.convert_variables_to_r()
            table.do_regression()
        '''
        The list of tables is then sorted using self.fit (called in via the return.fit function in tables) 
        as the key. Sort function results in ascending values by default.
        '''
        self.tables.sort(key=Table.return_fit)
        '''
        By then selecting the first item in the sorted list (at index 0) we return the table with the 'best'
        fit (the lowest number).
        '''
        return self.tables[0]
