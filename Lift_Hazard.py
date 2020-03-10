# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:27:55 2020

@author: RitamM
"""
import pandas as pd
import sys
def lift_hazard(position_of_lifts,calls):
    position_of_lifts = [int(i) for i in position_of_lifts]
    calls = [int(i) for i in calls]
    dist = []
    lifts = []
    for i in calls:
        for j in position_of_lifts:
            dist.append(abs(i - j))
        lifts.append(dist)
        dist = []
    df = pd.DataFrame(lifts)
    for j in range(len(df)):
        mindf = df.min(axis = 1).sort_values(ascending = True)
        key,value = zip(*mindf.iteritems())
        cols = df.loc[:,(df==value[0]).any()].columns.values[0]
        index = df[df[cols] == value[0]].index.values[0]
        print(cols)
        print(index)
        position_of_lifts[index] = calls[cols]
        df = df.drop(cols,axis = 1)
        df = df[df.index != index]
    print("Final Position of lifts =>\n",position_of_lifts)
if __name__=="__main__":
    position_of_lifts = input("Enter the position of 3 lifts 1st lift,2nd lift,3rd lift => ").split(',')
    print("\n Max number of registered call is 3, once a call is"+ 
          " registered to a lift, it discards all the next call and servs the first 3 calls.\n"+
          "So the length of a calls list will be 3.")
    calls = input("Enter the floors where lift is called 1st Call,2nd Call,3rd Call => ").split(',')
    if(len(calls) > 3):
        sys.exit("Read the condition again :) \n")
    lift_hazard(position_of_lifts,calls)