<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html"
            encoding="iso-8859-1"
	    indent="no"/>

<xsl:template match="entry">
	<hr/>
	<xsl:apply-templates/>
	<hr/>
</xsl:template>

<xsl:template match="form">
	<b>
	<xsl:variable name="nom"><xsl:value-of select="."></xsl:value-of>
	</xsl:variable>
        <a target="_blank" href="http://atilf.atilf.fr/gsouvay/scripts/dmfX.exe?LIEN_DMF;LEMME={$nom}">
	<font color="red">
	<xsl:apply-templates/>
	</font>
        </a>
	</b>
</xsl:template>

<xsl:template match="pos">
	<b>
	<font color="red">
	<xsl:text>, </xsl:text>
	<xsl:apply-templates/>
	</font>
	</b>
</xsl:template>

<xsl:template match="occurrences">
	<table border="0">
	<xsl:apply-templates/>
	</table>
</xsl:template>

<xsl:template match="occurrence">
	<tr>
	<xsl:apply-templates/>
	</tr>
</xsl:template>

<xsl:template match="br">
	<br/>
</xsl:template>

<xsl:template match="w">
	<td valign="top" colspan="2" >
	<b><xsl:apply-templates/></b>
	</td>
</xsl:template>

<xsl:template match="lemmes">
	<td valign="top" width="50">
	<xsl:apply-templates/>
	</td>
</xsl:template>

<xsl:template match="exemple">
	<tr>
	<xsl:apply-templates/>
	</tr>
</xsl:template>

<xsl:template match="texte">
    <td width="50">&#160;</td>
	<td bgcolor="#FFFFEE">
	<xsl:apply-templates/>
	</td>
</xsl:template>

<xsl:template match="occ">
    <i><font color="blue"><xsl:apply-templates/></font>	</i>
</xsl:template>

<xsl:template match="reference">
	<td valign="top">
	<xsl:apply-templates/>
	</td>
</xsl:template>

    
<xsl:template match="DMFBQ">	
	<br/>
	<xsl:apply-templates/>
    <br/>
    <br/>
    <a target="_blank" href="http://atilf.atilf.fr/gsouvay/scripts/dmfX.exe?LIEN_DMF;PROJET=GLOSSAIRE_CDP;LEMME={../form/orth};xxx">Voir les articles du DMF</a>
</xsl:template>

<xsl:template match="NON_TRAITE">
	<i>Non traité dans BQ</i>
	<xsl:apply-templates/>
</xsl:template>

<xsl:template match="VED">
        <br/>
        <b><xsl:apply-templates/></b>
</xsl:template>
    
<xsl:template match="CODE">
	<b>
	<xsl:text>, </xsl:text>
	<xsl:apply-templates/>
	</b>
</xsl:template>

<xsl:template match="P">
	<br/>
	<xsl:apply-templates/>
</xsl:template>

<xsl:template match="NUM">
	<b><xsl:apply-templates/></b>
</xsl:template>

<xsl:template match="EMPL|IND|DEF">
	<xsl:text> </xsl:text>
	<xsl:apply-templates/>
</xsl:template>

<xsl:template match="SYNT">
	<xsl:text> </xsl:text>
	<i>
	<xsl:apply-templates/>
	</i>
</xsl:template>

</xsl:stylesheet>

