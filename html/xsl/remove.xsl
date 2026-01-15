<!--
 Charlie Mansfield created this XSLT script with EditiX on Wed Jul 22 09:36:01 BST 2009 
-->
−
<!--
 This XSLT script transforms XML to another XML file 
-->
−
<!--
 Consider the encoding settings in lines 1 and 6 Tony and Gilles use iso-8859-1 while rest of Pizan is UTF-8  
-->
−
<xsl:stylesheet version="1.0">
<xsl:output method="xml" encoding="iso-8859-1" indent="yes"/>
−
<!--
 removed element simply does not have apply templates command 
-->
<xsl:template match="texte">
</xsl:template>
−
<!--
 All the other elements have to be painstakingly rescued by applying them again 
-->
<!-- and you have to type their element names again -->
−
<!--
 However this does mean that you could use this XSLT to change any element name if you wanted to 
-->
−
<xsl:template match="Glossaire">
−
<Glossaire>
<xsl:apply-templates/>
</Glossaire>
</xsl:template>
−
<xsl:template match="entry">
−
<entry>
<xsl:apply-templates/>
</entry>
</xsl:template>
−
<xsl:template match="form">
−
<form>
<xsl:apply-templates/>
</form>
</xsl:template>
−
<xsl:template match="orth">
−
<orth>
<xsl:apply-templates/>
</orth>
</xsl:template>
−
<xsl:template match="pos">
−
<pos>
<xsl:apply-templates/>
</pos>
</xsl:template>
−
<xsl:template match="occurrences">
−
<occurrences>
<xsl:apply-templates/>
</occurrences>
</xsl:template>
−
<xsl:template match="occurrence">
−
<occurrence>
<xsl:apply-templates/>
</occurrence>
</xsl:template>
−
<xsl:template match="w">
−
<w>
<xsl:apply-templates/>
</w>
</xsl:template>
−
<xsl:template match="lemmes">
−
<lemmes>
<xsl:apply-templates/>
</lemmes>
</xsl:template>
−
<xsl:template match="lem">
−
<lem>
<xsl:apply-templates/>
</lem>
</xsl:template>
−
<xsl:template match="exemples">
−
<exemples>
<xsl:apply-templates/>
</exemples>
</xsl:template>
−
<xsl:template match="exemple">
−
<exemple>
<xsl:apply-templates/>
</exemple>
</xsl:template>
−
<xsl:template match="reference">
−
<reference>
<xsl:apply-templates/>
</reference>
</xsl:template>
−
<xsl:template match="DMFBQ">
−
<DMFBQ>
<xsl:apply-templates/>
</DMFBQ>
</xsl:template>
−
<xsl:template match="corps">
−
<corps>
<xsl:apply-templates/>
</corps>
</xsl:template>
−
<xsl:template match="P">
−
<P>
<xsl:apply-templates/>
</P>
</xsl:template>
−
<xsl:template match="DISC">
−
<DISC>
<xsl:apply-templates/>
</DISC>
</xsl:template>
−
<xsl:template match="DEF">
−
<DEF>
<xsl:apply-templates/>
</DEF>
</xsl:template>
−
<xsl:template match="fr">
−
<fr>
<xsl:apply-templates/>
</fr>
</xsl:template>
</xsl:stylesheet>