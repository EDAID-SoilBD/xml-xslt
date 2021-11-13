# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:17:01 2021
Updated on Sat Nov 13 15:52:01 2021

@author: Ismael Navas and EDAID-SoilDB
"""

import pymongo
from pymongo import MongoClient
import pandas as pd

from xml.etree.ElementTree import Element, SubElement, Comment, tostring


soil_data = Element("soil-data")

comment = Comment("Data geranted from MongoDB")
soil_data.append(comment)

client = pymongo.MongoClient(
    "mongodb+srv://olegbrz:ZbPObMewgvMS1iqu@edaid-soil.hflhi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db = client.SoilDB
resultado = db.Data.find()

df = pd.DataFrame(list(resultado))

"""'_id': ObjectId('616752324bf720e8a8cd38e4'),
'CODE': 'G0201',
'PHOTOGRAPHS': 'See JPG: G0201-SSC y G0201-U',
'DESCRIPTION': 'Sandy soil',
'COORDINATES X': 323614,
'COORDINATES Y': 4074856,
'ALTITUDE': 478, 
INCLINE': 31,
'GRAVES': 280,
'VERY THICK SAND': 3,
'THICK SAND': 6,
'MEDIUM SAND': 29,
'FINE SAND': 48,
'VERY FINE SAND': 22,
'TOTAL SAND': 108,
'THICK LIMES': 29,
'FINE LIMES': 21,
'TOTAL LIMES': 50,
'CLAY': 2,
'K FACTOR': 0.74,
'APPARENT DENSITY': 0.6,
'AGGREGATE STABILITY': 45,
'PERMEABILITY': 150,
'FIELD CAPACITY': 25,
'PERMANENT WILTING POINT': 13,
'HYDROPHOBICITY': 1,
'ORGANIC CARBON': '5.03',
'C FACTOR': 0.52,
'ELECTRIC CONDUCTIVITY': '0.29',
'SPECTRAL RESPONSE ': ' See document: 0100550.asd'}"""

for index, row in df.iterrows():
    data_entry = SubElement(soil_data, "data-entry")

    code = SubElement(data_entry, "code")
    code.text = row["CODE"]

    photographs = SubElement(data_entry, "photographs")
    photographs.text = row["PHOTOGRAPHS"]

    description = SubElement(data_entry, "description")
    description.text = row["DESCRIPTION"]

    coord_x = SubElement(data_entry, "coordinates-x")
    coord_x.text = row["COORDINATES X"]

    coord_y = SubElement(data_entry, "coordinates-y")
    coord_y.text = row["COORDINATES Y"]

    altitutde = SubElement(data_entry, "altitude")
    altitutde.text = row["ALTITUDE"]

    incline = SubElement(data_entry, "incline")
    incline.text = row["INCLINE"]

    graves = SubElement(data_entry, "graves")
    graves.text = row["GRAVES"]

    vt_sand = SubElement(data_entry, "very-thick-sand")
    vt_sand.text = row["VERY THICK SAND"]

    t_sand = SubElement(data_entry, "thick-sand")
    t_sand.text = row["THICK SAND"]

    m_sand = SubElement(data_entry, "medium-sand")
    m_sand.text = row["MEDIUM SAND"]

    f_sand = SubElement(data_entry, "fine-sand")
    f_sand.text = row["FINE SAND"]

    vf_sand = SubElement(data_entry, "very-fine-sand")
    vf_sand.text = row["VERY FINE SAND"]

    total_sand = SubElement(data_entry, "total-sand")
    total_sand.text = row["TOTAL SAND"]

    t_limes = SubElement(data_entry, "thick-limes")
    t_limes.text = row["THICK LIMES"]

    f_limes = SubElement(data_entry, "fine-limes")
    f_limes.text = row["FINE LIMES"]

    total_limes = SubElement(data_entry, "total-limes")
    total_limes.text = row["TOTAL LIMES"]

    clay = SubElement(data_entry, "clay")
    clay.text = row["CLAY"]

    k_factor = SubElement(data_entry, "k-factor")
    k_factor.text = row["K FACTOR"]

    app_density = SubElement(data_entry, "apparent-density")
    app_density.text = row["APPARENT DENSITY"]

    agg_stability = SubElement(data_entry, "aggregate-stability")
    agg_stability.text = row["AGGREGATE STABILITY"]

    permeability = SubElement(data_entry, "permeability")
    permeability.text = row["PERMEABILITY"]

    field_capacity = SubElement(data_entry, "field-capacity")
    field_capacity.text = row["FIELD CAPACITY"]

    perm_wil_point = SubElement(data_entry, "permanent-wilting-point")
    perm_wil_point.text = row["PERMANENT WILTING POINT"]

    hydrophobicity = SubElement(data_entry, "hydrophobicity")
    hydrophobicity.text = row["HYDROPHOBICITY"]

    org_carb = SubElement(data_entry, "organic-carbon")
    org_carb.text = row["ORGANIC CARBON"]

    c_factor = SubElement(data_entry, "c-factor")
    c_factor.text = row["C FACTOR"]

    electric_cond = SubElement(data_entry, "electric-conductivity")
    electric_cond.text = row["ELECTRIC CONDUCTIVITY"]

    spectral_response = SubElement(data_entry, "spectral-response")
    spectral_response.text = row["SPECTRAL RESPONSE "]

print(tostring(soil_data))

f = open("restaureantesdesdemongo.xml", "w")

f.write(str(tostring(soil_data, encoding="utf-8")))

f.close()
