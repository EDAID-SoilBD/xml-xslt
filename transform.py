# -*- coding: utf-8 -*-

import lxml.etree as ET

dom = ET.parse("soildb-data.xml")

xslt = ET.parse("soil.xslt")

transform = ET.XSLT(xslt)

newdom = transform(dom)

print(newdom)

f = open("soil.html", "w")

f.write(str(newdom))

f.close()
