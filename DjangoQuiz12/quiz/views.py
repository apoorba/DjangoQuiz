from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from quiz.models import Question, Score
from pprint import pprint


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # def categories(self):
    #     dst_cat = Question.objects.values_list('category').distinct()
    #     return dst_cat
    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['categories'] = Question.objects.values_list('category').distinct()
        return context


def index(request):
    # return HttpResponse('HELLO from INDEX')
    # current_user = request.user.id
    # Score.objects.filter(user_id=current_user).delete()
    dst_cat = Question.objects.values_list('category').distinct()
    # pprint(dst_cat)
    context = {'dcat': dst_cat}
    return render(request, 'quiz/index.html', context)


@login_required(login_url='/accounts/login/')
def playquiz(request):
    # return HttpResponse('in play quiz')
    param = request.GET.get('category')
    # pprint(param)
    single_question = Question.objects.filter(category=param)[:1]
    categories = Question.objects.values_list('category').distinct()
    # pprint(single_question)
    context = {'sq': single_question, 'categories': categories}
    return render(request, 'quiz/play-quiz.html', context)


def playquiznext(request):
    # return HttpResponse('in play quiz next')
    user_choice = request.POST.get('choice1')
    user_taken_time = request.POST.get('userTakenTime')
    print('*****************TIME*******************')
    print('Time = '+user_taken_time)
    qid = request.POST.get('question')
    correct_answer = request.POST.get('answer')
    if user_choice == correct_answer:
        # output = "CORRECT"
        s = Score(question_id=qid, score=5, user_id=request.user.id)
        s.save()
    else:
        # output = "WRONG"
        s = Score(question_id=qid, score=0, user_id=request.user.id)
        s.save()

    question_already_played = Score.objects.values_list('question')
    # pprint(question_already_played)
    question_not_played = Question.objects.filter(category='Physics').exclude(id__in=question_already_played)[:1]
    # pprint(question_not_played)
    # return HttpResponse('PLAY QUIZ NEXT')
    if question_not_played:
        context = {'sq': question_not_played}
        return render(request, 'quiz/play-quiz.html', context)
    else:
        scores = Score.objects.all()
        total = sum([sc.score for sc in scores])
        context = {'score': scores, 'total': total}
        return render(request, 'quiz/result.html', context)
    # pprint(user_choice)


class QuestionList(generic.ListView):
    model = Question
    # queryset = Question.objects.all()
    # template_name = 'quiz/question_list.html'  # This is used to render specific html page
    context_object_name = 'get_questions'

    # Overriding
    # def get_queryset(self):
    #     query_set = Question.objects.all()[:2]
    #     return query_set

    # CRUD operations
    # CreateView, UpdateView, DeleteView, ListView, DetailView


class QuestionDetail(generic.DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['test'] = 'data'
        return context


class QuestionDelete(generic.DeleteView):
    model = Question
    success_url = reverse_lazy('index')


class QuestionCreate(generic.CreateView):
    model = Question
    fields = ['question_text', 'category']
    success_url = reverse_lazy('index')


class QuestionUpdate(generic.UpdateView):
    model = Question
    fields = ['question_text', 'category']
    success_url = reverse_lazy('index')


