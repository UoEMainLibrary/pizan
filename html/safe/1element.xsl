<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" indent="no"/>
<xsl:key name="N" match="g" use="'1'"/>
<xsl:template match="/">
Middle French Dictionary - Charlie MANSFIELD Jan 2008
<table border="1mm" bordercolor="#008080" bgcolor="#7FFFD4">
<tr>
<td><center> Moyen Français </center></td>
<td><center>ENGLISH</center></td>
<td><center>FRENCH</center></td>
</tr>
<xsl:for-each select="key('N',1)">
<xsl:sort select="."/>
<tr>
<td bgcolor="#ffffff">
<xsl:value-of select="."/>
</td>
<td bgcolor="#FFE4C4"><xsl:value-of select="@en"/></td>
<td bgcolor="#FF7F50"><xsl:value-of select="@fr"/></td>
<td>
<xsl:value-of select="preceding-sibling::lb[1]/@n"/>
</td>
</tr>
</xsl:for-each>
</table>
</xsl:template>
</xsl:stylesheet>
