# 学生管理系统（有界面）

## 项目环境
- python 3.8.1
- PyCharm 2024.1

## 项目功能
1. 实现基本的用户管理，但是具有强的可拓展性。
2. 使用 MySQL 存储专业，班级，学生，用户的信息。
3. 提供对数据库不同表进行操作的模块的包。
4. 用户具有角色属性（管理员，辅导员，学生），不同的角色有不同的权限。
5. 使用 nicegui 库，将 python 代码变为前端展示。

## 项目创建过程
###  表的创建（MySQL数据库）
- 内容：
    - 专业表(专业唯一id,专业名字)
    - 班级表(班级唯一id,班级名称,所属专业)
    - 学生表(学生唯一id(学号),学生名字,学生身份证号(唯一性),所属班级)
    - 用户表(用户唯一id,用户名,密码,角色（只能为:admin,class_manager,student）,班级id,学生id(可空))
- 建表语句

  ```sql
  CREATE TABLE Majors (
      major_id INT AUTO_INCREMENT PRIMARY KEY, -- 专业唯一ID
      major_name VARCHAR(255) NOT NULL -- 专业名字
  );
  
  CREATE TABLE Classes (
      class_id INT AUTO_INCREMENT PRIMARY KEY, -- 班级唯一ID
      class_name VARCHAR(255) NOT NULL, -- 班级名称
      major_id INT,
      FOREIGN KEY (major_id) REFERENCES Majors(major_id) -- 所属专业（外键）
  );
  
  CREATE TABLE Students (
      student_id INT AUTO_INCREMENT PRIMARY KEY, -- 学生唯一ID（学号）
      student_name VARCHAR(255) NOT NULL, -- 学生名字
      student_card_num VARCHAR(18) UNIQUE NOT NULL, -- 学生身份证号（唯一性）
      class_id INT,
      FOREIGN KEY (class_id) REFERENCES Classes(class_id) -- 所属班级（外键）
  );
  
  CREATE TABLE Users (
      user_id INT AUTO_INCREMENT PRIMARY KEY, -- 用户唯一ID
      username VARCHAR(255) NOT NULL, -- 用户名
      password VARCHAR(255) NOT NULL, -- 密码
      role ENUM('admin', 'class_manager', 'student') NOT NULL, -- 角色（只能为:admin,class_manager,student）
      class_id INT,
      student_id INT,
      FOREIGN KEY (class_id) REFERENCES Classes(class_id), -- 班级ID（外键）
      FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE SET NULL -- 学生ID（外键，可空）
  );
  -- 以下使用了 ai 进行数据的捏造
  -- 创建专业
  INSERT INTO Majors (major_name)
  VALUES ('大数据'), ('计算机科学与技术'), ('软件工程');
  
  -- 创建班级，假设每个专业有3个班级
  INSERT INTO Classes (class_name, major_id)
  SELECT CONCAT(m.major_name, '-', LPAD(c.class_number, 2, '0')), m.major_id
  FROM (
      SELECT 1 AS class_number UNION SELECT 2 UNION SELECT 3
  ) AS c
  CROSS JOIN Majors m;
  
  -- 创建学生，假设每个班级有10名学生
  INSERT INTO Students (student_name, student_card_num, class_id)
  WITH student_numbers AS (
      SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) - 1 AS num
      FROM Majors m, Majors m2 -- Just to get more rows
  )
  SELECT CONCAT('学生', s.num), CONCAT('111111111111111', LPAD(s.num, 8, '0')),
         c.class_id
  FROM student_numbers s
  JOIN Classes c ON s.num % 3 = c.class_id % 3 AND s.num < 30 -- 假设总共创建30名学生
  
  -- 创建用户，包括管理员、班级管理员和学生
  -- 假设只有一个管理员，每个班级有一个管理员，所有学生都是用户
  INSERT INTO Users (username, password, role, class_id, student_id)
  VALUES ('admin', 'admin123', 'admin', NULL, NULL); -- 管理员账号
  
  INSERT INTO Users (username, password, role, class_id, student_id)
  SELECT CONCAT('class_manager_', c.class_name), CONCAT('manager', c.class_id), 'class_manager', c.class_id, NULL
  FROM Classes c; -- 班级管理员账号
  
  INSERT INTO Users (username, password, role, class_id, student_id)
  SELECT CONCAT('student_', s.student_id), CONCAT('stu', s.student_id), 'student', s.class_id, s.student_id
  FROM Students s; -- 学生账号
  
  
  ```

  

### Python 连接数据库，并增删改查基类的创建

### 创建专业，班级，学生，用户类

### Python 增删改查不同表的类实现

### 实现具有不同权限的学生班级管理模块
- Functions
  - power model
    
    具有创建，读取，更新，删除资源的所有能力

  - power distribute
  
    1.manager power
        
    具有创建，读取，更新，删除所有资源

    2.instructor power

    读取，更新，以及管理学生信息

    3.student power 
    
    读取自己信息
  - power with character
      
    权限与角色之间分配的多对多的函数关系
  - character examination
    
    检测该角色，从而对应其具有的权限能力
  
  - test

    各种代码段进行测试，验证程序的正确线程.
    
    
  
  
  

### 界面的创建

 

## 项目结构

### 项目中的类

- 专业类（Major）
- 班级类（SchooClass）
- 学生类（Student）
- 数据库连接基类（BaseDao）
- 专业数据库操作类（MajorDao）
- 班级数据库操作类（SchoolClassDao）
- 学生数据库操作类（StudentDao）
- 用户类（User）

## 作者
  - 陈佳玮@2023154202
  - 范宏泰@2023154208
