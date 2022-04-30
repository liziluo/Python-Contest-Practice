<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta http-equiv="X-UA-Compatible" content="ie=edge" />
	<title>Document</title>
	<link rel="stylesheet" href="styledform.css" type="text/css" />
</head>
<?php
if(!isset($_GET['id'])){
	//如果没有取到参数id的值时，页面自动跳转到newsclasslist.php
	header("location:newsclasslist.php");	
}
require_once 'common/common_db.php';
$classid = $_GET['id'];
$row = findNewsClassByID($classid);
?>
<body>
	<form method="post" action="editNewsclass_ok.php">
		<div class="tableRow">
			<p></p>
			<p class="heading"></p>
		</div>
		<div class="tableRow">
			<p>分类名称:</p>
			<p>
				<input type="text" name="classname" value="<?php echo $row['classname'];?>"/>
			</p>
		</div>
		<div class="tableRow">
			<p>新闻分类描述:</p>
			<p>
				<textarea name="classdesc"><?php
					echo $row['classdesc'];
					?></textarea>
			</p>
		</div>
		<div class="tableRow">
			<p></p>
			<p>
				<input type="hidden" name="classid" value="<?php echo $classid;?>">
				<input type="submit" value="修改" />
			</p>
		</div>
	</form>