from django.shortcuts import render
from django.template.response import TemplateResponse
# Create your views here.


def IndexView(request):
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