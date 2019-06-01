-- 1．查询选修 1 号课程的学生学号与姓名。 

-- SELECT SC.Sno,Sname
-- FROM S,SC
-- WHERE SC.Sno = S.Sno AND SC.Cno = "1";


-- 2．查询选修课程名为数据结构的学生学号与姓名。

-- SELECT S.Sno,Sname
-- FROM S,SC,C
-- WHERE C.Cno = SC.Cno AND C.Cname = "数据结构" AND S.Sno = SC.Sno;


-- 3．查询不选 1 号课程的学生学号与姓名

-- SELECT Sno,Sname
-- FROM S
-- WHERE Sno Not IN(
--     SELECT S.Sno
--     FROM S,SC
--     WHERE S.Sno = SC.Sno AND SC.Cno = "1"
-- );

-- 4．查询学习全部课程学生姓名。

-- SELECT Sname
-- FROM S
-- WHERE Sno IN(
--     SELECT Sno
--     FROM SC
--     GROUP BY Sno
--     HAVING COUNT(*) = (
--         SELECT COUNT(*)
--         FROM C
--     )
-- );

-- 5．查询所有学生除了选修 1 号课程外所有成绩均及格的学生的学号和平均成绩，其结果按平均成绩的降序排列
-- SELECT Sno,AVG(Grade)
-- FROM SC
-- WHERE SC.Sno In (
--     SELECT Sno
--     FROM SC
--     WHERE Cno = "1"  
-- )
-- GROUP BY Sno
-- HAVING MIN(Grade) > 60
-- ORDER BY AVG(Grade) DESC;  --ASC升序,DESC降序


-- 6．查询选修数据库原理成绩第 2 名的学生姓名。 
-- SELECT Sname
-- FROM S,SC,C
-- WHERE S.Sno = SC.Sno AND SC.Cno = C.Cno AND C.Cname = "数据库原理" AND SC.Grade = (
--      SELECT MAX(Grade)
--      FROM SC,C
--      WHERE SC.Cno = C.Cno AND C.Cname = "数据库原理" AND SC.Grade < MAX(Grade)
--      GROUP BY Cname
-- );



-- 7. 查询所有 3 个学分课程中有 3 门以上（含 3 门）课程获 80 分以上（含 80 分）的学生的姓名。 
-- 8. 查询选课门数唯一的学生的学号。 
-- 9．SELECT 语句中各种查询条件的实验