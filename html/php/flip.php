<?php
  $address = $_POST['address'];
  $DOCUMENT_ROOT = $_SERVER['DOCUMENT_ROOT'];
?>
<html>
<head>
<title></title>
</head>
<body>
<?php
$order = " ";
$filename = $address.".txt";
@$fp = fopen($filename, 'rb');
   if (!$fp) {
     echo "";
     exit;
   }
while (!feof($fp)) {
      $order= fgets($fp, 9999);
echo "<br />".strrev($order);
}
fclose($fp); 
?>
</body>
</html>

