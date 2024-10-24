#Import necessary Libraries
import math
import itertools
import random
import numpy as np
import matplotlib.pyplot as plt


no_of_cups = 12
with_milk = 6 
#How many ways of guessing all 6 correctly?
ways = math.comb(no_of_cups, with_milk)
print (ways)
#Prints 924