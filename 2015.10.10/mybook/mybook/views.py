#coding:gbk
from django.http import HttpResponse

import time

def hello(request):
    return HttpResponse('hello world')
def times(request):
    ctimes = time.ctime()
    html = '''
    <html>
        <head>
            <title>
                hello world
            </title>
        </head>
        <body>
            %s
        </body>
    </html>
    '''
    return HttpResponse(html%ctimes)
def d_time(request,number):
    number = int(number)
    num = time.ctime(time.time()+3600*number)
    html = '''
    <html>
        <head>
            <title>
                hello world
            </title>
        </head>
        <body>
            再过%s个小时是%s
        </body>
    </html>
    '''
    return HttpResponse(html%(number,num))
def hi(request):
    content = '''
    《炼金术士》全集

作者： 离狂

声明:本书由选书网(www.xuanshu.com)自网络收集整理制作,仅供交流学习使用,版权归原作者和出版社所有,如果喜欢,请支持正版.

第0章 1 术士

“前一阵我跟人出海，在一处荒岛边上驻扎，当时我正在解手，突然跳过来一只青蛙，它对我说，你和人赌钱下大就能赢，当时其他人都没注意到，我有些发愣，也没怎么在意。后来晚上和人赌钱，果然，下大一直都在赢，当天晚上我赢了一大笔钱。第二天我找到了那只青蛙，它又对我说，今天晚上你下小就能赢，我深信不疑，结果又赢了一大笔钱，接下来我发财了，所以我就把它带了回来。但就在不久前，它突然变成了一个非常漂亮的美女，她说非常感谢我把它带离了那座岛，所以要好好报答我，要一辈子和我开开心心的在一起，可是我没有答应，因为我挂念着你。老婆，我说的都是真的啊，身边这个女孩就是这么来的，你不要打我啊。”

一名醉醺醺的酒客拉着旁边女子的手，紧紧抓着，不肯松开，引发了旁边群众的一片哄笑。

那名女子非常无奈，抬起手掌，狠狠的拍了那名酒客一下：“死鬼，你看看你旁边那人是谁！”

酒客抬头一看，身旁一张满是络绎胡的粗犷面孔正朝他傻呵呵笑着，表情有些茫然：“哎，你怎么长胡子了……”

酒馆里又是一阵轰然大笑，声浪如潮，蔓延了这片空间。

在这沸然笑声中，正向盘子里摆放东西的文森抬头看了一眼，附和着弯弯嘴角，低下眼眸，继续着自己的事情。

事情的结尾终究在酒客被他妻子拖走作为终章，闹剧结束，半分钟后，文森的眉角跳动一下，和厨师打了招呼，端着盘子，从柜台后面走出。

这里是一家名为皮普的小酒馆，地处海边的望洋港口，装修陈黄，泛着岁月浸透的陈旧味，酒类价格低廉，颇受欢迎。

由于生意很不错，狭小的空间里有了太多的人，空气显得嘈杂闷热，水手身上的汗臭味混合着酒味的芬芳，混杂出了一股奇怪的味道。

嗅着这已经习惯了的怪味，文森行走在人群中间，匆匆将酒液放在不同的桌上，旋即快步离开，周而复始着这个过程。

他是这家酒馆的侍从，而这就是他的工作。

“转眼之间，来到这个世界，已经十四年了啊。”

将最后一杯琥珀色的酒液放在桌上，文森的嘴角扬起，抬头扫过眼前的酒客，内心隐隐有些感慨。

前世的一切皆是浮云，不做他想，穿越到这个世界十几年以来，人生重来，他只是想活的更加精彩。

这里，是一个浩瀚而神秘的宏伟世界。


    '''
    return HttpResponse(content)