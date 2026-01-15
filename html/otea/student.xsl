<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" encoding="UTF-8"/>
<xsl:template match="/">
<html>
<head>
<title>XML transformed to Student Edition in HTML</title>
<link rel="stylesheet" type="text/css" href="classes.css">
</link>
<script type="text/javascript" src="javascript.js"></script>
</head>
<body background="quad.jpg">
<div id="loups" class="loupage" onmousedown="dragStart(event)">
</div>
<div id="gloss" class="glossing" onmousedown="dragStart(event)">
</div>
<div id="notes" class="noted" onmousedown="dragStart(event)">
</div>
<pre>
<xsl:apply-templates select="//text"/>
</pre>
</body>
</html>
</xsl:template>
<!-- 17 June 2009 Charlie Mansfield Middle French Transformation for Student Edition of Harley 4431 -->

<xsl:template match="abbr">
<span class="abbr"><xsl:value-of select="@type"/><xsl:apply-templates/></span> 
</xsl:template>

<xsl:template match="brace">
<span class="braces" name="ordinal">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="c">
<span class="c"><xsl:value-of select = "translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZaàbcdeéèfghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyzAÀBCDEÉÈFGHIJKLMNOPQRSTUVWXYZ')" />
</span> 
</xsl:template>

<xsl:template match="corr">
<span class="corr">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="del">
</xsl:template>

<xsl:template match="del[@rend='expunctuate']">
<span class="expunctuate">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="div4">
<br/><xsl:apply-templates/><br/></xsl:template>

<!-- Include miniatures from sub-directory on Pizan server, there are notes from MTG in WORD there too -->
<xsl:template match="figure">
<xsl:variable name="path">http://www.pizan.lib.ed.ac.uk/miniatures/</xsl:variable>
<xsl:variable name="miniature" select="@ref" />
<xsl:variable name="jpeg">.jpg</xsl:variable>
<xsl:variable name="doc">.doc</xsl:variable>
<xsl:variable name="PictureID" select="concat($path,$miniature,$jpeg)"/>
<xsl:variable name="document" select="concat($path,$miniature,$doc)"/>
<a><xsl:attribute name="href">javascript:popmin("<xsl:value-of select = "translate($document, ' ', '')" />")</xsl:attribute><img src='{$PictureID}' border="0" width="325" alt=""/>
<xsl:apply-templates/></a></xsl:template>

<xsl:template match="frontmatter">
</xsl:template>

<!--?This command switches off the catchwords -->
<xsl:template match="fw[@type='catch']">
</xsl:template>

<!--?This command switches off the signatures -->
<xsl:template match="fw[@type='sig']">
</xsl:template>

<xsl:template match="g">
<xsl:variable name="sans" select="text()" />
<xsl:variable name="expansion" select="abbr/@expan" />
<xsl:variable name="apres" select="text()[2]" />
<xsl:variable name="thirdbit" select="rhyme" />
<xsl:variable name="whole" select="concat($sans,$expansion,$apres,$thirdbit)"/>
<a><xsl:attribute name="href">javascript:gloss("<xsl:value-of select = "translate($whole, '&#xA;', '')" />","<xsl:value-of select="@en"/>","<xsl:value-of select="@fr"/>")</xsl:attribute><span class="gloss"><xsl:apply-templates/></span></a>
</xsl:template>

<xsl:template match="group">
<span class="group"><xsl:value-of select="@n"/><xsl:apply-templates/></span> 
</xsl:template>

<!--?This command switches off the running titles -->
<xsl:template match="hi[@rend='run']">
</xsl:template>

<xsl:template match="l">
<span class="l"><xsl:value-of select="@n"/><xsl:apply-templates/></span> 
</xsl:template>

<xsl:template match="lb">
<xsl:apply-templates/>
<span class="lb" name="d"><xsl:value-of select="@n"/></span> 
</xsl:template>

<xsl:template match="lg">
<xsl:apply-templates/>
<span class="lv">[<xsl:value-of select="@type"/>] </span> 
</xsl:template>

<xsl:template match="name">
<a><xsl:attribute name="href">javascript:popname('<xsl:value-of select="@ref"/>')
</xsl:attribute><span class="name" name="noms">
<xsl:apply-templates/></span></a>
</xsl:template>

<xsl:template match="note">
<a><xsl:attribute name="href">javascript:nota("<xsl:value-of select = "translate(., '&#xA;', '')" />")</xsl:attribute><span class="note">
<img src="fleur.png" alt=""/>
<xsl:apply-templates/></span></a></xsl:template>

<xsl:template match="num[@type='cardinalblack']">
<span class="suprablack">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="num[@type='ordinalblack']">
<span class="suprablack">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="num[@type='cardinalred']">
<span class="suprared">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="num[@type='ordinalred']">
<span class="suprared">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="orig">
</xsl:template>

<!-- Silence pb element -->
<xsl:template match="pb">
</xsl:template> 

<xsl:template match="ref">
<span class="briefcase">
<a><xsl:attribute name="href">javascript:popfiche('<xsl:value-of select = "@type"/>')</xsl:attribute><img src="fichier.gif" border="0" alt=""/>
<xsl:apply-templates/></a></span></xsl:template>

<xsl:template match="seg">
<span class="seg"><xsl:apply-templates/></span> 
</xsl:template>

<xsl:template match="sic">
</xsl:template>

<xsl:template match="supplied">
<span class="supplied"><xsl:apply-templates/></span> 
</xsl:template>

<!-- typographie -->

<xsl:template match="add">
<span class="add">
<xsl:apply-templates/></span>
</xsl:template> 

<xsl:template match="del[@rend='erasure']">
</xsl:template> 

<xsl:template match="del[@rend='overwritten']">
</xsl:template> 

<xsl:template match="del[@rend='overstrike']">
<span class="overstrike">
<xsl:apply-templates/></span>
</xsl:template> 

<xsl:template match="div9">
<span class="frontmatter">
<xsl:apply-templates/></span></xsl:template>

<xsl:template match="emph[@rend='headline']">
<span class="headline"><b>
<xsl:apply-templates/></b></span></xsl:template>

<xsl:template match="emph[@rend='italic']">
<span class="italic">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="emph[@rend='sup']">
<sup><xsl:apply-templates/></sup></xsl:template>

<xsl:template match="fw[@rend='centred']">
<span class="centred">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="fw[@rend='inset']">
<span class="inset">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="fw[@rend='italic']">
<span class="italic">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="fw[@size='larger']">
<span class="larger" title="larger text">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="fw[@rend='raligned']">
<span class="raligned">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="fw[@rend='centred, smaller point']">
<span class="smaller" title="smaller text">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="fw[@rend='smaller point']">
<span class="smaller" title="smaller text">
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

<xsl:template match="hi[@rend='inset']">
<span class="inset">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="hi[@rend='red']">
<span class="rubric">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="hi[@rend='purple']">
<span class="purple">
<xsl:apply-templates/></span>
</xsl:template>

<xsl:template match="text()">
<xsl:value-of select="translate(., $with, $sans)" />
</xsl:template>

<xsl:variable name="empty"></xsl:variable>
<xsl:variable name="punct">/\&#x95;</xsl:variable>
<xsl:variable name="ninepunct" select="concat($empty,$empty)"/>

<xsl:variable name="with" select="($punct)"/>
<xsl:variable name="sans" select="($ninepunct)"/>
    
</xsl:stylesheet>
