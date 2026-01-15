<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" indent="no"/>
<xsl:key name="N" match="g" use="'1'"/>
<xsl:template match="/">
<head>
<title>Glossary of Middle French in Harley 4431 with In-Search and Link to DMF 19 January 2009 C Mansfield</title>
<meta http-equiv="content-type" content="text/html;charset=iso-8859-1" />
<meta http-equiv="Content-Style-Type" content="text/css" />
 <style type="text/css">
body {color: #000000; font-family: Verdana, Arial, sans-serif; font-size: 3.1mm;}
.two {color: #000000; font-weight: bold; font-family: Verdana, Arial, sans-serif; font-size: 3.3mm;}
.langs {color: #000000; font-family: Verdana, Arial, sans-serif; font-weight: bold; font-size: 2.6mm;}
.boldred {color: #ff0000; font-weight: bold; font-size: 4.7mm;}
</style>
<script type="text/javascript">
function replacer()
{
thisform=document.dataIn4;
var counting=document.getElementById("textarea4");
var find="";
var hifind="";
var array9="";
var occurs=0;
hifind=myValue+" ";
find = new RegExp(hifind, "g");
var replace="";
replace='<span class="boldred"><a name="pointto"></a>' + hifind + '</span>';
var array9 = document.getElementById("source");
var col_array=array9.innerHTML.split(hifind);
occurs=col_array.length-1;
counting.value = occurs;
array9.innerHTML = array9.innerHTML.replace(find, replace); 
}

var newwindow;
function popdmf(url)
{
var mot=document.location.search.substring(1);
urlmot=url+mot;
newwindow=window.open(urlmot,'name','height=400,width=400,left=380,top=100,scrollbars=yes,resizable=yes');
if (window.focus) {newwindow.focus()}
}

</script>
</head>
<body>
<font face="Verdana" size="1.7mm">
<script type="text/javascript">
setTimeout("self.close()", 100000);
var myValue=document.location.search.substring(1);
document.writeln("Search for :<b> " + myValue +"</b>");
</script>
</font>
<table bgcolor="#FFF0F5">
<tr>
<td>
<font face="Verdana">
<form name="dataIn4" action=""> 
<a href="javascript:replacer()">Click</a> to highlight in this Glossary  
<input type="text" id="textarea4" size="4" value="TOTAL"></input> 
<a href="#pointto">... then jump to first entry »</a>
</form>
<br />
<a href="javascript:popdmf('http://atilf.atilf.fr/gsouvay/scripts/dmfX.exe?LIEN_DMF;LEMME=')"> Or search DMF direct</a>
<br/>
<br/>
</font>
</td>
</tr>
</table>
<p>
<b>Middle French Glossary</b>
<br/><br/>
<div id="source">
<span class="two">Lemma</span> ( Form in Harley 4431 )  Sense in English; Sense in French; Type; Line Number
<br/><br/>
<xsl:for-each select="key('N',1)">
<xsl:sort select="@lemma"/>
<span class="two"><xsl:value-of select="@lemma"/></span> ( <xsl:value-of select="."/> ) 
  <span class="langs">EN </span> <xsl:value-of select="@en"/>;
  <span class="langs">FR </span> <xsl:value-of select="@fr"/>; <xsl:value-of select="@type"/>; 
  <xsl:value-of select="preceding::lb[1]/@n"/>  <xsl:value-of select="text/div1/div2/lb[last()]/@n"/>
  <br/><br/>

</xsl:for-each>
</div>
</p></body>
</xsl:template>
</xsl:stylesheet>
