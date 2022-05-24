import requests
from bs4 import BeautifulSoup, NavigableString

#-------------------- STEM -------------------------

list_of_stemJobs = []

web_res = requests.get("https://www.onetonline.org/find/stem?t=0")
web_src = web_res.content
soup = BeautifulSoup(web_src, 'html.parser')

web_content = soup.find('div', id = "content")
table = web_content.find('table').find_all('tr')

for row in table:
    cols = row.find_all('td')
    if(cols != []):
        colWithLink = cols[1]
        for job_data in colWithLink:
            if type(job_data) == NavigableString:
                break
            if (job_data.has_attr('href')):
                job_link = job_data.get('href')
                list_of_stemJobs.append(job_data.string)

#-------------------- All Jobs -------------------------

file = open('/Users/chrismendoza/Desktop/CSC366/366-Project/OnetJobs.sql', "w")

web_res2 = requests.get("https://www.onetonline.org/find/all")
web_src2 = web_res2.content
soup2 = BeautifulSoup(web_src2, 'html.parser')

web_content2 = soup2.find('div', id = "content")
table2 = web_content2.find('table').find_all('tr')

for row in table2:
    cols = row.find_all('td')
    if(cols != []):
        colWithLink = cols[2]
        for job_data in colWithLink:
            if type(job_data) == NavigableString:
                break
            if (job_data.has_attr('href')):
                job_link = job_data.get('href')
                job_res = requests.get(job_link)
                job_src = job_res.content
                job_soup = BeautifulSoup(job_src, 'html.parser')
                job_content = job_soup.find('div', id = "content")

                quote = "'"

                job_link_db = '"' + str(job_link) + '"'

                job_name_span = job_content.find('span')
                job_name_string = job_name_span.get_text()
                job_name_string_db = '"' + str(job_name_string) + '"'


                job_desc_p = job_content.find('p')
                job_desc_string = job_desc_p.get_text()
                job_desc_string_db = '"' + str(job_desc_string) + '"'

                if job_name_string in list_of_stemJobs:
                    #print(job_name_string + ": " + job_desc_string + " - " + "Stem") 
                    file.write(f"INSERT INTO ONetJobs(Title, Description, Link, isStem) Values ({job_name_string_db},{job_desc_string_db},{job_link_db},{1});\n")

                else:
                    #print(job_name_string + ": " + job_desc_string + " - " + "Non-Stem") 
                    file.write(f"INSERT INTO ONetJobs(Tile, Description, Link, isStem) Values ({job_name_string_db},{job_desc_string_db},{job_link_db},{0});\n")

file.close()
           




            
