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
print("Probability of guessing all 6 cups correct:", probability_all_correct)

#5 correct 1 wrong
#correct_guesses = 1: Since there is only one possible combination that would be correct, correct_guesses is set to 1.
#probability_all_correct = correct_guesses / ways: Shows the probability of guessing all 6 cups correctly by dividing the 1 correct combination by the total number of combinations (ways).
correct = math.comb(with_milk, 5) 
wrong = math.comb(no_of_cups - with_milk, 1)  
total = correct * wrong
probability = correct / total 
