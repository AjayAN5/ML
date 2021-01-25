import numpy as np
import pandas as pd
data=pd.read_csv('finds.csv')
concepts = np.array(data)[:, 0:-1]
target = np.array(data)[:, -1]


def learn(concepts, target):
    #initialize Specific and General Hypothesis
    specific_h = concepts[0].copy()
    general_h = [["?" for i in range(len(specific_h))]
                 for i in range(len(specific_h))]

    for i, h in enumerate(concepts):
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        if target[i] == "No":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
        
        print("Iteration[" + str(i+1) + "]")
        print("Specific: " + str(specific_h))
        print("General: " + str(general_h) + "\n")
        
    #Trimming general_h by Removing completely generalized list
    general_h=[general_h[i] for i, h in enumerate(general_h) if h!= ['?' for x in range(len(specific_h))]]
    return specific_h,general_h

specific,general=learn(concepts,target)

print("Final Hypothesis: ")
print("Specific hypothesis: " + str(specific))
print("General hypothesis: " + str(general))
