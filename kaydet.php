<?php
if (isset($_POST['log'])) {
    file_put_contents("loglar.txt", $_POST['log'] . PHP_EOL, FILE_APPEND);
    echo "OK";
} else {
    echo "No data";
}
?>
