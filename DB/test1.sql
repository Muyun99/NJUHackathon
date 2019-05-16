-- 1. 创建数据库
-- CREATE DATABASE DBLEARN;

-- 2. 表相关操作

-- 2.1 创建表
-- CREATE TABLE S(
--     Sno VARCHAR(20) PRIMARY KEY,    /*列级完整约束条件，Sno是主码*/
--     Sname VARCHAR(20) ,             /*Sname不去唯一值(和书上P82不一样)*/
--     Ssex VARCHAR(2),
--     Sage SMALLINT,
--     Sdept VARCHAR(20)
-- );

-- CREATE TABLE C(
--     Cno VARCHAR(4) PRIMARY KEY, /*列级完整约束条件，Cno是主码*/
--     Cname VARCHAR(20) NOT NULL, /*列级完整性约束条件，Cname不能取空值*/
--     Cpno VARCHAR(4),
--     Ccredit FLOAT,
--     FOREIGN KEY(Cpno) REFERENCES C(Cno)
--     /*表级完整性约束条件，Cpno是外码，被参照表是C，被参照列是Cno*/
-- );

-- CREATE TABLE SC(
--     Sno VARCHAR(20),
--     Cno VARCHAR(4),
--     Grade SMALLINT,
--     FOREIGN KEY (Sno) REFERENCES S(Sno),
--     /*表级完整性约束条件，Sno是外码，被参照表是S，被参照列是Sno*/
--     FOREIGN KEY (Cno) REFERENCES C(Cno)
--     /*表级完整性约束条件，Cno是外码，被参照表是C，被参照列是Cno*/
-- );

-- 2.2 删除数据库
-- DROP TABLE SC RESTRICT;
-- DROP TABLE S CASCADE;
-- DROP TABLE C CASCADE

-- 2.3 修改数据库
-- ALTER TABLE C ADD S_entrace DATE;
-- ALTER TABLE C DROP COLUMN S_entrace 
-- ALTER TABLE S ADD S_entrace DATE;
-- ALTER TABLE C ADD UNIQUE(Cname);
-- ALTER TABLE S ALTER COLUMN Sage VARCHAR(10);

-- 3. 索引相关操作
-- 3.1 创建索引
-- CREATE UNIQUE INDEX Sno ON S(Sno);
-- 3.2 重命名索引
-- ALTER TABLE S RENAME INDEX Sno TO StudenTno;
-- 3.2 删除索引
-- DROP INDEX Sno ON S; 

-- 4. 插入数据(INSERT)
-- INSERT INTO S(Sno,Sname,Ssex,Sage,Sdept,S_entrace)
-- VALUES ("161640111","杜云","男","20","计算机系","2016-09-01");

-- 先删除C课程的外键
-- ALTER TABLE C DROP FOREIGN KEY PREC_KEY;

-- 添加两条记录
-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("1","数据库原理","2","3");

-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("2","数据结构","1","3");

-- 添加C课程的先修课程的外键
-- ALTER TABLE C ADD CONSTRAINT PREC_KEY1 FOREIGN KEY (Cpno) REFERENCES C(Cno);

-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("3","数据结构2","3","3");



-- 删除数据
-- DELETE 
-- FROM C
-- WHERE Cno = "3";

-- 删除数据的S_entrace这一列并插入S表格的示例数据
-- ALTER TABLE S DROP COLUMN S_entrace;

-- INSERT INTO S(Sno,Sname,Ssex,Sage,Sdept)
-- VALUES ("201215121","李勇","男"," 20","CS");

-- INSERT INTO S(Sno,Sname,Ssex,Sage,Sdept)
-- VALUES ("201215122","刘晨","女","19","CS");

-- INSERT INTO S(Sno,Sname,Ssex,Sage,Sdept)
-- VALUES ("201215123","王敏","女","18","MA");

-- INSERT INTO S(Sno,Sname,Ssex,Sage,Sdept)
-- VALUES ("201215125","张立","男","19","IS");

-- 插入C表的记录(先删除外键)
-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("1","数据库","5","4");

-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("2","数学","","2");

-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("3","信息系统","1","4");

-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("4","操作系统","6","3");

-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("5","数据结构","7","4");

-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("6","数据处理","","2");

-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("7","PASCAL语言","6","4");

-- INSERT INTO C(Cno,Cname,Cpno,Ccredit)
-- VALUES ("","","","");



-- 插入SC表的记录(需要先新建S表和C表)
-- INSERT INTO SC(Sno,Cno,Grade)
-- VALUES("201215121","1","92");

-- INSERT INTO SC(Sno,Cno,Grade)
-- VALUES("201215121","2","85");

-- INSERT INTO SC(Sno,Cno,Grade)
-- VALUES("201215121","3","88");

-- INSERT INTO SC(Sno,Cno,Grade)
-- VALUES("201215122","2","90");

-- INSERT INTO SC(Sno,Cno,Grade)
-- VALUES("201215122","3","90");