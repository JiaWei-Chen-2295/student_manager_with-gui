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
