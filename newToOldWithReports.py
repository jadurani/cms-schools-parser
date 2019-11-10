#!/usr/bin/env python2

import json
import sys


# OUTPUT viea stout redirection
# ./toDB.py 1 > toDB_output/1_new_schools.sql
# ./toDB.py 2 > toDB_output/2_new_schools.sql

TODB_PATH = "manuallyMatch_output/toDB.json"



count = 0

print("CREATE TEMPORARY TABLE OLD_SCHOOLS_WITH_REPORTS AS ")

with open(TODB_PATH, 'r') as fileInput:
  schoolList = json.load(fileInput)
  for schoolData in schoolList:
    if "school_id" in schoolData.keys():
      print("  SELECT {} as school_id, {} as official_school_id".format(schoolData["school_id"], schoolData["official_school_id"]))
      count += 1
      if count != 307: # we know beforehand how many schools we have
        print("  union all")
    # if count == 4:
    #   break

print(";")

print ("SELECT * FROM OLD_SCHOOLS_WITH_REPORTS;")

updateQuery = """
CREATE TEMPORARY TABLE NEW_ID_SCHOOLS_WITH_REPORTS AS
  SELECT
    ks.school_id as new_school_id,
    oswr.school_id as old_school_id
  FROM ki_schools ks, OLD_SCHOOLS_WITH_REPORTS oswr
  WHERE ks.official_school_id=oswr.official_school_id
;

SELECT * FROM NEW_ID_SCHOOLS_WITH_REPORTS;

CREATE TEMPORARY TABLE REPORTS_UNCHANGED AS
  SELECT
    kr.id as report_id,
    kr.school_id as report_school_id,
    niswr.new_school_id as new_school_id,
    niswr.old_school_id as old_school_id
  FROM
    ki_reports kr,
    NEW_ID_SCHOOLS_WITH_REPORTS niswr
  WHERE
    kr.school_id=niswr.old_school_id
;

SELECT * FROM REPORTS_UNCHANGED;

UPDATE ki_reports kr, NEW_ID_SCHOOLS_WITH_REPORTS niswr
SET kr.school_id=niswr.new_school_id
WHERE kr.school_id=niswr.old_school_id;

CREATE TEMPORARY TABLE REPORTS_CHANGED AS
  SELECT
    kr.id as report_id,
    kr.school_id as report_school_id,
    niswr.new_school_id as new_school_id,
    niswr.old_school_id as old_school_id
  FROM
    ki_reports kr,
    NEW_ID_SCHOOLS_WITH_REPORTS niswr
  WHERE
    kr.school_id=niswr.new_school_id
;

SELECT * FROM REPORTS_CHANGED;
"""

print(updateQuery)