#Week 2 assignment

import urllib.request
import urllib.error
import datetime
import csv
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help="Enter a URL that links to a CSV file")
args = parser.parse_args()

logging.basicConfig(filename='errors.log', level=logging.ERROR)
logger = logging.getLogger('assignment2')

def downloadData(url):
	#Opens the URL link that is supplied
	datafile = urllib2.urlopen(url)
	return datafile
	
def processData(datafile):
	#Process datafile in the csv format and creates a dictionary with userid keys
	readfile = csv.DictReader(datafile)
	newdictionary = {}
	for num, line in enumerate(readfile):
		try:
			born = datetime.datetime.strptime(line['birthday'], '%d/%m/%Y')
			newdict[line['id']] = (line['name'], born)
		except:
			logging.error('Error processing line #{} for ID# {}'.format(num, line['id']))
	return newdict
	
def displayPerson(id, personData):
	#Finds the ID# in the newdict and returns DOB and name linked to ID#
	idnumber = str(id)
	if idnumber in personData.keys():
		print('Person #{} is {} with a birthday of {}'.format(
		id, personData[idnumber][0],
		 datetime.datetime.strftime(personData[idnumber][1], '%Y-%m-%d')))
	else:
		print('No user found with that ID.')

def main():
	#Combines all three functions into one program
	if not args.url:
		raise SystemExit
	try:
		csvData = downloadData(args.url)
	except urllib2.URLError:
		print('Please enter a valid URL.')
		raise
	else:
		personData = processData(csvData)
		idchoose = raw_input('Please enter an ID # for lookup:')
		print(idchoose)
		idchoose = int(idchoose)
		if idchoose <= 0:
			print('Number equal to or less than zero entered. Exiting program.')
			raise SystemExit
		else:
			displayPerson(idchoose, personData)
			main()
