# Django-Blog

此项目是一个简易博客系统
====
Powered by python 3.5 and django 1.10
---
实现功能：<br>

  1：文章归档<br>
  2：文章分类<br>
  3：添加标签<br>
  4：添加评论<br>
  5：分页显示<br>
 
项目主要结构：
--- 
  blog/<br>
      __init__.py<br>
      admin.py<br>
      apps.py<br>
      forms.py
      models.py       ---模型<br>
      tests.py<br>
      urls.py         ---url解析<br>
      views.py        ---视图函数<br>
      static/         ---存放hmtl相关静态文件<br>
            blog/<br>
                 css/<br>
                 img/<br>
                 js/<br>
      templates/     ---html文件<br>
                base.html<br>
                base2.html<br>
                blog/<br>
   mycode/<br>
   manage.py<br>
---                    
 项目运行方式<br>
 
 1：<br>
  (1) 下载项目文件到你的电脑<br>
  (2) cd到manage.py所在文件夹<br>
  (3) 执行以下cmd命令 ：python manage.py makemigrations<br>
                      python manage.py migrate<br>
                      python manage.py createsuperuser<br>
  (4) 运行python manage.py runserver<br>
  (5) 127.0.0.1:8000/blog  到博客首页<br>
  (6) 127.0.0.1:8000/admin 到博客后台<br>
             
  注：本项目的db.sqlite3文件为原有数据库文件，可直接使用，则可以跳过第3步<br>
     username : haha<br>
     password : wode1234<br>
 --- 
  2:<br>
    (1) fork 本项目到你的仓库<br>
    (2) 克隆你的仓库到本地<br>
    (3) 命令行执行 pip install -r requirements.txt（注意在 requirements.txt 所在目录下执行，否则请输入完整路径名）安装依赖包<br>
    (4) cd到manage.py所在文件夹<br>
    (5) 执行以下cmd命令 ：python manage.py makemigrations<br>
                        python manage.py migrate<br>
                        python manage.py createsuperuser<br>
    (6) 运行python manage.py runserver<br>
    (7) 127.0.0.1:8000/blog  到博客首页<br>
    (8) 127.0.0.1:8000/admin 到博客后台<br>
    
    注：本项目的db.sqlite3文件为原有数据库文件，可直接使用，则可以跳过第5步<br>
       username : haha<br>
       password : wode1234<br>
  


