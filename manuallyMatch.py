#!/usr/bin/env python2

import json

MANUALLY_MATCHED_PATH = "matchOldToNew_output/manuallyMatched.json"
NEW_SCHOOLS_PATH = "matchOldToNew_output/newSchoolsMatched.json"


newSchoolsFile = open(NEW_SCHOOLS_PATH, 'r')
newSchoolsData = json.load(newSchoolsFile)
newSchoolsFile.close()

def getMatchId(schoolId, offSchoolId):
  for newSchoolObj in newSchoolsData:
    if newSchoolObj["official_school_id"] == offSchoolId:
      newSchoolObj["school_id"] = schoolId
      return schoolId
  print schoolId, offSchoolId

# outArr = []
with open(MANUALLY_MATCHED_PATH, 'r') as fileInput:
  data = json.load(fileInput)
  for d in data:
    getMatchId(d["school_id"], d["official_school_id"])

with open("manuallyMatch_output/toDB.json", 'w') as outFile:
  json.dump(newSchoolsData, outFile, indent=2)
