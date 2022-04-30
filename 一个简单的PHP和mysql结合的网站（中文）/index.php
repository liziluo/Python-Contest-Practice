<html>
<head>
<meta charset="utf-8">
<title></title>
<link href="style/styledform.css" rel="stylesheet">
</head>
<body>
<form name="form1" action="" method="post" enctype="multipart/form-data">
   <div class="tableRow">
     <p></p>
     <p class="heading">用户登录</p>
   </div>      
   <div class="tableRow">
      <p>用户名:</p>
      <p><input type="text" name="uname" size="30" required/></p>
   </div> 
   <div class="tableRow">
      <p>密码:</p>
      <p><input type="password" name="upass" size="30"/></p>
   </div>
   <div class="tableRow">
      <p><input type="hidden" name="power" value="1"></p>
      <p><input type="submit" value="登录"> </p>
   </div>
    </form>
</body>
</html>
<?php

if(!empty($_POST)){
$user=$_POST['uname'];
$pwd=$_POST['upass'];

	     if ($user =='admin' && $pwd=='123' ){
			 echo'登录成功';
			 header("location:all.php");
		 }else{
			 echo '用户密码错误或账号错误';
			
		 }
}
?>
