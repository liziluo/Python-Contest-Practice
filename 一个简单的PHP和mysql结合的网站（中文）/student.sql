
CREATE DATABASE `studb`;

# 使用数据库
USE `studb`;                 

#创建数据表
CREATE TABLE `student` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL COMMENT '姓名',
  `sex` char(2) DEFAULT NULL COMMENT '性别',
  `age` varchar(6) DEFAULT NULL COMMENT '年龄',
  `edu` varchar(12) DEFAULT NULL COMMENT '学历',
  `salary` decimal(10,2) DEFAULT NULL COMMENT '工资',
  `bonus` decimal(10,2) DEFAULT NULL COMMENT '奖金',
  `city` varchar(32) DEFAULT NULL COMMENT '籍贯',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#插入测试数据
INSERT INTO `student` VALUES ('1', '测试工程师1', '男', '22', '研究生', '25000.00', '10000.00', '广东');
INSERT INTO `student` VALUES ('2', 'ui工程师', '女', '20', '本科', '7000.00', '5000.00', '湖南');
INSERT INTO `student` VALUES ('3', '后端工程师1', '女', '22', '研究生', '20000.00', '7000.00', '湖南');
INSERT INTO `student` VALUES ('4', '前端工程师2', '女', '25', '本科', '17000.00', '2000.00', '湖南');
INSERT INTO `student` VALUES ('5', '数据科学家', '男', '29', '博士生', '40000.00', '2000.00', '湖南');

                           



