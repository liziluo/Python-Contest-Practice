<?php
    // add code to get the data from the form
    $username='';
	$password='';
	$repassword='';
	$email='';
	$sex='';
	$notes='';
	$count=2;
	//add code to get the user information from the table here
	include('database.php');
	if ($_POST["username"]){
		 	$username=$_POST["username"];
		 	$password=$_POST["password"];
		 	$repassword=$_POST["repassword"];
		 	$email=$_POST["email"];
		 	$sex=$_POST["sex"];
		 	$notes=$_POST["notes"];}
	
    // add code to validate username
  
	// add code to validate if the userName is unique here.
	if ( empty($username) )  {
	    $error_message = 'username is a required field.'; 
	} else if (strlen($username) < 3 || strlen($username)>20 ) {
	    $error_message = 'length of password  must be between 3 and 20.'; 
	
	}
	
	 // validate password
	if ( empty($password) )  {
        $error_message = 'password is a required field.'; 
    } else if ( strlen($password) < 6 || strlen($password)>12 ) {
        $error_message = 'length of password  must be between 6 and 12.'; 
    
    }
	//validate that two password boxes are the same entry
  if ($password==$repassword){
  }
  else{
	  $error_message ="two password boxes must be the same value";
  }

    // if an error message exists, go to the index page
    if (!empty($error_message)) {
        include('index.php');
        exit(); 
    }
// add code for adding a new user  to the database here
 $sql="select * from user where UserName='$username'";
$result=$db->query($sql);
if ($result=True){	
 echo"userName entered into the text box is unique.";
	
}
else{
	$sql1= "insert into user "."(userID, UserName, password, sex, email, notes) "."values({$count}','{$username}','{$password}','{$sex}','{$email}','{$notes}')";
	$result2=$db->query($sql1);	
	if($result2){
		$count=$count+1;
	}
	else{
		echo"添加失败";
	}
}


   ?>
<!DOCTYPE html>
<html>
<head>
    <title>login information</title>
    <link rel="stylesheet" type="text/css" href="main.css">
</head>
<body>
    <main>
        <h1>login information</h1>

        <label>username:</label>
        <?php echo $username; ?><br>

        <label>password:</label>
        <?php echo $password; ?><br>
		
		<label>sex:</label>
        <?php echo $sex; ?><br>

        <label>email:</label>
        <?php echo $email; ?><br>
		<label>notes:</label>
        <?php echo $notes; ?><br>

          </main>
</body>
</html>
