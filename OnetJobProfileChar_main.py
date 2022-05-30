import openpyxl

import csv
import requests
from bs4 import BeautifulSoup, NavigableString

wb = openpyxl.load_workbook('O-NetComputerScienceTemplateforSurvey_5_13_2022.xlsx')
ws = wb['Sheet1']

# creation of csv file
file = open('/Users/chrismendoza/Desktop/CSC366/366-Project/ProfileCharacteristics.csv', "w")
writer = csv.writer(file)
header = ['Job','Task Characteristic','Column','Value']
writer.writerow(header)

# iterate through each task characteristic of csv
for row in ws.iter_rows(min_row=7):
    characteristic = row[0].value
    print(characteristic) 
    # iterate through each column   
    for cell in row:
        if cell.hyperlink:
            # open each link up from csv and create bs object
            link = cell.hyperlink.display
            web_res = requests.get(link)
            web_src = web_res.content
            soup = BeautifulSoup(web_src, 'html.parser')
            # find table in each link and extract data
            web_content = soup.find('div', id = "content")
            table = web_content.find('table').find_all('tr')
            ProfileCharacteristics = [0,0,0,0]
            # Level/Importance ----------------
            if (cell.column < 11 and cell.column > 2):
                for row in table:
                    cols = row.find_all('td')
                    if(cols != []):
                        # for col in cols:
                        ProfileCharacteristics[0] = (cols[4].get('data-text'))
                        ProfileCharacteristics[1] = characteristic
                        ProfileCharacteristics[2] = cell.column
                        # if level is null, use importance as value
                        value = (cols[1].get('data-text')) 
                        if (value == "-2" or value == "-1"):
                            value = (cols[0].get('data-text')) 
                        else:
                            value = (cols[1].get('data-text')) 
                        ProfileCharacteristics[3] = value
                        writer.writerow(ProfileCharacteristics)
            
            # Context ---------------------
            if (cell.column < 14 and cell.column > 11):
                for row in table:
                    cols = row.find_all('td')
                    if(cols != []):
                        # for col in cols:
                        ProfileCharacteristics[0] = (cols[3].get('data-text'))
                        ProfileCharacteristics[1] = characteristic
                        ProfileCharacteristics[2] = cell.column
                        ProfileCharacteristics[3] = (cols[0].get('data-text'))
                        writer.writerow(ProfileCharacteristics)
file.close()        


                              

