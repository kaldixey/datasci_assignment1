'''
ARCL0160 Assessment 1 2018

@author: CTRL0
'''
'''
IMPORTS:
os is imported for file path id & manipulation
Table class is imported to test functions
Analysis class imported for analysis
pyper imported to facilitate regression in R. Pyper R object created.
'''

import os
from analyseCSV.table import Table
from analyseCSV.analysis import Analysis
import pyper

r = pyper.R(RCMD="C:\\Program Files\\R\\R-3.4.1\\bin\\x64\\R")
#r = pyper.R()
r.has_numpy = False
r.has_pandas = False

'''
__file__ refers to the location of the module. The os.path functions return
and normalise path/directory and these are assigned to src_folder.
The first part of src_folder is assigned to project_folder.
os.path.join joins the first part of the filepath with  "data" (or test_data) 
and assigns this as the folder to be operated on. This is printed to confirm 
the location of files being used for analysis.
'''
src_folder = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
project_folder = os.path.split(src_folder)[0]
data_folder = os.path.join(project_folder, "data")
print("Data files are in " + data_folder + "\n")
'''
The code below allowed interim testing of individual functions in Tables
before constructing and using the Analysis class.
'''
#table1 = Table(data_folder, "test_file1.csv", r)
#table1.print_input_table()
#table1.do_scaling()
#table1.print_scaled_table()
#table1.test_R()
#table1.convert_variables_to_r()
#table1.do_regression("scaled_size", "scaled_population")
#table1.print_filename()
#table1.print_table_summary()        
'''
Creates an Analysis object instance called analysis1 using the data_folder 
variable assigned above. Also calls in r as an argument.
'''
analysis1 = Analysis(data_folder,r)
'''
The code below calls do_analysis on the instance above to find the table
with the best fit and print, along with the filename and table summary defined
in the Table class to put the result into context.
'''
best_fit_table = analysis1.do_analysis()
print("The file with the best fit between size and population is: ")
best_fit_table.print_filename()
best_fit_table.print_table_summary()

