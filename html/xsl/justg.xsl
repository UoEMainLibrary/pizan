<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" encoding="UTF-8" indent="no"/>
<xsl:template match="/">
<html>
<head>
<link rel="stylesheet" type="text/css" href="classes.css"/>

</head>
<body>
<table>
<tr>
<xsl:template match="lb">
<xsl:apply-templates/><td>
<xsl:value-of select="@n"/></td>
</xsl:template>

<xsl:template match="g"><td>
<xsl:apply-templates/></td>
</xsl:template>
</tr>
</table>
</body>
</html>
</xsl:template>
<!-- 23 Aug 2008 Charlie trimming -->
<!-- 25 July 2008 Jim and Charlie agreeing what to transform to show in the browser for a diplomatic edition -->
<!-- The TRANSLATE below attempts to convert all accented characters to non-accented ones  -->

<xsl:variable name="empty"></xsl:variable>
<xsl:variable name="punct">'.,":;!?-</xsl:variable>
<xsl:variable name="ninepunct" select="concat($empty,$empty,$empty,$empty,$empty,$empty,$empty,$empty,$empty)"/>

<xsl:variable name="withtemp">ÀäàÇçÉëèéÏïöùūûŸÿ</xsl:variable>
<xsl:variable name="sanstemp">AaaCcEeeeIiouuuYy</xsl:variable>


<xsl:variable name="with" select="concat($withtemp,$punct)"/>
<xsl:variable name="sans" select="concat($sanstemp,$ninepunct)"/>
    
<xsl:template match="text()">
<xsl:value-of select="translate(., $with, $sans)" />
</xsl:template>

<xsl:template match="abbr">|<xsl:value-of select="@expan"/>|<xsl:apply-templates/>
</xsl:template>

<xsl:template match="cb">
</xsl:template>

<xsl:template match="l">
</xsl:template>

<xsl:template match="brace">
</xsl:template>

<xsl:template match="note">
</xsl:template>

<xsl:template match="pb">
</xsl:template>


<xsl:template match="num[@rend='ordinal']">
</xsl:template>

<xsl:template match="supplied">
</xsl:template>

<xsl:template match="c">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="name">
</xsl:template>


<xsl:template match="seg">
</xsl:template>

<xsl:template match="del[@rend='overstrike']">
</xsl:template> 

<xsl:template match="del[@type='expunctuate']">
</xsl:template> 

<xsl:template match="emph[@rend='headline']">
</xsl:template>

<xsl:template match="emph[@rend='italic']">
</xsl:template>

<xsl:template match="emph[@rend='sup']">
</xsl:template>

<xsl:template match="hi[@rend='red']">
</xsl:template>

<xsl:template match="hi[@rend='block']">
</xsl:template>

<xsl:template match="hi[@rend='purple']">
</xsl:template>

<xsl:template match="hi[@rend='centred']">
</xsl:template>

<xsl:template match="hi[@rend='cap2']">
</xsl:template>

<xsl:template match="hi[@rend='cap3']">
</xsl:template>

<xsl:template match="hi[@rend='cap4']">
</xsl:template>

<xsl:template match="hi[@rend='cap5']">
</xsl:template>

<xsl:template match="title">
</xsl:template> 

<xsl:template match="msDesc">
</xsl:template> 

<xsl:template match="p">
</xsl:template> 

<xsl:template match="orig">
</xsl:template> 

<xsl:template match="reg">
</xsl:template> 

<xsl:template match="sic">
</xsl:template> 

</xsl:stylesheet>
