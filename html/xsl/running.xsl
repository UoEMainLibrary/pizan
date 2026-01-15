<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" indent="no"/>
<xsl:key name="N" match="hi[@rend='run']" use="'1'"/>
<xsl:template match="/">
<head>
<title>Running Titles in Table Cells</title>
<meta http-equiv="content-type" content="text/html;charset=iso-8859-1" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<link rel="stylesheet" type="text/css" href="classes.css">
</link>
</head>
<body>
<center><b>Running Titles</b></center><br/>
<br/>
<table border="0" cellpadding="6">
<xsl:for-each select="key('N',1)">
<!-- <xsl:sort select="."/> ?-->
<tr>
<td bgcolor="#D3D3D3">
<xsl:value-of select="preceding::lb[1]/@n"/>  <xsl:value-of select="text/div1/div2/lb[last()]/@n"/>
</td>
<td bgcolor="#eae2c8">
<span class="rubric">
<xsl:value-of select="./fw[@type='header1']"/>
</span></td>
<td bgcolor="#eae2c8">
<span class="rubric">
<xsl:value-of select="./fw[@type='header2']"/>
</span></td>
<td bgcolor="#eae2c8">
<span class="rubric">
<xsl:value-of select="./fw[@type='header3']"/>
</span></td>
<td bgcolor="#eae2c8">
<span class="rubric">
<xsl:value-of select="./fw[@type='header4']"/>
</span></td>
<td bgcolor="#eae2c8">
<span class="rubric">
<xsl:value-of select="./fw[@type='header5']"/>
</span></td>
<td bgcolor="#eae2c8">
<span class="rubric">
<xsl:value-of select="./fw[@type='header6']"/>
</span></td>
</tr>
</xsl:for-each>
</table>

</body>
</xsl:template>
</xsl:stylesheet>

