import numpy as np
import random
from fractions import Fraction
def mchain(input,order, output_length):
    """When feeding the model a string of letters, under order one, ensure that there is a space between each letter"""
    if order==0:
        input_temp=input
        input_length=len(input)
        numberoflett=int(input_length-(input_length/2))+1
        unique_letters=list(set(input_temp.replace(" ","")))
        counts=[]
        for letter in unique_letters:
            count=input_temp.lower().count(letter)
            counts.append(count)

        probab=[]
        for ele in counts:
            probab.append(ele/numberoflett)
                
        test=[]
        for i in range(output_length):
            step=np.random.choice(a=unique_letters, p=probab)
            test.append(step) 
        
        out_string=""
        return out_string.join(test)
    #else:
        
    

"""
input="a g g g c a g c g g g c g"
order=0
output_length=13
mchain(input,order, output_length)

RETURNS: 'gcgccggcagcgg'
"""

                             
