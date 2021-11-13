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

for index, row in df.iterrows():
    data_entry = SubElement(soil_data, "data-entry")

    code = SubElement(data_entry, "code")
    code.text = str(row["CODE"])

    photographs = SubElement(data_entry, "photographs")
    photographs.text = str(row["PHOTOGRAPHS"])

    description = SubElement(data_entry, "description")
    description.text = str(row["DESCRIPTION"])

    coord_x = SubElement(data_entry, "coordinates-x")
    coord_x.text = str(row["COORDINATES X"])

    coord_y = SubElement(data_entry, "coordinates-y")
    coord_y.text = str(row["COORDINATES Y"])

    altitutde = SubElement(data_entry, "altitude")
    altitutde.text = str(row["ALTITUDE"])

    incline = SubElement(data_entry, "incline")
    incline.text = str(row["INCLINE"])

    graves = SubElement(data_entry, "graves")
    graves.text = str(row["GRAVES"])

    vt_sand = SubElement(data_entry, "very-thick-sand")
    vt_sand.text = str(row["VERY THICK SAND"])

    t_sand = SubElement(data_entry, "thick-sand")
    t_sand.text = str(row["THICK SAND"])

    m_sand = SubElement(data_entry, "medium-sand")
    m_sand.text = str(row["MEDIUM SAND"])

    f_sand = SubElement(data_entry, "fine-sand")
    f_sand.text = str(row["FINE SAND"])

    vf_sand = SubElement(data_entry, "very-fine-sand")
    vf_sand.text = str(row["VERY FINE SAND"])

    total_sand = SubElement(data_entry, "total-sand")
    total_sand.text = str(row["TOTAL SAND"])

    t_limes = SubElement(data_entry, "thick-limes")
    t_limes.text = str(row["THICK LIMES"])

    f_limes = SubElement(data_entry, "fine-limes")
    f_limes.text = str(row["FINE LIMES"])

    total_limes = SubElement(data_entry, "total-limes")
    total_limes.text = str(row["TOTAL LIMES"])

    clay = SubElement(data_entry, "clay")
    clay.text = str(row["CLAY"])

    k_factor = SubElement(data_entry, "k-factor")
    k_factor.text = str(row["K FACTOR"])

    app_density = SubElement(data_entry, "apparent-density")
    app_density.text = str(row["APPARENT DENSITY"])

    agg_stability = SubElement(data_entry, "aggregate-stability")
    agg_stability.text = str(row["AGGREGATE STABILITY"])

    permeability = SubElement(data_entry, "permeability")
    permeability.text = str(row["PERMEABILITY"])

    field_capacity = SubElement(data_entry, "field-capacity")
    field_capacity.text = str(row["FIELD CAPACITY"])

    perm_wil_point = SubElement(data_entry, "permanent-wilting-point")
    perm_wil_point.text = str(row["PERMANENT WILTING POINT"])

    hydrophobicity = SubElement(data_entry, "hydrophobicity")
    hydrophobicity.text = str(row["HYDROPHOBICITY"])

    org_carb = SubElement(data_entry, "organic-carbon")
    org_carb.text = str(row["ORGANIC CARBON"])

    c_factor = SubElement(data_entry, "c-factor")
    c_factor.text = str(row["C FACTOR"])

    electric_cond = SubElement(data_entry, "electric-conductivity")
    electric_cond.text = str(row["ELECTRIC CONDUCTIVITY"])

    spectral_response = SubElement(data_entry, "spectral-response")
    spectral_response.text = str(row["SPECTRAL RESPONSE "])

print(tostring(soil_data))

f = open("soildb-data.xml", "w")

f.write(str(tostring(soil_data, encoding="unicode")))

f.close()
