<?php
function get_connect(){
	$link = mysqli_connect("127.0.0.1","root");
	if(!$link){
		die("数据库连接失败").mysqli_error();
	}
	mysqli_query($link, "set names utf8");
	mysqli_query($link, "use db_news");
	return $link;
}
function findNewsClass(){
	$sql = "select * from tbl_newsclass";
	//step1:连接数据库
	$link= get_connect();
	//step2:执行sql语句
	
	$result = mysqli_query($link,$sql);
	//step3:处理查询结果
	$rows = array();
	while($row = mysqli_fetch_assoc($result)){
		$rows[] = $row;
	}
	//step4:关闭数据库连接
	mysqli_close($link);
	return $rows;
}

//$rst = findNewsClass();

function addNewsClass($classname,$classdesc){
	$sql = "insert into tbl_newsclass (classname,classdesc) values ('$classname','$classdesc')";
	//step1:连接数据库
	$link = get_connect();
	//step2:执行语句
	$result = mysqli_query($link, $sql);
	//step3:关闭数据库
	mysqli_close($link);
	return $result;
}
function deleteNewsClass($classid){
	$sql = "delete from tbl_newsclass where classid = $classid";
	//step1:连接数据库
	$link = get_connect();
	//step2:执行语句
	$result = mysqli_query($link, $sql);
	//step3:关闭数据库
	mysqli_close($link);
	return $result;
}

function editNewsClass($classid,$classname,$classdesc){
	$sql = "update tbl_newsclass set classname = '$classname', classdesc = '$classdesc' where classid = $classid";
	//step1:连接数据库
	$link = get_connect();
	//step2:执行语句
	$result = mysqli_query($link, $sql);
	//step3:关闭数据库
	mysqli_close($link);
	return $result;
}

function  findNewsClassByID($classid){
	$sql = "select * from tbl_newsclass where classid = $classid";
	//step1:连接数据库
	$link= get_connect();
	//step2:执行sql语句
	
	$result = mysqli_query($link,$sql);
	//step3:处理查询结果
	$rows = array();
	while($row = mysqli_fetch_assoc($result)){
		$rows[] = $row;
	}
	//step4:关闭数据库连接
	mysqli_close($link);
	if(count($rows) > 0){
		return $rows[0];
	}
	return $rows;
}


//$result = addNewsClass('测试分类444', 'sdfsdfsdfdsdfsdfdsfdfds');
//echo $result ?'success' : 'fail';

//$result = deleteNewsClass(17);
//echo $result ?'success' : 'fail';

//$result = editNewsClass(12,'测试分类555', 'sdfsdfsdfdsdfsdfdsfdfds');
//echo $result ?'success' : 'fail';

//$result = findNewsClassNyID(18);
//var_dump($result);

/*
$link = get_connect();
$result = mysqli_query($link, "select * from tbl_newsclass");

//var_dump($result);

while($row = mysqli_fetch_assoc($result));{
//var_dump($row);
//echo '<br>';
//$rows[] = $row;
}
var_dump($rows[]);
 */
?>