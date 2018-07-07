from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required()
def IndexView(request):
    print(request.user.is_authenticated())
    return render(request, "polladmin/index.html")


def ProductInfoView(request):
    print("in product info")
    return render(request, "polladmin/productInfo.html")


def Test_changepage(request):
    print("call change")
    return render(request, "changepage/mainpage.html")


def Test_changepage_one(request):
    print("call change one", request.META.get("HTTP_X_PJAX", None))
    return render(request, "changepage/itemonepage.html")


def Test_changepage_two(request):
    print("call change two", request.META.get("HTTP_X_PJAX", None))
    return render(request, "changepage/itemtwopage.html")

def datatable(request):
    return render(request, 'mydatatable.html')


def userInfo(request):
    offset = request.GET.get('offset')
    limit = request.GET.get('limit')
    from users import models
    users = models.GrouperUser.objects.all()
    total = users.count()

    data = []
    for user in users:
        temp = {'username': user.username,
                'employeeID': user.employeeID,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'operate': '<button class="btn btn-info btn-sm" type="button"><a class="fa fa-paste"></a> 详情</button>'}
        data.append(temp)

    import json
    result = {'total': total, 'rows': data[0+int(offset):0+int(offset)+int(limit)]}
    result = {'total': 0, 'rows': []}
    print('in userinfo')
    return HttpResponse(json.dumps(result))