# ToDoList后端
  * 第一个前后端都是自己开发的项目
  * 通过这个文档记录一下django的学习过程
  * 接口

## django学习过程
### 安装
本次开发环境在mac上
* django
mac自带的python是2.x版本,所以我先用[brew](https://brew.sh/index_zh-cn.html/ "brew")安装了python3
```
brew install python3
sudo vi ~/.bash_profile  // 然后配一下环境变量

PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
export PATH
// 记得安装的时候好像自动帮你配好了,可以检查一下

source ~/.bash_profile   // 一定要更新一下啊

pip3 install Django      // 安装django,注意使用pip3,不然会先去python2.x里找pip

django-admin startproject firstproject   // 新建一个项目
django-admin startapp firstapp           // 在项目目录下创建一个应用,需要在settings.py的INSTALLED_APPS里注册'firstapp'

python3 manage.py makemigrations
python3 manage.py migrate                // 执行这两句可以依据models.py中编辑的类来自动生成数据库,但不推荐

python3 manage.py inspectdb > ToDoList/models.py    //推荐自己用sql语句生成数据库之后执行这句来自动生成models.py

python3 manage.py runserver              // 启动本地测试服务
```
* 连接数据库及增删改查
本次项目中我用了mysql来作为数据库,需要安装pymysql来连接,同样用pip安装
```
pip3 install PyMySql

// __init__.py
import pymysql 
pymysql.install_as_MySQLdb()

// settings.py
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',  # mysql数据库引擎
    'NAME': 'todo',  # 数据库名字
    'USER': 'root',  # 用户名
    'PASSWORD': '?GC1>AuMQf)o',  # 密码
    'HOST': 'localhost',  # 主机
    'PORT': '3306'  # 端口
  }
}
// 增删改查方法看文档或其他博文(懒
```
* 写成接口
1. 跨域问题django-cors-headers百度一下.
2. post报错@csrf_exempt修饰器

## 接口
###### 接口功能
> 获取所有标签

###### URL
> /lag/get/

###### HTTP请求方式
> GET

###### 请求参数
> 无

###### 返回字段
> |返回字段|字段类型|说明         |
|:-----   |:------|:--------  |
|id       |int    | id        |
|name     |string | 标签名     |
|color    |string | 标签颜色   |

###### 接口功能
> 创建新标签

###### URL
> /lag/create/

###### HTTP请求方式
> POST

###### 请求参数
> |参数|必选|类型|说明|
|:-----  |:-------|:-----|-----                               |
|name    |是      |string | 标签名                           |
|color   |是      |string | 标签颜色                         |

###### 返回字段
> |返回字段|字段类型|说明                              |
|:-----   |:------|:-----------------------------   |
|id       |int    | id                              |
|name     |string | 标签名                           |
|color    |string | 标签颜色                         |

###### 接口功能
> 获取日历上所有日期的标签类型及数量

###### URL
> article/get_calendar/

###### HTTP请求方式
> GET

###### 请求参数
> |参数|必选|类型|说明|
|:-----        |:-------|:-----|-----                               |
|first_unix    |是      |string | 日历的[0][0]位置的时间戳            |

###### 返回字段
> 日,有空再写接口文档,脑子痛


