<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
 <xsl:output method="html" indent="no"/>
 <xsl:key name="N" match="rhyme" use="'1'"/>
<xsl:template match="/">
    Rhyme Words in Harley 4431
 in Alphabetic Order
    <table border="1mm" bordercolor="#008080" bgcolor="#7FFFD4">
        <tr>
            <td><center> Rhyme Word </center></td>
            <td><center> Line Number </center></td>
        </tr>
<xsl:for-each select="key('N',1)">
<xsl:sort select="."/>
<tr>
 <td bgcolor="#ffffff">
<xsl:value-of select="."/>
</td>
<td>
<xsl:value-of select="preceding-sibling::lb[1]/@n"/>
</td>
</tr>
</xsl:for-each>
</table>
</xsl:template>
 </xsl:stylesheet>
