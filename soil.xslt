<?xml version="1.0"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/soil-data">
    <html>
      <head>
        <title>SoilDB XSLT</title>
      </head>
      <body>
        <h1>SoilDB</h1>
        <table style="text-align:center;" border="1">
          <tr bgcolor="#b1ab99">
            <th>CODE</th>
            <th>PHOTOGRAPHS</th>
            <th>DESCRIPTION</th>
            <th>COORDINATES X</th>
            <th>COORDINATES Y</th>
            <th>ALTITUDE</th>
            <th>INCLINE</th>
            <th>GRAVES</th>
            <th>VERY THICK SAND</th>
            <th>THICK SAND</th>
            <th>MEDIUM SAND</th>
            <th>FINE SAND</th>
            <th>VERY FINE SAND</th>
            <th>TOTAL SAND</th>
            <th>THICK LIMES</th>
            <th>FINE LIMES</th>
            <th>TOTAL LIMES</th>
            <th>CLAY</th>
            <th>K FACTOR</th>
            <th>APPARENT DENSITY</th>
            <th>AGGREGATE STABILITY</th>
            <th>PERMEABILITY</th>
            <th>FIELD CAPACITY</th>
            <th>PERMANENT WILTING POINT</th>
            <th>HYDROPHOBICITY</th>
            <th>ORGANIC CARBON</th>
            <th>C FACTOR</th>
            <th>ELECTRIC CONDUCTIVITY</th>
            <th>SPECTRAL RESPONSE</th>
          </tr>
          <xsl:for-each select="data-entry">
            <tr bgcolor="#fbfaf0">
              <td>
                <xsl:value-of select="code" />
              </td>
              <td>
                <xsl:value-of select="photographs" />
              </td>
              <td>
                <xsl:value-of select="description" />
              </td>
              <td>
                <xsl:value-of select="coordinates-x" />
              </td>
              <td>
                <xsl:value-of select="coordinates-y" />
              </td>
              <td>
                <xsl:value-of select="altitude" />
              </td>
              <td>
                <xsl:value-of select="incline" />
              </td>
              <td>
                <xsl:value-of select="graves" />
              </td>
              <td>
                <xsl:value-of select="very-thick-sand" />
              </td>
              <td>
                <xsl:value-of select="thick-sand" />
              </td>
              <td>
                <xsl:value-of select="medium-sand" />
              </td>
              <td>
                <xsl:value-of select="fine-sand" />
              </td>
              <td>
                <xsl:value-of select="very-fine-sand" />
              </td>
              <td>
                <xsl:value-of select="total-sand" />
              </td>
              <td>
                <xsl:value-of select="thick-limes" />
              </td>
              <td>
                <xsl:value-of select="fine-limes" />
              </td>
              <td>
                <xsl:value-of select="total-limes" />
              </td>
              <td>
                <xsl:value-of select="clay" />
              </td>
              <td>
                <xsl:value-of select="k-factor" />
              </td>
              <td>
                <xsl:value-of select="apparent-density" />
              </td>
              <td>
                <xsl:value-of select="aggregate-stability" />
              </td>
              <td>
                <xsl:value-of select="permeability" />
              </td>
              <td>
                <xsl:value-of select="field-capacity" />
              </td>
              <td>
                <xsl:value-of select="permanent-wilting-point" />
              </td>
              <td>
                <xsl:value-of select="hydrophobicity" />
              </td>
              <td>
                <xsl:value-of select="organic-carbon" />
              </td>
              <td>
                <xsl:value-of select="c-factor" />
              </td>
              <td>
                <xsl:value-of select="electric-conductivity" />
              </td>
              <td>
                <xsl:value-of select="spectral-response" />
              </td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>