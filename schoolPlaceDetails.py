#!/usr/bin/env python2

import json
import os
import sys

SCHOOLS_FILE = 'schoolPlaceDetails_input/new_schools_1711-9-nov-2019.json'
PLACES_FILE = 'placeParser_output/PHLocations.json'

placesFile = open(PLACES_FILE, 'r')
placesData = json.load(placesFile)
placesFile.close()


matchedSchoolsArr = []
def getSchoolPlace(cityName, divName, regName):
  return cityName.lower() + "_" + divName.lower() + "_" + regName.lower()

invalidIds = {}
count = 0
with open(SCHOOLS_FILE, 'r') as schoolsFile:
  schoolsData = json.load(schoolsFile)
  for school in schoolsData:

    schoolPlaceId = getSchoolPlace(school["city"], school["division"], school["region"])
    if schoolPlaceId not in placesData:
      invalidIds[schoolPlaceId] = 0
      count += 1
    else:
      placeObj = placesData[schoolPlaceId]
      matchedSchoolObj = {}
      matchedSchoolObj["name"] = school["school_name"]
      matchedSchoolObj["official_school_id"] = school["school_id"]
      matchedSchoolObj["division"] = school["division"]
      matchedSchoolObj["division_id"] = placeObj["divId"]
      matchedSchoolObj["region"] = school["region"]
      matchedSchoolObj["region_id"] = placeObj["regId"]
      matchedSchoolObj["city"] = school["city"]
      matchedSchoolObj["city_id"] = placeObj["cityId"]
      matchedSchoolObj["address"] = school["address"]
      matchedSchoolsArr.append(matchedSchoolObj)

print len(invalidIds.keys()), count
# for i in invalidIds.keys():
#   print i
# print invalidIds

OUTFILE_PATH = 'schoolPlaceDetails_output/newSchoolsWithIds.json'
print 'output at ', OUTFILE_PATH
with open(OUTFILE_PATH, 'w') as updatedSchoolsFile:
  json.dump(matchedSchoolsArr, updatedSchoolsFile, indent=2)