<?php 
    //set default value of variables for initial page load
    if (!isset($username)) { $username = ''; } 
    if (!isset($password)) { $password = ''; } 
    if (!isset($email)) { $email = ''; } 
	 if (!isset($notes)) { $notes = ''; } 
	
?> 
<!DOCTYPE html>
<html>
<head>
    <title>login</title>
    <link rel="stylesheet" type="text/css" href="main.css">
</head>

<body>
    <main>
    <h1>login</h1>
    <?php if (!empty($error_message)) {  
	
	echo '<p class="error">'.htmlspecialchars($error_message).'</p>';
	
	}
	?>
   <!--    <p class="error"><?php echo htmlspecialchars($error_message); ?></p>-->
   <?php //} ?>
    <form action="display_results.php" method="post">

        <div id="data">
            <label>username:</label>
            <input type="text" name="username"
                   value="<?php echo htmlspecialchars($username); ?>">
				   <span>*</span>
            <br>

            <label>password:</label>
            <input type="password" name="password"
                   value="<?php echo htmlspecialchars($password); ?>">
				   <span>*</span>
            <br>
            <label>repassword:</label>
            <input type="password" name="repassword"
                   value="<?php echo htmlspecialchars($password); ?>">
				   <span>*</span>
            <br>
			<label>sex:</label>
		</div>
		<div id="radio">
			<input type="radio" name="sex" value="male" checked="checked" >male</input>
			<input type="radio" name="sex" value="female" >female</input>
		</div>
			<br>
		<div id="data1">
            <label>email:</label>
            <input type="text" name="email"
                   value="<?php echo htmlspecialchars($email); ?>">
            <br>
			<label>notes:</label>
			<textarea name="notes" rows=4 cols=50><?php echo htmlspecialchars($notes); ?></textarea>
		</div>

        <div id="buttons">
            <label>&nbsp;</label>
            <input type="submit" value="submit"><br>
        </div>

    </form>
    </main>
</body>
</html>