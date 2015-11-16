开始项目：
在cmd或者terminal的当中输入
    python django-admin.py startporject project_name
    #django-admin路径
        强装：
            python python27/lib/site-package/django/bin/django-admin.py startproject project_name
        正装：
            python python27/scripts/django-admin.py startporject project_name
    #项目路径
        就是cmd或者terminal的当前路径
运行django服务器：
    1、django可以和市面上主流的http服务器契合使用但是在开发的过程当中我们习惯使用
    django自带的轻量级服务器
    2、django自带的轻量级服务器的启动命令
        python manage.py runserver
            1、你运行哪一个项目就对那个项目的manage.py执行runserver命令
            2、注意manage.py的路径
            3、在1.5版本左右，django在运行之后不会自动生成sqlite3数据库，但是
            1.7.1可以用生成。
        python manage.py runserver 9000 默认更换端口号

        python manage.py runserver 0.0.0.0:9000 默认更换端口号
常用术语
    response 应答
    request 请求

第一个views
views 部分
from django.http import HttpResponse 从django下的http下导入HttpResponse功能

def hello(request): 定义一个函数，该函数需要接受请求，也就是参数request
    return HttpResponse('hello world') 当接到请求以后进行响应，响应内容是hello world

urls 部分
    (r'hello',hello)
    前面部分是URL上要匹配的内容，后面部分是匹配成功以后要请求的views函数
#模板配置：
TEMPLATE_DIRS是用来指出项目当中的静态模板存放路径的配置，里面需要跟一个
绝对路径
    #1、我们在本地可以这么干:
TEMPLATE_DIRS = (
    'F:\python_django_job\2\2015.10.12\mybook\mybook\template',
)
    #2、django的路径是和Linux上一样的所以路径‘\’必须都变成‘/’,也就是说:
TEMPLATE_DIRS = (
    'F:/python_django_job/2/2015.10.12/mybook/mybook/template',
) 我们需要改成这样
    #3、但是我们如果按照上面写绝对路径会影响我们项目的可移植性
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__),'template').replace('\\','/'),
)

#django shell
    python manage.py shell

#加载外部文件
from django.http import HttpResponse #导入一个http应答
from django.template.loader import get_template #导入加载外部模板的功能
from django.template import Context #导入传值功能

def index(request):
    tem = get_template('index.html') #加载外部文件index.html
    content = Context({'name':'laobian'}) #编译要传的值
    return HttpResponse(tem.render(content)) #进行响应






