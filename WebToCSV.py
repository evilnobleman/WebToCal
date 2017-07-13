import requests
from bs4 import BeautifulSoup
import csv

url = 'http://bulletin.auburn.edu/generalinformation/auburnuniversitycalendar/'
r = requests.get(url)

page_source = r.text

soup = BeautifulSoup(page_source, "html.parser")

Heading = []
Cal_Event_list = []
count = 0
for heading in soup.select('h3'):
	Heading.append(heading)
for table in soup.select('table tbody tr'):
	cells = table.findAll('td')
	print(len(cells))
	date = cells[0].text.strip()
	description = cells[1].text.strip()
	Cal_Event = [date, description ,headin]
	Cal_Event_list.append(Cal_Event)
	
with open('Cal_CSVs.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for row in range(len(Cal_Event_list)):
    	date = Cal_Event_list[row][0]
    	description = Cal_Event_list[row][1]
    	print(date + ": " + description)
    	#wr.writerow(date.encode('utf8'))
    	#wr.writerow(description.encode('utf8'))
