<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" encoding="UTF-8" indent="no"/>
<xsl:template match="/">
<html>
<head>
<link rel="stylesheet" type="text/css" href="classes.css"/>

</head>
<body>
<pre>
<xsl:apply-templates select="//text"/>
</pre>
</body>
</html>
</xsl:template>
<!-- 23 Aug 2008 Charlie trimming -->
<!-- 25 July 2008 Jim and Charlie agreeing what to transform to show in the browser for a diplomatic edition -->
<!-- The TRANSLATE below attempts to convert all accented characters to non-accented ones  -->
 <!-- 3 November 2008 Jim changed "abbr">|<xsl:value-of select="@expan"/> to "abbr">|<xsl:value-of select="@type"/> -->

<xsl:variable name="empty"></xsl:variable>
<xsl:variable name="punct">'.,":;!?-</xsl:variable>
<xsl:variable name="ninepunct" select="concat($empty,$empty,$empty,$empty,$empty,$empty,$empty,$empty,$empty)"/>

<xsl:variable name="withtemp">ÀäàÇçÉëèéÏïöùūŸÿ</xsl:variable>
<xsl:variable name="sanstemp">AaaCcEeeeIiouuYy</xsl:variable>

<xsl:variable name="with" select="concat($withtemp,$punct)"/>
<xsl:variable name="sans" select="concat($sanstemp,$ninepunct)"/>
    
<xsl:template match="text()">
<xsl:value-of select="translate(., $with, $sans)" />
</xsl:template>

<xsl:template match="abbr">
<span class="abbr"><xsl:value-of select="@type"/><xsl:apply-templates/></span> 
</xsl:template>

<xsl:template match="cb">
</xsl:template>

<xsl:template match="l">
</xsl:template>

<xsl:template match="lg">
</xsl:template>

<xsl:template match="brace">
<span class="braces" name="ordinal">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="note">
</xsl:template>

<xsl:template match="pb">
</xsl:template>

<xsl:template match="lb">
<xsl:apply-templates/>
<span class="n"><xsl:value-of select="@n"  /></span>
</xsl:template>

<xsl:template match="num[@rend='ordinal']">
<span class="supra">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="supplied">
</xsl:template>

<xsl:template match="c">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="name">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="g">
<xsl:apply-templates/> 
</xsl:template>

<xsl:template match="seg">
</xsl:template>

<xsl:template match="del[@rend='overstrike']">
<span class="overstrike">
<xsl:apply-templates/></span>
</xsl:template> 

<xsl:template match="del[@type='expunctuate']">
<span class="expunctuate">
<xsl:apply-templates/></span>
</xsl:template> 


<xsl:template match="emph[@rend='headline']">
<span class="headline"><center>
<xsl:apply-templates/></center></span></xsl:template>

<xsl:template match="emph[@rend='italic']">
<span class="italic"><xsl:apply-templates/></span></xsl:template>

<xsl:template match="emph[@rend='sup']">
<sup><xsl:apply-templates/></sup></xsl:template>

<xsl:template match="hi[@rend='red']">
<span class="rubric">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="hi[@rend='block']">
<span class="block">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="hi[@rend='purple']">
<span class="purple">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="hi[@rend='centred']">
<span class="centred">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="hi[@rend='cap2']">
<span class="cap2">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="hi[@rend='cap3']">
<span class="cap3">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="hi[@rend='cap4']">
<span class="cap4">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="hi[@rend='cap5']">
<span class="cap5">
<xsl:apply-templates/></span>
</xsl:template>


<xsl:template match="title">
<span class="title"><xsl:apply-templates/></span>
</xsl:template> 

<xsl:template match="msDesc">
</xsl:template> 

<xsl:template match="p">
<span class="para"><br/><xsl:apply-templates/><br/></span>
</xsl:template> 

<xsl:template match="orig">
<xsl:apply-templates/></xsl:template> 

<xsl:template match="reg">
</xsl:template> 

<xsl:template match="sic">
<xsl:apply-templates/> (<i>sic</i>) </xsl:template> 

</xsl:stylesheet>
