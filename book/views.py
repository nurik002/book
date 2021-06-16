from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from book.form import CommentFormsModel
from book.models import BookModel


class BookListView(ListView):
    template_name = 'book_list.html'
    queryset = BookModel.objects.all()
    paginate_by = 3


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
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def to_book(request, pk):
    book = BookModel.objects.filter(pk=pk)
    if book.model.is_booked != None:
        book.model.is_booked = None
        messages.add_message(request, messages.INFO, ' not to_book')
    else:
        book.model.is_booked = request.user
        messages.add_message(request, messages.INFO, 'to_book')
    return redirect('home')
