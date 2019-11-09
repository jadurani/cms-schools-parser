#!/usr/bin/env python2

import json

CITIES_FILE_PATH = 'placeParser_input/ki_cities_2053-9-nov-2019.json'
DIVS_FILE_PATH = 'placeParser_input/ki_divisions_2053-9-nov-2019.json'
REG_FILE_PATH = 'placeParser_input/ki_region_2053-9-nov-2019.json'

# STEP 1
citiesDict = {}
citiesFile = open(CITIES_FILE_PATH, 'r')
citiesData = json.load(citiesFile)
citiesFile.close()

print len(citiesData)

for city in citiesData:
  newId = city["name"].lower() + "_" + city["division_id"]
  citiesDict[newId] = {
    "cityName": city["name"].lower(),
    "cityId": city["city_id"],
    "divId": city["division_id"]
  }

print len(citiesDict.keys())

# STEP 2
divsDict = {}
divsFile = open(DIVS_FILE_PATH, 'r')
divsData = json.load(divsFile)
divsFile.close()

# for easier retrieval
divsDataDict = {}
for div in divsData:
  divsDataDict[div["division_id"]] = {
    "name": div["name"].lower(),
    "regId": div["region_id"]
  }

nonDupsContainer = []
count = 0
for cityKey in citiesDict:
  cityObj = citiesDict[cityKey]
  cityName = cityObj["cityName"]
  divObj = divsDataDict[cityObj["divId"]]
  divName = divObj["name"]
  newId = cityName + "_" + divName + "_" + divObj["regId"]
  divsDict[newId] = {
    "cityName": cityName,
    "divName": divName,
    "cityId": cityObj["cityId"],
    "divId": cityObj["divId"],
    "regId": divObj["regId"]
  }
  if newId not in nonDupsContainer:
    nonDupsContainer.append(newId)
    count += 1
  else:
    print newId

print len(divsDict.keys())


# STEP 3
regDict = {}
regFile = open(REG_FILE_PATH, 'r')
regData = json.load(regFile)
regFile.close()

# for easier retrieval
regDataDict = {}
for reg in regData:
  regDataDict[reg["region_id"]] = reg["name"].lower()

for divKey in divsDict:
  divObj = divsDict[divKey]
  cityName = divObj["cityName"]
  divName = divObj["divName"]
  regName = regDataDict[divObj["regId"]]
  newId =  cityName + "_" + divName + "_" + regName
  regDict[newId] = {
    "cityId": divObj["cityId"],
    "divId": divObj["divId"],
    "regId": divObj["regId"]
  }

print len(regDict.keys()), count


with open('placeParser_output/PHLocations.json', 'w') as phLocFile:
  json.dump(regDict, phLocFile, indent=2)