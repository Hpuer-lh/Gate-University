# Gate University

这是一个基于 Flask 和 Django 的大学管理系统项目。

## 项目结构

- `app.py` - Flask 应用主文件
- `models.py` - 数据库模型定义
- `config.py` - Flask 配置文件
- `route/` - Flask 路由目录
  - `student.py` - 学生路由
  - `dormitory.py` - 宿舍路由
  - `academic.py` - 学术路由
  - `financial.py` - 财务路由
  - `admin.py` - 管理员路由
- `templates/` - HTML 模板目录
- `requirements.txt` - 项目依赖文件

## 安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/Hpuer-lh/Gate-University.git
   cd Gate_University

2. 创建虚拟环境并激活：
   ```bash
   python -m venv venv
   source venv/bin/activate  # 对于 Windows 系统，使用 `venv\Scripts\activate`
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 运行

1. 运行 Django 服务器：
    使用以下命令初始化数据库迁移环境并应用迁移：
    flask db init
    flask db migrate
    **会生成一个migrate文件夹，需要配置一些信息**
    flask db upgrade

2. 运行 Flask 应用：
   使用Django的管理命令启动开发服务器：
   ```bash
   python app.py
   ```
   访问本地服务器查看应用程序。
3. 初次使用
   通过浏览器访问应用对应的 register 路由对应的页面（通常在浏览器地址栏输入类似 http://localhost:5000/register，假设应用在本地以默认端口 5000 运行且未做额外的域名配置等情况），此时会加载 register.html 模板来展示注册页面。

   如果你是第一次使用，则**注册的用户名必须为“root”**，“学生ID”栏随便填写，以确保你有一个能进入网页的账号，否则你将无法使用该系统。




## 功能

- 用户注册和登录
- 验证码功能
- 学生信息管理
- 宿舍管理
- 进出记录管理
- 课程管理
- 实验时间管理
- 选课管理
- 财务管理
- 管理员功能

## 贡献

欢迎提交问题和拉取请求来改进此项目。