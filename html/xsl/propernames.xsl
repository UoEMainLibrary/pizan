<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
 <xsl:output method="html" indent="no"/>
<xsl:key name="M" match="name" use="'1'"/>
<xsl:key name="N" match="name/attribute::ref" use="'1'"/>
<xsl:template match="/">
    Proper Names in Harley 4431
    <table border="1mm" bordercolor="#008080" bgcolor="#7FFFD4">
        <tr>
            <td><center>Disambiguation for Wiki  </center></td>
            <td><center>Contextual Rendering</center></td>
            <td><center>Line Number</center></td>
<td><center>Link to Wiki</center></td>
        </tr>

<xsl:for-each select="key('M',1)">
<xsl:sort select="."/>
<tr>

 <td bgcolor="#ffffff">
<xsl:value-of select="."/>
</td>

<td bgcolor="#FFE4C4">
<xsl:for-each select="key('N',1)">
</xsl:for-each>
</td>

<td>
<xsl:value-of select="preceding::lb[1]/@n"/>
</td>

<td>
<a><xsl:attribute name="href">https://www.wiki.ed.ac.uk/display/4431wiki/<xsl:value-of select="@ref"/>
</xsl:attribute>
<xsl:apply-templates/></a>
</td>
</tr>
</xsl:for-each>
</table>
</xsl:template>
 </xsl:stylesheet>
