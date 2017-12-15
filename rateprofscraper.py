import requests
import json
import time
import pymongo
import csv

db = pymongo.MongoClient().local.ratemyprofs
pdata = open('output.csv', 'w')
output = csv.writer(pdata)

counter = 0

for i in range(1,500):
	
	#http://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=University+of+California+Berkeley&schoolID=1072&queryoption=TEACHER
	query = "http://www.ratemyprofessors.com/filter/professor/?department=&institution=University+of+California+Berkeley&page="+str(i)+"&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=1072"

	
	try:
		page = requests.get(query)
		jsonpage = json.loads(page.content)
		professorlist = jsonpage['professors']

		for prof in professorlist:
			if counter == 0:
				header = prof.keys()
				output.writerow(header)
				counter = 1
			output.writerow(prof.values())
			db.insert(prof)

		print "page "+str(i)+" "+'\xF0\x9F\x98\x8F'
	except:
		pass

	time.sleep(1)
pdata.close()