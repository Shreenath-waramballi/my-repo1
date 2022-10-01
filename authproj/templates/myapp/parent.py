from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
def emp_data_view(request):
    emp_data={'eno':100,'ename':'Shreenath','esal':60000}
    response='<h1>Employee Num:{}<br> Employee Name:{} 
<br> Employee Sal:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'])
    return HttpResponse(response)
def emp_json_data_view1(request):
    emp_data={'eno':200,'ename':'Shreya','esal':70000}
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')
def emp_json_data_view2(request):
    emp_data={'eno':300,'ename':'Shreeram','esal':80000}
    return JsonResponse(emp_data)