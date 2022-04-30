<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta http-equiv="X-UA-Compatible" content="ie=edge" />
	<title>Document</title>
</head>
<body>
<?php
    if(!empty($_POST)){
    	//step1:收集数据表单
    	$fields = array('classname','classdesc','classid');
		foreach($fields as $v){
			$save_data[$v] = isset($_POST[$v])? $_POST[$v]:'';
		}
		//step2:执行添加操作
		require_once 'common/common_db.php';
		$result = editNewsClass($save_data['classid'],$save_data['classname'], $save_data['classdesc']);
		if($result){
			echo '修改成功';
		}else{
			echo '修改失败';
		}
    }

?>
</body>