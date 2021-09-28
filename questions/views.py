from django.shortcuts import render
from django.views.generic import FormView
from .forms import QuestionForm
from .models import Question, Search
from .utils import so_advanced_search, monitor_search

class SearchView(FormView):
    template_name = 'questions/search.html'
    success_url = '...'
    form_class = QuestionForm

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context["show_results"] = False
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if not monitor_search(request):
            return self.form_invalid(form, **kwargs)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)


    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context["show_results"] = False
        return self.render_to_response(context)

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        question_data = form.cleaned_data.copy()
        del question_data['site']
        question = Question.objects.filter(**question_data)
        if question.exists():
            print("data exists")
            search = Search.objects.filter(question=question.first())
            if search.exists():
                answer = search[0].answer
                context["show_results"] = True
                context["answers"] = answer
        else:
            print("data does not exists; fetching...")
            question = Question.objects.create(**question_data)
            response = so_advanced_search(form.cleaned_data)
            if 'error' in response:
                context['form'] = form
                context["show_results"] = False
                return self.render_to_response(context)
            form.cleaned_data['filter'] = 'total'
            response['data'] = response.pop('items')
            Search.objects.create(
                question = question,
                answer = response
            )
            context["show_results"] = True
            context["answers"] = response
        context['form'] = form
        return self.render_to_response(context)