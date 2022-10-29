from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    telegram_chat_id = models.IntegerField()

