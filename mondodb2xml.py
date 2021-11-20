# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:17:01 2021
Updated on Sat Nov 13 15:52:01 2021

@author: EDAID-SoilDB
"""

import pymongo
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

client = pymongo.MongoClient(
    "mongodb+srv://olegbrz:ZbPObMewgvMS1iqu@edaid-soil.hflhi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db = client.SoilDB
result = list(db.Data.find())

soil_data = Element("soil-data")
comment = Comment("Data geranted from MongoDB")

for elem in result:
    data_entry = SubElement(soil_data, "data-entry")
    for attr in list(result[0].keys())[1:]:
        col = SubElement(data_entry, attr.lower().strip().replace(" ", "-"))
        col.text = str(elem[attr])


with open("soildb-data.xml", "w") as f:
    f.write(str(tostring(soil_data, encoding="unicode")))
