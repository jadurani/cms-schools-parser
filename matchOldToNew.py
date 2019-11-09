#!/usr/bin/env python2

import json
import csv

OLD_SCHOOLS_PATH = "matchOldToNew_input/schoolsWithReports.tsv"
NEW_SCHOOLS_PATH = "schoolPlaceDetails_output/newSchoolsWithIds.json"


newSchoolsFile = open(NEW_SCHOOLS_PATH, 'r')
newSchoolsData = json.load(newSchoolsFile)
newSchoolsFile.close()

def getMatchId(dbId, schoolName, cityId):
  for newSchoolObj in newSchoolsData:
    if newSchoolObj["name"] == schoolName and cityId == newSchoolObj["city_id"]:
      newSchoolObj["school_id"] = dbId
      return schoolName
  print dbId, schoolName, cityId

# outArr = []
with open(OLD_SCHOOLS_PATH, 'r') as fileInput:
  data = csv.reader(fileInput, delimiter='\t')
  for d in data:
    getMatchId(d[0], d[1], d[2])

with open("matchOldToNew_output/newSchoolsMatched.json", 'w') as outFile:
  json.dump(newSchoolsData, outFile, indent=2)
