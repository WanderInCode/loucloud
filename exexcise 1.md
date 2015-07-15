# 仿OpenStack开发云计算管理软件 
##第一周
------
###1.技术架构
整个项目的上层为Flask web框架，中间层的接口为Flask-SqlAlchemy以及Libvirt API，底层为mysql数据库和QEMU虚拟化。
------
###2.开发环境搭建
```
sudo apt-get install python-virtualenv mysql-server
# 安装虚拟化组件
sudo apt-get install qemu libvirt-bin python-libvirt
# 启动 libvirt-bin 服务
sudo service libvirt-bin start
# 查看 libvirt-bin 服务状态
sudo service libvirt-bin status
# 查看当前虚拟机列表，具体可使用virsh --help 帮助命令
sudo virsh list
```
创建loucloud的代码框架
```
cd /home/shiyanlou/Code/shiyanlou_cs354
touch manage.py
mkdir loucloud
cd loucloud
mkdir user static templates
touch __init__.py config.py app.py extension.py
cd user
touch __init__.py views.py
cd ../../
```
|-- README.md
|-- loucloud
|   |-- __init__.py
|   |-- app.py
|   |-- config.py
|   |-- extension.py
|   |-- static
|   |-- templates
|   |-- user
|       |-- __init__.py
|       |-- views.py
|-- manage.py
其中
>1.manage.py 提供了测试和初始化命令；
>2.loucloud 模块为核心代码；
>3.loucloud/user 模块提供用户登陆认证及用户管理等基本操作；
>4.loucloud/static 与 loucloud/templates 用来存放界面实现所需的静态文件以及 jinja2 模板；
>5.loucloud/app.py loucloud/init.py 及loucloud/config.py 用于初始化和部署Flask 应用；
>6.loucloud/extension.py 用来初始化和配置 Flask 的扩展，例如 Flask-Login 等；

------
###3.Flask相关扩展及激活virtualenv
>1.Flask：Flask 框架基础包
>2.Flask-SQLAlchemy：在 Flask 中使用的 SQLALchemy ORM，用于数据库操作；
>3.Flask-WTF：页面表单扩展；
>4.Flask-Cache：缓存扩展；
>5.Flask-Login：用户登陆认证及会话管理组件；
>6.Flask-Script：Flask 的脚本支持，例如 manage.py 这类启动和管理脚本；

创建requirement.txt文件，
```
touch requirement.txt
vim requirement.txt
```

输入以下内容，每个包占一行
flask
flask-sqlalchemy
flask-wtf
flask-cache
flask-login
flask-script
paramiko
mysql-python
libvirt-python

>1.paramiko：SSH链接管理组件；
>2.mysql-python：MySQL链接管理；
>3.libvirt-python：Libvirt 虚拟化管理组件

```
cd /home/shiyanlou/Code/shiyanlou_cs354
# 初始化虚拟环境venv
virtualenv venv
# 进入virtualenv venv
source venv/bin/activate
pip install -r requirement.txt
```
之后提交
```
cd /home/shiyanlou/Code/shiyanlou_cs354
# 查看当前文件修改的列表
git status
touch .gitignore
echo "venv" >> .gitignore
# commit
git add *
git commit -m 'first commit of loucloud'
# push到git.shiyanlou.com远程仓库
git push origin master
```
