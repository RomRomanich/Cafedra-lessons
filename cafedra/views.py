from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.db.models import Q  # new

from django.views import View, generic
from django.views.generic import *
from rangefilter.filters import DateTimeRangeFilter

from .forms import *
from .utils import *


# ----------------Login-----------------------
class RegisterUser(DataMixin, CreateView):
    form_class = User
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LoginUser(View):
    def get(self, request):
        return render(request, 'registration/login.html', {'form': AuthenticationForm})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            try:
                form.clean()
            except ValidationError:
                return render(
                    request,
                    'registration/login.html',
                    {'form': form, 'invalid_creds': True}
                )

            login(request, form.get_user())

            return redirect(reverse('central'))

        return render(request, 'registration/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def central(request):
    return render(request, 'central.html')

# ----------------Cafedra 1-----------------------


class LessonsList(LoginRequiredMixin, DataMixin, ListView):
    model = Lessons
    paginate_by = 10
    template_name = 'cafedra/lessons.html'
    list_filter = ('name', ('datetime', DateTimeRangeFilter), 'vid')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class SearchLessonsView(LoginRequiredMixin, DataMixin, ListView):
    model = Lessons
    template_name = 'cafedra/lessons_search.html'


    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Lessons.objects.filter(
            Q(name__icontains=query) | Q(text__icontains=query) | Q(datetime__icontains=query)
        )
        return object_list

class SearchLessonsViewDate(LoginRequiredMixin, DataMixin, ListView):
    model = Lessons
    template_name = 'cafedra/lessons_search_date.html'

    def get_queryset(self):
        fromDateTime = self.request.GET.get('fromDateTime', None)
        toDateTime = self.request.GET.get('toDateTime', None)
        response = Lessons.objects.filter(datetime__range=[fromDateTime, toDateTime])
        return response


class AddLessonsPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddLessonsForm
    template_name = 'cafedra/lessons_add.html'
    success_url = reverse_lazy('lessons_add')
    success_message = "Lessons add"
    login_url = reverse_lazy('lessons_add')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        messages.success(self.request, "Lessons add")
        return super(AddLessonsPage, self).form_valid(form)


class ReferatList(LoginRequiredMixin, DataMixin, ListView):
    model = Referat
    template_name = 'cafedra/referat.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('login')
    login_url = reverse_lazy('cafedra')
    raise_exception = True
    paginate_by = 10
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SearchReferatView(LoginRequiredMixin, DataMixin, ListView):
    model = Referat
    template_name = 'cafedra/referat_search.html'


    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Referat.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(text__icontains=query) | Q(
                datetime__icontains=query)
        )
        return object_list

class SearchReferatViewDate(LoginRequiredMixin, DataMixin, ListView):
    model = Referat
    template_name = 'cafedra/referat_search_date.html'

    def get_queryset(self):
        fromDateTime = self.request.GET.get('fromDateTime', None)
        toDateTime = self.request.GET.get('toDateTime', None)
        response = Referat.objects.filter(datetime__range=[fromDateTime, toDateTime])
        return response


class AddReferatPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddReferatForm
    template_name = 'cafedra/referat_add.html'
    success_url = reverse_lazy('referat_add')
    login_url = reverse_lazy('referat_add')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        messages.success(self.request, "Referat add")
        return super(AddReferatPage, self).form_valid(form)


#  --------------------------Ustav-------------------------------------------
@login_required
def cafedra_order(request):
    return render(request, 'order/cafedra_order.html')

@login_required
def cafedra_1(request):
    return render(request, 'order/cafedra_1.html')

@login_required
def cafedra_2(request):
    return render(request, 'order/cafedra_2.html')
