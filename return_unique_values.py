# Code by:      MROSARIO
# Date Created: 13-MAR-2025
# Description:  The code will:
#               1. Checks list or dictionaries and and remove the duplicates 
#               2. Returns values in the same order of the elements without the duplicates

def unique(elements=[]):
    return_values = []
    for element in elements:
        if element not in return_values:
            return_values.append(element)
    return return_values

unique([0, 1, 1, 1, 1, 1, 23, 12, 12, 391, 98])
            
