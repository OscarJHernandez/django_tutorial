from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import loader
from .models import Question

# # Create your views here.
# def index(request):
#
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     #output = ','.join([q.question_text for q in latest_question_list])
#
#     context = {
#         'latest_question_list': latest_question_list
#     }
#
#     return HttpResponse(template.render(context,request))


def index(request):
    '''
    Reders the html in a more simple method

    :param request:
    :return:
    '''

    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list
    }

    return render(request,'polls/index.html',context)

#def detail(request,question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question': question})

#
# def detail(request,question_id):
#     try:
#         question = Question.object.get(pk=question_id)
#         context = {
#             'question': question
#         }
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#
#     return render(request,'polls/detail.html',context)

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request,'poll/detail.html', {
            'question': question,
            'error_message': "You didn't make a choice."
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return  HttpResponseRedirect(reverse('polls:results',args=(question_id,)))
