# Django-Blog

此项目是一个简易博客系统

Powered by python 3.5 and django 1.10

实现功能：

  1：文章归档
  2：文章分类
  3：添加标签
  4：添加评论
  5：分页显示
 
项目主要结构：
 
  blog/
      __init__.py
      admin.py
      apps.py
      forms.py
      models.py       ---模型
      tests.py
      urls.py         ---url解析
      views.py        ---视图函数
      static/         ---存放hmtl相关静态文件
            blog/
                 css/
                 img/
                 js/
      templates/     ---html文件
                base.html
                base2.html
                blog/
   mycode/
   manage.py
                    
 项目运行方式
 
 1：
  (1) 下载项目文件到你的电脑
  (2) cd到manage.py所在文件夹
  (3) 执行以下cmd命令 ：python manage.py makemigrations
                      python manage.py migrate
                      python manage.py createsuperuser
  (4) 运行python manage.py runserver
  (5) 127.0.0.1:8000/blog  到博客首页
  (6) 127.0.0.1:8000/admin 到博客后台
             
  注：本项目的db.sqlite3文件为原有数据库文件，可直接使用，则可以跳过第3步
     username : haha
     password : wode1234
  
  2:
    (1) fork 本项目到你的仓库
    (2) 克隆你的仓库到本地
    (3) 命令行执行 pip install -r requirements.txt（注意在 requirements.txt 所在目录下执行，否则请输入完整路径名）安装依赖包
    (4) cd到manage.py所在文件夹
    (5) 执行以下cmd命令 ：python manage.py makemigrations
                        python manage.py migrate
                        python manage.py createsuperuser
    (6) 运行python manage.py runserver
    (7) 127.0.0.1:8000/blog  到博客首页
    (8) 127.0.0.1:8000/admin 到博客后台
    
    注：本项目的db.sqlite3文件为原有数据库文件，可直接使用，则可以跳过第5步
       username : haha
       password : wode1234
  


