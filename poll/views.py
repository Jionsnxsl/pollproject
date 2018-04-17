from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from . import models


# Create your views here.

class IndexView(generic.ListView):
    template_name = "poll/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        '''返回最近时间的五个问题'''
        return models.Question.objects.order_by("-pub_date")[:5]


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
    return render(request, "index.html")

def search_box(request):
    return render(request, "searchbox.html", {"test": "test"})


def vertical_timeline(request):
    return render(request, "vertical_timeline.html")


def btn_down(request):
    return render(request, "btn_down.html")