# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
 
# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        s = request.GET['q']
        message = '你搜索的内容为: ' + s.decode('gbk','ignore').encode('gb18030')
    else:
        message = '你提交了空表单'
    return HttpResponse(message)