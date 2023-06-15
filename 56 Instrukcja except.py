# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:00:25 2023

@author: mateu
"""



import sys

taskPerPerson = 0

try:
    tasks = 32
    personsStr = input("How many persons are there is the team? ")
    persons = int(personsStr)
    
    taskPerPerson = tasks / persons
    
# except mozna zwrocic nazwe bledu, wowczas gdy dany blad wystapi mozna wyswietlic komunikat zwiazany z 
# obsluzonym bledem
# as e mozna przekazac do komunikatu dodatkowe informacje o bledzie
except ValueError as e:
    print("Sorry - you need to enter an integer number: ", e)    
    
except ZeroDivisionError as e:
    print("Sorry - you need to enter value > 0: ", e)    
    
    
except:    
    print("Smoething went wrong...", sys.exc_info()[0])

print("Every person should have around ", taskPerPerson, "tasks")  






import sys
 
file_path = r'c:\temp\data_input\orders.csv'
 
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))
            
        except ValueError as e:
            print("Problem with conversion. Check whether the amount is correct. Line: %s" % line)
        
        except IndexError as e:
            print("Missing information. Check whether the line is build of at least 3 fields separated by comma. Line: %s" % line)
            
        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])
 
print("Processing finished")












































