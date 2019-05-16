/*CREATE DATABASE DBLEARN;*/

CREATE TABLE S(
    Sno VARCHAR(20) PRIMARY KEY,    /*列级完整约束条件，Sno是主码*/
    Sname VARCHAR(20) ,             /*Sname不去唯一值(和书上P82不一样)*/
    Ssex VARCHAR(2),
    Sage SMALLINT,
    Sdept VARCHAR(20)
);



CREATE TABLE C(
    Cno VARCHAR(4) PRIMARY KEY, /*列级完整约束条件，Cno是主码*/
    Cname VARCHAR(20) NOT NULL, /*列级完整性约束条件，Cname不能取空值*/
    Cpno VARCHAR(4),
    Ccredit FLOAT,
    FOREIGN KEY(Cpno) REFERENCES C(Cno)
    /*表级完整性约束条件，Cpno是外码，被参照表是C，被参照列是Cno*/
);

CREATE TABLE SC(
    Sno VARCHAR(20),
    Cno VARCHAR(4),
    Grade SMALLINT,
    FOREIGN KEY (Sno) REFERENCES S(Sno),
    /*表级完整性约束条件，Sno是外码，被参照表是S，被参照列是Sno*/
    FOREIGN KEY (Cno) REFERENCES C(Cno)
    /*表级完整性约束条件，Cno是外码，被参照表是C，被参照列是Cno*/
);


-- DROP TABLE SC RESTRICT;
-- DROP TABLE S CASCADE;
-- DROP TABLE C CASCADE