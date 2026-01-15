<?php
  //create short variable name
  $tireqty = $_POST['tireqty'];
  $oilqty = $_POST['oilqty'];
  $sparkqty = $_POST['sparkqty'];
  $address = $_POST['address'];
  $DOCUMENT_ROOT = $_SERVER['DOCUMENT_ROOT'];
?>
<html>
<head>
<title>flipped Charlie Mansfield October 2009</title>
<style type="text/css">
.loc2 {
z-index : 2;
position : fixed;
max-width : 86mm;
max-height : 50mm;
overflow : scroll;
right : 92mm;
top : 2mm;
border : 1mm solid gray;
padding : 1mm;
background-color : #ccff99;
font-family : Verdana, sans-serif;
font-size : 3.7mm;
}
.loc3 {
z-index : 2;
position : fixed;
max-width : 86mm;
max-height : 50mm;
overflow : scroll;
right : 2mm;
top : 2mm;
border : 1mm solid gray;
padding : 1mm;
background-color : #ffccff;
font-family : Verdana, sans-serif;
font-size : 3.7mm;
}
.loc4 {
z-index : 2;
position : fixed;
max-width : 86mm;
max-height : 50mm;
overflow : scroll;
right : 182mm;
top : 55mm;
border : 1mm solid gray;
padding : 1mm;
background-color : #66ffcc;
font-family : Verdana, sans-serif;
font-size : 3.7mm;
}
.loc5 {
z-index : 2;
position : fixed;
max-width : 86mm;
max-height : 50mm;
overflow : scroll;
right : 92mm;
top : 55mm;
border : 1mm solid gray;
padding : 1mm;
background-color : #f5f5dc;
font-family : Verdana, sans-serif;
font-size : 3.7mm;
}
.loc6 {
z-index : 2;
position : fixed;
max-width : 86mm;
max-height : 50mm;
overflow : scroll;
right : 2mm;
top : 55mm;
border : 1mm solid gray;
padding : 1mm;
background-color : #ffcc66;
font-family : Verdana, sans-serif;
font-size : 3.7mm;
}
.loc7 {
z-index : 2;
position : fixed;
max-width : 86mm;
max-height : 50mm;
overflow : scroll;
right : 182mm;
top : 108mm;
border : 1mm solid gray;
padding : 1mm;
background-color : #ccccff;
font-family : Verdana, sans-serif;
font-size : 3.7mm;
}
.loc8 {
z-index : 2;
position : fixed;
max-width : 86mm;
max-height : 50mm;
overflow : scroll;
right : 92mm;
top : 108mm;
border : 1mm solid gray;
padding : 1mm;
background-color : #ff6600;
font-family : Verdana, sans-serif;
font-size : 3.7mm;
}
.blanc {
border : 0.5mm solid gray;
padding : 0.5mm;
background-color : #ffffff;
font-family : Verdana, sans-serif;
font-size : 3.7mm;
}
</style>
</head>
<body>
<?php
$mot = array( 'dessus', ' cy', 'ce', 'gauche', 'droite', 'derriere', 'dessous' );
$en = array( 'above', 'here', 'this', 'left', 'right', 'behind', 'below' );
$loc = array( '2', '5', '3', '4', '6', '7', '8' );
$carreau = array( 'empty0', 'empty1', '[2] ABOVE ci-dessus', '[3] IN FRONT en avant', '[4] TO THE LEFT à gauche', '[5] INSIDE WITH dans avec', '[6] TO THE RIGHT à droite', '[7] BEHIND derrière ', '[8] BELOW ci-dessous', 'empty9');
$sub = array( 0, 0, 0, 0, 0, 0, 0, 0, 0 );
$count = 0;
$total = 0;
$reddot = '<span class="barre"><font color="red">|</font></span>';
$greendot = '<span class="green"><font color="green">|</font></span>';
$bluedot = '<span class="blue"><font color="blue">|</font></span>';
$greydot = '<span class="gris">|</span>';
$dots = "";
$found = "0";
$filename = $address.".txt";
echo "".$tireqty."  ".$oilqty. "  ".$sparkqty;
echo strrev($tireqty); // outputs "!dlrow olleH"
echo "<br />_________________________________________<br />";
   @$fp = fopen($filename, 'rb');

   if (!$fp) {
     echo "<p>No results. Pas de résultats</p>";
     exit;
   }

   while (!feof($fp)) {
      $order= fgets($fp, 9999);
for ($i = 0; $i<9; $i++) {
if (stristr($order, $mot[$i])) {
$highlit= "<b>".$mot[$i]."</b>";
$order = str_replace($mot[$i], $highlit, $order, &$count);
$total = $total + $count;
$sub[$loc[$i]] = $sub[$loc[$i]] + $count;
$carreau[$loc[$i]] = $carreau[$loc[$i]]."<br />".$order;
 }
 }
}
    //loop through each pane (le carreau) 2 to 8
for ($i = 2; $i<9; $i++) {
echo "<span class='loc".$i."'>".'<span class="blanc">'.$sub[$i]."</span>&nbsp;&nbsp;".$carreau[$i]."&nbsp;&nbsp;</span>";
}

   echo "<br />";
   echo "Final position of the file pointer is ".(ftell($fp));
   echo "<br />";
   fclose($fp);
  echo "<br />";
   echo "Count total of locemes found is: ";
   echo "$total";
  echo "<br />";
echo "<br />";
echo "<span class='gris'>_________________________________________ <br />";
echo "PHP by Charlie Mansfield Oct 2009 <br /></span>";
?>
</body>
</html>
