# -*- coding: utf-8 -*-

import lxml.etree as ET

dom = ET.parse("soil.xml")

xslt = ET.parse("soil.xslt")

transform = ET.XSLT(xslt)

newdom = transform(dom)

print(newdom)

f = open("patients.html", "w")

f.write(str(newdom))

f.close()
