<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<title>显示新闻分类的列表</title>
	</head>
	<?php
	require_once 'common/common_db.php';
	$rows = findNewsClass();
	?>
	<body>
		<table border="1">
			<tr>
				<th>编号</th>
				<th>新闻分类名称</th>
				<th>分类描述</th>
				<th>编辑</th>
				<th>删除</th>
			</tr>
			<?php
		foreach($rows as $row){
		?>
		<tr>
			<td><?php echo $row['classid']; ?></td>
			<td><?php echo $row['classname']; ?></td>
			<td><?php echo $row['classdesc']; ?></td>
			<td>
				<a href="editNewsClass.php?id=<?php echo $row['classid'];?>">修改</a>
				
			</td>
			<td>
				<a href="editNewsClass.php?id=<?php echo $row['classid'];?>">删除</a>
			</td>
		</tr>
		<?php
		}
		?>
		</table>
		
</body>