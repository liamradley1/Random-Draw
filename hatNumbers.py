# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:23:25 2020

@author: Liam
"""

#   WARNING this program has complexity O(m*n^2), with m - number of iterations
#   and n - number of items in the hat. Observe further that getting any 
#   reasonable probability distribution for a large n requires a larger still.
#   As the question mandates n=2020, you may be in for a long wait.


import random
import matplotlib.pyplot as plt


def hatNumber(maxNumber):
    # Input : maxNumber - the maximum number on the set of cards.
    numbers=[]
    for i in range(1,maxNumber+1):
        numbers.append(i)                                       # Initialise the list of numbers
    while len(numbers)!=1:                                      # Once length is 1, we have only one number remaining
        numbersChosen=random.choices(numbers,k=2)               # Choose 2 numbers from the remaining list of numbers
        numberReadded=abs(numbersChosen[0]-numbersChosen[1])    # Readd the difference between the two as per the brief
        for number in numbersChosen:
            for number2 in numbers:
                if(number==number2):                            
                    numbers.remove(number2)                     # Remove the numbers just used.
        numbers.append(numberReadded)       
    return(numbers[0])                                                              

def probDist(maxNumber,numIterations):
    # Inputs : maxNumber - the maximum number on the set of cards.
    # numIterations      - the number of times the experiment will be carried out.
    x=[]
    y=[]
    indicator = False
    for i in range(0,numIterations):
        print(i)
        indicator = False
        num=hatNumber(maxNumber)
        for number in x: 
            if num==number:        # if the number has appeared as a result already, add one to its frequency of occurring.
                indx=x.index(num)
                y[indx]+=1         
                indicator=True
            continue
        if(indicator == False):    # if it has not appeared yet, then add this number to the list of possible results.
            x.append(num)
            y.append(1)            # add one to this number's frequency of occurring, too.
    for i in range(0,len(y)):
        y[i]/=numIterations        # once all experiments are complete, convert the frequencies to probabilities.
    print(str(x)+","+str(y))       # print the of each number that occurs with its probability.
    zippedLists=zip(x,y)           # zip the lists so they can be paired and sorted into order together
    sortedLists=sorted(zippedLists)
    return sortedLists

def extractAndPlot(sortedLists):
    tuples= zip(*sortedLists)               # unzip lists so they can be used separately again.
    x,y=[list(tuple) for tuple in tuples]
    plt.plot(x,y)                           # plot the two lists against one another.
    plt.show()
    plt.savefig("probDistribution.png")     # save the list into a format which can be viewed.

def main(): 
    random.seed(1)
    maxNumber = 100
    numIterations = 1000000    # Chosen to be large enough to obtain a reasonable probability distribution.
    sortedLists = (probDist(maxNumber,numIterations)) 
    extractAndPlot(sortedLists)

main()