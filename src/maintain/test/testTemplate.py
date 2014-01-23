# -*- coding:utf-8 -*-

from django.template import Template,Context

#设置在django在admin后天显示的名称

t=Template("my name is {{name}}")
c=Context({"name":"wangkui"})
print t.render(c)


person={"name":"kuiwang","age":25}
t=Template("my name is {{p.name}} and age is {{p.age}}")
c=Context({"p":person})
print t.render(c)