#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:10:55 2018

@author: giovimax
"""

"""first writing of the duble entry system code"""
#%%
from copy import copy
import pickle 

#%%

def computeTotal(movList):#computes the absolute value of the entry
    #to complete with safety mesures
    """inferring that accounting equation holds"""
    total = 0
    for movement in movList:
        if movement.way == "Debt":
            total += movement.ammount
    return total
            
class entry():
    
    def __init__(self, movementList, ID = None):
        self.ID = ID
        self.movementList = movementList
        self.total = computeTotal(movementList)
        
        
    def describe(self):
        print("Entry ID:",self.ID)
        for movement in self.movementList:
            print(" Account:",movement.account,"\n",
                  "Way:",movement.way,"\n",
                  "Ammount:",movement.ammount)
    pass
    

class movement():
    def __init__(self, account, way, ammount):
            self.account = account
            self.way = way
            self.ammount = ammount
        
            
#%%
class book():

    
    def __init__(self):
        self.entryList = []
        self.accountList = []
        self.entryID = -1 #so the first entry has ID 0 
        self.entryDictID = {}
    
    def createEntry(self, movementList):
        
        def entryCheck(movList):
            
            accountCheck = {} #saving the name of accounts is possible to flag multiple wrong accounts
            total = 0
            
            for movement in movList: #iterating over each movement to gather data
                
                if True:#flagging unexisting accounts
                    #debug
                    print(movement.account)
                    
                    if movement.account in self.accountList: #existing accounts
                        
                        accountCheck[str(movement.account)] = True
                    else: #non existing accounts
                        accountCheck[str(movement.account)] = False
                
                if True: #calculating total value of transaction
                    if movement.way == "Debt":
                        total += movement.ammount
                    elif movement.way == "Credit":
                        total -= movement.ammount
                    else: #also catching eventually misspelled ways 
                        print("error with:",movement.way)
                        raise ValueError
                        
                    #debug
                    print(total)
            #end of loop        
            accountError = False
            
            #debug
            print(accountCheck)
            
            
            
            for Check in accountCheck: #verifying 
                if accountCheck[Check] == False:
                    print(str(Check)+" not in accountList")
                    accountError = True
            if accountError:
                raise ValueError#improve error handling

            if total != 0: #verifying accoung identity
                print("error whith accounting identity: total =",total)
                raise ValueError  

                
            return True
        
        if entryCheck(movementList):#if the data is correct cretes the entry      
        #saving entry data
            self.entryID += 1 #accounting for the new entry 
            self.entryList.append(entry(movementList, ID= self.entryID))
            self.entryDictID[copy(self.entryID)] = self.entryList[-1] 
        
    def newAccount(self, *args):
        for a in args:
            if type(a) == str:
                if a not in self.accountList:
                    self.accountList.append(a)
                else:
                    print("error with new account: "+a)
                    raise ValueError
            else:
                print("account namen must be string")
                raise ValueError
        print(args,"have been added to accountList")
        
    def describe(self):
        print("Describing...")
        for n, entry in enumerate(self.entryList):
            print(n)
            entry.describe()
        
    def delent(self, ID): #deletes an entry based on it's id
        for n, e in enumerate(self.entryList):
            if e.ID == ID:
                del self.entryList[n]
                break
        else:
            print("problem in deleting entry %i" %ID)
            raise ValueError
            
    
#%%
#debug
B = book()
B.newAccount("cash","bank")
movList = [movement("cash","Debt",10),movement("bank","Credit",10)]
B.createEntry(movList)
#specific debug
#test = entry(0,movList)
B.createEntry([movement("BBB", "Debt",5),movement("AAA","Credit",5)])


        


        



            
        
        