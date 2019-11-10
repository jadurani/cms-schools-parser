#!/usr/bin/env python2

import json
import sys


# OUTPUT viea stout redirection
# ./toDB.py 1 > toDB_output/1_new_schools.sql
# ./toDB.py 2 > toDB_output/2_new_schools.sql

TODB_PATH = "manuallyMatch_output/toDB.json"
BATCH = int(sys.argv[1])

def addToInsertData(schoolData):
  stmt = """
INSERT INTO ki_schools (`official_school_id`, `name`, `address`, `region_id`, `division_id`, `city_id`, `added_date`, `added_by`)
VALUES (%d, "%s", "%s", %d, %d, %d, %s, %d);"""
  # print u''.join(schoolData["name"]).encode('utf-8').strip()
  # print(u"{}".format(schoolData["name"]))
  # print schoolData["name"].encode('utf-8')

  values = (
    int(schoolData["official_school_id"]),
    schoolData["name"].replace("\"", "\\\"").encode('utf-8'),
    schoolData["address"].replace("\"", "\\\"").encode('utf-8'),
    int(schoolData["region_id"]),
    int(schoolData["division_id"]),
    int(schoolData["city_id"]),
    "NOW()",
    26
  )

  print(stmt % values)

# count = 0
with open(TODB_PATH, 'r') as fileInput:
  schoolList = json.load(fileInput)
  maxIdx = BATCH * 10000 if BATCH * 10000 < len(schoolList) else len(schoolList)
  minIdx = 0 if BATCH == 1 else (BATCH - 1) * 10000
  # print maxIdx, minIdx

  # break
  for schoolData in schoolList[minIdx:maxIdx]:
    addToInsertData(schoolData)
    # count += 1
    # if count == 50:
    #   break
