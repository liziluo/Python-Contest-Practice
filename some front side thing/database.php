<?php
       $dsn="mysql:host=localhost:3316;dbname=user_test";
       $user="root";
       $password="";
    try {
		$db=new PDO($dsn,$user,$password);
       // add code for connect "user_test" database, use "msg_user" as username and "pa55word" as password 
    } catch (PDOException $e) {
        $error_message = $e->getMessage();
        echo $error_message;
        exit();
    }
?>