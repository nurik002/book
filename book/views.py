from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from book.form import CommentFormsModel
from book.models import BookModel


class BookListView(ListView):
    template_name = 'book_list.html'
    queryset = BookModel.objects.all()


class BookDetailView(DetailView):
    model = BookModel
    template_name = 'book_detail.html'


class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentFormsModel
    template_name = 'book_detail.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        form.instance.book = get_object_or_404(BookModel, pk=pk)
        return super().form_valid(form)
