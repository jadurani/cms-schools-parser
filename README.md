
placeParser.py
INPUT:
ki_cities
[
  {
    "city_id": "110",
    "name":"AGNO",
    "status":"Y",
    "division_id":"127",
    "added_by":"5",
    "added_date":"2017-12-07 17:06:19"
  }
]

ki_divisions
[
  {
    "division_id":"125",
    "name":"Pangasinan II, Binalonan",
    "status":"Y",
    "region_id":"192",
    "added_by":"5",
    "added_date":"2017-12-07 12:12:03"
  }
]

ki_region
[
  {
    "region_id":"192",
    "name":"Region I",
    "status":"Y",
    "position":"6",
    "added_date":"2017-12-07 12:11:17",
    "added_by":"5"
  }
]

OUTPUT:
{
  cityName_divisionName_regionName: {
    cityId: #,
    regionId: #,
    divisionId: #
  },
}

STEPS:

1. City first
Output:
{
  "city_divId": {
    cityId: #,
    divId: #
  }
}

2. Division
Output:
{
  "city_div_regId": {
    cityId: #,
    divId: #,
    regId: #
  }
}

3. Region
{
  "city_div_reg": {
    cityId: #,
    divId: #,
    regId: #
  }
}

schoolPlaceDetails.py
INPUT:

1. New schools
[
  {
    "region":"Region IV-B",
    "division":"Palawan",
    "district":"Aborlan Central",
    "school_id":"430505",
    "school_name":"Aborlan Bible Baptist Christian School",
    "address":"National Highway, Mabini, Aborlan, Palawan",
    "city":"ABORLAN",
    "extracolumn":"rawrextra\r"
  }
]

2. places id
{
  "city_div_reg": {
    cityId: #,
    divId: #,
    regId: #
  }
}

STEPS:

1. Go through the whole list of new schools combining each school's city, division, and region to lower case concatenated by `_` and looking for its match on the places id dict/obj
2. include cityId, divId, and regId to school obj
3. Remove `extracolumn`; Replace `school_id` with `official_school_id`

OUTPUT
[
  {
    "region":
    "region_id": #
    "division":
    "division_id"
    "district":
    "city_id"
    "official_school_id":
    "school_name":
    "address":
    "city":
  }
]


matchOldToNew
-- we only need to bother finding the duplicates for schools with existing reports 
INPUT: 

1. List of schools with existing reports
2. Compare list of schools against new list of schools....


STEPS:
1. 