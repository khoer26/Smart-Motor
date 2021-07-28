<?php
$file = "buttonStatus.txt";
$handle = fopen($file,'w+');
if(isset($_POST['off']))
{
$offstring = "OFF";
fwrite($handle, $offstring);
fclose($handle);
print "
<!DOCTYPE html>
<html lang='en'>
<head>
<title>Raspberry Pi - IoT motorcycle automation project</title>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>
  <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
  <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>
<body align='center'>
<h2>Raspberry Pi - Internet of Things Implementation</h2>
<h2 style='background:red'>Motor anda telah mati </h2>
</body>
</html>
";
}
if (isset($_POST['on1']))
{
$on1string = "ON1";
fwrite($handle,$on1string);
sleep(3);
$defstring = "DEF";
fwrite($handle,$defstring);
fclose($handle);
print "
<!DOCTYPE html>
<html lang='en'>
<head>
<title>IoT Raspberry pi</title>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>
  <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
  <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>
<body align='center'>
<title>Raspberry Pi - IoT home automation project</title>
<h2>Raspberry Pi - Internet of Things Implementation</h2>
<h2 style='background:green'>Motor anda telah nyala </h2>
</body>
</html>
";
}
if(isset($_POST['on2']))
{
$on2string = "ON2";
fwrite($handle, $on2string);
sleep(2);
$defstring = "DEF";
fwrite($handle,$defstring);
fclose($handle);
print "
<!DOCTYPE html>
<html lang='en'>
<head>
<title>Raspberry Pi - IoT motorcycle automation project</title>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>
  <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
  <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>
<body align='center'>
<h2>Raspberry Pi - Internet of Things Implementation</h2>
<h2 style='background:blue'>Klakson anda telah nyala </h2>
</body>
</html>
";
}
if(isset($_POST['on3']))
{
$on3string = "ON3";
fwrite($handle, $on3string);
fclose($handle);
print "
<!DOCTYPE html>
<html lang='en'>
<head>
<title>Raspberry Pi - IoT motorcycle automation project</title>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>
  <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
  <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>
<body align='center'>
<h2>Raspberry Pi - Internet of Things Implementation</h2>
<h2 style='background:yellow'>Fitur anti maling telah diaktifkan </h2>
</body>
</html>
";
}
?>