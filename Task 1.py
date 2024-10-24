#Import necessary Libraries
import math
import itertools
import random
import numpy as np
import matplotlib.pyplot as plt

#Reference: https://github.com/ianmcloughlin/2425_applied_statistics/blob/main/02_lady_tasting_tea.ipynb
no_of_cups = 12
with_milk = 6 
#How many ways of guessing all 6 correctly?
ways = math.comb(no_of_cups, with_milk)
print (ways)
#Prints 924

#Probability of guessing all 6 correctly
correct_guesses = 1
probability_all_correct = correct_guesses / ways
print("Probability of guessing all 6 cups correctly:", probability_all_correct)

