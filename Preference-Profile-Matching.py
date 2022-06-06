import pandas as pd
import sys
from scipy import spatial
from numpy import char, dot 
from numpy.linalg import norm
import scipy

mycsv = pd.read_csv("characteristics.csv", skiprows=2)

myrow = mycsv["Dimension: Task Characteristics"]
myrow = list(myrow)

chardict = {}
temp = []
for x in myrow:
    if x != " " and type(x) == str and len(x) < 50 and x.split()[0] != "Dimension:":
        x = x.lstrip("*")
        temp.append(x.lower().rstrip(" "))
    
for x in range(len(temp)):
    chardict[temp[x]] = x+1

mycsv = pd.read_csv("ProfileCharacteristics.csv")
grouped = mycsv.groupby('Job')


charVal = pd.read_csv("charVal.sql", header=None)
profileGrouped = charVal.groupby(3)

with open('Match-Preference-Profile.sql', 'w') as f:
    sys.stdout = f

    for profId, group in profileGrouped:
        profId = ''.join(x for x in profId if x.isdigit())        #print(group)
        charId = group[4].tolist()
        charVal = group[5].tolist()
        weight = group[6]
        weight = [int(x.rstrip(");").lstrip(" ")) for x in weight]
        #print(charId)
        #print(charVal)
        #print(weight)
        #print(" ")

        # Job, Task Characteristic, Column, Value
        comparisonJobs = []
        similaritys = []
        for job, group in grouped:
                characteristicDimension = []
                charString = group["Task Characteristic"].tolist()
                charString = [x.lower() for x in charString]
                charString = [x.replace("-", " ") for x in charString]
                charString = [x.split('(')[0].rstrip(" ") for x in charString]
                charString = [x.replace("the organization", "research group") for x in charString]
                val = group["Value"].tolist()
                for temp in charString:
                    characteristicDimension.append(chardict[temp])

                comparisonList = []
                newWeight = []
                for y in characteristicDimension:
                    if y in charId:
                        comparisonList.append(charVal[charId.index(y)])
                        newWeight.append(weight[charId.index(y)])
                    else:
                        val.pop(characteristicDimension.index(y))

                comparisonList = [float(x) for x in comparisonList]
                val = [float(x) for x in val]

                #print(charId)
                #print(charVal)
                #print(weight)
                #print(" ")
                #print(characteristicDimension)
                #print(comparisonList)
                #print(val)
                #print("___________")

                comparisonJobs.append(job)
                similaritys.append(scipy.spatial.distance.cosine(val, comparisonList, newWeight))
        
        sortedsimilaritys = sorted(similaritys)
        sortedJobs = [x for _, x in sorted(zip(similaritys, comparisonJobs))]
        for x in range(10):
            print("profId: " + str(profId) + ", Ranking: " + str(x) + ", Job: " + str(sortedJobs[x]) + ", Similarity: " + str(sortedsimilaritys[x]))




