from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from book.views import BookListView, BookDetailView, CommentCreateView, to_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookListView.as_view(), name='home'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('comment/<int:pk>', CommentCreateView.as_view(), name='comment'),
    path('accounts/', include('registration.backends.default.urls')),
    path('to_book/<int:pk>', to_book, name='to-book'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
