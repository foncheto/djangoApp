from django.shortcuts import render, get_object_or_404
from django import http

from .models import Question, Choice


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = "polls/index.html"
    context = {"latest_question_list": latest_question_list}
    return render(request, template, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice_pk = request.POST["choice"]
        selected_choice = question.choice_set.get(pk=selected_choice_pk)
    except:
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "No choice selected."},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return http.HttpResponseRedirect("/polls/%s/results/" % question_id)
