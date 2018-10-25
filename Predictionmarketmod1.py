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
        self.stateOfWorld =  0
        #Prior value which can be adjusted(stays the same throughout)
        self.prior = 0.5
        #Price of contract start at 0.01
        self.price = 0.01
        #Payout if belief is true (not changed)
        self.payout = 1
        #epsilon, which is the change applied to sigma
        self.epsilon = 1/self.numAgents


    #A function to allow more readability for getting a normal distribution
    def get_truncated_normal(self,mean=0, sd=1, low=0, upp=10):
        return truncnorm(
            (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

    def randomSignal (self,a,b):
        number = random.random()
        if number <0.5:
            return a
        else:
            return b


    #Bayesian update of each round for belief
    def bayesianUpdate (self,likelihood,prior,accuracy):
        belief = (likelihood*self.prior)/accuracy
        return belief
    


    #Implementing the market strategies
    def marketStrategy(self,agent):
        maxPrice = self.beliefArray[agent]
        if self.price > maxPrice and self.investedArray[agent] >= 1:
            otherBeliefPrice = 1.0-self.price
            belief = self.beliefArray[agent]
            investableWealth = (1.0-belief)/self.wealthArray[agent]
            sellNumContracts = int(investableWealth/otherBeliefPrice)
            if (sellNumContracts<=self.investedArray[agent]):
                self.sellArray[agent]=sellNumContracts
                self.investedArray[agent]= self.investedArray[agent]-self.sellArray[agent]
                self.wealthArray[agent] = self.wealthArray[agent]+(self.price*self.sellArray[agent])
                self.investedArray[agent] = self.investedArray[agent]- (self.sellArray[agent]*self.price)
            else:
                self.sellArray[agent]= self.investedArray[agent]
                self.investedArray[agent]= 0
                self.wealthArray[agent] = self.wealthArray[agent]+(self.price*self.sellArray[agent])
                self.investedArray[agent] = self.investedArray[agent]- (self.sellArray[agent]*self.price)
        else:
            investableWealth = self.beliefArray[agent]/self.wealthArray[agent]
            numContracts = int(investableWealth/self.price)
            self.purchaseArray[agent]=numContracts
            self.wealthArray[agent] = self.wealthArray[agent]-(self.price*self.purchaseArray[agent])
            self.investedArray[agent] = self.investedArray[agent]+(self.purchaseArray[agent]*self.price)

      
        

    #determining a price of contract based on the number of agents willing to buy in that round and available contracts
    def priceOfContract(self):
        for 
        return price

    #updates the number of available contracts that can be bought which determines the price of a contract

    def updateMarket(self):
        


    # Running of the market over a few rounds and updating itself
    def runMarket(self):
        for a in range(len(self.beliefArray)): 
            self.beliefArray[a] = self.bayesianUpdate(self.signalArray[a],self.prior,self.accuracyArray[a])
            self.marketStrategy(a)
        self.updateAvailableContracts()
        #updates the price which also equates to the percentage believing a certain event would happen as a whole in the market
        self.price = self.priceOfContract()
        
        for i in range(len(self.signalArray)):
            self.signalArray[i] = self.beliefArray[i]
        print (self.beliefArray)
        print (self.price)
            


    #Setting up the market and agents
    def setMarket(self):
        # set the distribution of accuracy
        normAccuracy = self.get_truncated_normal(0.75,1,0.5 ,1)
        # set the distribution of wealth (THIS CAN BE CHANGED)
        normWealth = self.get_truncated_normal(0.5, 1, 0 , 1)
        # set the distribution of signals 
        normSignal = self.get_truncated_normal(0.5, 1, 0 , 1)
        # set the accuracy of each agent 
        self.accuracyArray = normAccuracy.rvs(self.numAgents)
        #set the state of that world in that certain market we would like to run
        self.stateOfWorld = int(random.uniform(0, 1) )
        print "state of world:"
        print (self.stateOfWorld)
        #set the wealth of each agent 
        self.wealthArray = normWealth.rvs(self.numAgents)
        self.wealthArray = self.wealthArray/self.wealthArray.sum()
        self.signalArray = normWealth.rvs(self.numAgents)
        #initialize signal array
            
        for i in range(self.numAgents):
            self.beliefArray.append(0)

        for i in range(self.numAgents):
            self.investedArray.append(0)
   
        #print(self.accuracyArray)
        #print(self.beliefArray)
        #print(self.signalArray)
        print(self.wealthArray)
        

if __name__ == "__main__":
    r = run()
    r.setMarket()
    #r.runMarket()



    
