<?php
$colorselect="";
$colorfill="";
//add code to request option value and text value

?>
<!DOCTYPE html>
<html>
<head>
    <title>Loop Tester</title>
    <link rel="stylesheet" type="text/css" href="main.css"/>
</head>

<body>
<main>
    <h1>Your Favorite Color:</h1>
       <form action="index.php" method="post">
        <input type="hidden" name="action" value="process_rolls">
        <label style="white-space:nowrap; padding-right:100px;">Choose Your Favorite Color:</label>
        <select name="colorselect">
        <?php if (isset($colorselect)){ ?>
            <option value="<?php echo $colorselect ?>" selected="selected"><?php echo $colorselect ?></option>
            <?php
			}
			?>
            <!--use a for loop to display the <option> tags
            -->
            <option value="red">red</option>
            <option value="green">green</option>
            <option value="blue">blue</option>
            <option value="orange">orange</option>
            <option value="white">white</option>
            <option value="black">black</option>
        </select><br>
		<?php #$colorselect=$_POST["colorselect"];
#$colorfill=$_POST["color"];?>
			 <label style="white-space:nowrap;padding-right:100px;">Or Fill in the color:</label>
        <input type="text" name="colorfill" value="<?php echo $colorfill?>"/>
        <p>
        <br>
        
        <input type="submit" value="SUBMIT" >
       <p>
        
        <label style="white-space:nowrap;">Your Favorite Color:</label>
        <spxan style="font-size:24px;text-align:left;display:block;color:red">
		<!--display the option value and text value 
        -->
		
			<?php
			if($_POST){
			
			echo $_POST["colorselect"].' '.$_POST["colorfill"];
			
			}
			 
			?></textarea>
          </span>
        <br>        

    </form>

</main>
</body>
</html>