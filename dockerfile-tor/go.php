<?php

require 'vendor/autoload.php';


$tc = new TorControl\TorControl(
    array(
        'hostname'   => 'localhost',
        'port'       => 8051,
        'password'   => "my_password",
        'authmethod' => 1
    )
);

$tc->connect();

$tc->authenticate();

// Renew identity
$res = $tc->executeCommand('SIGNAL NEWNYM');
//
// Echo the server reply code and message
echo $res[0]['code'].': '.$res[0]['message'];
//
// Quit
$tc->quit();
