from django import template
import datetime
register = template.Library()

def cut(value,arg):
    return value.replace(arg,'')

def lower(value):
    return value.lower()

register.filter('replace',cut)
register.filter('lower',lower)

def do_something(perser,token):
    try:
        tag_name,format = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format[1:-1])

class CurrentTimeNode(template.Node):
    def __init__(self,format_string):
        self.format_string = str(format_string)
    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)


def do_thing(perser,token):
    try:
        tag_name,format = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimes(format[1:-1])

class CurrentTimes(template.Node):
    def __init__(self,format_string):
        self.format_string = str(format_string)
    def render(self, context):
        now = datetime.datetime.now()
        context['current_time'] = now.strftime(self.format_string)
        return ''
register.tag('hello',do_something)
register.tag('hei',do_thing)

import re

class CurrentTimeNode3(template.Node):
    def __init__(self, format_string, var_name):
        self.format_string = str(format_string)
        self.var_name = var_name

    def render(self, context):
        now = datetime.datetime.now()
        context[self.var_name] = now.strftime(self.format_string)
        return ''

def do_current_time(parser, token):

    try:
        tag_name, arg = token.contents.split(None,1)
    except ValueError:
        msg = '%r tag requires arguments' % token.contents[0]
        raise template.TemplateSyntaxError(msg)

    m = re.search(r'(.*?) as (\w+)', arg)
    if m:
        fmt,var_name = m.groups()
    else:
        msg = '%r tag had invalid arguments' % tag_name
        raise template.TemplateSyntaxError(msg)

    if not (fmt[0] == fmt[-1] and fmt[0] in ('"', "'")):
        msg = "%r tag's argument should be in quotes" % tag_name
        raise template.TemplateSyntaxError(msg)

    return CurrentTimeNode3(fmt[1:-1], var_name)


def do_comment(parser, token):
    nodelist = parser.parse(('endnice',))
    parser.delete_first_token()
    return CommentNode()

class CommentNode(template.Node):
    def render(self, context):
        return 'HELLO'

def do_upper(parser, token):
    nodelist = parser.parse(('endupper',))
    parser.delete_first_token()
    return UpperNode(nodelist)

class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()

def current_time(format_string):
    try:
        return datetime.datetime.now().strftime(str(format_string))
    except UnicodeEncodeError:
        return ''

def ll(format_string):
    return format_string.upper()

register.simple_tag(ll)
register.simple_tag(current_time)


register.tag('upper',do_upper)
register.tag('nice',do_comment)
register.tag('hi',do_current_time)

from mybook.temps.models import *

def books_for_author(author):
    books = Persion.objects.filter(gender = author.id)
    return {'books': books}
register.inclusion_tag('persion.html')(books_for_author)









