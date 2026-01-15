<!-- fonctions JavaScript (ECMAScript) de Charlie Mansfield 2005 2008 2009  -->

<!-- The Pop-Up for Index of Proper Names October 2007 -->
var newwindow;
function popname(url)
{
var mot="https://www.wiki.ed.ac.uk/display/4431wiki/";
urlmot=mot+url;
newwindow=window.open(urlmot,'name','height=400,width=480,left=380,top=100,toolbar=yes,location=yes,status=yes,menubar=yes,scrollbars=yes,resizable=yes');
if (window.focus) {newwindow.focus()}
}

<!-- The Pop-Up for Index of Proper Names October 2007 -->
var newwindow;
function popfiche(url)
{
var mot="";
urlmot=mot+url;
newwindow=window.open(urlmot,'fiche','height=200,width=580,left=200,top=30,toolbar=yes,location=yes,status=yes,menubar=yes,scrollbars=yes,resizable=yes');
if (window.focus) {newwindow.focus()}
}

<!-- Pop up WORD document from MTG associated with miniature -->
var newwindow;
function popmin(url)
{
var mot="";
urlmot=mot+url;
newwindow=window.open(urlmot,'mini','height=300,width=320,left=430,top=30,toolbar=yes,location=yes,status=yes,menubar=yes,scrollbars=yes,resizable=yes');
if (window.focus) {newwindow.focus()}
}


<!-- Glossaire M. Charlie MANSFIELD septembre 2007 -->
var la='<span class="tiny">GLOSES - Ctrl R les supprimera</span><br />';
var en="", fr="";
var replacer="";
var find="-";
function gloss(mf, en, fr)
{
thisform=document.dataIn;
{
la=mf+'  <b>'+en+'</b> '+fr+'<br />'+la;
if (document.getElementById)  document.getElementById("gloss").innerHTML=la;
}
}

<!-- Nota Bene Charlie MANSFIELD fevrier 2008 -->
var inst='<span class="tiny">Ctrl R</span><br />';
function nota(note)
{
thisform=document.dataIn;
{
inst=note+'<br />';
if (document.getElementById)  document.getElementById("notes").innerHTML=inst;
}
}


<!--  Chercher DMF2 Charlie MANSFIELD mars 2008 -->
var text = "";
var myValue = "";
function getActiveText(e) { 
text = (document.all) ? document.selection.createRange().text : document.getSelection();
myValue=text+"";
if (document.selection) document.selection.empty();
else if (window.getSelection) window.getSelection().removeAllRanges();
if (myValue!="") {
window.open("get.html?" + myValue,"",'height=540,width=700,left=80,top=40,scrollbars=yes,resizable=yes')
    } 
return true;
}

document.onmouseup = getActiveText;
if (!document.all) document.captureEvents(Event.MOUSEUP);


//  End -->