# -*- coding:utf-8 -*-
from hostinfo.models import Host, HostGroup
from django.contrib import admin
#设置在django在admin后天显示的名称
class HostAdmin(admin.ModelAdmin):
    list_display = ['vendor',
        'sn',
        'product',
        'cpu_model',
        'cpu_num',
        'cpu_vendor',
        'memory_part_number',
        'memory_manufacturer',
        'memory_size',
        'device_model',
        'device_version',
        'device_sn',
        'device_size',
        'osver',
        'hostname',
        'os_release'
        ]
#在django后台amdin显示的组名称
class HostGroupAdmin(admin.ModelAdmin):
    list_display = ['name', ]
#将如上两个类的数据展示到django的后台
admin.site.register(HostGroup, HostGroupAdmin)
admin.site.register(Host, HostAdmin)
