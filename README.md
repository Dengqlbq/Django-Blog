# Django-Blog

此项目是一个简易博客系统
====
Powered by python 3.5 and django 1.10
---
实现功能：<br>

	1：文章归档
  	2：文章分类
  	3：添加标签
  	4：添加评论
  	5：分页显示
 
项目主要结构：<br>
--- 
  >mycode/<br>
  >manage.py<br>
  >blog/<br>
  >> __init__.py<br>
  >> admin.py<br>
  >> apps.py<br>
  >> forms.py<br>
  >> models.py       ---模型<br>
  >> tests.py<br>
  >> urls.py         ---url解析<br>
  >> views.py        ---视图函数<br>
  >> static/         ---存放hmtl相关静态文件<br>
  >>templates/      ---html文件<br>
  
---                    
 项目运行方式<br>

1. fork 本项目到你的仓库
2. 克隆你的仓库到本地
3. 命令行执行 pip install -r requirements.txt（注意在 requirements.txt 所在目录下执行，否则请输入完整路径名）安装依赖包
4. 迁移数据库，在 manage.py 所在目录执行

        python manage.py makemigrations
        python manage.py migrate

5. 类似步骤4，运行命令创建超级用户

        python manage.py createsuperuser

6. 类似步骤4、5，在 manage.py 所在目录执行

        python manage.py runserver

7. 浏览器输入 http://127.0.0.1:8000/blog
    
8. 注：本项目的db.sqlite3文件为原有数据库文件，可直接使用，则可以跳过第4,5步

 	  	username : haha
	   password : wode1234
  


