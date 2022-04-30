<?php
//set default values
$name = '';
$email = '';
$phone = '';
$message = 'Enter some data and click on the Submit button.';

//process
$action = filter_input(INPUT_POST, 'action');

switch ($action) {
    case 'process_data':
        $name = filter_input(INPUT_POST, 'name');
        $email = filter_input(INPUT_POST, 'email',FILTER_VALIDATE_EMAIL);
        $phone = filter_input(INPUT_POST, 'phone',FILTER_SANITIZE_NUMBER_INT);

        /*************************************************
         * validate and process the name
         ************************************************/
        // 1. make sure the user enters a name
        // 2. display the name with only the first letter capitalized
			$name=ucfirst($name);
			$i = strpos($name, ' ');
			 $first= substr($name, 0, $i);
			    $last = substr($name, $i+1);
		
        /*************************************************
         * validate and process the email address
         ************************************************/
        // 1. make sure the user enters an email
        // 2. make sure the email address has at least one @ sign and one dot character
$at=strpos($email, '@');
$a=strpos($email, '.');
if(isset($a)&&isset($at)){
	;
}
else{
	 $emai =" email address has at least one @ sign and one dot character" ;
}
//上述已经用FILTER_VALIDATE_EMAIL判断邮箱地址
        /*************************************************
         * validate and process the phone number
         ************************************************/
        // 1. make sure the user enters at least seven digits, not including formatting characters
        // 2. format the phone number like this 123-4567 or this 123-456-7890
$part1=substr($phone,0,3);
	$part2=substr($phone,3,3);
	$part3=substr($phone,6);
	$part4=substr($phone,3,4);
	$format1= $part1."-".$part2."-".$part3;
	$format2= $part1."-".$part4;
	$num1=strlen($phone);
	if($num1>7){
	 $phone1=$format1;
	}
	if($num1==7){
      $phone1=$format2;
	}
	else if($num1 <7) {
			$phone1 = 'make sure the user enters at least seven digits'; 
		 }
        /*************************************************
         * Display the validation message
         ************************************************/
        $message = "Hello $first,

Thank you for entering this data:

Name: $name

Email:  $email

Phone:  $phone1 ";

        break;
}
include 'string_tester.php';
?>