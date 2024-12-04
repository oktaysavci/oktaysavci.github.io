<?php
$fullName = $_POST['fullName'];
$message = $_POST['message'];
$filename = 'contact_messages.txt';
$dataToWrite = "$fullName: $message\n";
file_put_contents($filename, $dataToWrite, FILE_APPEND);
echo 'Mesaj başarıyla kaydedildi.';
?>