# 学生管理系统（有界面）

## 项目地址
https://github.com/JiaWei-Chen-2295/student_manager_with-gui

## 项目环境
- python 3.8.1
- PyCharm 2024.1
- 库详见本目录下的 requirements.txt

## 运行本项目

1. 首先确保你的 python 版本为 3.8.x 否则项目无法正常运行

2. 使用以下命令安装 requirements.txt 中的库

   ```shell
   pip install -r requirements.txt
   ```

3. 安装 mysql 数据库（云端已有请忽略）

4. 按照文档下方的建表语句进行建表

5. 如果你的项目根目录下无 test_config 目录请自行添加，并在目录中新建  DBconnInfo.yml ，格式如下

   ```
     host: mysql服务器地址（127.0.0，1）
     port: 3306
     username: username
     database: databasename
     password: password
   ```

6. 运行 NewStar/start/main.py

7. 如果没有反应，请尝试浏览器地址栏输入 [新建标签页](http://127.0.0.1:8080/)

8. 登录账号密码

   ```
   账号：admin
   密码：adminPass
   ```

9. 登录成功后浏览器不会关闭，但会弹出主界面窗口，请留意状态栏

## 项目功能

1. 实现基本的用户管理，并具有强的可拓展性。
2. 使用 MySQL 存储专业，班级，学生，用户的信息。
3. 提供对数据库不同表进行操作的模块的包。
4. 用户具有角色属性（管理员，辅导员，学生），不同的角色有不同的权限。
5. 使用 nicegui 库，将 python 代码变为前端展示。
6. 使用 pyqt5 展示主界面

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
