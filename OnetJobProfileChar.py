import openpyxl

wb = openpyxl.load_workbook('O-NetComputerScienceTemplateforSurvey_5_13_2022.xlsx')
ws = wb['Sheet1']

for row in ws.iter_rows(min_row=7):
    characteristic = row[0].value
            
    for cell in row:
        if cell.hyperlink:
            link = cell.hyperlink.display
            print(link)
    print(characteristic)
            

        #open each hyperlink
