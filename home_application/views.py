# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json
from common.log import logger
from app_control.decorators import  function_check
from app_control.models import  Function_controller


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


# def redis_online(request):
#     """
#     线上redis-查询
#     """
#     return render_mako_context(request, '/home_application/redis-online.html')







