<?php
if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
    $ip = $_SERVER['HTTP_CLIENT_IP'];
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
} else {
    $ip = $_SERVER['REMOTE_ADDR'];
}

error_log("bla bla bla");
echo $ip;

$servername = "localhost";
$username = "root";
$password = "";

// Create connection
$conn = new PDO('mysql:host=localhost;dbname=rfid1', $username, $password);
$conn->beginTransaction();

var_dump($_GET['device_id']);
var_dump($_GET['ip_from']);
var_dump($_GET['badge_id']);
var_dump($_GET['badge_content']);

$sql = "INSERT INTO request_log(device_id, ip_from, badge_id, badge_content, datetimes) values(".(int)$_GET['device_id'].",'".$_GET['ip_from']."', ".(int)$_GET['badge_id'].",'".$_GET['badge_content']."', now())";
error_log($sql);
$s = $conn->prepare($sql);
$s->execute(array(
));
$conn->commit();
?>