import pandas as pd
import sys
from scipy import spatial
from numpy import char, dot 
from numpy.linalg import norm

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

#print(chardict)

mycsv = pd.read_csv("ProfileCharacteristics.csv")
grouped = mycsv.groupby('Job')



ureProfile = pd.read_csv("URE-Profiles.sql", header=None)
ureProfile = ureProfile[ureProfile[1].str.contains("charId")]
uregrouped = ureProfile.groupby(2)

with open('Match-EXP-Profile.sql', 'w') as f:
    sys.stdout = f

    for profId, masterCharId in uregrouped:
        profId = ''.join(x for x in profId if x.isdigit())
        #print(profId)
        charId = masterCharId[3].tolist()
        masterCharId = masterCharId[4].tolist()
        masterCharId = [x.rstrip(");").lstrip(" ") for x in masterCharId]
        #print(charId)
        #print(masterCharId)
        



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
                for y in characteristicDimension:
                    if y in charId:
                        comparisonList.append(masterCharId[charId.index(y)])
                    else:
                        val.pop(characteristicDimension.index(y))

                #print(" ")
                #print(characteristicDimension)
                comparisonList = [float(x) for x in comparisonList]
                val = [float(x) for x in val]
                #print(comparisonList)
                #print(len(comparisonList))
                #print(len(val))
                #print(" ")
                #print(val)
                #print("___________")

                comparisonJobs.append(job)
                similaritys.append(dot(comparisonList, val)/(norm(comparisonList)*norm(val)))
        
        sortedsimilaritys = sorted(similaritys)
        sortedJobs = [x for _, x in sorted(zip(similaritys, comparisonJobs))]
        for x in range(10):
            print("profId: " + str(profId) + ", Ranking: " + str(x) + ", Job: " + str(sortedJobs[x]) + ", Similarity: " + str(sortedsimilaritys[x]))



