<?php
$user = $_GET['user'] ?? '';
$status = $_GET['status'] ?? '';
$user = base64_decode($user);
if (!empty($user) && !empty($status)) {
    if(preg_match("/^.*[;()$|&]/", $user,$match)){
        echo "No No hacker not this time.";
    } else {
    $date = date('Y-m-d H:i:s');
    $command = "echo \"[+] Auth Attempt $date $user $status\" >> app_log";
    shell_exec($command);
    echo "Log entry added successfully.";
    }
} else {
    echo "Please provide both user and status parameters.";
}
?>
