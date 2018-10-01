from urllib.request import urlopen
import json
import csv
import os.path
from os import listdir
from os.path import isfile,join

# Initialise some variables
mypath="wikidata"
jsonfiles=[f1 for f1 in listdir(mypath) if isfile(join(mypath,f1))]
numfiles=len(jsonfiles)
finaldata = []

# Get claim type wikidata ID
def getClaimProperty(clinst):
	return clinst["mainsnak"]["property"]

count=1
# Extract provenance data from JSON files
for file in jsonfiles:
	print(str(count) + "/" + str(numfiles))
	count=count+1
	with open(mypath+"/"+str(file), encoding='utf-8') as f:
		data=json.load(f)
		wikidataID = os.path.splitext(str(file))[0]
		claims=data["entities"][wikidataID]["claims"]
		for claim in claims:
			claiminstances=claims[claim]
			for claiminstance in claiminstances:
				if "references" in claiminstance:
					claimproperty = getClaimProperty(claiminstance)
					claiminstance_references=claiminstance["references"]
					for reference in claiminstance_references:
						referencetypes=reference["snaks"]
						for referencetype in referencetypes:
							finaldata.append([wikidataID, claimproperty, referencetype])
							
# Write data to file
with open('wikidata_provenance_results.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(finaldata)