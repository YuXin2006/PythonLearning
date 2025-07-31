from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from poll.models import Question,Choice
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.views.generic import *
# Create your views here.
def index(request):
    template=loader.get_template("poll/index.html")
    latest_questions=Question.objects.order_by("-pub_date")[:5]
    #return HttpResponse("-".join(str(question.text) for question in top_two_question))
    context={"latest_questions_list":latest_questions}
    return HttpResponse(template.render(context,request))
def detail(request, question_id):
    #try:
        #question=Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:  
        #raise Http404("question is not found,id is invalid")
    question=get_object_or_404(Question,pk=question_id)
    context={"question":question}
    return render(request,"poll/detail.html",context)
    


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "poll/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,"poll/detail.html", {"question": question,"error_message": "You didn't select a choice.",})
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("poll:results", args=(question.id,)))
#--------------generic views - class based view------------
class IndexView(ListView):
    template_name = "poll/index.html"
    context_object_name ="latest_questions_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
class QDetailView(DetailView):
    model = Question
    template_name = "poll/detail.html"


class QResultsView(DetailView):
    model = Question
    template_name = "poll/results.html"    
    