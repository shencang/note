# SQL

## 未分类

### 1.在关系数据库设计中，关系模式是用来记录用户数据的（  ）

* 二维表

```t
在关系数据库中用关系模型来表示数据结构，表示为一个二维表，一个关系就是一个二维表
```

### 2.运动会比赛信息的数据库，有如下三个表

```t
运动员ATHLETE（运动员编号 Ano，姓名Aname，性别Asex，所属系名 Adep）， 项目 ITEM （项目编号Ino，名称Iname，比赛地点Ilocation）， 成绩SCORE （运动员编号Ano，项目编号Ino，积分Score）。
写出目前总积分最高的系名及其积分，SQL语句实现正确的是：（      ）
```

```sql
SELECT Adep,SUM(Score)FROM ATHLETE,SCORE  WHERE ATHLETE.Ano=SCORE.Ano GROUP BY Adep  HAVING SUM(Score)>=ALL

(SELECT SUM(Score) FROM ATHLETE,SCORE  WHERE ATHLETE.Ano=SCORE.Ano GROUP BY Adep)
```
