from django.shortcuts import render
from .models import Thread
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
                ListView,
                DetailView,
                CreateView,
                UpdateView
)

def main(request) :
    content = {
        'threads' : Thread.objects.all()
    }
    return render(request, 'main/home.html', content)

class ThreadListView(ListView):
    model = Thread
    template_name = 'main/home.html'
    context_object_name = 'threads'
    ordering = ['-date_posted'] # сортировка threads

class ThreadDetailView(DetailView):
    model = Thread

class ThreadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Thread
        fields = ['title', 'language', 'max_people', 'lingualevel']

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

        def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['title', 'language', 'max_people', 'lingualevel']

    def form_valid(self, form):
        form.instance.author = self.model.user
        return super(ThreadCreateView, self).form_valid(form)


    # def from_valid(self, from):
    #     from.instance.author = self.request.user
    #     return super
