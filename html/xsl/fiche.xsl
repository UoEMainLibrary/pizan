<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" encoding="UTF-8" indent="no"/>
<xsl:template match="/">
<html>
<head>
<title>XML transformed to Student Edition in HTML</title>
<link rel="stylesheet" type="text/css" href="classes_18June2009.css">
</link>
</head>
<body>
<xsl:apply-templates select="//text"/>
</body>
</html>
</xsl:template>
<!-- 2nd March 2009 Charlie Mansfield Middle French Transformation for Student Edition of Harley 4431 -->

<xsl:template match="ref">
<a><xsl:attribute name="href">javascript:popfiche('<xsl:value-of select = "@type"/>')</xsl:attribute><img src="fichier.gif" border="0" alt=""/>
<xsl:apply-templates/></a></xsl:template>

<xsl:template match="abbr">
<span class="abbr"><xsl:value-of select="@type"/><xsl:apply-templates/></span> 
</xsl:template>

<xsl:template match="l">
<span class="l"><xsl:value-of select="@n"/><xsl:apply-templates/></span> 
</xsl:template>

<xsl:template match="lg">
<xsl:apply-templates/>
<span class="lv">[<xsl:value-of select="@type"/>] </span> 
</xsl:template>

<xsl:template match="brace">
<span class="braces" name="ordinal">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="note">
<a><xsl:attribute name="href">javascript:nota("<xsl:value-of select = "translate(., '&#xA;', '')" />")</xsl:attribute><span class="note">
<img src="fleur.png" alt=""/>
<xsl:apply-templates/></span></a></xsl:template>

<xsl:template match="lb">
<xsl:apply-templates/>
<span class="lb" name="d"><xsl:value-of select="@n"/></span> 
</xsl:template>

<xsl:template match="num[@rend='ordinal']">
<span class="supra">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="supplied">
<span class="savant"><xsl:apply-templates/></span> 
</xsl:template>

<xsl:template match="c">
<span class="c"><xsl:value-of select = "translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZaàbcdeéfghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyzAÀBCDEÉFGHIJKLMNOPQRSTUVWXYZ')" />
</span> 
</xsl:template>


<xsl:template match="name">
<a><xsl:attribute name="href">javascript:popname('<xsl:value-of select="@ref"/>')
</xsl:attribute><span class="name" name="noms">
<xsl:apply-templates/></span></a>
</xsl:template>

<xsl:template match="g">
<xsl:variable name="sans" select="text()" />
<xsl:variable name="expansion" select="abbr/@expan" />
<xsl:variable name="apres" select="text()[2]" />
<xsl:variable name="thirdbit" select="rhyme" />
<xsl:variable name="whole" select="concat($sans,$expansion,$apres,$thirdbit)"/>
<a><xsl:attribute name="href">javascript:gloss("<xsl:value-of select = "translate($whole, '&#xA;', '')" />","<xsl:value-of select="@en"/>","<xsl:value-of select="@fr"/>")</xsl:attribute><span class="gloss"><xsl:apply-templates/></span></a>
</xsl:template>

<xsl:template match="seg">
<span class="seg"><xsl:apply-templates/></span> 
</xsl:template>

<!-- typographie -->
<xsl:template match="del[@rend='overstrike']">
<span class="overstrike">
<xsl:apply-templates/></span>
</xsl:template> 

<xsl:template match="emph[@rend='headline']">
<span class="headline"><b>
<xsl:apply-templates/></b></span></xsl:template>

<xsl:template match="div9">
<div class="frontmatter">
<xsl:apply-templates/></div></xsl:template>

<xsl:template match="div4">
<br/><xsl:apply-templates/><br/></xsl:template>

<xsl:template match="emph[@rend='sup']">
<sup><xsl:apply-templates/></sup></xsl:template>

<xsl:template match="emph[@rend='italic']">
<span class="italic">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="hi[@rend='red']">
<span class="rubric">
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

<xsl:variable name="empty"></xsl:variable>
<xsl:variable name="punct">/\</xsl:variable>
<xsl:variable name="ninepunct" select="concat($empty,$empty)"/>

<xsl:variable name="with" select="($punct)"/>
<xsl:variable name="sans" select="($ninepunct)"/>
    
<xsl:template match="text()">
<xsl:value-of select="translate(., $with, $sans)" />
</xsl:template>

</xsl:stylesheet>
