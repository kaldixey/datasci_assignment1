'''
ARCL0160 Assessment 1 2018

@author: CTRL0
'''
'''
IMPORTS:
os and csv imported to manipulate the filepath and read the csv file
math imported to sum the values of self.size and self.population
'''
import os, csv
import math


class Table(object):    
    '''
    This class reads in a csv file and carries out scaling and regression on some of the resulting
    data using the pyper library to call in R.
    Each variable in this class represents a datatype found in each table in the data folder. 
    Alpha, beta and fit are floats, the filename is a string and the remaining variables
    will be lists.
    '''
    alpha = 0.0
    beta = 0.0
    size = []
    scaled_size = []
    population = []
    scaled_population = []
    fit = 0.0
    filename = ""
    r = None
    
    def __init__(self, path, filename, r):
        self.r = r
        '''
        Below is the method I originally used to create the pyper R object and test
        it using a try/except statement. This caused a problem as it created a connection
        to R for all files in data, which overloaded the system. To address this I have 
        created the connection to R once only inside run.py.
        '''        
        #try:
        '''
            
            '''
            #self.r = pyper.R()
            #self.r.has_numpy = False
            #self.r.has_pandas = False
            #pi = self.r["pi"]
            #print("\nIt seems your connection to R is working!\nR returns this value for pi: " + str(pi))
        #except:
            #print("\nIt seems your connection to R is NOT working!\nTerminating.")
        
        '''
        Here the constructor opens a single file and loads in the alpha, beta, size and
        population values using the os and csv libraries.
        '''
        self.filename = filename
        
        tmp_size = []
        tmp_population = []
        
        with open(os.path.join(path, self.filename), 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            #print(reader.fieldnames)
            '''
            reader.next() reads the first row of data and assigns it to row. The subsequent
            code assigns each item in the row to the relevant class variables.
            '''
            row = reader.next()
            #print(row)
            self.alpha = float(row["Alpha"])
            self.beta = float(row["Beta"])
            #print("Alpha=" + str(self.alpha) + " Beta=" + str(self.beta))
            tmp_size.append(float(row["Size"]))
            tmp_population.append(float(row["Population"]))
            
            '''
            Here the remaining values of size and population in the table are appended to the
            relevant lists.
            '''
            for row in reader:
                tmp_size.append(float(row["Size"]))
                tmp_population.append(float(row["Population"]))
        '''
        tmp_size and tmp_population are assigned to the size and population class variables.
        '''
        self.size = tmp_size
        self.population = tmp_population
        
    #def convert_variables_to_r(self):
        '''
        this function originally converted the variables to a form to be called inside pyper.
        However after modifying the way pyper was called in this is no longer applicable.
        '''
        #this function converts the variables to a form that can be called inside pyper
        #self.r["r_scaled_size"] = self.scaled_size
        #self.r["r_scaled_population"] = self.scaled_population
    
        
    def do_regression(self):
        '''
        do_regression runs a regression analysis of scaled_size against scaled_population, and
        saves the regression coefficient in self.fit. This is used in Analysis to 
        sort the list of tables and locate the best fit.
        '''
        self.r.a = self.scaled_size
        self.r.b = self.scaled_population
        formula = "a ~ b"
        self.r("r_regression_model <- lm(" + formula + ")") 
        self.fit = self.r["deviance(r_regression_model)"]
        return self.fit
    
    def do_scaling(self):
        '''
        do_scaling takes the sum of the size and population lists defined above and divides each list
        item by the total, appending the result to a new scaled list. These lists are used in do_regression.
        '''
        total_size = math.fsum(self.size)
        total_population = math.fsum(self.population)
        scaled_size = []
        scaled_population = []
        
        for item in self.size:
            scaled = item / total_size
            scaled_size.append(scaled)
        
        for item in self.population:
            scaled = item / total_population
            scaled_population.append(scaled)
        
        self.scaled_size = scaled_size
        self.scaled_population = scaled_population
    
    
    def print_filename(self):
        '''
        prints the filename so it can be identified in the final output
        '''
        print("File = " + self.filename)
         
        
    def print_input_table(self):
        '''
        prints the values and lists extracted from each table above. Used to check constructor
        functionality. Omitted for final analysis.
        '''
        print(self.filename, self.alpha, self.beta, self.fit, self.size, self.population)
    
    
    def print_scaled_table (self):
        '''
        prints the values and scaled lists extracted from each table. Used to check constructor
        functionality and scaling function. Omitted for final analysis.
        '''
        print(self.filename, self.alpha, self.beta, self.fit, self.scaled_size, self.scaled_population)
        
    
    def print_table_summary(self):
        '''
        prints a summary of the table containing the best for for final analysis. Ints/floats
        converted to strings for successful concatenation.
        '''
        print("Alpha = " + str(self.alpha) + ", Beta = " + str(self.beta) + ", Fit = " + str(self.fit))
        
        
    def return_fit (self):
        '''
        A function to return the fit of the table instance for use in Analysis.
        '''
        return self.fit
    
    
    #def test_R (self):
        '''
        Tests the functionality of R. Not used in final analysis.
        ''' 
        #pi = self.r['pi']
        #print("\nR returns this value for pi: " + str(pi[0]))
        
        
