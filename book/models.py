from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class BookModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='book')
    description = models.TextField()
    is_booked = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comments.order_by('-pk')


class CommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_comments',
                             null=True, blank=True)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
