from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.encoding import escape_uri_path
from django.http import StreamingHttpResponse

from . import models


# Create your views here.

class IndexView(generic.ListView):
    template_name = "poll/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        '''返回最近时间的五个问题'''
        return models.Question.objects.order_by("-pub_date")[:5]

def mobileDesign(request):
    return render(request, 'mobile_design_sui.html')


def GenerateQRCode(request,pid):
    '''生成二维码并显示在网页上'''
    import qrcode
    from django.utils.six import BytesIO
    print("pid"+"-----------"+pid)
    img = qrcode.make("http://www.baidu.com")
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    # response = HttpResponse(image_stream, content_type='image/png')
    # #
    # # response = HttpResponse(mimetype='image/png')
    file = "中文.png"
    response = HttpResponse(image_stream)
    response['Content-Type'] = 'application/image'
    response['Content-Disposition'] = "attachment; filename*=utf-8''{0}".format(escape_uri_path(file))
    # response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file)
    return response



class DetailView(generic.DetailView):
    model = models.Question
    template_name = "poll/detail.html"


class ResultsView(generic.DetailView):
    model = models.Question
    template_name = "poll/results.html"


@login_required(login_url='/')
def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST.get("choice"))
    except (KeyError, models.Choice.DoesNotExist):
        return render(request, "poll/detail.html", {
            "question": question,
            "error_message": "you didn't select a choice!"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse("poll:results", kwargs={"pk": question_id, }))

def homepage(request):
    if not request.user.is_authenticated():
        return HttpResponse("not login")
    return render(request, "index.html")

def search_box(request):
    return render(request, "searchbox.html", {"test": "test"})


def vertical_timeline(request):
    return render(request, "search_result_demo.html")


def btn_down(request):
    return render(request, "btn_down.html")

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_image(request):
    path = request.get_full_path()
    if request.method == "POST" and path.find("delete") != -1:
        import re
        p = re.compile("delete-(\d+)")
        img_id = int(p.findall(path)[0])
        try:
            models.MyImage.objects.filter(id=img_id).delete()
        except Exception as e:
            pass

        result = {
            "status": "OK"
        }
        import json
        return HttpResponse(json.dumps(result))
    elif request.method == "POST" and path.find("delete") == -1:
        img = models.MyImage(img=request.FILES.get("img"))
        img.save()
        result = {
            "status": "OK"
        }
        import json
        return HttpResponse(json.dumps(result))
    if request.method == "GET":
        imgs = models.MyImage.objects.all().first()
        context = {
            "imgs": imgs
        }
        return render(request, "upload2.html", context)

@csrf_exempt
def show_img(request):
    # imgs = models.MyImage.objects.all()
    # context = {
    #     "imgs": imgs
    # }
    # return render(request, "showImg.html", context)
    return render(request, "upload3.html")


def test_url(request):
    print(request.body)
    return HttpResponse("ok")