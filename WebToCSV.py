import requests
from bs4 import BeautifulSoup
import csv

url = 'http://bulletin.auburn.edu/generalinformation/auburnuniversitycalendar/'
r = requests.get(url)

page_source = r.text

soup = BeautifulSoup(page_source, "html.parser")

Cal_Event_list = []
for table in soup.select('table tbody tr'):
	cells = table.findAll('td')
	print(len(cells))
	date = cells[0].text.strip()
	description = cells[1].text.strip()
	Cal_Event = {date, description}
	Cal_Event_list.append(Cal_Event)
print(Cal_Event_list)