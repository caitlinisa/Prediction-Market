from scipy.stats import truncnorm
import math
import random
import numpy as np
import matplotlib.pyplot as plt

class run:

    def __init__(self):
        #Initialize number of agents N
        self.numAgents = 100
        #The array of agents with their corresponding accuracy
        self.accuracyArray = []
        # The array of agents with their corresponding wealth 
        self.wealthArray = []
        # The array of agents with their corresponding information probability (signals)
        self.signalArray = []
        # The array of agents with their corresponding belief
        self.beliefArray = []
        # The array that stores the invested number of contracts purchased by an agent
        self.investedArray = []
        # The number of available contracts to be traded (plus determining of the price)
        self.numberofContracts = 1
        #Fix the true state of the world
        self.stateOfWorld =  1
        #Prior value which can be adjusted(stays the same throughout)
        self.prior = 0.5
        #Price of contract start at 0.01
        self.price = 0.01
        #Payout if belief is true (not changed)
        self.payout = 1
        #epsilon, which is the change applied to sigma
        self.epsilon = 1/self.numAgents
        #sum of invested wealth
        self.sum = 0


    #A function to allow more readability for getting a normal distribution
    def get_truncated_normal(self,mean=0, sd=1, low=0, upp=10):
        return truncnorm(
            (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)



    #Bayesian update of each round for belief
    def bayesianUpdate (self,likelihood,prior,accuracy):
        belief = (likelihood*self.prior)/accuracy
        return belief

    def investWealth(self,belief,wealth):
        investedAmount = belief*wealth
        return investedAmount

    
    def priceOfContract(self):
        print ("sum of investement")
        print (self.sum)
        price = self.sum
        return price

    def runMarket(self):
        for a in range(self.numAgents): 
            self.beliefArray[a] = self.bayesianUpdate(self.signalArray[a],self.prior,self.accuracyArray[a])
            self.investedArray[a]= self.investWealth(self.beliefArray[a],self.wealthArray[a])
            self.sum = self.sum + self.investedArray[a]
        #updates the price which also equates to the percentage believing a certain event would happen as a whole in the market
        self.price = self.priceOfContract()
        print ("belief array:")
        print (self.beliefArray)
        print ("price:")
        print (self.price)

#calculating maximum utility in each agent so as to change epsilon and price of contracts




    def setMarket(self):
        # set the distribution of accuracy
        normAccuracy = self.get_truncated_normal(0.75,1,0.5 ,1)
        # set the distribution of wealth 
        normWealth = self.get_truncated_normal(0.5, 1, 0 , 1)
        # set the distribution of signals 
        normSignal = self.get_truncated_normal(0.5, 1, 0 , 1)
        # set the accuracy of each agent 
        self.accuracyArray = normAccuracy.rvs(self.numAgents)
        #set the state of that world in that certain market we would like to run
        #self.stateOfWorld = int(random.uniform(0, 1) )
        print ("state of world:")
        print (self.stateOfWorld)
        #Initialize all arrays
        self.wealthArray = normWealth.rvs(self.numAgents)
        self.wealthArray = self.wealthArray/self.wealthArray.sum()
        #self.signalArray = normWealth.rvs(self.numAgents)

        for i in range(self.numAgents):
            self.signalArray.append(random.uniform(0, 1))
        
        for i in range(self.numAgents):
            self.beliefArray.append(0)

        for i in range(self.numAgents):
            self.investedArray.append(0)
        
        print(self.accuracyArray)
        print(self.beliefArray)
        print(self.signalArray)
        print(self.wealthArray)



if __name__ == "__main__":
    r = run()
    r.setMarket()
    r.runMarket()